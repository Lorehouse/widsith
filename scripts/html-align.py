import xml.etree.ElementTree as ET

def xml_to_html(root):
    html_lines = []
    
    for line in root.findall('.//{http://www.tei-c.org/ns/1.0}l'):
        line_number = line.attrib['n']
        line_text = ''.join(line.itertext()).replace("<caesura/>", "&emsp;")
        
        html_line = f'\t\t\t\t<div class="poetry-line" data-line="{line_number}">{line_text}</div><br/>'
        html_lines.append(html_line)
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
    return oe_html, me_html
    # combined_html = oe_html + "\n" + me_html
    # return combined_html

def html_generator(in_file1, in_file2, outfile):
    in_file1, in_file2 = alignment_files(in_file1, in_file2)
    with open(outfile, "w", encoding="utf-8") as outfile:
        outfile.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Side by Side Widsið</title>\n\t<link rel="stylesheet" href="sidebysidestyles.css">\n</head>\n')
        outfile.write('<body>\n\t<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button>\n\t<div class="container">\n\t\t<div class="column">\n\t\t\t<h2>Widsið</h2>\n\t\t\t<h3>Old English</h3>\n\t\t\t<p>')
        outfile.write(f'\n{in_file1}\n')
        outfile.write('\t\t\t</p>\n\t\t</div>\n\n\t\t<div class="column">\n\t\t\t<h2>Widsith</h2>\n\t\t\t<h3>Modern English</h3>\n\t\t\t<p>')
        outfile.write(f'\n{in_file2}\n')
        outfile.write('</p>\n\t\t</div>\n\t</div>\n</body>\n</html>')
    print(f"Your file has been created")

oe_xml = "../widsith_oe.xml"
me_xml =  "../modern-english/translationone.xml"
alignment_html = "../views/alignment2.html"

html_generator(oe_xml, me_xml, alignment_html)
