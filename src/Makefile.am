## Process this file with automake to produce Makefile.in

XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
LEXEMES=lexemes/lexemes.tsv
STEMPARTS=stub-stem-inflections/acronym-stems.tsv \
		  stub-stem-inflections/adjective-stems.tsv \
		  stub-stem-inflections/digit-stubs.tsv \
		  stub-stem-inflections/digit-stems.tsv \
		  stub-stem-inflections/noun-stems.tsv \
		  stub-stem-inflections/numeral-stems.tsv \
		  stub-stem-inflections/particle-stems.tsv \
		  stub-stem-inflections/pronoun-stems.tsv \
		  stub-stem-inflections/symbol-stems.tsv \
		  stub-stem-inflections/51-stems.tsv \
		  stub-stem-inflections/verb-stems.tsv
INFLECTIONS=stub-stem-inflections/acro-inflections.tsv \
			stub-stem-inflections/adjective-inflections.tsv \
			stub-stem-inflections/digit-inflections.tsv \
			stub-stem-inflections/noun-inflections.tsv \
			stub-stem-inflections/numeral-inflections.tsv \
			stub-stem-inflections/particle-inflections.tsv \
			stub-stem-inflections/pronoun-inflections.tsv \
			stub-stem-inflections/symbol-inflections.tsv \
			stub-stem-inflections/verb-inflections.tsv
JOINS=attributes/boundaries.tsv \
	  attributes/origin.tsv \
	  attributes/plurale-tantum.tsv \
	  attributes/possessives.tsv \
	  attributes/pronunciation.tsv \
	  attributes/proper-classes.tsv \
	  attributes/paradigm-data.tsv \
	  attributes/particle-classes.tsv \
	  attributes/pronoun-classes.tsv \
	  attributes/symbol-classes.tsv \
	  attributes/semantic.tsv \
	  attributes/subcategories.tsv \
	  attributes/usage.tsv \
	  attributes/verb-arguments.tsv
SCIRPTS=tsv2lexc.py tsvjoin.py tsv_expand.py tsv2monodix.py \
		tsv2kotussanalista.py tsv2yaml.py \
		serialise-reweighter.py
FINNISC=\
		format_output.py \
		gradation.py \
		parse_csv_data.py \
		plurale_tantum.py \
		stub.py \
		guess_feats.py guess_new_class.py wordmap.py \
		omor_strings_io.py \
		apertium_formatter.py \
		ftb3_formatter.py
HFST_FLAGS=--verbose

if WANT_MORPHOLOGY
MAYBE_MORPHOLOGY=morphology.ftb3.hfst \
				 lemmatize.default.hfst
endif
if WANT_GENERATION
MAYBE_GENERATION=generation.ftb3.hfst
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
		   $(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) $(FINNISC) \
		   $(STEMPARTS) $(INFLECTIONS) \
		   voikko-fi_FI.pro index.xml

TESTS=format_output.py apertium_formatter.py

noinst_DATA=omorfi-ftb3.lexc omorfi.dix omorfi-sanalista.xml \
			omorfi-ftb3.reweight #gtd-tests-ftb3.yaml

if CAN_PYTHON
gtd-tests-ftb3.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/tsv2yaml.py -i $< -o $@ -f=ftb3 -v

omorfi-ftb3.reweight: serialise-reweighter.py format_output.py
	$(PYTHON) $(srcdir)/serialise-reweighter.py -v -f=ftb3 -o $@

joint.tsv: lexemes/lexemes.tsv $(JOINS)
	$(PYTHON) $(srcdir)/tsvjoin.py -v -i $< \
		-j $(srcdir)/attributes/boundaries.tsv \
		-j $(srcdir)/attributes/origin.tsv \
		-j $(srcdir)/attributes/plurale-tantum.tsv \
		-j $(srcdir)/attributes/possessives.tsv \
		-j $(srcdir)/attributes/pronunciation.tsv \
		-j $(srcdir)/attributes/particle-classes.tsv \
		-j $(srcdir)/attributes/proper-classes.tsv \
		-j $(srcdir)/attributes/pronoun-classes.tsv \
		-j $(srcdir)/attributes/semantic.tsv \
		-j $(srcdir)/attributes/subcategories.tsv \
		-j $(srcdir)/attributes/symbol-classes.tsv \
		-j $(srcdir)/attributes/usage.tsv \
		-j $(srcdir)/attributes/verb-arguments.tsv -o $@

master.tsv: joint.tsv
	$(PYTHON) $(srcdir)/tsv_expand.py \
		-j $(srcdir)/attributes/paradigm-data.tsv -v -i $< -o $@.unsrt
	head -n 1 < $@.unsrt > $@
	tail -n +2 < $@.unsrt | sort >> $@
	-rm -f $@.unsrt

stemparts.tsv: $(STEMPARTS)
	cat $^ | grep -v '^#' | fgrep -v 'HEADERS' | sort -k 1,1 > $@

inflections.tsv: $(INFLECTIONS)
	cat $^ | grep -v '^#' | fgrep -v 'HEADERS' | sort -k 1,1 > $@

omorfi-ftb3.lexc: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/tsv2lexc.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=ftb3

omorfi.dix: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/tsv2monodix.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@

omorfi-sanalista.xml: master.tsv
	$(PYTHON) $(srcdir)/tsv2kotussanalista.py -v -m master.tsv -o $@
else
gtd-tests-ftb3.yaml:
	echo "Lexical data preprocessing requires python3"
	false

omorfi-ftb3.reweight:
	echo "Lexical data preprocessing requires python3"
	false
	false

joint.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

master.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

stemparts.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

inflections.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

omorfi-ftb3.lexc:
	echo "Lexical data preprocessing requires python3"
	false

omorfi.dix: 
	echo "Lexical data preprocessing requires python3"
	false

omorfi-sanalista.xml: 
	echo "Lexical data preprocessing requires python3"
	false
endif

clean-local:
	-rm -f master.tsv joint.tsv stemparts.tsv inflections.tsv \
		omorfi.lexc omorfi.dix omorfi-sanalista.xml



# combine lexical data with phonology
temporary-ftb3.phon.hfst: morphology/omorfi-ftb3.lexc.hfst phonology/omorfi.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 morphology/omorfi-ftb3.lexc.hfst \
		-2 phonology/omorfi.twolc.hfst > $@

# make orthographical adjustments to phonemic version
temporary-ftb3.orth.hfst: temporary-ftb3.phon.hfst orthography/uppercase-$(UPPERCASING).hfst orthography/sh.hfst orthography/zh.hfst orthography/orthographic-variations.hfst orthography/hyphenations.hfst
	cat temporary-ftb3.phon.hfst |\
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
temporary-ftb3.tagged.hfst: temporary-ftb3.orth.hfst taghacks/rewrite-ftb3.hfst
	cat $< |\
		$(HINV) $(HFST_FLAGS) |\
		$(HIC) $(HFST_FLAGS) -2 taghacks/rewrite-ftb3.hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove word boundaries at this point
temporary-ftb3.unbounded.hfst: temporary-ftb3.tagged.hfst
	cat $< |\
		$(HMIN) $(HFST_FLAGS) > $@

if WANT_TAGWEIGHTS
# corpus trained weights
temporary-ftb3.tagweights-only.hfst: temporary-ftb3.unbounded.hfst weights/weights-ftb3.$(TAGWEIGHTS).hfst
	$(HCOMP) $(HFST_FLAGS) weights/weights-ftb3.$(TAGWEIGHTS).hfst temporary-ftb3.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

temporary-ftb3.tag-backoff.hfst: temporary-ftb3.unbounded.hfst weights/analysis-sigma-star.hfst
	$(HREW) -e -a 7.9 weights/analysis-sigma-star.hfst |\
		$(HCOMP) $(HFST_FLAGS) -1 temporary-ftb3.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# weight by combining trained and backoff model
# TODO: it includes lots of duplicate paths?
temporary-ftb3.tagweighted.hfst: temporary-ftb3.tagweights-only.hfst temporary-ftb3.tag-backoff.hfst
	$(HUN) $(HFST_FLAGS) temporary-ftb3.tagweights-only.hfst temporary-ftb3.tag-backoff.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@
else
# hand-written weights
temporary-ftb3.tagweighted.hfst: temporary-ftb3.unbounded.hfst lexical/omorfi-ftb3.reweight
	$(HREW) $(HFST_FLAGS) -T lexical/omorfi-ftb3.reweight temporary-ftb3.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@
endif

# the token weights from corpus without flags
if WANT_TOKENWEIGHTS
temporary-ftb3.tokenweights-only.hfst: temporary-ftb3.tagweighted.hfst weights/weights.$(TOKENWEIGHTS).hfst
	$(HCOMP) -F $(HFST_FLAGS) temporary-ftb3.tagweighted.hfst weights/weights-ftb3.$(TOKENWEIGHTS).hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# also include the tokens not in corpus, somehow
temporary-ftb3.token-backoff.hfst: temporary-ftb3.tagweighted.hfst weights/surface-sigma-star.hfst
	$(HREW) -e -a 5.267 weights/surface-sigma-star.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HCOMP) $(HFST_FLAGS) -1 temporary-ftb3.tagweighted.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# weight by combining trained and backoff model
# TODO: it includes lots of duplicate paths?
temporary-ftb3.tokenweighted.hfst: temporary-ftb3.tokenweights-only.hfst temporary-ftb3.token-backoff.hfst
	$(HUN) $(HFST_FLAGS) temporary-ftb3.tokenweights-only.hfst temporary-ftb3.token-backoff.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

else
temporary-ftb3.tokenweighted.hfst: temporary-ftb3.tagweighted.hfst
	cp -v $< $@
endif

temporary-ftb3.weighted.hfst: temporary-ftb3.tokenweighted.hfst
	cp -v $< $@

# create morphological analyzer
temporary.ftb3.hfst: temporary-ftb3.weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

morphology.ftb3.hfst: temporary.ftb3.hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
generation.ftb3.hfst: temporary-ftb3.unbounded.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

# lemmatization is a special case of tagset variant
lemmatize.default.hfst: temporary.ftb3.hfst taghacks/lemmatize-ftb3.relabel
	$(HSUB) $(HFST_FLAGS) -F $(srcdir)/taghacks/lemmatize-ftb3.relabel -i $< -o $@

# create one tape spell checker
dictionary.default.hfst: temporary.ftb3.hfst
	$(HPR) $(HFST_FLAGS) --project=upper -i $< -o $@

# create basic corpus tokeniser
# Should split at even-odd boundaries of word punct* word punct*
tokeniser.default.hfst: dictionary.default.hfst orthography/inconditionals.hfst\
						orthography/token.hfst
	$(HCAT) $(HFST_FLAGS) orthography/inconditionals.hfst \
		orthography/token.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 -o temporary-ftb3.inconditional-tokens.hfst
	$(HCAT) $(HFST_FLAGS) dictionary.default.hfst orthography/token.hfst \
		-o temporary-ftb3.word-tokens.hfst
	$(HCAT) temporary-ftb3.word-tokens.hfst temporary-ftb3.inconditional-tokens.hfst |\
		$(HREP) -f 1 -o $@

# hyphenation dictionary
hyphenation.dict.hfst: temporary-ftb3.orth.hfst hyphenation/hyphenation.rule.hfst
	cat temporary-ftb3.orth.hfst |\
		$(HPR) $(HFST_FLAGS) --project=lower |\
		$(HIC) $(HFST_FLAGS) -2 hyphenation/hyphenation.rule.hfst > $@

# voikko speller HFST beta targets
speller-omorfi.zhfst: dictionary.default.hfst spell-checking/error.edit-distance-2.hfst index.xml
	$(HF2F) -f olw < dictionary.default.hfst > acceptor.default.hfst
	$(HF2F) -f olw < spell-checking/error.edit-distance-2.hfst > errmodel.default.hfst
	$(ZIP) -v -9 $@ index.xml acceptor.default.hfst errmodel.default.hfst
	-rm -f acceptor.default.hfst errmodel.default.hfst


clean-local:
	-rm -f $(TARGETS) temporary-ftb3.*.hfst
