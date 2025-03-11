
def neset(tsv_file):
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    ne_dict = {}
    update_dict = {}
    
    for line in tsv_file:
        lemma, gloss, form, ln, pos, comment = line.strip().split("\t")
        if comment == "@@@":
            update_dict.update({lemma: ln})
        if comment != "None":
            ne_dict.update({lemma: comment})
        
    print(f"You have {len(update_dict)} entries to correct")
    print(f"{update_dict}")        
    return ne_dict

#neset('../transitiondocs/sortedgloss.tsv')