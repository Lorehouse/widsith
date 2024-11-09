import pandas as pd
from lxml import etree

df = pd.read_csv('../linebylinegloss.tsv', sep='\t', encoding='utf-8')

for line, group_df in df.groupby('Line'):
    html_data = pd.DataFrame([group_df[col].tolist() for col in group_df.columns if col != 'Line'], 
                             index=[col for col in group_df.columns if col != 'Line'])
    
    html_output = html_data.to_html(header=False, index=False, border=0)
    # Modify the HTML to add classes for styling each row type
    tree = etree.HTML(html_output)
    
    # Add a class to each row type for styling
    rows = tree.xpath('//tr')
    for idx, row in enumerate(rows):
        # Apply specific classes based on the content of the row
        if idx == 0:  # First row is 'Forms'
            row.set('class', 'form-row')
        elif idx == 1:  # Second row is 'Lemmas'
            row.set('class', 'lemma-row')
        elif idx == 2:  # Third row is 'POS'
            row.set('class', 'pos-row')
        elif idx == 3:  # Fourth row is 'Gloss'
            row.set('class', 'gloss-row')

    # Convert the modified tree back to a string
    modified_html = etree.tostring(tree, pretty_print=True, encoding="unicode")
    
    filename = f"../views/line/line-{line}.html"

    if line < 144:
        nextline = int(line) + 1
    else: 
        nextline = 1

    prevline = int(line) - 1

    with open(filename, "w", encoding='utf=8') as f:
        f.write(f'<html>\n<head>\n\t<meta charset="UTF-8">\n\t<title>Line {line}</title>\n\t')
        f.write('<link rel="stylesheet" href="../linebyline.css">\n<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">\n\t<link href="https://fonts.googleapis.com/css2?family=Noto+Serif:wght@200;400;700&display=swap" rel="stylesheet">\n</head>\n<body>\n')
        f.write('<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button><br>')
        f.write(f'<h1>Line {line}</h1>')
        f.write(modified_html)
        f.write('\n\t<div class="button-container">\n\t\t')
        f.write(f'<button class="prevbutton" onclick="document.location=\'https://lorehord.com/views/line/line-{prevline}.html\'">Previous</button>')
        f.write(f'<button class="nextbutton" onclick="document.location=\'https://lorehord.com/views/line/line-{nextline}.html\'">Next</button>')
        f.write('\n\t</div>')
        

    print(f"HTML file created as '{filename}'")