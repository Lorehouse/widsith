import sys
from lxml import etree

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# Get the filename from the command-line argument
filename = sys.argv[1]

# Parse the XML file
try:
    tree = etree.parse(filename)
    root = tree.getroot()
    # print(root)
    all_tags=[elem.tag for elem in root.iter() if not isinstance(elem, etree._Comment)]
    print(all_tags)
 
    # for child in root:
    #     if isinstance(child, etree._Element) and not isinstance(child, etree._Comment):  # Ensure it's an element, not a comment
    #        print(child.tag, child.attrib)
    #     else:
    #        print(f"Skipping non-element or comment node: {child.tag}")
except Exception as e:
    print(f"Error: {e}")
