from unorderedtsv import maketsv
from sortgloss import sortgloss
from tsvtohtml_ne import tsv_to_html

def pipeline(startxml):
    glossunsort = maketsv(startxml)
    sorted = sortgloss(glossunsort)
    finalgloss = tsv_to_html(sorted, "../views/test_ne_pipeline.html")
    print(f"Your file has been created at {finalgloss}.")

pipeline("../word-tagging.xml")