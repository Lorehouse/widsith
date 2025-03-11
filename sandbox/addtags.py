from bs4 import BeautifulSoup

# Read the HTML file
with open('sidebyside.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize a line number counter
line_number = 1

# Find all <l> elements and wrap them in <div> tags with calculated line numbers
for line in soup.find_all('l'):
    line_text = ''.join(line.stripped_strings)
    new_div = soup.new_tag('div', **{'class': 'poetry-line', 'data-line': str(line_number)})
    new_div.string = line_text
    line.replace_with(new_div)
    line_number += 1

# Generate the modified HTML content
modified_html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poetry with Line Numbers</title>
    <style>
        .poetry-line {{
            position: relative;
            padding-right: 30px; /* Space for the line number */
        }}
        .poetry-line::after {{
            content: attr(data-line);
            position: absolute;
            right: 0;
            top: 0;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        .poetry-line:hover::after {{
            opacity: 1;
        }}
    </style>
</head>
<body>
    {soup.prettify()}
</body>
</html>
"""

# Save the modified HTML content to a file
with open('mode_poetry_with_line_numbers.html', 'w', encoding='utf-8') as file:
    file.write(modified_html_content)

print("HTML file created successfully!")
