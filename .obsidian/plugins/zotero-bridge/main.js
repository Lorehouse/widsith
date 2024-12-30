var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);
var __async = (__this, __arguments, generator) => {
  return new Promise((resolve, reject) => {
    var fulfilled = (value) => {
      try {
        step(generator.next(value));
      } catch (e) {
        reject(e);
      }
    };
    var rejected = (value) => {
      try {
        step(generator.throw(value));
      } catch (e) {
        reject(e);
      }
    };
    var step = (x) => x.done ? resolve(x.value) : Promise.resolve(x.value).then(fulfilled, rejected);
    step((generator = generator.apply(__this, __arguments)).next());
  });
};

// src/main.ts
var main_exports = {};
__export(main_exports, {
  ZoteroItem: () => ZoteroItem,
  default: () => main_default
});
module.exports = __toCommonJS(main_exports);

// src/ZoteroBridge.ts
var import_obsidian6 = require("obsidian");

// node_modules/@vanakat/plugin-api/index.js
var import_obsidian = require("obsidian");
function registerAPI(name, api, plugin) {
  window["PluginApi"] = window["PluginApi"] || {};
  window["PluginApi"][name] = api;
  plugin.register(() => {
    delete window["PluginApi"][name];
  });
}

// src/ZoteroBridgeSettings.ts
var DEFAULT_SETTINGS = {
  connectionType: 1 /* ZotServer */,
  userOrGroup: "users/0",
  host: "localhost",
  port: "23119"
};

// src/ZoteroAdapter.ts
var import_obsidian3 = require("obsidian");

// src/ZoteroItem.ts
var import_obsidian2 = require("obsidian");
var ZoteroItem = class {
  constructor(raw) {
    this.raw = raw;
  }
  getKey() {
    return this.raw.key;
  }
  getTitle() {
    return this.raw.title || this.raw.shortTitle || this.getNoteExcerpt() || "[No Title]";
  }
  getShortTitle() {
    return this.raw.shortTitle;
  }
  getAuthors() {
    return this.getCreators().filter((creator) => creator.creatorType === "author").map(this.normalizeName);
  }
  getAuthor() {
    return this.getAuthors()[0];
  }
  getCreators() {
    return this.raw.creators || [];
  }
  getDate() {
    return this.raw.date ? this.formatDate(this.raw.date) : { year: null, month: null, day: null };
  }
  getNoteExcerpt() {
    if (this.raw.note) {
      const div = document.createElement("div");
      div.appendChild((0, import_obsidian2.sanitizeHTMLToDom)(this.raw.note));
      return (div.textContent || div.innerText || "").trim().substring(0, 50) + "...";
    }
    return "";
  }
  normalizeName(creator) {
    const names = {
      firstName: creator.firstName,
      lastName: creator.lastName,
      fullName: ""
    };
    if (creator.hasOwnProperty("name")) {
      const delimiter = creator.name.lastIndexOf(" ");
      names.firstName = creator.name.substring(0, delimiter + 1).trim();
      names.lastName = creator.name.substring(delimiter).trim();
      names.fullName = creator.name;
    } else {
      names.fullName = `${names.firstName} ${names.lastName}`;
    }
    return names;
  }
  formatDate(date) {
    const dateObject = new Date(date);
    if (isNaN(dateObject.getTime())) {
      return null;
    }
    return {
      year: dateObject.getFullYear(),
      month: dateObject.getMonth() + 1,
      day: dateObject.getDate()
    };
  }
  getValues() {
    return {
      key: this.getKey(),
      title: this.getTitle(),
      shortTitle: this.getShortTitle(),
      date: this.getDate(),
      authors: this.getAuthors(),
      firstAuthor: this.getAuthor()
    };
  }
};

// src/ZoteroAdapter.ts
var LocalAPIV3Adapter = class {
  constructor(settings) {
    this.settings = settings;
  }
  get baseUrl() {
    return `http://${this.settings.host}:${this.settings.port}/api/${this.settings.userOrGroup}`;
  }
  search(query) {
    return this.items({
      itemType: "-attachment",
      q: query
    });
  }
  groups() {
    return (0, import_obsidian3.request)({
      url: `http://${this.settings.host}:${this.settings.port}/api/users/0/groups`,
      method: "get",
      contentType: "application/json"
    }).then(JSON.parse).then((groups) => groups.map((group) => group.data));
  }
  items(parameters) {
    return (0, import_obsidian3.request)({
      url: `${this.baseUrl}/items?` + new URLSearchParams(parameters).toString(),
      method: "get",
      contentType: "application/json"
    }).then(JSON.parse).then((items) => items.filter((item) => !["attachment", "note"].includes(item.data.itemType)).map((item) => new ZoteroItem(item.data))).catch(() => {
      new import_obsidian3.Notice(`Couldn't connect to Zotero, please check the app is open and Zotero Local API is enabled`);
      return [];
    });
  }
};
var ZotServerAdapter = class {
  constructor(settings) {
    this.settings = settings;
  }
  get baseUrl() {
    return `http://${this.settings.host}:${this.settings.port}/zotserver`;
  }
  search(query) {
    return this.items({
      q: query
    });
  }
  items(parameters) {
    return (0, import_obsidian3.request)({
      url: `${this.baseUrl}/search`,
      method: "post",
      contentType: "application/json",
      body: JSON.stringify([{
        condition: "quicksearch-titleCreatorYear",
        value: parameters.q
      }])
    }).then(JSON.parse).then((items) => items.filter((item) => !["attachment", "note"].includes(item.itemType)).map((item) => new ZoteroItem(item))).catch(() => {
      new import_obsidian3.Notice(`Couldn't connect to Zotero, please check the app is open and ZotServer is installed`);
      return [];
    });
  }
};
var ZoteroAdapters = {
  [1 /* ZotServer */]: ZotServerAdapter,
  [2 /* LocalAPIV3 */]: LocalAPIV3Adapter
};

// src/ZoteroSuggestModal.ts
var import_obsidian4 = require("obsidian");
var ZoteroSuggestModal = class extends import_obsidian4.SuggestModal {
  constructor(app, adapter, onSelect) {
    super(app);
    this.adapter = adapter;
    this.onSelect = onSelect;
  }
  getSuggestions(query) {
    return this.adapter.search(query);
  }
  renderSuggestion(item, el) {
    const authors = item.getAuthors();
    el.createEl("div", { text: item.getTitle() });
    if (authors.length > 0) {
      let text = authors[0].fullName + " ";
      if (authors.length > 1) {
        text += "et al. ";
      }
      el.createEl("small", { text });
      if (item.getDate()) {
        el.createEl("small", { text: `(${item.getDate().year}) ` });
      }
    }
    el.createEl("small", { text: `[${item.getKey()}]`, cls: "zotero-bridge__text-secondary" });
  }
  onChooseSuggestion(item) {
    this.onSelect(item);
  }
};
function promisedZoteroSuggestModal(...args) {
  return new Promise((resolve, reject) => {
    try {
      new ZoteroSuggestModal(...args, (item) => resolve(item)).open();
    } catch (e) {
      reject(e);
    }
  });
}

// src/plugin-api/ZoteroBridgeApiV1.ts
var ZoteroBridgeApiV1 = class {
  constructor(plugin) {
    this.plugin = plugin;
  }
  search() {
    return promisedZoteroSuggestModal(this.plugin.app, this.plugin.zoteroAdapter);
  }
};

// src/ZoteroBridgeApi.ts
var ZoteroBridgeApi = class {
  constructor(plugin) {
    this.plugin = plugin;
  }
  v1() {
    return new ZoteroBridgeApiV1(this.plugin);
  }
};

// src/ZoteroBridgeSettingTab.ts
var import_obsidian5 = require("obsidian");
var ZoteroBridgeSettingTab = class extends import_obsidian5.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    this.containerEl.empty();
    new import_obsidian5.Setting(this.containerEl).setName("Connection type").setDesc("Note that you either need to install ZotServer plugin in Zotero 6 or enable Local API support in Zotero 7 advanced settings.").addDropdown((dropdown) => {
      dropdown.addOption(1 /* ZotServer */.toString(), "Zotero 6 ZotServer Plugin").addOption(2 /* LocalAPIV3 */.toString(), "Zotero 7 Local API (v3)").setValue(this.plugin.settings.connectionType.toString()).onChange((value) => __async(this, null, function* () {
        yield this.plugin.saveSettings({
          connectionType: +value
        });
      }));
    });
    new import_obsidian5.Setting(this.containerEl).setName("User or group").setDesc("This parameter only works with Zotero 7 connection type.").addDropdown((dropdown) => __async(this, null, function* () {
      const adapter = new LocalAPIV3Adapter(this.plugin.settings);
      const groups = yield adapter.groups();
      dropdown.addOption(`users/0`, "My Library");
      groups.forEach((group) => {
        dropdown.addOption(`groups/${group.id}`, group.name);
      });
      dropdown.setValue(this.plugin.settings.userOrGroup).onChange((value) => __async(this, null, function* () {
        yield this.plugin.saveSettings({
          userOrGroup: value
        });
      }));
    }));
    new import_obsidian5.Setting(this.containerEl).setName("Zotero server port").setDesc(`Don't change unless you really know what you are doing`).addText((txt) => {
      txt.setValue(this.plugin.settings.port.toString()).onChange((value) => __async(this, null, function* () {
        yield this.plugin.saveSettings({
          port: value
        });
      }));
    });
  }
};

// src/ZoteroBridge.ts
var ZoteroBridge = class extends import_obsidian6.Plugin {
  onload() {
    return __async(this, null, function* () {
      this.settings = Object.assign({}, DEFAULT_SETTINGS, yield this.loadData());
      this.zoteroAdapter = new ZoteroAdapters[this.settings.connectionType](this.settings);
      this.addSettingTab(new ZoteroBridgeSettingTab(this.app, this));
      registerAPI("ZoteroBridge", new ZoteroBridgeApi(this), this);
    });
  }
  saveSettings(newSettings) {
    return __async(this, null, function* () {
      Object.assign(this.settings, newSettings);
      yield this.saveData(this.settings);
    });
  }
};

// src/main.ts
var main_default = ZoteroBridge;

/* nosourcemap */