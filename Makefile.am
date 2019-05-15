## Process this file with automake to produce Makefile.in
## Author: Tommi A Pirinen <flammie@iki.fi>
## Licence: GPL v3 (not newer)

## N.B. GNU standards COPYING AUTHORS INSTALL README NEWS need not be declared
SUBDIRS = src doc man docs
ACLOCAL_AMFLAGS = -I m4

pkgconfigdir=$(datarootdir)/pkgconfig
pkgconfig_DATA=omorfi.pc

.PHONY: doc

conversions:
	$(MAKE) -C src conversions

test:
	$(MAKE) check

clean-local:
	if test -d com ; then \
		find com/github/flammie/omorfi -name '*.class' -delete ;\
	fi
