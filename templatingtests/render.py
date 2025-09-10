#!/usr/bin/env python3

from pathlib import Path

from ryland import Ryland


ROOT_DIR = Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / "views"
PANTRY_DIR = ROOT_DIR / "pantry"
TEMPLATE_DIR = ROOT_DIR / "templatingtests/templates"

ryland = Ryland(output_dir=OUTPUT_DIR, template_dir=TEMPLATE_DIR)

ryland.clear_output()

## copy and hash static files

ryland.copy_to_output(PANTRY_DIR / "styles.css")
ryland.copy_to_output(PANTRY_DIR / "glossstyles.css")
ryland.copy_to_output(PANTRY_DIR / "sidebysidestyles.css")
ryland.copy_to_output(PANTRY_DIR / "linebyline.css")
ryland.add_hash("styles.css")
ryland.add_hash("glossstyles.css")
ryland.add_hash("sidebysidestyles.css")
ryland.add_hash("linebyline.css")


ryland.render_template(
    'thesis.html',
    'thesis.html',
    {"page_title":"Widsið and the Digital Age",
    "author":"Sarah Monnier"}
)
ryland.render_template(
    'index.html',
    '../index.html',
    {"page_title":"Widsið Translation and Thesis"}
    )
ryland.render_template(
    'alignment1.html',
    'alignment1.html',
    {"page_title":"Alignment"},
)
ryland.render_template(
    'named_entities.html',
    'named_entities.html',
    {"page_title":"Named Entities"}
)
ryland.render_template(
    'furtherreading.html',
    'furtherreading.html',
    {"page_title":"Further Reading"}
)
ryland.render_template(
    'beowulf_alignment.html',
    'beowulf_alignment.html', 
    {"page_title":"Beowulf Alignment"}
)
for i in range(1, 144):
    ryland.render_template(
        f'line/line-{i}.html',
        f'line/line-{i}.html',
        {"lineno":i,
        "page_title":f"Widsið Line {i}"}
    )
for i in range(1, 16):
    ryland.render_template(
        f'riddle1/line-{i}.html',
        f'riddle1/line-{i}.html',
        {"lineno":i,
        "page_title":f"Riddle One Line {i}"}
    )
ryland.render_template(
    'acknowledgements.html',
    'acknowledgements.html',
    {"page_title":"acknowledgements",
    "email":"sarahjmonnier@gmail.com"}
)

ryland.render_template(
    'llm_glossary.html',
    'llm_glossary.html',
    {"page_title":"LLM Glossary"}
)
