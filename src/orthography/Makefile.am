## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose
HTWOLC_FLAGS=$(HFST_FLAGS) --resolve
HREGEX_FLAGS=$(HFST_FLAGS)

EXTRA_DIST=uppercase-word.twolc uppercase-first.twolc uppercase-no.twolc \
		   sh.regex zh.regex orthographic-variations.regex hyphenations.twolc

noinst_DATA=uppercase-word.hfst uppercase-first.hfst uppercase-no.hfst \
			sh.hfst zh.hfst orthographic-variations.hfst \
			hyphenations.hfst


%.hfst: %.twolc
	$(HTWOLC) $(HTWOLC_FLAGS) -o $@ -i $<

sh.hfst: sh.regex 
	$(HREGEX) $(HREGEX_FLAGS) -i $(srcdir)/sh.regex |\
		$(HMIN) $(HFST_FLAGS) -o $@

zh.hfst: zh.regex 
	$(HREGEX) $(HREGEX_FLAGS) -i $(srcdir)/zh.regex |\
		$(HMIN) $(HFST_FLAGS) -o $@

orthographic-variations.hfst: orthographic-variations.regex 
	$(HREGEX) $(HREGEX_FLAGS) -i $(srcdir)/orthographic-variations.regex |\
		$(HMIN) $(HFST_FLAGS) -o $@

clean-local:
	-rm -f *.hfst *.ol

