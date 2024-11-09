import csv

def tsv_to_html(tsv_file, html_file):
    with open(tsv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        data = list(reader)
    
    
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write('<html>\n<head>\n\t<meta charset="UTF-8">\n\t<title>Glossary</title>\n\t<link rel="stylesheet" href="glossstyles.css">\n</head>\n<body>\n')
        file.write('<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button>')
        file.write('<h1>Glossary</h1>')
        file.write('<table border="1">\n')
        for column in data[0]:
            file.write(f'    <th>{column}</th>\n')
        
        for row in data[1:]:
            file.write('  <tr>\n')
            for column in row:
                file.write(f'    <td>{column}</td>\n')
            file.write('  </tr>\n')
        
        
        file.write('</table>\n</body>\n</html>')
    print(f"Your file has been created at '{html_file}'.")


tsv_to_html('../sorted-glosstest.tsv', '../views/glossary.html')