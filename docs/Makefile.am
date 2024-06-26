## Process this file with automake to produce Makefile.in
## Author: Tommi A Pirinen <flammie@iki.fi>
## Licence: GPL v3 (not newer)

## N.B. GNU standards COPYING AUTHORS INSTALL README NEWS need not be declared

.PHONY: update always-update

update: stuff.markdown paradigms.markdown lexemes.markdown statistics.markdown\
		mwe.markdown \
		NEWS.markdown README.markdown AUTHORS.markdown CITATION.markdown \
		CODE_OF_CONDUCT.markdown CONTRIBUTING.markdown COPYING.markdown \
		ChangeLog.markdown INSTALL.markdown THANKS.markdown \
		TODO.markdown

stuff.markdown: always-update
	PYTHONPATH=$(srcdir)/../src/python $(PYTHON) generate-stuffs.py \
			   -S $(srcdir)/../src/docs/stuff.tsv -o stuff.markdown

paradigms.markdown: always-update
	$(PYTHON) generate-paradigms.py -P ../src/docs/paradigms.tsv \
		-A ../src/paradigms.tsv -o paradigms.markdown 

lexemes.markdown: generate-lexemes.py
	$(PYTHON) $< -L ../src/docs/lexemes.tsv -l ../src/generated/master.tsv -o $@

mwe.markdown: generate-mwe.py
	$(PYTHON) $< -m ../src/generated/mwe-master.tsv -o $@

statistics.markdown: always-update
	./generate-statistics.bash ..

inflection-lists.markdown: generations.list
	while read w ; do \
		echo $w;\
		echo $w > word;\
		bash ../src/bash/generate-wordlist.sh word \
			gen/`echo $w | sed -e 's/^\(.\).*$/\1/' |\
					  tr '[:lower:]' '[:upper:]' |\
					  sed -e 's/ä/Ä/' -e 's/ö/Ö/'`/$w.markdown;\
	done < $<
	touch $@

noun-tables.markdown: generations.noun
	while read w ; do \
		$(PYTHON) ../src/omorfi-wikitable.py -u NOUN \
			-g ../src/generated/omorfi.generate.hfst \
			-i $w -o gen/`echo $w | sed -e 's/^\(.\).*$/\1/' |\
					  tr '[:lower:]' '[:upper:]' |\
					  sed -e 's/ä/Ä/' -e 's/ö/Ö/'`/$w_wikt.markdown; \
	done < $<
	touch $@

NEWS.markdown: ../NEWS
	cp -v $< $@

README.markdown: ../README.md
	cp -v $< $@

AUTHORS.markdown: ../AUTHORS
	cp -v $< $@

CITATION.markdown: ../CITATION
	cp -v $< $@

CODE_OF_CONDUCT.markdown: ../CODE_OF_CONDUCT.md
	cp -v $< $@

CONTRIBUTING.markdown: ../CONTRIBUTING.md
	cp -v $< $@

COPYING.markdown: ../COPYING
	cp -v $< $@

ChangeLog.markdown: 
	git log > ChangeLog.new
	cat ChangeLog.new ../ChangeLog.old > $@

INSTALL.markdown: ../INSTALL
	cp -v $< $@

THANKS.markdown: ../THANKS
	cp -v $< $@

TODO.markdown: ../TODO
	cp -v $< $@

doxygen:
	doxygen

clean-local:
	if test -d com ; then \
		find com/github/flammie/omorfi -name '*.class' -delete ;\
	fi
