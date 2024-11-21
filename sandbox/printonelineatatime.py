import xml.etree.ElementTree as ET

def printoneline(xml_file):
    line_no = 1
    print(f'Starting with line number: {line_no}')
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    namespaces = {'ns': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

    # Find <l> tags
    line_tags = root.findall('.//ns:l', namespaces) if namespaces else root.findall('.//l')
    print(f'Found {len(line_tags)} <l> tags.')
    for line in line_tags:
        line_number = line.get('n')
        print(f'Checking line with number: {line_number}')
        if line_number:
            if int(line_number) == line_no:
                print(f'Matching line found: {line_number}')
                html_line = ''.join(
                    ET.tostring(element, encoding='unicode') if element.tag != 'caesura' else '&emsp;' 
                    for element in line.iter()
                    )
                html_line = html_line.replace(f'<l n="{line_number}">', '').replace('</l>', '').replace(' <caesura/>', '&emsp;').replace('</l>', '')
                with open(f'../transitiondocs/views/line/disaster{line_no}.txt', 'w', encoding='utf-8') as f:
                    f.write(f'Line {line_number}{html_line}')
                line_no += 1
            else:
                print("No match found")
        else:
            print("what the heck")

    # tree.write(f'oneline{line}.html', encoding='utf-8', xml_declaration=True)

in_file = '../modern-english/translationone.xml'
#out_file = 'l-nums.xml'
printoneline(in_file)