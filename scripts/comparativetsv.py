from lxml import etree


def maketsv(input):
    filename = input
    outputtsv = "../transitiondocs/comparative.tsv"
    print(f"your input file is {filename}")

    with open(outputtsv, 'w', encoding='utf-8') as f:
        f.write(f"Word\tLemma\tPart of Speech\tGloss\n")
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
                f.write(f"{entry['form']}\t{entry['lemma']}\t{entry['pos']}\t{entry['gloss']}\n")


        print(f"Unsorted glossary has been written to {outputtsv}")
        return outputtsv
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__": 
    maketsv("../word-tagging.xml")
