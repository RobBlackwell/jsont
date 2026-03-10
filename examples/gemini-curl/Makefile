JSONT = ../../jsont.py

script.sh: ../questions/questions.jsonl
	$(JSONT) --header shebang.jsont template.jsont $< > $@

clean:
	rm -f script.sh
