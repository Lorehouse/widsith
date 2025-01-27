import csv

def tsv_to_html(tsv_file, html_file):
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write('<html>\n<head>\n\t<meta charset="UTF-8">\n\t<title>Named Entities Glossary</title>\n\t<link rel="stylesheet" href="glossstyles.css">\n\t<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@200;400;700&display=swap" rel="stylesheet">\n\t<link href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">\n</head>\n<body>\n')
        file.write('<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button>\n')
        file.write('<h1>Named Entities Glossary</h1>')
        file.write('<table border="1">\n')
        file.write('\t<th>Lemma</th>\n\t<th>Gloss</th>\n\t<th>Line</th>\n\t<th>POS</th>\n\t<th>Comment</th>\n')
        for line in tsv_file:
            lemma, gloss, form, line, pos, comment = line.strip().split("\t")
            if comment != "None":
                file.write(f'\t<tr>\n\t<td class="lemma">{lemma}</td>\n\t<td class="gloss">{gloss}</td>\n\t<td class="line">{line}</td>\n\t<td class="POS">{pos}</td>\n\t<td class="comment">{comment}</td>\n\t</tr>\n')
        
        
        file.write('</table>\n</body>\n</html>')
    print(f"Your file has been created at '{html_file}'.")
    return html_file

if __name__ == "__main__":
    tsv_to_html('../ne-gloss-sorted.tsv', '../views/named-entities-gloss.html')