from jinja2 import Environment, FileSystemLoader
from ne_dict import namedentities

# Set up the Jinja environment
env = Environment(loader=FileSystemLoader('templates'))

# Render the base template
base_template = env.get_template('base.html')

lineno = 27
#need for loop here iterating over line numbersX
output = base_template.render(lineno=lineno, namedentities=namedentities)
outfile = f'output/test{lineno}.html'
with open(outfile, 'w', encoding="utf-8") as f:
    f.write(output)

print("Base template with includes rendered successfully!")