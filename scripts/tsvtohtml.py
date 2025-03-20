import csv

def tsv_to_html(tsv_file, html_file):
    tsv_file = open(tsv_file, encoding="utf-8")
    tsv_file.readline()
    
    
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write('{% extends "base.html" %}\n{% block title %}{{ page_title }}{% endblock %}}\n{% block extra_css %}\n<link rel="stylesheet" href="../static/glossstyles.css">\n{% endblock %}\n{% block content %}\n')
        file.write('<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button>')
        file.write('<h1>Glossary</h1>')
        file.write('<table border="1">\n')
        file.write('\t<th>Lemma</th>\n\t<th>Form</th>\n\t<th>Line</th>\n\t<th>POS</th>\n\t<th>Gloss</th>\n')
        for line in tsv_file:
            lemma, gloss, form, line, pos, comment = line.strip().split("\t")
            file.write(f'\t<tr>\n\t<td class="lemma">{lemma}</td>\n\t<td class="form">{form}</td>\n\t<td class="line">{line}</td>\n\t<td class="POS">{pos}</td>\n\t<td class="gloss">{gloss}</td>\n\t</tr>\n')
        # for column in data[0]:
        #     file.write(f'    <th>{column}</th>\n')
        
        # for row in data[1:]:
        #     file.write('  <tr>\n')
        #     for column in row:
        #         file.write(f'    <td>{column}</td>\n')
        #     file.write('  </tr>\n')
        
        
        file.write('</table>\n{% endblock %}')
    print(f"Your file has been created at '{html_file}'.")
    return (html_file)