import xml.etree.ElementTree as ET

def add_line_numbers(xml_file, out_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find <l> tags
    line_tags = root.findall('.//l')

    # Add n="" attribute with number
    for idx, line in enumerate(line_tags, start=1):
        line.set('n', str(idx))

    tree.write(out_file, encoding='utf-8', xml_declaration=True)

in_file = '../widsith_oe.xml'
out_file = 'l-nums.xml'
add_line_numbers(in_file, out_file)