import sys
from lxml import etree


if len(sys.argv) < 2:
    print("Usage: python script.py <input_filename> <output_filename>")
    sys.exit(1)

filename = sys.argv[1]
outputfile = sys.argv[2]

try:
    tree = etree.parse(filename)
    root = tree.getroot()
    
    unique_lemmas = set(elem.get('lemma') for elem in root.iter('word') if elem.get('lemma'))

    with open(outputfile, 'w', encoding='utf-8') as f:
        for lemma in sorted(unique_lemmas):
            f.write(f"{lemma}\n")

    print(f"Unique lemmas have been written to {outputfile}")
except Exception as e:
    print(f"Error: {e}")