JSONT = ../../jsont.py


questions.jsonl: colours.jsonl template1.jsont
	$(JSONT) --remove-line-endings template1.jsont $< > $@

clean:
	rm -f rquestions.jsonl
