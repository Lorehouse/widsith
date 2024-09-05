## This is My Thesis Progress Log

# Semester One

#### Stuff has, in fact, happened to date. I will record it eventually
* Chose poem
* Chose thesis advisor
* The gracious Dr. Crane agreed to be my second reader
* Met with Dr. Goering, started to get the poem into an xml doc and discussed POS tagging
* Got poem loosely marked up in XML in TEI format in `widsith_oe.xml`
* Acquired Kemp Malone's _Widsith_ book.
* Started reading about POS tagging
* Created `word-tagging.xml` in repo
* put each word in an individual tag like the Greek tagging that was done in the Beyond Translation repo
* Put the Brunetti CSV into an actual spreadsheet for reference
* Got horribly overwhelmed

#### 2024-05-31
* Started tagging some words
* UPOS tags do not match more specific OE tags
* Created a tag glossary, as it were, at the top of `word-tagging.xml`
* Will discuss tags with Dr. Goering on the next call. Also need to bring up with James
* Decided to keep notes in this repo so that I wouldn't have to switch back and forth between here and obsidian as I take notes. This file should still render in Obsidian okay though.

#### 2024-6-2
* Line 4 Kemp Malone has "hine" in line 5 where mine has "him". Probably should amend.
* Discuss gender. n-stem/a-stem/ja-stem (etc.) nouns with Nelson. Should these be tagged?
* How can I standardize tags?
* Add long vowel markings? Do that in a second pass or start now?
* Might be fun to add a "cognates" list later on
* Line 6 has onwocon in my text. Malone has that in the facsimile version but changes it to "on wocon" in his regularized text.

#### 2024-06-07
* Reading Malone has me second guessing myself. He goes through his reasoning for various emendations he has made but do I want to render them? Do I want to use his edition? What about where it disagrees with my Wikisource edition?
* Got a third edition from sacred-texts.org as well to compare to. 

#### 2024-06-09
* Wrote a python script to add line numbers to <l> tags in the `word-tagging.xml`
* discovered only 143 lines when I expected 144 based on 5-line milestones in the `widsith_oe.xml` file.
* ran code on that to add line numbers, ran into namespace issue that ChatGPT helped with, added line numbers to that file too
* turns out the milestones were coming _before_ the line they referred to, when they seemed like they should come after, there are, in fact, 143 lines in Widsith. This was a stupid error I should have fixed easily early on. All is well now.
* Adding the line numbers will help with morphosyntactic tagging as I use the glossary, to make sure I'm in the correct line and working with the word Malone is referring to.
* `scripts/l-index.xml` and `scripts/l-nums.xml` will serve as raw records of the output of the codes 

#### 2024-06-10
* Call with Nelson
    * O-stem nouns, ja-stem nouns, etc. refer to proto-Germanic inflections which no longer reflect the grammar of the language as currently written. This seems to
    * A Grammar of Old English, Hogg and Fulk in the Declensions Chapter.
    * Strong verbs (skip the numbering as that's really just relevant to proto-Germanic) and Weak verbs (Weak verbs classes are obvious from the infinitive)
    * Annotate his bigger changes but don't 
    * Chambers _Widsith_
    * _Anglo-Saxon Poetic Records_ Clasp and Dobbie -- More editorial consensus
    * Lit Review: Transmission history, Articles by Neidorf, Weiskott, and Pascual (very recent), John Niles paper on Widsith and the Anthropology of the Past (can be peculiar), scholarship on it in relationship to other texts.
    * People who have argued it's a poetic showcase of all the things the poet _could_ discuss.
    * Call in two weeks 2024-24-06 at 0915
* Questions for James
    * Alignment possibilities
    * What is necessary and practical
* Goals
    * A tagging TEAR (Let's try and get 30 lines by then)
    * Read three+ articles
    * Discuss at least two different versions

#### 2024-06-19
* Some progress on tagging, still making decisions (making strong or weak its own attribute on verb tags)
* Read [[neidorf_dating-of-widsith]], notes on `neidorf_dating-of-widsith.md`, need to read more
* Need to get other versions of the text to look at

#### 2024-06-23
* Started reading the [[weiskott_meter-of-widsith]] text, taking notes in `weiskott_meter-of-widsith.md`

#### 2024-06-24
* Call with Nelson today. Questions for call:
    * How much would it benefit me to get the Germanic philology any time audits?
    * þ vs ð practices in modern Old English orthographical practice
    * Line ten instrumental use?
    * Lines 11-13 no nominative? Or is it "eorl"? But that seems to be in a dependent clause.

#### 2024-06-25
* Call with James
    * Individual tokens vs forms vs lemmas

#### 2024-07-01
* After a hiatus for Tolkien and Tradition, I am starting to get the Malone and Chambers editions into xml
* [[Chambers]] Sometimes he hyphenates things like "Sæ-Denum" (28b) and it offers clarity that I really like.

#### 2024-08-16
* Returning from break, Chambers, Malone, my version, and now the Anglo-Saxon Poetic Record version is in xml for comparisons.
* Goals for this coming semester include creating a lit review of 10+ sources and a bibliography of 40+ sources found in `literature.md` [[literature]]
* emailed Dr. Scott Kleinman about DH resources
* Need to finish [[pascual_metrical-history]] reading
* start [[niles_anthropology-of-the-past]]

#### 2024-08-18
* Put in interlibrary loan requests for Liuzza _Old English Literature_, Niles _Old English heroic poems and the social life of texts_, Gillespie, and Fulk and Cain _A history of Old English literature_
* Looked at Old English Poetry in Facsimile site. It is ugly but it is aligned. The navigation is unclear, and there's no significant linking to other projects. 
* I'd love to see linked open data, especially geographical, for the time period and locations to tie into my tagging.

#### 2024-08-24
* Lost a lot of work, including line-numbering and all proper names that I'd filled in. 
* Ask Nelson, James about tagging compound words, specifically Sæ-denum (l 28)
* Got as far as Emerca (was hoping to finish "E" but didn't quite)
* CHecking everything into GitHub NOW

#### 2024-08-25
* Tagged named-entites through F
* Wrote script that generated word numbers for the word-tagging file
    * script is in `word-numbers_oe.py`
    * Currently saved as `w-nums.xml`
    * not combining yet with `word-tagging.xml` because the w-nums file lost my comments and the numbers aren't 00-padded. I'd like to talk to Nelson and/or James about whether or not they should be padded.
* started Wright's Old English Grammar

#### 2024-09-02
* What does "im" mean in the PARSE of the Brunetti Beowulf? All verbs are in infinitve but with "nne" ending.

#### 2024-09-03
* tagging proper nouns again
* Fascinating confusion around line 81 "WOW this is interesting. I had interpreted this on my read-through as "heroes" but Malone and some other writers identify this with the inhabitants ot the _Hala heret_ in _Jordebog_ of King Valdemar II of Denmark. Lappenberg 1838 and Grein read it as _Hæreþum_, identifying the tribe with the Charudes of classical antiquity (all in Malone 157). Mackie and Dobbie keep the MS reading and take it as the dpn "hæleþ" or hero, which I am adopting for the time being. This corresponds to the term hæþen in the same line, which is by some read as "heathen" and by others as a Norwegian tribe dwelling in the Hedemark."

#### 2024-09-05
* more proper nouns. Fun controversy over Heoden/Henden in line 21, where the word in the manuscript is very unclear. Malone makes an odd choice to have it as Henden but everyone else seems content to amend it to Heoden, of the Hild Saga. This is brought up in the Gillespie footnotes as well on pgs 69 and 73.
* logged proper nouns through I. Interesting questions arise and I have made comments.