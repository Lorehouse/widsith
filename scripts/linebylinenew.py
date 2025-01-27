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
comment_file_path = '../sandbox/commentdoc.tsv'

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
        filename = f"../views/line/line-{line}.html"

        if line_no < 143:
            nextline = line_no + 1
        else: 
            nextline = line_no
        if line_no == 1:
            prevline = 1
        else:
            prevline = line_no - 1

        with open(filename, "w", encoding='utf-8') as f:
            f.write(f'<html>\n<head>\n\t<meta charset="UTF-8">\n\t<title>Line {line_no}</title>\n\t')
            f.write('<link rel="stylesheet" href="../linebyline.css">\n<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">\n\t<link href="https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">\n</head>\n<body>\n')
            f.write('<button class="button" onclick="document.location=\'https://lorehord.com/\'">Home</button><br>\n')
            f.write(f'<main>\n\t<h1>Widsið</h1>\n')            
            f.write(f'<h2>Line {line_no}</h2>\n')
            f.write(modified_html)
            f.write('\n\t<div class="button-container">\n\t\t')
            if line != 1:
                f.write(f'<a href="https://lorehord.com/views/line/line-{prevline}.html">Previous</a>')
            else:
                f.write('<a></a>')
            if line != 143:
                f.write(f'<a href="https://lorehord.com/views/line/line-{nextline}.html">Next</a>')
            else:
                f.write('<a></a>')
            f.write('\n\t</div>') 
            f.write('\n\t<h2 class="translation">Translation</h2><br>\n')
            f.write(f'\t<p class="translation">{html_line}</p>\n')
            f.write("\t</main>\n")
            f.write("\n\t<h2 class='translation'>Named Entities</h2>\n")
            
            comment_rows = comments_df[comments_df['Line'] == line_no]
            for _, row in comment_rows.iterrows():
                lemma = row['Lemma']
                ne_comment = row['Comment']
                f.write(f'\t<p class="translation">{lemma}: {ne_comment}</p>\n')

            f.write("\n\t</body>\n\t</html>")

        print(f"HTML file created as '{filename}'")
    else:
        print(f"No matching line found for line number {line_no}")
