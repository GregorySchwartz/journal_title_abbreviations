#! /usr/bin/env python

url = "https://raw.githubusercontent.com/JabRef/abbrv.jabref.org/main/journals/journal_abbreviations_"

sources = ["ams", "annee-philologique", "dainst", "entrez", "general", "geology_physics", "geology_physics_variations", "ieee", "ieee_strings", "lifescience", "mathematics", "mechanical", "medicus", "meteorology", "sociology", "webofscience-dots", "webofscience"]

import requests
for origin in sources:
    source_url = url + origin + ".csv"
    r = requests.get(source_url)
    fname = origin + "_abbr.csv"
    with open(fname, 'w') as abbrlist:
        abbrlist.write(r.text)

