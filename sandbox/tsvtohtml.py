import csv

def tsv_to_html(tsv_file, html_file):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        data = list(reader)
    
    
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write('<html>\n<head>\n<title>TSV to HTML Table</title>\n</head>\n<body>\n')
        file.write('<table border="1">\n')

        
        for row in data:
            file.write('  <tr>\n')
            for column in row:
                file.write(f'    <td>{column}</td>\n')
            file.write('  </tr>\n')
        
        
        file.write('</table>\n</body>\n</html>')


tsv_to_html('../gloss.tsv', 'glossary.html')
