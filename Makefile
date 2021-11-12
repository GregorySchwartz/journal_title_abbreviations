python = python

abbreviations.json: list.csv
	cat $< | sort | uniq >> uniques.csv
	rm $<
	sed -i '/^#/d' uniques.csv
	sed -i '/^$$/d' uniques.csv
	$(python) jsonify.py
	rm uniques.csv

list.csv: get_lists.py
	$(python) $<
	cat *_abbr.csv >> $@
	rm *_abbr.csv
