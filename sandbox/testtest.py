import pandas as pd

# Load the comments TSV file without a header
comment_file_path = 'commentdoc.tsv'
comments_df = pd.read_csv(comment_file_path, sep='\t', encoding='utf-8', header=None)
print(comments_df.head())  # Print the first few rows to inspect the structure
