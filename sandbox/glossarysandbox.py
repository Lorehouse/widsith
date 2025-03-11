import sys
from lxml import etree


if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
outputtsv = sys.argv[2]

with open(outputtsv, 'w', encoding='utf-8') as f:
    f.write(f"Lemma\tGloss\tForm\tLine\tPOS\tComment\n")
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
        comment = word.get('comment')
        glossary.append({
            'lemma': lemma,
            'gloss': gloss,
            'form': form,
            'line': line,
            'pos': pos,
            'comment': comment,
        })



    with open(outputtsv, 'a', encoding='utf-8') as f:
        for entry in glossary:
            f.write(f"{entry['lemma']}\t{entry['gloss']}\t{entry['form']}\t{entry['line']}\t{entry['pos']}\t{entry['comment']}\n")


    print(f"Unsorted glossary has been written to {outputtsv}")
except Exception as e:
    print(f"Error: {e}")