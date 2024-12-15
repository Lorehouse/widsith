
def tsv_to_html(tsv_file, html_file):
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    
    with open(html_file, 'w', encoding='utf-8') as file:
        for line in tsv_file:
            lemma, gloss, form, line, pos, comment = line.strip().split("\t")
            if comment != "None":
                file.write(f'{lemma}\t{gloss}\t{form}\t{line}\t{pos}\t{comment}\n')
        
        
        file.write('</table>\n</body>\n</html>')
    print(f"Your file has been created at '{html_file}'.")
    return html_file


tsv_to_html('../ne-gloss-sorted.tsv', '../named-entities.tsv')