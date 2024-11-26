import yaml
from lxml import etree

def load_yaml(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data

def parse_xml(xml_file):
    parser = etree.XMLParser(encoding="utf-8")
    tree = etree.parse(xml_file, parser=parser)
    return tree

def find_matches(xml_tree, yaml_data):
    results = []
    for element in xml_tree.xpath("//persName | //placeName | //name"):
        same_as = element.get("sameAs")
        if same_as and same_as in yaml_data:
            results.append((same_as, yaml_data[same_as]))
        else:
            content = element.text.strip() if element.text else None
            if content and content in yaml_data: 
                results.append((content, yaml_data[content]))
    return results

def main(xml_file, yaml_file, out_file):
    yaml_data = load_yaml(yaml_file)
    xml_tree = parse_xml(xml_file)
    with open(out_file, 'w', encoding='utf-8') as f:
        matches = find_matches(xml_tree, yaml_data)
        for match in matches:
            key, value = match
            f.write(f"Match found {key} -> {value}\n")
    print(f"Your file has been created at {out_file}.")

if __name__ == "__main__":
    xml_file = "../widsith_oe.xml"
    yaml_file = "../transitiondocs/ne_dictionary.yaml"
    outputfile= "../transitiondocs/matches.txt"
    main(xml_file, yaml_file, outputfile)