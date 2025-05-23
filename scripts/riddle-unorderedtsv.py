from lxml import etree
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python unorderedtsv.py input_file.xml")
        sys.exit(1)
    
    input_file = sys.argv[1]
    print(f"Processing: {input_file}")
    maketsv(input_file)
    

def maketsv(input):
    filename = input
    outputtsv = "../transitiondocs/unorderedriddle.tsv"
    print(f"your input file is {filename}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Trying to create file: {outputtsv}")
    print(f"Absolute path: {os.path.abspath(outputtsv)}")
    print(f"Directory exists: {os.path.exists(os.path.dirname(outputtsv))}")
    print(f"Directory path: {os.path.dirname(outputtsv)}")
    print(f"Full directory path: {os.path.abspath(os.path.dirname(outputtsv))}")
    

    with open(outputtsv, 'w', encoding='utf-8') as f:
        f.write(f"Form\tLemma\tPOS\tGloss\tLine\n")
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
                'gloss': gloss,
                'line': line,
                
            })



        with open(outputtsv, 'a', encoding='utf-8') as f:
            for entry in glossary:
                f.write(f"{entry['form']}\t{entry['lemma']}\t{entry['pos']}\t{entry['gloss']}\t{entry['line']}\n")


        print(f"Unsorted glossary has been written to {outputtsv}")
        return outputtsv
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()