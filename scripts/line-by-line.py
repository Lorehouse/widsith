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
    
    with open(filename, "w", encoding='utf=8') as f:
        f.write(modified_html)

    print(f"HTML table created and saved as '{filename}'")