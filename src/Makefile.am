## Process this file with automake to produce Makefile.in

XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
LEXEMES=lexemes/lexemes.tsv
STEMPARTS=stub-stem-inflection/acronym-stems.tsv \
		  stub-stem-inflection/adjective-stems.tsv \
		  stub-stem-inflection/digit-stubs.tsv \
		  stub-stem-inflection/digit-stems.tsv \
		  stub-stem-inflection/noun-stems.tsv \
		  stub-stem-inflection/numeral-stems.tsv \
		  stub-stem-inflection/particle-stems.tsv \
		  stub-stem-inflection/pronoun-stems.tsv \
		  stub-stem-inflection/symbol-stems.tsv \
		  stub-stem-inflection/51-stems.tsv \
		  stub-stem-inflection/verb-stems.tsv
INFLECTIONS=stub-stem-inflection/acro-inflections.tsv \
			stub-stem-inflection/adjective-inflections.tsv \
			stub-stem-inflection/digit-inflections.tsv \
			stub-stem-inflection/noun-inflections.tsv \
			stub-stem-inflection/numeral-inflections.tsv \
			stub-stem-inflection/particle-inflections.tsv \
			stub-stem-inflection/pronoun-inflections.tsv \
			stub-stem-inflection/symbol-inflections.tsv \
			stub-stem-inflection/verb-inflections.tsv
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
FORMAT_SCIRPTS=tagset_formatter.py \
			   apertium_formatter.py \
			   ftb3_formatter.py
CONVERSION_SCIRPTS=tsv2lexc.py tsvjoin.py tsv_expand.py tsv2monodix.py \
				   tsv2kotussanalista.py tsv2yaml.py \
				   serialise-reweighter.py
FIN_SCIRPTS=gradation.py \
			parse_csv_data.py \
			plurale_tantum.py \
			stub.py \
			guess_feats.py \
			guess_new_class.py \
			wordmap.py \
			omor_strings_io.py
SCIRPTS=$(FORMAT_SCIRPTS) $(CONVERSION_SCIRPTS) $(FIN_SCIRPTS)
HFST_FLAGS=--verbose

hfstfidatadir=$(datadir)/hfst/fi/
voikkosharedir=$(libdir)/voikko/3/

hfstfidata_DATA=morphology.ftb3.hfst \
				lemmatize.default.hfst \
				generation.ftb3.hfst \
				dictionary.default.hfst \
				tokeniser.default.hfst \
				hyphenation.dict.hfst 
voikkoshare_DATA=speller-omorfi.zhfst

EXTRA_DIST=\
		   $(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) \
		   $(STEMPARTS) $(INFLECTIONS) \
		   voikko-fi_FI.pro index.xml

TESTS=tagset_formatter.py apertium_formatter.py

noinst_DATA=omorfi-ftb3.lexc omorfi.dix omorfi-sanalista.xml \
			omorfi-ftb3.reweight #gtd-tests-ftb3.yaml

if CAN_PYTHON
gtd-tests-ftb3.yaml: $(top_srcdir)/test/gtd-tests.tsv $(FORMAT_SCIRPTS)
	$(PYTHON) $(srcdir)/tsv2yaml.py -i $< -o $@ -f=ftb3 -v

omorfi-ftb3.reweight: serialise-reweighter.py tagset_formatter.py $(FORMAT_SCIRPTS)
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

omorfi-ftb3.lexc: master.tsv stemparts.tsv inflections.tsv $(FORMAT_SCIRPTS)
	$(PYTHON) $(srcdir)/tsv2lexc.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=ftb3

omorfi-ftb3-phon.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r stub-phon -o $@

omorfi-ftb3-uppercase-any.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r uppercase-any -o $@


omorfi.dix: master.tsv stemparts.tsv inflections.tsv $(FORMAT_SCIRPTS)
	$(PYTHON) $(srcdir)/tsv2monodix.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@

omorfi-sanalista.xml: master.tsv $(FORMAT_SCIRPTS)
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

# compile lexc
%.lexc.hfst: %.lexc
	$(HLEXC) --Werror -o $@ $<

# compile twolc
%.twolc.hfst: %.twolc
	$(HTWOLC) -o $@ $<

# combine lexical data with phonology
temporary-ftb3.phon.hfst: omorfi-ftb3.lexc.hfst omorfi-ftb3-phon.twolc.hfst
	$(HINV) $(HFST_FLAGS) omorfi-ftb3.lexc.hfst |\
		$(HIC) $(HFST_FLAGS) -1 - -2 omorfi-ftb3-phon.twolc.hfst > $@

# make orthographical adjustments to phonemic version
temporary-ftb3.orth.hfst: temporary-ftb3.phon.hfst \
	omorfi-ftb3-uppercase-any.hfst orthography/sh.hfst orthography/zh.hfst orthography/orthographic-variations.hfst orthography/hyphenations.hfst
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
	-rm -f temporary-ftb3.*.hfst \
		master.tsv joint.tsv stemparts.tsv inflections.tsv \
		omorfi-ftb3.lexc omorfi.dix omorfi-sanalista.xml

