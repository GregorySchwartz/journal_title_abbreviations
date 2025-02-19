abbrev = {}
containers = {}

import json, io

with io.open("uniques.csv", 'r', encoding='utf-8') as abbreviations:
    for line in abbreviations:
        keyval = line.lstrip().replace('"', '').rstrip().rstrip(';').split(';')
        if len(keyval) == 2:
            containers[keyval[0]] = keyval[1]

temp = {}
temp["container-title"] = containers
abbrev["default"] = temp

with io.open('abbreviations.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(abbrev, jsonfile, ensure_ascii=False, sort_keys=True, indent=4)
