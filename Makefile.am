## Process this file with automake to produce Makefile.in
## Author: Tommi A Pirinen <flammie@iki.fi>
## Licence: GPL v3 (not newer)

EXTRA_DIST=README.bindist
## N.B. GNU standards COPYING AUTHORS INSTALL README NEWS need not be declared
SUBDIRS = src doc test man
ACLOCAL_AMFLAGS = -I m4

pkgconfigdir=$(datarootdir)/pkgconfig
pkgconfig_DATA=omorfi.pc

.PHONY: doc


bindist-dir: all
	if ! test -d $(PACKAGE)-binaries-$(VERSION) ; then \
		$(MKDIR_P) omorfi-binaries-$(VERSION) ;\
	fi
	cp README README.bindist omorfi-binaries-$(VERSION)
	cp src/*.hfst omorfi-binaries-$(VERSION)

ftb3-distdir: all
	if ! test -d $(PACKAGE)-ftb3-$(VERSION) ; then \
		$(MKDIR_P) $(PACKAGE)-ftb3-$(VERSION)  \
	fi
	cp -v src/omorfi-ftb3* $(PACKAGE)-ftb3-$(VERSION)/
	cp -vR src/scripts $(PACKAGE)-ftb3-$(VERSION)/

$(PACKAGE)-binaries-$(VERSION).tar.xz: bindist-dir
	tar Jcvf $@ $(PACKAGE)-binaries-$(VERSION)

$(PACKAGE)-ftb3-$(VERSION).tar.xz: ftb3-distdir
	tar Jcvf $@ $(PACKAGE)_ftb3-$(VERSION)

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
		-A src/paradigms/ -o paradigms.markdown -O paradigms/
	$(PYTHON) doc/generate-lexemes.py -L src/docs/lexemes.tsv \
		-l src/lexemes.tsv -o lexemes.markdown -O lexemes/
	doc/generate-statistics.bash test/
