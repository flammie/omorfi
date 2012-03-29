## Process this file with automake to produce Makefile.in
## Author: Tommi A Pirinen <tommi.pirinen@helsinki.fi>
## Licence: GPL v3 (not newer)

EXTRA_DIST=README.bindist
## N.B. GNU standards COPYING AUTHORS INSTALL README NEWS need not be declared
SUBDIRS = src doc test man

bindist: bindist-xz bindist-gzip

bindist-xz: bindist-dir
	tar Jcvf omorfi-$(VERSION)-automata.tar.xz omorfi-transducers-$(VERSION)

bindist-gzip: bindist-dir
	tar zcvf omorfi-$(VERSION)-automata.tar.gz omorfi-transducers-$(VERSION)

bindist-dir: all
	mkdir -p omorfi-automata-$(VERSION)
	cp README README.bindist omorfi-automata-$(VERSION)
	mkdir -p omorfi-automata-$(VERSION)/doc
	cp doc/*.rst omorfi-automata-$(VERSION)/doc/
	cp src/morphology.* src/hyphenation.* src/generation.* src/suggestion.* src/dictionary.* omorfi-automata-$(VERSION)
