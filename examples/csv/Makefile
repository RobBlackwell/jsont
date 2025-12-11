JSONT = ../../jsont.py

colours.csv: colours.jsonl template1.jsont
	$(JSONT) template1.jsont $< > $@

clean:
	rm -f *.csv
