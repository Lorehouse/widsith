
def neset(tsv_file):
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    ne_dict = {}
    
    for line in tsv_file:
        lemma, gloss, form, ln, pos, comment = line.strip().split("\t")
        ne_dict.update({lemma: comment})

    return ne_dict

neset('../named-entities.tsv')