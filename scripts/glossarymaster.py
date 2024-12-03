from unorderedtsv import maketsv
from sortgloss import sortgloss
from tsvtohtml import tsv_to_html

def pipeline(startxml):
    glossunsort = maketsv(startxml)
    sorted = sortgloss(glossunsort)
    finalgloss = tsv_to_html(sorted, "../views/testglosspipeline.html")
    print(f"Your file has been created at {finalgloss}.")

pipeline("../word-tagging.xml")