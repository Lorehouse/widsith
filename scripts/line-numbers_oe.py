import xml.etree.ElementTree as ET

def add_line_numbers(xml_file, output_file):
    # Register the default namespace (empty string is for default namespace) -- Help from ChatGPT here
    ET.register_namespace('', "http://www.tei-c.org/ns/1.0")

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract the namespace if present -- help from ChatGPT here
    ns = {'ns': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

    line_tags = root.findall('.//ns:l', namespaces=ns) if ns else root.findall('.//l')

    for idx, line in enumerate(line_tags, start=1):
        line.set('n', str(idx))
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

input_file = '../widsith_oe.xml'
output_file = 'l-nums.xml'
add_line_numbers(input_file, output_file)