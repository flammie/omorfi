## Process this file with automake to produce Makefile.in
## Author: Tommi A Pirinen <flammie@iki.fi>
## Licence: GPL v3 (not newer)

## N.B. GNU standards COPYING AUTHORS INSTALL README NEWS need not be declared

.PHONY: update

update: stuff.markdown paradigms.markdown lexemes.markdown statistics.markdown

stuff.markdown:
	PYTHONPATH=$(srcdir)/../src/python $(PYTHON) generate-stuffs.py \
			   -S src/docs/stuff.tsv -o stuff.markdown -O stuffs/

paradigms.markdown:
	$(PYTHON) generate-paradigms.py -P ../src/docs/paradigms.tsv \
		-A ../src/paradigms.tsv -o paradigms.markdown -O paradigms/

lexemes.markdown: generate-lexemes.py
	$(PYTHON) generate-lexemes.py -L ../src/docs/lexemes.tsv \
		-l ../src/generated/master.tsv -o lexemes.markdown -O lexemes/

statistics.markdown:
	./generate-statistics.bash ..

NEWS.markdown: ../NEWS
	cp -v $< $@

README.markdown: ../README
	cp -v $< $@

clean-local:
	if test -d com ; then \
		find com/github/flammie/omorfi -name '*.class' -delete ;\
	fi
