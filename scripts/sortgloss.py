import csv
from pyuca import Collator

def sortgloss(infile):
    c = Collator()

    def sort_key(entry):
        return c.sort_key(entry[0])

    readfile = infile
    writefile = "../transitiondocs/sortedgloss.tsv"

    with open(readfile, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile, delimiter="\t")
        header = next(reader)
        rows_sorted = sorted(reader, key=sort_key)

    with open(writefile, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile, delimiter="\t")
        writer.writerow(header)
        writer.writerows(rows_sorted)

    print("Your file has been alphabetized.")
    return writefile