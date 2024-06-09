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

#### 2024-6-7
* Reading Malone has me second guessing myself. He goes through his reasoning for various emendations he has made but do I want to render them? Do I want to use his edition? What about where it disagrees with my Wikisource edition?
* Got a third edition from sacred-texts.org as well to compare to. 

#### 2024-6-9
* Wrote a python script to add line numbers to <l> tags in the `word-tagging.xml`
* discovered only 143 lines when I expected 144 based on 5-line milestones in the `widsith_oe.xml` file.
* ran code on that to add line numbers, ran into namespace issue that ChatGPT helped with, added line numbers to that file too
* turns out the milestones were coming _before_ the line they referred to, when they seemed like they should come after, there are, in fact, 143 lines in Widsith. This was a stupid error I should have fixed easily early on. All is well now.
* Adding the line numbers will help with morphosyntactic tagging as I use the glossary, to make sure I'm in the correct line and working with the word Malone is referring to.
* `scripts/l-index.xml` and `scripts/l-nums.xml` will serve as raw records of the output of the codes 