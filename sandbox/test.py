import sys
from lxml import etree

# Unicode replacements for long vowels and long ash
replacement_map = {
    'ā': '\u0101',
    'ē': '\u0113',
    'ī': '\u012B',
    'ō': '\u014D',
    'ū': '\u016B',
    'ǣ': '\u01E3'  # Long ash
}

# Function to ensure unicode compliance
def ensure_unicode_compliance(text):
    if text is not None:
        for key, value in replacement_map.items():
            text = text.replace(key, value)
    return text

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# Get the filename from the command-line argument
filename = sys.argv[1]

# Parse the XML file
try:
    parser = etree.XMLParser(encoding="utf-8")
    tree = etree.parse(filename, parser)
    root = tree.getroot()
    lemmas = [ensure_unicode_compliance(elem.get('lemma')) for elem in root.iter('word') if elem.get('lemma')]

    # Debugging output
    print("Lemmas found:")
    for lemma in lemmas:
        print(repr(lemma))
except Exception as e:
    print(f"Error: {e}")
