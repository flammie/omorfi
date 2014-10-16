## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose
HTWOLC_FLAGS=$(HFST_FLAGS) --resolve
HREGEX_FLAGS=$(HFST_FLAGS) -S

EXTRA_DIST=rewrite-ftb3.regex rewrite-omor.twolc rewrite-ktnkav.twolc \
		   rewrite-segments.twolc rewrite-google.regex \
		   rewrite-apertium.regex \
		   lemmatize-apertium.relabel lemmatize-ftb3.relabel \
		   lemmatize-google.relabel lemmatize-omor.relabel \
		   lemmatize-segments.relabel

noinst_DATA=rewrite-ftb3.hfst rewrite-omor.hfst rewrite-ktnkav.hfst \
			rewrite-segments.hfst rewrite-google.hfst \
			rewrite-apertium.hfst \
			lemmatize-apertium.relabel lemmatize-ftb3.relabel \
			lemmatize-google.relabel lemmatize-omor.relabel \
			lemmatize-segments.relabel

%.hfst: %.twolc
	$(HTWOLC) $(HTWOLC_FLAGS) -o $@ -i $<

%.hfst: %.regex 
	$(HREGEX) $(HREGEX_FLAGS) -i $< |\
		$(HMIN) $(HFST_FLAGS) -o $@

clean-local:
	-rm -f *.hfst *.ol

