## Process this file with automake to produce Makefile.in

# Parallel unsafe: lexical -> others -> . ($CWD)
SUBDIRS=lexical \
		morphology phonology orthography\
		probabilistics hyphenation spell-checking \
		. \
		scripts

HFST_FLAGS=--verbose

if WANT_MORPHOLOGY
MAYBE_MORPHOLOGY=morphology.omor.hfst \
				 lemmatize.default.hfst
endif
if WANT_GENERATION
MAYBE_GENERATION=generation.omor.hfst
endif
if WANT_DICTIONARY
MAYBE_DICTIONARY=dictionary.default.hfst
endif
if WANT_HYPHENATION
MAYBE_HYPHENATION=hyphenation.dict.hfst
endif
if WANT_VOIKKO
MAYBE_VOIKKO=speller.zhfst
voikkosharedir=$(libdir)/voikko/2/mor-hfst-fi/
voikkoshare_DATA=$(MAYBE_VOIKKO) voikko-fi_FI.pro
endif

TARGETS=$(MAYBE_MORPHOLOGY) $(MAYBE_GENERATION) $(MAYBE_DICTIONARY) \
		$(MAYBE_HYPHENATION) $(MAYBE_VOIKKO)
hfstfidatadir=$(datadir)/hfst/fi/
hfstfidata_DATA=$(MAYBE_MORPHOLOGY) $(MAYBE_GENERATION) $(MAYBE_DICTIONARY) \
				$(MAYBE_HYPHENATION)

EXTRA_DIST=\
		eliminate-boundaries.relabel \
		lemmatize.relabel \
		voikko-fi_FI.pro index.xml

# combine lexical data with phonology
temporary.phon.hfst: morphology/omorfi.lexc.hfst phonology/omorfi.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 morphology/omorfi.lexc.hfst \
		-2 phonology/omorfi.twolc.hfst > $@

# make orthographical adjustments to phonemic version
temporary.orth.hfst: temporary.phon.hfst orthography/uppercase-$(UPPERCASING).hfst orthography/sh.hfst orthography/zh.hfst orthography/orthographic-variations.hfst orthography/hyphenations.hfst
	cat temporary.phon.hfst |\
		$(HIC) $(HFST_FLAGS) -2 orthography/hyphenations.hfst |\
		$(HIC) $(HFST_FLAGS) -2 orthography/uppercase-$(UPPERCASING).hfst |\
		$(HSUB) $(HFST_FLAGS) -f '@_EPSILON_SYMBOL_@:[CASECHANGE=NONE]' -t '[CASECHANGE=NONE]:@_EPSILON_SYMBOL_@' |\
		$(HSUB) $(HFST_FLAGS) -f '@_EPSILON_SYMBOL_@:[CASECHANGE=UPALL]' -t '[CASECHANGE=UPALL]:@_EPSILON_SYMBOL_@' |\
		$(HSUB) $(HFST_FLAGS) -f '@_EPSILON_SYMBOL_@:[CASECHANGE=UPFIRST]' -t '[CASECHANGE=UPFIRST]:@_EPSILON_SYMBOL_@' |\
		$(HSUB) $(HFST_FLAGS) -f š -T orthography/sh.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T orthography/zh.hfst |\
		$(HIC) $(HFST_FLAGS) -2 orthography/orthographic-variations.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove word boundaries at this point
temporary.unbounded.hfst: temporary.orth.hfst eliminate-boundaries.relabel
	cat $< |\
		$(HSUB) $(HFST_FLAGS) -F $(srcdir)/eliminate-boundaries.relabel |\
		$(HMIN) $(HFST_FLAGS) > $@

# note here: tag weights are made with regexps containing flags, 
if WANT_TAGWEIGHTS
temporary.tagweights-only.hfst: temporary.unbounded.hfst weights/weights.$(TAGWEIGHTS).hfst
	$(HCOMP) $(HFST_FLAGS) weights/weights.$(TAGWEIGHTS).hfst temporary.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

temporary.tag-backoff.hfst: temporary.unbounded.hfst weights/analysis-sigma-star.hfst
	$(HREW) -e -a 7.9 weights/analysis-sigma-star.hfst |\
		$(HCOMP) $(HFST_FLAGS) -1 temporary.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# weight by combining trained and backoff model
# TODO: it includes lots of duplicate paths?
temporary.tagweighted.hfst: temporary.tagweights-only.hfst temporary.tag-backoff.hfst
	$(HUN) $(HFST_FLAGS) temporary.tagweights-only.hfst temporary.tag-backoff.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

else
temporary.tagweighted.hfst: temporary.unbounded.hfst
	cp -v $< $@
endif

# the token weights from corpus without flags
if WANT_TOKENWEIGHTS
temporary.tokenweights-only.hfst: temporary.tagweighted.hfst weights/weights.$(TOKENWEIGHTS).hfst
	$(HCOMP) -F $(HFST_FLAGS) temporary.tagweighted.hfst weights/weights.$(TOKENWEIGHTS).hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# also include the tokens not in corpus, somehow
temporary.token-backoff.hfst: temporary.tagweighted.hfst weights/surface-sigma-star.hfst
	$(HREW) -e -a 5.267 weights/surface-sigma-star.hfst |\
		$(HCOMP) $(HFST_FLAGS) -1 temporary.tagweighted.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# weight by combining trained and backoff model
# TODO: it includes lots of duplicate paths?
temporary.tokenweighted.hfst: temporary.tokenweights-only.hfst temporary.token-backoff.hfst
	$(HUN) $(HFST_FLAGS) temporary.tokenweights-only.hfst temporary.token-backoff.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

else
temporary.tokenweighted.hfst: temporary.tagweighted.hfst
	cp -v $< $@
endif

# add unlikelihood to guesses by 1/65536
temporary.weighted.hfst: temporary.tokenweighted.hfst
	$(HREW) $(HFST_FLAGS) -S '[GUESS=COMPOUND]' -a 11.09 $< |\
		$(HREW) $(HFST_FLAGS) -S '[GUESS=DERIVE]' -a 11.09 -o $@

# create morphological analyzer
temporary.omor.hfst: temporary.weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

morphology.omor.hfst: temporary.omor.hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
generation.omor.hfst: temporary.unbounded.hfst
	$(HMIN) $(HFST_FLAGS) $< |\
		$(HF2F) $(HFST_FLAGS) -f olw -o $@

# lemmatization is a special case of tagset variant
lemmatize.default.hfst: temporary.omor.hfst lemmatize.relabel
	$(HSUB) $(HFST_FLAGS) -F $(srcdir)/lemmatize.relabel -i $< -o $@

# create one tape spell checker
dictionary.default.hfst: temporary.omor.hfst
	$(HPR) $(HFST_FLAGS) --project=upper -i $< -o $@

# hyphenation dictionary
hyphenation.dict.hfst: temporary.orth.hfst eliminate-boundaries.relabel hyphenation/hyphenation.rule.hfst
	cat temporary.orth.hfst |\
		$(HPR) $(HFST_FLAGS) --project=lower |\
		$(HIC) $(HFST_FLAGS) -2 hyphenation/hyphenation.rule.hfst |\
		$(HSUB) $(HFST_FLAGS) -F $(srcdir)/eliminate-boundaries.relabel > $@

# compatibility formats
%.openfst: %.hfst
	$(HF2F) $(HFST_FLAGS) -f openfst -i $< -o $@

%.sfst: %.hfst
	$(HF2F) $(HFST_FLAGS) -f sfst -i $< -o $@

# voikko speller HFST beta targets
speller.zhfst: dictionary.default.hfst spell-checking/error.edit-distance-2.hfst index.xml
	cp -f dictionary.default.hfst acceptor.default.hfst
	cp -f spell-checking/error.edit-distance-2.hfst errmodel.default.hfst
	$(ZIP) -v -9 $@ index.xml acceptor.default.hfst errmodel.default.hfst


clean-local:
	-rm -f $(TARGETS) temporary.*.hfst
