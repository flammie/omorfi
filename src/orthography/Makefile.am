## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose
HTWOLC_FLAGS=$(HFST_FLAGS) --resolve
HREGEX_FLAGS=$(HFST_FLAGS)

EXTRA_DIST=uppercase-word.twolc uppercase-first.twolc uppercase-no.twolc \
		   uppercase-any.twolc \
		   sh.regex zh.regex orthographic-variations.regex hyphenations.twolc \
		   inconditionals.regex token.regex

noinst_DATA=uppercase-word.hfst uppercase-first.hfst uppercase-no.hfst \
			uppercase-any.hfst \
			sh.hfst zh.hfst orthographic-variations.hfst \
			hyphenations.hfst inconditionals.hfst token.hfst


%.hfst: %.twolc
	$(HTWOLC) $(HTWOLC_FLAGS) -o $@ -i $<

%.hfst: %.regex 
	$(HREGEX) $(HREGEX_FLAGS) -i $< |\
		$(HMIN) $(HFST_FLAGS) -o $@

clean-local:
	-rm -f *.hfst *.ol

