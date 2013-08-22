## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose
HTWOLC_FLAGS=$(HFST_FLAGS) --resolve
HREGEX_FLAGS=$(HFST_FLAGS) -S

EXTRA_DIST=rewrite-ftb3.twolc rewrite-omor.twolc rewrite-ktnkav.twolc

noinst_DATA=rewrite-ftb3.hfst rewrite-omor.hfst rewrite-ktnkav.hfst

%.hfst: %.twolc
	$(HTWOLC) $(HTWOLC_FLAGS) -o $@ -i $<

%.hfst: %.regex 
	$(HREGEX) $(HREGEX_FLAGS) -i $< |\
		$(HMIN) $(HFST_FLAGS) -o $@

clean-local:
	-rm -f *.hfst *.ol

