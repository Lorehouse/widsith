import pandas as pd
from lxml import etree

# Function to read XML content from a file
def read_xml_file(file_path):
    with open(file_path, 'rb') as file:
        xml_content = file.read()
    return xml_content

# Define the XML and TSV file paths
df = pd.read_csv('../linebylinegloss.tsv', sep='\t', encoding='utf-8')
translatefile = '../modern-english/translationone.xml'
comment_file_path = '../transitiondocs/commentdoc.tsv'

def printoneline(xml_file, line_no):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Find the namespace if any
    namespaces = {'ns': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

    # Find <l> tags with namespace handling
    line_tags = root.findall('.//ns:l', namespaces) if namespaces else root.findall('.//l')

    for line in line_tags:
        line_number = line.get('n')
        if line_number and int(line_number) == line_no:
            html_line = ''.join(
                etree.tostring(element, encoding='unicode', with_tail=False) if element.tag != 'caesura' else '&emsp;'
                for element in line.iter()
            )
            html_line = html_line.replace(f'<l n="{line_number}">', '').replace('</l>', '').replace(' <caesura/>', '&emsp;')
            return html_line
    return None

# Read the XML content from the file
xml_content = read_xml_file(translatefile)

# Load the comments TSV file without a header and assign column names manually
comments_df = pd.read_csv(comment_file_path, sep='\t', encoding='utf-8', header=None)
comments_df.columns = ['Line', 'Lemma', 'Comment']
print("Column names in comments_df:", comments_df.columns)  # Debug statement

for line, group_df in df.groupby('Line'):
    # Convert the dataframe group to HTML
    html_data = pd.DataFrame([group_df[col].tolist() for col in group_df.columns if col != 'Line'], 
                             index=[col for col in group_df.columns if col != 'Line'])
    html_output = html_data.to_html(header=False, index=False, border=0)

    tree = etree.HTML(html_output).xpath('//table')[0]
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

    modified_html = etree.tostring(tree, pretty_print=False, encoding="unicode")

    # Get the line number and convert it to HTML
    line_no = int(line)
    html_line = printoneline(translatefile, line_no)

    if html_line:
        filename = f"../templatingtests/templates/line/line-{line}.html"

        if line_no < 143:
            nextline = line_no + 1
        else: 
            nextline = line_no
        if line_no == 1:
            prevline = 1
        else:
            prevline = line_no - 1

        with open(filename, "w", encoding='utf-8') as f:
            f.write('{% extends "base.html" %}\n{% block title %}{{ page_title }}{% endblock %}\n{% block extra_css %}\n<link rel="stylesheet" href="linebyline.css">\n{% endblock %}\n{% block content %}\n')
            f.write('<link rel="stylesheet" href="linebyline.css">\n</head>\n')
            f.write('\t<h1>Widsið</h1>\n')            
            f.write(f'<h2>Line {line_no}</h2>\n')
            f.write(modified_html)
            if line != 1:
                f.write(f'\n\t<div class="button-container">\n\t\t<a href="https://lorehord.com/views/line/line-{prevline}.html">Previous</a>\n')
            else:
                f.write('\n\t<div class="button-container">\n\t\t<a></a>')
            if line != 143:
                f.write(f'\t\t<a href="https://lorehord.com/views/line/line-{nextline}.html">Next</a>\n\t</div>')
            else:
                f.write('\n\t\t<a></a></div>')
            f.write('\n\t<h2 class="translation">Translation</h2><br>\n')
            f.write(f'\t<p class="translation">{html_line}</p>\n')

            comment_rows = comments_df[comments_df['Line'] == line_no]
            f.write("\n\t<div class='namedentities' style='text-align: justify;'>\n\t\t<h2 class='translation'>Named Entities</h2>\n")
            for _, row in comment_rows.iterrows():
                lemma = row['Lemma']
                ne_comment = row['Comment']
                
                f.write(f'\t<ul>\n\t\t<li><span class="named-entity">{lemma}</span>: {ne_comment}</li>\n\t</ul>')

            f.write('\n\t</div>\n</table>\n{% endblock %}')

        print(f"HTML file created as '{filename}'")
    else:
        print(f"No matching line found for line number {line_no}")
