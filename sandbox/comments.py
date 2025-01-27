
def comment_file(tsv_file, html_file):
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    
    with open(html_file, 'w', encoding='utf-8') as file:
        for line in tsv_file:
            lemma, gloss, form, line, pos, comment = line.strip().split("\t")
            if comment != "None":
                file.write(f'{line}\t{lemma}\t{comment}\n')
        
    
    print(f"Your file has been created at '{html_file}'.")
    return html_file


comment_file('../transitiondocs/unorderedgloss.tsv', 'commentdoc.tsv')