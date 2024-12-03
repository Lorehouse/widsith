file = "add-comments.tsv"
data = open(file, encoding='utf-8')
data.readline()

lemma_forms = {}  # dict mapping lemmas to dict mapping forms/postag to list of lines
lemma_glosses = {}  # dict mapping lemmas to list of glosses

for line in data:
    lemma, gloss, form, line, posttag, comment = line.strip().split("\t")
    lemma_forms.setdefault(lemma, {}).setdefault((form, posttag), []).append(line)
    lemma_glosses.setdefault(lemma, set()).add(gloss)


print(lemma_forms)

for lemma, glosses in lemma_glosses.items():
    print(lemma, sorted(glosses))