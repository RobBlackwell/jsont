JSONT = ../../jsont.py

colours.html: colours.jsonl template1.jsont
	$(JSONT) template1.jsont $< > $@

clean:
	rm -f *.html
