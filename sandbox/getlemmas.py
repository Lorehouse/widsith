import sys
from lxml import etree


if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
outputfile = sys.argv[2]

# Parse the XML file
#try:
# tree = etree.parse(filename)
# root = tree.getroot()
# lemmas = [elem.get('lemma') for elem in root.iter('word') if elem.get('lemma')]
# for lemma in lemmas:
#     try:
#         print(type(lemma))
#     except Exception as e:
#         print(f"Error:{e}")
#         pass
try:
    tree = etree.parse(filename)
    root = tree.getroot()
    
    # Collect unique lemmas
    unique_lemmas = set(elem.get('lemma') for elem in root.iter('word') if elem.get('lemma'))

    # Write unique lemmas to the output file
    with open(outputfile, 'w', encoding='utf-8') as f:
        for lemma in sorted(unique_lemmas):
            f.write(f"{lemma}\n")

    print(f"Unique lemmas have been written to {outputfile}")
except Exception as e:
    print(f"Error: {e}")