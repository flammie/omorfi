## Process this file with automake to produce Makefile.in

# Parallel unsafe: lexical -> others -> . ($CWD)
SUBDIRS=lexical \
		morphology phonology orthography taghacks \
		probabilistics hyphenation spell-checking \
		. \
		scripts

HFST_FLAGS=--verbose

if WANT_MORPHOLOGY
MAYBE_MORPHOLOGY=morphology.$(TAG_FORMAT).hfst \
				 lemmatize.default.hfst
endif
if WANT_GENERATION
MAYBE_GENERATION=generation.$(TAG_FORMAT).hfst
endif
if WANT_DICTIONARY
MAYBE_DICTIONARY=dictionary.default.hfst \
				 tokeniser.default.hfst
endif
if WANT_HYPHENATION
MAYBE_HYPHENATION=hyphenation.dict.hfst
endif
if WANT_VOIKKO
MAYBE_VOIKKO=speller-omorfi.zhfst
voikkosharedir=$(libdir)/voikko/3/
voikkoshare_DATA=$(MAYBE_VOIKKO)
endif

TARGETS=$(MAYBE_MORPHOLOGY) $(MAYBE_GENERATION) $(MAYBE_DICTIONARY) \
		$(MAYBE_HYPHENATION) $(MAYBE_VOIKKO)
hfstfidatadir=$(datadir)/hfst/fi/
hfstfidata_DATA=$(MAYBE_MORPHOLOGY) $(MAYBE_GENERATION) $(MAYBE_DICTIONARY) \
				$(MAYBE_HYPHENATION)

EXTRA_DIST=\
		lemmatize.relabel \
		voikko-fi_FI.pro index.xml

# combine lexical data with phonology
temporary-$(TAG_FORMAT).phon.hfst: morphology/omorfi-$(TAG_FORMAT).lexc.hfst phonology/omorfi.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 morphology/omorfi-$(TAG_FORMAT).lexc.hfst \
		-2 phonology/omorfi.twolc.hfst > $@

# make orthographical adjustments to phonemic version
temporary-$(TAG_FORMAT).orth.hfst: temporary-$(TAG_FORMAT).phon.hfst orthography/uppercase-$(UPPERCASING).hfst orthography/sh.hfst orthography/zh.hfst orthography/orthographic-variations.hfst orthography/hyphenations.hfst
	cat temporary-$(TAG_FORMAT).phon.hfst |\
		$(HIC) $(HFST_FLAGS) -2 orthography/hyphenations.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HIC) $(HFST_FLAGS) -2 orthography/uppercase-$(UPPERCASING).hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T orthography/sh.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f ž -T orthography/zh.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HIC) $(HFST_FLAGS) -2 orthography/orthographic-variations.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# make tag adjustments to orthographical version
temporary-$(TAG_FORMAT).tagged.hfst: temporary-$(TAG_FORMAT).orth.hfst taghacks/rewrite-$(TAG_FORMAT).hfst
	cat $< |\
		$(HINV) $(HFST_FLAGS) |\
		$(HIC) $(HFST_FLAGS) -2 taghacks/rewrite-$(TAG_FORMAT).hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove word boundaries at this point
temporary-$(TAG_FORMAT).unbounded.hfst: temporary-$(TAG_FORMAT).tagged.hfst
	cat $< |\
		$(HMIN) $(HFST_FLAGS) > $@

if WANT_TAGWEIGHTS
# corpus trained weights
temporary-$(TAG_FORMAT).tagweights-only.hfst: temporary-$(TAG_FORMAT).unbounded.hfst weights/weights-$(TAG_FORMAT).$(TAGWEIGHTS).hfst
	$(HCOMP) $(HFST_FLAGS) weights/weights-$(TAG_FORMAT).$(TAGWEIGHTS).hfst temporary-$(TAG_FORMAT).unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

temporary-$(TAG_FORMAT).tag-backoff.hfst: temporary-$(TAG_FORMAT).unbounded.hfst weights/analysis-sigma-star.hfst
	$(HREW) -e -a 7.9 weights/analysis-sigma-star.hfst |\
		$(HCOMP) $(HFST_FLAGS) -1 temporary-$(TAG_FORMAT).unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# weight by combining trained and backoff model
# TODO: it includes lots of duplicate paths?
temporary-$(TAG_FORMAT).tagweighted.hfst: temporary-$(TAG_FORMAT).tagweights-only.hfst temporary-$(TAG_FORMAT).tag-backoff.hfst
	$(HUN) $(HFST_FLAGS) temporary-$(TAG_FORMAT).tagweights-only.hfst temporary-$(TAG_FORMAT).tag-backoff.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@
else
# hand-written weights
temporary-$(TAG_FORMAT).tagweighted.hfst: temporary-$(TAG_FORMAT).unbounded.hfst lexical/omorfi.reweight
	$(HREW) $(HFST_FLAGS) -T lexical/omorfi-$(TAG_FORMAT).reweight temporary-$(TAG_FORMAT).unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@
endif

# the token weights from corpus without flags
if WANT_TOKENWEIGHTS
temporary-$(TAG_FORMAT).tokenweights-only.hfst: temporary-$(TAG_FORMAT).tagweighted.hfst weights/weights.$(TOKENWEIGHTS).hfst
	$(HCOMP) -F $(HFST_FLAGS) temporary-$(TAG_FORMAT).tagweighted.hfst weights/weights-$(TAG_FORMAT).$(TOKENWEIGHTS).hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# also include the tokens not in corpus, somehow
temporary-$(TAG_FORMAT).token-backoff.hfst: temporary-$(TAG_FORMAT).tagweighted.hfst weights/surface-sigma-star.hfst
	$(HREW) -e -a 5.267 weights/surface-sigma-star.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HCOMP) $(HFST_FLAGS) -1 temporary-$(TAG_FORMAT).tagweighted.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# weight by combining trained and backoff model
# TODO: it includes lots of duplicate paths?
temporary-$(TAG_FORMAT).tokenweighted.hfst: temporary-$(TAG_FORMAT).tokenweights-only.hfst temporary-$(TAG_FORMAT).token-backoff.hfst
	$(HUN) $(HFST_FLAGS) temporary-$(TAG_FORMAT).tokenweights-only.hfst temporary-$(TAG_FORMAT).token-backoff.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

else
temporary-$(TAG_FORMAT).tokenweighted.hfst: temporary-$(TAG_FORMAT).tagweighted.hfst
	cp -v $< $@
endif

temporary-$(TAG_FORMAT).weighted.hfst: temporary-$(TAG_FORMAT).tokenweighted.hfst
	cp -v $< $@

# create morphological analyzer
temporary.$(TAG_FORMAT).hfst: temporary-$(TAG_FORMAT).weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

morphology.$(TAG_FORMAT).hfst: temporary.$(TAG_FORMAT).hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
generation.$(TAG_FORMAT).hfst: temporary-$(TAG_FORMAT).unbounded.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

# lemmatization is a special case of tagset variant
lemmatize.default.hfst: temporary.$(TAG_FORMAT).hfst taghacks/lemmatize-$(TAG_FORMAT).relabel
	$(HSUB) $(HFST_FLAGS) -F $(srcdir)/taghacks/lemmatize-$(TAG_FORMAT).relabel -i $< -o $@

# create one tape spell checker
dictionary.default.hfst: temporary.$(TAG_FORMAT).hfst
	$(HPR) $(HFST_FLAGS) --project=upper -i $< -o $@

# create basic corpus tokeniser
# Should split at even-odd boundaries of word punct* word punct*
tokeniser.default.hfst: dictionary.default.hfst orthography/inconditionals.hfst\
						orthography/token.hfst
	$(HCAT) $(HFST_FLAGS) orthography/inconditionals.hfst \
		orthography/token.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 -o temporary-$(TAG_FORMAT).inconditional-tokens.hfst
	$(HCAT) $(HFST_FLAGS) dictionary.default.hfst orthography/token.hfst \
		-o temporary-$(TAG_FORMAT).word-tokens.hfst
	$(HCAT) temporary-$(TAG_FORMAT).word-tokens.hfst temporary-$(TAG_FORMAT).inconditional-tokens.hfst |\
		$(HREP) -f 1 -o $@

# hyphenation dictionary
hyphenation.dict.hfst: temporary-$(TAG_FORMAT).orth.hfst hyphenation/hyphenation.rule.hfst
	cat temporary-$(TAG_FORMAT).orth.hfst |\
		$(HPR) $(HFST_FLAGS) --project=lower |\
		$(HIC) $(HFST_FLAGS) -2 hyphenation/hyphenation.rule.hfst > $@

# voikko speller HFST beta targets
speller-omorfi.zhfst: dictionary.default.hfst spell-checking/error.edit-distance-2.hfst index.xml
	$(HF2F) -f olw < dictionary.default.hfst > acceptor.default.hfst
	$(HF2F) -f olw < spell-checking/error.edit-distance-2.hfst > errmodel.default.hfst
	$(ZIP) -v -9 $@ index.xml acceptor.default.hfst errmodel.default.hfst
	-rm -f acceptor.default.hfst errmodel.default.hfst


clean-local:
	-rm -f $(TARGETS) temporary-$(TAG_FORMAT).*.hfst
