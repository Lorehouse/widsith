import pandas as pd
from lxml import etree

df = pd.read_csv('../transitiondocs/unorderedriddle.tsv', sep='\t', encoding='utf-8')
translatefile = '../modern-english/r1-trans.xml'

for line, group_df in df.groupby('Line'):
    html_data = pd.DataFrame([group_df[col].tolist() for col in group_df.columns if col != 'Line'], 
                             index=[col for col in group_df.columns if col != 'Line'])
    
    html_output = html_data.to_html(header=False, index=False, border=0)
    
    tree = etree.HTML(html_output)
    
    rows = tree.xpath('//tr')
    for idx, row in enumerate(rows):
        
        if idx == 0:
            row.set('class', 'form-row')
        elif idx == 1:
            row.set('class', 'lemma-row')
        elif idx == 2:
            row.set('class', 'pos-row')
        elif idx == 3:
            row.set('class', 'gloss-row')

    modified_html = etree.tostring(tree, pretty_print=True, encoding="unicode")
    
    filename = f"../views/riddle1/line-{line}.html"

    if line < 16:
        nextline = int(line) + 1
    else: 
        nextline = line
    if line == 1:
        prevline = 1
    else:
        prevline = int(line) - 1

    with open(filename, "w", encoding='utf=8') as f:
        f.write(f'<html>\n<head>\n\t<meta charset="UTF-8">\n\t<title>Line {line}</title>\n\t')
        f.write('<link rel="stylesheet" href="../linebyline.css">\n<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">\n\t<link href="https://fonts.googleapis.com/css2?family=Noto+Serif:wght@200;400;700&display=swap" rel="stylesheet">\n</head>\n<body>\n')
        f.write('<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button><br>')
        f.write(f'<h1>Exeter Book Riddle One</h1>')
        f.write(f'<h2>Line {line}</h2>')
        f.write(modified_html)
        f.write('\n\t<div class="button-container">\n\t\t')
        f.write(f'<a href="https://lorehord.com/views/riddle1/line-{prevline}.html">Previous</a>')
        f.write(f'<a href="https://lorehord.com/views/riddle1/line-{nextline}.html">Next</a>')
        f.write('\n\t</div>')
        

    print(f"HTML file created as '{filename}'")