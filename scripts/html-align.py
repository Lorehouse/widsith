import xml.etree.ElementTree as ET

def xml_to_html(root):
    html_lines = []
    
    for line in root.findall('l'):
        line_number = line.attrib['n']
        
        line_text = ''.join(line.itertext()).replace("<caesura/>", "&emsp;")
        
        html_line = f'<div class="poetry-line" data-line="{line_number}">{line_text}</div><br/>'
        html_lines.append(html_line)
        print(f"Generated HTML for line {line_number}, containing {html_line}")
    return '\n'.join(html_lines)

def process_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return xml_to_html(root)
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return ""

def alignment_files(file_path1, file_path2):
    oe_html = process_xml_file(file_path1)
    me_html = process_xml_file(file_path2)

    combined_html = oe_html + "\n" + me_html
    return combined_html

# Specify the path to your XML file
oe_xml = "../widsith_oe.xml"
me_xml =  "../modern-english/translationone.xml"
# alignment_html = "../views/alignmenttest.html"
try:
    print(oe_xml + me_xml)
except LookupError:
    print("Yu suck")


# Generate the HTML output from the XML file
alignment_html_output = alignment_files(oe_xml, me_xml)

# Print or save the HTML output
print(alignment_html_output)
