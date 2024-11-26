import csv

def tsv_to_yaml(tsv_file, yaml_file):
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    
    with open(yaml_file, 'w', encoding='utf-8') as f:
        for line in tsv_file:
            lemma, gloss, form, line, pos, comment = line.strip().split("\t")
            if comment != "None":
                f.write(f'{lemma}: "{comment}"\n')
        
    print(f"Your file has been created at '{yaml_file}'.")


tsv_to_yaml('../ne-gloss-sorted.tsv', '../transitiondocs/ne_dictionary.yaml')