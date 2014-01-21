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
temporary.phon.hfst: morphology/omorfi.lexc.hfst phonology/omorfi.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 morphology/omorfi.lexc.hfst \
		-2 phonology/omorfi.twolc.hfst > $@

# make orthographical adjustments to phonemic version
temporary.orth.hfst: temporary.phon.hfst orthography/uppercase-$(UPPERCASING).hfst orthography/sh.hfst orthography/zh.hfst orthography/orthographic-variations.hfst orthography/hyphenations.hfst
	cat temporary.phon.hfst |\
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
temporary.tagged.hfst: temporary.orth.hfst
	cat $< |\
		$(HINV) $(HFST_FLAGS) |\
		$(HIC) $(HFST_FLAGS) -2 taghacks/rewrite-$(TAG_FORMAT).hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove word boundaries at this point
temporary.unbounded.hfst: temporary.tagged.hfst
	cat $< |\
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
	$(HREW) $(HFST_FLAGS) -S '[GUESS=COMPOUND]' -a 16 < $< |\
		$(HREW) $(HFST_FLAGS) -S '[GUESS=DERIVE]' -a 16 |\
		$(HREW) $(HFST_FLAGS) -S '[STYLE=NONSTANDARD]' -a 32 |\
		$(HREW) $(HFST_FLAGS) -S '[STYLE=RARE]' -a 32 |\
		$(HREW) $(HFST_FLAGS) -S '[STYLE=DIALECTAL]' -a 32 |\
		$(HREW) $(HFST_FLAGS) -S '[STYLE=ARCHAIC]' -a 32 > $@
endif

# the token weights from corpus without flags
if WANT_TOKENWEIGHTS
temporary.tokenweights-only.hfst: temporary.tagweighted.hfst weights/weights.$(TOKENWEIGHTS).hfst
	$(HCOMP) -F $(HFST_FLAGS) temporary.tagweighted.hfst weights/weights.$(TOKENWEIGHTS).hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# also include the tokens not in corpus, somehow
temporary.token-backoff.hfst: temporary.tagweighted.hfst weights/surface-sigma-star.hfst
	$(HREW) -e -a 5.267 weights/surface-sigma-star.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
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

temporary.weighted.hfst: temporary.tokenweighted.hfst
	cp -v $< $@

# create morphological analyzer
temporary.$(TAG_FORMAT).hfst: temporary.weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

morphology.$(TAG_FORMAT).hfst: temporary.$(TAG_FORMAT).hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
generation.$(TAG_FORMAT).hfst: temporary.unbounded.hfst
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
		$(HREP) $(HFST_FLAGS) -f 1 -o temporary.inconditional-tokens.hfst
	$(HCAT) $(HFST_FLAGS) dictionary.default.hfst orthography/token.hfst \
		-o temporary.word-tokens.hfst
	$(HCAT) temporary.word-tokens.hfst temporary.inconditional-tokens.hfst |\
		$(HREP) -f 1 -o $@

# hyphenation dictionary
hyphenation.dict.hfst: temporary.orth.hfst hyphenation/hyphenation.rule.hfst
	cat temporary.orth.hfst |\
		$(HPR) $(HFST_FLAGS) --project=lower |\
		$(HIC) $(HFST_FLAGS) -2 hyphenation/hyphenation.rule.hfst > $@

# voikko speller HFST beta targets
speller-omorfi.zhfst: dictionary.default.hfst spell-checking/error.edit-distance-2.hfst index.xml
	$(HF2F) -f olw < dictionary.default.hfst > acceptor.default.hfst
	$(HF2F) -f olw < spell-checking/error.edit-distance-2.hfst > errmodel.default.hfst
	$(ZIP) -v -9 $@ index.xml acceptor.default.hfst errmodel.default.hfst
	-rm -f acceptor.default.hfst errmodel.default.hfst


clean-local:
	-rm -f $(TARGETS) temporary.*.hfst
