from ne_list import neset
from lxml import etree

def parse_xml(xml_file):
    parser = etree.XMLParser(encoding="utf-8")
    tree = etree.parse(xml_file, parser=parser)
    return tree

def find_matches(xml_tree, ne_dict):
    results = []
    for element in xml_tree.xpath("//persName | //placeName | //name"):
        same_as = element.get("sameAs")
        content = element.text.strip() if element.text else None
        line = element.getparent().get('n')
        if same_as and same_as in ne_dict:
            results.append((same_as, ne_dict[same_as]))
            
        elif content and content in ne_dict: 
            results.append((content, ne_dict[content]))
        else:
            print(f"{content} in line {line} does not have a dictionary entry.")
    return results

def main(xml_file, out_file):
    ne_dict = neset('../transitiondocs/sortedgloss.tsv')
    xml_tree = parse_xml(xml_file)
    with open(out_file, 'w', encoding='utf-8') as f:
        matches = find_matches(xml_tree, ne_dict)
        for match in matches:
            key, value = match
            f.write(f"Match found {key} -> {value}\n")
    print(f"Your file has been created at {out_file}.")

if __name__ == "__main__":
    xml_file = "../widsith_oe.xml"
    outputfile= "../transitiondocs/matches.txt"
    main(xml_file, outputfile)