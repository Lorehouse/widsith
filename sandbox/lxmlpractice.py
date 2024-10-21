import sys
from lxml import etree

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

tree = etree.parse(filename)
root = tree.getroot()

def strip_namespace(tag):
    if '}' in tag:
        return tag.split('}', 1)[1]  # Strip off the namespace part
    return tag

def print_children(element, level=0):
    tag = strip_namespace(element.tag)

    print("  " * level + element.text)
    for child in element:
        print_children(child, level + 1)
root_tag = strip_namespace(root.tag)
print_children(root)