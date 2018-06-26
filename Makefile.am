## Process this file with automake to produce Makefile.in
## Author: Tommi A Pirinen <flammie@iki.fi>
## Licence: GPL v3 (not newer)

## N.B. GNU standards COPYING AUTHORS INSTALL README NEWS need not be declared
SUBDIRS = doc man
ACLOCAL_AMFLAGS = -I m4

pkgconfigdir=$(datarootdir)/pkgconfig
pkgconfig_DATA=omorfi.pc

.PHONY: doc

conversions:
	$(MAKE) -C src conversions

test:
	$(MAKE) check

gh-pages: doc
	$(JEKYLL) build

doc:
	PYTHONPATH=$(srcdir)/src/python $(PYTHON) doc/generate-stuffs.py \
			   -S src/docs/stuff.tsv -o stuff.markdown -O stuffs/
	$(PYTHON) doc/generate-paradigms.py -P src/docs/paradigms.tsv \
		-A src/paradigms.tsv -o paradigms.markdown -O paradigms/
	$(PYTHON) doc/generate-lexemes.py -L src/docs/lexemes.tsv \
		-l src/lexemes.tsv -o lexemes.markdown -O lexemes/
	doc/generate-statistics.bash test/

clean-local:
	if test -d com ; then \
		find com/github/flammie/omorfi -name '*.class' -delete ;\
	fi
