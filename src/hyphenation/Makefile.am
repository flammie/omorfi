## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose
HTWOLC_FLAGS=$(HFST_FLAGS) --resolve

EXTRA_DIST=hyphenate.twolc hyphenate.relabel
hfstfidatadir=$(datadir)/hfst/fi_FI/
hfstfidata_DATA=hyphenation.rule.hfst

hyphenation.twol.hfst: hyphenate.twolc
	$(HTWOLC) $(HTWOLC_FLAGS) -o $@ -i $<

hyphenation.rule.hfst: hyphenation.twol.hfst hyphenate.relabel
	$(HSPL) $(HFST_FLAGS) --prefix=hyphenation. --extension=.hfst $<
	$(HIX) $(HFST_FLAGS) hyphenation.1.hfst hyphenation.2.hfst |\
		$(HIX) $(HFST_FLAGS) hyphenation.3.hfst |\
		$(HSUB) $(HFST_FLAGS) -F $(srcdir)/hyphenate.relabel > $@

clean-local:
	-rm -f *.hfst *.ol
