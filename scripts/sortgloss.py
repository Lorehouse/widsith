import csv
import sys
from pyuca import Collator


def main():
    if len(sys.argv) != 3:
        print("Usage: python sortgloss.py input_file.tsv output_file.tsv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f"Processing: {input_file}")
    sortgloss(input_file, output_file)

def sortgloss(infile, outfile):
    c = Collator()

    def sort_key(entry):
        return c.sort_key(entry[0])

    readfile = infile
    writefile = outfile

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

if __name__ == "__main__":
    main()