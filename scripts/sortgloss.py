import csv
import sys
from pyuca import Collator

c = Collator()

def sort_key(entry):
    return c.sort_key(entry[0])

if len(sys.argv) < 3:
    print("Usage: python script.py <inputfilename> <outputfilename>")
    sys.exit(1)

readfile = sys.argv[1]
writefile = sys.argv[2]

with open(readfile, "r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile, delimiter="\t")
    header = next(reader)
    rows_sorted = sorted(reader, key=sort_key)

with open(writefile, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerow(header)
    writer.writerows(rows_sorted)

print("Your file has been alphabetized.")