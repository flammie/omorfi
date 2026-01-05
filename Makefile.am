## Process this file with automake to produce Makefile.in
## Author: Tommi A Pirinen <flammie@iki.fi>
## Licence: GPL v3 (not newer)

## N.B. GNU standards COPYING AUTHORS INSTALL README NEWS need not be declared
SUBDIRS = src man test docs
ACLOCAL_AMFLAGS = -I m4

pkgconfigdir=$(datarootdir)/pkgconfig
pkgconfig_DATA=omorfi.pc

omorfi-hfst-models-$(PACKAGE_VERSION).tar.xz:
	tar -C src/generated -cJvf $@ \
		omorfi.accept.hfst omorfi.analyse.hfst omorfi.describe.hfst \
		omorfi.generate.hfst omorfi_recased.analyse.hfst \
		omorfi_recased.describe.hfst omorfi.segment.hfst \
		omorfi.labelsegment.hfst


conversions:
	$(MAKE) -C src conversions

test:
	$(MAKE) check

clean-local:
	if test -d com ; then \
		find com/github/flammie/omorfi -name '*.class' -delete ;\
	fi
