import pandas as pd
import sys
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase


with open(sys.argv[1]) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(type(bib_database.entries))

print(len(bib_database.entries))

print(type(bib_database.entries[0]))

d  = bib_database.entries

new_bib = BibDatabase()

new_bib.entries = [dict(y) for y in set(tuple(x.items()) for x in d)]


print(new_bib.entries[0])

new_bib.entries = sorted(new_bib.entries, key= lambda x: x['title'])



print(len(new_bib.entries))

with open('bibtex.bib', 'w') as bibtex_file:
    bibtexparser.dump(new_bib, bibtex_file)
