import sys
from lxml import etree


if len(sys.argv) < 3:
    print("Usage: python script.py <inputfilename> <outputfilename>")
    sys.exit(1)

filename = sys.argv[1]
outputtsv = sys.argv[2]

with open(outputtsv, 'w', encoding='utf-8') as f:
    f.write(f"Lemma\tForm\tPOS\tLine\tGloss\n")
try:
    tree = etree.parse(filename)
    root = tree.getroot()
    glossary = []
    for word in root.findall('.//word'):
        line = word.getparent().get('n')
        lemma = word.get('lemma')
        form = word.get('form')
        pos = word.get('pos')
        gloss = word.get('gloss')
        glossary.append({
            'form': form,
            'lemma': lemma,            
            'pos': pos,
            'line': line,
            'gloss': gloss
        })



    with open(outputtsv, 'a', encoding='utf-8') as f:
        for entry in glossary:
            f.write(f"{entry['form']}\t{entry['lemma']}\t{entry['pos']}\t{entry['line']}\t{entry['gloss']}\n")


    print(f"Unsorted glossary has been written to {outputtsv}")
except Exception as e:
    print(f"Error: {e}")