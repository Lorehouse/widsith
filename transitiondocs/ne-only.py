import csv

inputtsv = '../ne-gloss-sorted.tsv'
outputtsv = 'ne-only.tsv'
with open(inputtsv, 'r', newline='', encoding='utf-8') as infile, open(outputtsv, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile, delimiter='\t')
    writer = csv.writer(outfile, delimiter='\t')
    
    # Write headers to the output file
    headers = next(reader)
    writer.writerow(headers)
    
    # Iterate through each row in the input file
    for row in reader:
        # Check if the comment column is not "None"
        if row[5] != "None":
            writer.writerow(row)
print(f"Your file awaits at {outputtsv}.")