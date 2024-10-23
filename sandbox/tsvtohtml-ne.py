import csv

def tsv_to_html(tsv_file, html_file):
    # with open(tsv_file, 'r', newline='', encoding='utf-8') as file:
        # reader = csv.reader(file, delimiter='\t')
        # data = list(reader)
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write('<html>\n<head>\n\t<meta charset="UTF-8">\n\t<title>Glossary</title>\n\t<link rel="stylesheet" href="glossstyles.css">\n</head>\n<body>\n')
        file.write('<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button>\n')
        file.write('<h1>Named Entities Glossary</h1>')
        file.write('<table border="1">\n')
        file.write('\t<th>Lemma</th>\n\t<th>Gloss</th>\n\t<th>Form</th>\n\t<th>Line</th>\n\t<th>POS</th>\n\t<th>Comment</th>\n')
        for line in tsv_file:
            lemma, gloss, form, line, pos, comment = line.strip().split("\t")
            if comment != "None":
                file.write(f'\t<tr>\n\t<td>{lemma}</td>\n\t<td>{gloss}</td>\n\t<td>{form}</td>\n\t<td>{line}</td>\n\t<td>{pos}</td>\n\t<td>{comment}</td>\n\t</tr>\n')
        # for column in data[0]:
        #     file.write(f'    <th>{column}</th>\n')
        
        # for row in data[1:]:
        #     file.write('  <tr>\n')
        #     for column in row:
        #         if column[5] != "None":
        #             file.write(f'    <td>{column}</td>\n')
            # file.write('  </tr>\n')
        
        
        file.write('</table>\n</body>\n</html>')
    print(f"Your file has been created at '{html_file}'.")


tsv_to_html('sort-gloss-comments.tsv', '../views/named-entities-gloss.html')