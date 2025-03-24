from jinja2 import Environment, FileSystemLoader
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
output_dir = os.path.join(os.path.dirname(__file__), '../views')

os.makedirs(output_dir, exist_ok=True)

env = Environment(loader=FileSystemLoader(template_dir))

def render_template(template_name, output_name, **kwargs):
    """Render a template and save to the output directory"""
    template = env.get_template(template_name)
    rendered_html = template.render(**kwargs)
    
    with open(os.path.join(output_dir, output_name), 'w', encoding='utf-8') as f:
        f.write(rendered_html)
    
    print(f"Rendered {output_name}")

# Render the thesis page
render_template(
    'thesis.html',
    'thesis.html',
    page_title="Widsið and the Digital Age",
    author="Sarah Monnier"
)

# You can add more pages here
render_template(
    'index.html',
    f'../index.html',
    page_title="Widsið Translation and Thesis"
)

# render_template(
#     'glossary.html',
#     'glossary.html',
#     page_title="Widsið Glossary",
# )

render_template(
    'alignment1.html',
    'alignment1.html',
    page_title="Alignment",
)
render_template(
    'named_entities.html',
    'named_entities.html',
    page_title="Named Entities",
)

render_template(
    'furtherreading.html',
    'furtherreading.html',
    page_title="Further Reading",
)

render_template(
    'beowulf_alignment.html',
    'beowulf_alignment.html', 
    page_title="Beowulf Alignment",
)

for i in range(1, 144):
    render_template(
        f'line/line-{i}.html',
        f'line/line-{i}.html',
        lineno=i,
        page_title=f"Widsið Line {i}"
    )


print("All templates rendered successfully!")