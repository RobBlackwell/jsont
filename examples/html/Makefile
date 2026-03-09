JSONT = ../../jsont.py

colours.html: colours.jsonl template1.jsont
	$(JSONT) template1.jsont --header header.jsont --trailer trailer.jsont $< --title "Colours" > $@

clean:
	rm -f *.html
