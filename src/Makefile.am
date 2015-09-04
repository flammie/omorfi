## Process this file with automake to produce Makefile.in

# Settings
HFST_FLAGS=--verbose
voikkosharedir=$(libdir)/voikko/3/

# {{{ Files
# Origins
XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
# Lexicography
# 
LEXEMES=lexemes.tsv
# lexical features
LEMMA_JOINS=attributes/adjective-classes.tsv \
			attributes/boundaries.tsv \
			attributes/noun-classes.tsv \
			attributes/numeral-classes.tsv \
			attributes/plurale-tantum.tsv \
			attributes/possessives.tsv \
			attributes/pronunciation.tsv \
			attributes/proper-classes.tsv \
			attributes/particle-classes.tsv \
			attributes/pronoun-classes.tsv \
			attributes/symbol-classes.tsv \
			attributes/semantic.tsv \
			attributes/usage.tsv \
			attributes/verb-arguments.tsv
# paradigm features
PARADIGM_JOINS=paradigms/morphophonology.tsv \
			   paradigms/stub-deletions.tsv

# Morphology
# stem variants by deletion and concatenations
STEMPARTS=continuations/acronym-stems.tsv \
		  continuations/adjective-stems.tsv \
		  continuations/digit-stubs.tsv \
		  continuations/digit-stems.tsv \
		  continuations/noun-stems.tsv \
		  continuations/numeral-stems.tsv \
		  continuations/particle-stems.tsv \
		  continuations/pronoun-stems.tsv \
		  continuations/symbol-stems.tsv \
		  continuations/51-stems.tsv \
		  continuations/verb-stems.tsv
# suffixes by concatenations
INFLECTIONS=continuations/acro-inflections.tsv \
			continuations/adjective-inflections.tsv \
			continuations/digit-inflections.tsv \
			continuations/noun-inflections.tsv \
			continuations/numeral-inflections.tsv \
			continuations/particle-inflections.tsv \
			continuations/pronoun-inflections.tsv \
			continuations/symbol-inflections.tsv \
			continuations/verb-inflections.tsv

# }}}
#
# {{{Scripts 
# NB: (variable name = SCIRPTS cause automagic _SCRIPTS)
# tag formats
FORMAT_SCIRPTS=python/omorfi/apertium_formatter.py \
			   python/omorfi/ftb3_formatter.py \
			   python/omorfi/omor_formatter.py \
			   python/omorfi/giella_formatter.py \
			   python/omorfi/tdt_formatter.py \
			   python/omorfi/lexc_formatter.py \
			   python/omorfi/twolc_formatter.py \
			   python/omorfi/regex_formatter.py \
			   python/omorfi/monodix_formatter.py \
			   python/omorfi/formatters.py \
			   python/omorfi/kotus_sanalista_formatter.py
# file formats
GENERATOR_SCIRPTS=python/generate-lexcs.py \
				  python/generate-twolcs.py \
				  python/generate-regexes.py \
				  python/generate-reweights.py \
				  python/generate-edit-distance.py \
				  python/generate-monodix.py \
				  python/generate-yaml.py \
				  python/generate-kotus-sanalista.py
# Raw-ish database handling
DATABASE_SCIRPTS=python/tsvjoin.py \
				 python/tsv_expand.py
# Finnish specific lot
FIN_SCIRPTS=python/omorfi/gradation.py \
			python/omorfi/parse_csv_data.py \
			python/omorfi/plurale_tantum.py \
			python/omorfi/stub.py \
			python/omorfi/guess_feats.py \
			python/omorfi/guess_new_class.py \
			python/omorfi/wordmap.py \
			python/omorfi/string_manglers.py \
			python/omorfi/error_logging.py \
			python/omorfi/settings.py
SCIRPTS=$(FORMAT_SCIRPTS) $(GENERATOR_SCIRPTS) $(DATABASE_SCIRPTS) \
		$(FIN_SCIRPTS)
# }}}
#
# {{{Generated files
if WANT_HFST
GENERIC_AUTOMATA=generated/omorfi.accept.hfst \
				 generated/omorfi.lemmatise.hfst \
				 generated/omorfi.tokenise.hfst \
				 generated/omorfi.segment.hfst \
				 generated/omorfi.hyphenate-rules.hfst
# hyphenate-dict is unusable atm
GENERIC_GENERATED=generated/omorfi-uppercase-any.twolc \
				  generated/omorfi-uppercase-first.twolc \
				  generated/omorfi-recase-any.twolc \
				  generated/omorfi-phon.twolc \
				  generated/omorfi-zh.regex \
				  generated/omorfi-sh.regex \
				  generated/omorfi-orthographic-variations.regex \
				  generated/omorfi-remove-boundaries.regex
				  generated/omorfi-hyphens.twolc \
				  generated/omorfi-between-tokens.regex.hfst \
				  generated/omorfi.yaml \
				  generated/omorfi-token.regex.hfst
if WANT_FTB3
FTB3_AUTOMATA=generated/omorfi-ftb3.analyse.hfst \
			  generated/omorfi-ftb3.generate.hfst
FTB3_GENERATED=generated/omorfi-ftb3.lexc \
			   generated/omorfi-ftb3.reweight \
			   generated/omorfi-ftb3-tests.yaml \
			   generated/omorfi-ftb3-rewrite-tags.regex

endif
if WANT_FTB1
FTB1_AUTOMATA=generated/omorfi-ftb1.analyse.hfst

endif
if WANT_OMOR
OMOR_AUTOMATA=generated/omorfi-omor.analyse.hfst \
			  generated/omorfi-omor_recased.analyse.hfst \
			  generated/omorfi-omor.generate.hfst
OMOR_GENERATED=generated/omorfi-omor.lexc \
			   generated/omorfi-omor.reweight \
			   generated/omorfi-omor-tests.yaml \
			   generated/omorfi-omor-rewrite-tags.regex \
			   generated/omorfi-omor-between-tokens.regex.hfst \
			   generated/omorfi-omor-token.regex.hfst

endif
if WANT_APERTIUM
APE_AUTOMATA=generated/fin-automorf.hfst generated/fin-autogen.hfst
APE_GENERATED=generated/apertium-fin.fin.lexc \
			  generated/apertium-fin.fin.twolc \
			  generated/apertium-fin.fin.reweight \
			  generated/apertium-fin.fin.yaml
endif
if WANT_OMOR
GIELLA_AUTOMATA=generated/omorfi-giella.analyse.hfst \
				generated/omorfi-giella.generate.hfst
GIELLA_GENERATED=generated/omorfi-giella.lexc \
				 generated/omorfi-giella.twolc \
				 generated/omorfi-giella.reweight

endif
DB_GENERATED=generated/master.tsv generated/joint.tsv

endif # HFST
if CAN_VISLCG3
VISLCG3_GENERATED=generated/omorfi.cg3bin
endif
# }}}
# {{{Autotools install
# destnations directories for this stuff at the top of the file
pkgdata_DATA=$(GENERIC_AUTOMATA) $(FTB3_AUTOMATA) $(OMOR_AUTOMATA) \
				$(APE_AUTOMATA) $(VISLCG3_GENERATED) \
				$(FTB1_AUTOMATA)
voikkoshare_DATA=voikko/speller-omorfi.zhfst
pkgdata_DATA+=generated/master.tsv

bin_SCRIPTS=bash/omorfi-analyse-text.sh \
			bash/omorfi-analyse-tokenised.sh \
			bash/omorfi-generate.sh \
			bash/omorfi-spell.sh \
			bash/omorfi-segment.sh \
			bash/omorfi-hyphenate.sh \
			bash/omorfi-disambiguate-text.sh \
			python/omorfi-factorise.py \
			python/omorfi-analyse.py

pkgpython_PYTHON=python/omorfi/__init__.py \
				 python/omorfi/omorfi.py \
				 python/omorfi/settings.py


# These go into dist tarballs... which we no longer make
# N.B. for distcheck anyways
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(LEMMA_JOINS) $(PARADIGM_JOINS) \
		   $(SCIRPTS) \
		   $(STEMPARTS) $(INFLECTIONS) \
		   voikko/voikko-fi_FI.pro voikko/index.xml \
		   python/omorfi-factorise.py \
		   python/omorfi-analyse.py \
		   bash/validate-database.bash \
		   vislcg3/omorfi.cg3

# These are ran with make check. All modules should have stuff
TESTS=bash/validate-database.bash
XFAIL_TESTS=tdt_formatter.py

# python is anti-unit tests
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
AM_PY_LOG_FLAGS=-m omorfi
PY_LOG_COMPILER=$(PYTHON)

# These aren't installed but generated
noinst_DATA=generated/omorfi.dix generated/omorfi-sanalista.xml

# Things that make clean isn't smart enought to wipe
CLEANFILES=$(GENERIC_GENERATED) $(FTB3_GENERATED) $(DB_GENERATED) \
		   keys duplicate-keys lc-sort-keys
# }}}
#
# {{{GENERATING
if CAN_PYTHON
generated/timestamp:
	mkdir -p generated
	touch $@

# database to database
generated/joint.tsv: lexemes.tsv $(LEMMA_JOINS) generated/timestamp
	$(PYTHON) $(srcdir)/python/tsvjoin.py -v -i $< \
		-j $(srcdir)/attributes/adjective-classes.tsv \
		-j $(srcdir)/attributes/boundaries.tsv \
		-j $(srcdir)/attributes/noun-classes.tsv \
		-j $(srcdir)/attributes/numeral-classes.tsv \
		-j $(srcdir)/attributes/plurale-tantum.tsv \
		-j $(srcdir)/attributes/possessives.tsv \
		-j $(srcdir)/attributes/pronunciation.tsv \
		-j $(srcdir)/attributes/particle-classes.tsv \
		-j $(srcdir)/attributes/proper-classes.tsv \
		-j $(srcdir)/attributes/pronoun-classes.tsv \
		-j $(srcdir)/attributes/semantic.tsv \
		-j $(srcdir)/attributes/symbol-classes.tsv \
		-j $(srcdir)/attributes/usage.tsv \
		-j $(srcdir)/attributes/verb-arguments.tsv -o $@

generated/master.tsv: generated/joint.tsv
	$(PYTHON) $(srcdir)/python/tsv_expand.py \
		-j $(srcdir)/paradigms/morphophonology.tsv \
		-c $(srcdir)/paradigms/stub-deletions.tsv -v -i $< -o $@.unsrt
	head -n 1 < $@.unsrt > $@
	tail -n +2 < $@.unsrt | sort >> $@
	-rm -f $@.unsrt

generated/stemparts.tsv: $(STEMPARTS) generated/timestamp
	cat $^ | grep -v '^#' | fgrep -v 'HEADERS' | sort -k 1,1 > $@

generated/inflections.tsv: $(INFLECTIONS) generated/timestamp
	cat $^ | grep -v '^#' | fgrep -v 'HEADERS' | sort -k 1,1 > $@

# database to generic
generated/omorfi.lexc: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/python/generate-lexcs.py -v -m generated/master.tsv -p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=generic

generated/omorfi-phon.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -r phon -o $@

generated/omorfi-recase-any.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -r recase-any -o $@

generated/omorfi-uppercase-any.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -r uppercase-any -o $@

generated/omorfi-uppercase-first.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -r uppercase-first -o $@

generated/omorfi-hyphens.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -r hyphens -o $@

generated/omorfi-orthographic-variations.regex: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-regexes.py \
		-r orthographic-variations -o $@

generated/omorfi-zh.regex: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-regexes.py \
		-r zh -o $@

generated/omorfi-sh.regex: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-regexes.py \
		-r sh -o $@

generated/omorfi-remove-boundaries.regex: generated/timestamp
	$(PYTHON) $(srcdir)/python/generate-regexes.py \
		-r remove-boundaries -o $@

generated/omorfi-between-tokens.regex:
	$(PYTHON) $(srcdir)/python/generate-regexes.py \
		-r between-tokens -o $@

generated/omorfi-token.regex:
	$(PYTHON) $(srcdir)/python/generate-regexes.py \
		-r token -o $@

generated/omorfi-token-separator.regex:
	$(PYTHON) $(srcdir)/python/generate-regexes.py \
		-r token-separator -o $@

generated/omorfi-hyphenate.twolc:
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -f=ftb3 -r hyphenate -o $@

generated/omorfi-boundary.reweight: 
	$(PYTHON) $(srcdir)/python/generate-reweights.py -v -f=boundary -o $@

# database to omor 
generated/omorfi-omor-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/python/generate-yaml.py -i $< -o $@ -f=omor -v

generated/omorfi-omor.reweight: 
	$(PYTHON) $(srcdir)/python/generate-reweights.py -v -f=omor -o $@

generated/omorfi-omor.lexc: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/python/generate-lexcs.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=omor

generated/omorfi-omor-rewrite-tags.regex:
	$(PYTHON) $(srcdir)/python/generate-regexes.py -f=omor \
		-r rewrite-tags -o $@

# database to ftb3 
generated/omorfi-ftb3-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/python/generate-yaml.py -i $< -o $@ -f=ftb3 -v

generated/omorfi-ftb3.reweight:
	$(PYTHON) $(srcdir)/python/generate-reweights.py -v -f=ftb3 -o $@

generated/omorfi-ftb3.lexc: generated/master.tsv generated/stemparts.tsv generated/inflections.tsv
	$(PYTHON) $(srcdir)/python/generate-lexcs.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=ftb3

generated/omorfi-ftb3-rewrite-tags.regex:
	$(PYTHON) $(srcdir)/python/generate-regexes.py -f=ftb3 \
		-r rewrite-tags -o $@

generated/omorfi-ftb3-lemmatise.regex:
	$(PYTHON) $(srcdir)/python/generate-regexes.py -f=ftb3 \
		-r lemmatise -o $@

# database to apertium
generated/apertium-fin.fin.lexc: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/python/generate-lexcs.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=apertium

generated/apertium-fin.fin.twolc:
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -v -f=apertium -r apertium -o $@

generated/apertium-fin.fin.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/python/generate-yaml.py -i $< -o $@ -f=apertium -v

# database to monodix
generated/omorfi.dix: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/python/generate-monodix.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@

# database to giella
generated/omorfi-giella.lexc: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/python/generate-lexcs.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=giella



# database (back) to kotus
generated/omorfi-sanalista.xml: generated/master.tsv
	$(PYTHON) $(srcdir)/python/generate-kotus-sanalista.py -v -m generated/master.tsv -o $@
endif
# }}}
#
# {{{ COMPILATION RECIPES
# compile lexc
%.lexc.hfst: %.lexc
	$(HLEXC) --Werror -o $@ $<

# compile twolc
%.twolc.hfst: %.twolc
	$(HTWOLC) $(HFST_FLAGS) --resolve -o $@ $<

%.regex.hfst: %.regex
	$(HREGEX) $(HFST_FLAGS) --semicolon -j -i $< |\
		$(HMIN) $(HFST_FLAGS) -o $@

%.hfst: %.txt
	$(HT2F) $< -o $@

# }}}
#
# {{{ GENERIC tagsetless stuff
# word-boundary huphens
generated/temporary.hyphenated.hfst: generated/omorfi.lexc.hfst \
	generated/omorfi-hyphens.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/omorfi-hyphens.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

generated/temporary.boundary-weights.hfst: generated/temporary.hyphenated.hfst \
		generated/omorfi-boundary.reweight
	$(HREW) -T generated/omorfi-boundary.reweight $< -o $@ 

# spelling variations
generated/temporary.relaxed.hfst: generated/temporary.boundary-weights.hfst \
	generated/omorfi-sh.regex.hfst \
	generated/omorfi-zh.regex.hfst \
	generated/omorfi-orthographic-variations.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-orthographic-variations.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T generated/omorfi-sh.regex.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T generated/omorfi-zh.regex.hfst -o $@

# case variations
generated/temporary.orth.hfst: generated/temporary.relaxed.hfst \
	generated/omorfi-uppercase-first.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/omorfi-uppercase-first.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# remove remaining morph boundaries at this point
generated/temporary.unbounded.hfst: generated/temporary.orth.hfst |\
	generated/omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@


# lemmatisation is now built by messing with ftb3
generated/omorfi.lemmatise.hfst: generated/temporary.ftb3.hfst generated/omorfi-ftb3-lemmatise.regex.hfst
	$(HCOMP) $(HFST_FLAGS) $< generated/omorfi-ftb3-lemmatise.regex.hfst |\
		$(HF2F) -f olw -o $@

# 
generated/omorfi.segment.hfst: generated/temporary.unbounded.hfst
	$(HINV) $< | $(HF2F) -f olw -o $@

# create one tape spell checker
generated/omorfi.accept.hfst: generated/temporary.ftb3.hfst
	$(HPR) $(HFST_FLAGS) --project=upper -i $< |\
		$(HMIN) $(HFST_FLAGS) --encode-weights |\
		$(HF2F) $(HFST_FLAGS) -f olw -o $@

# create basic corpus tokeniser
# Should split at even-odd boundaries of word punct* word punct*

generated/omorfi.tokenise.hfst: generated/omorfi.accept.hfst \
					  generated/omorfi-between-tokens.regex.hfst \
					  generated/omorfi-token.regex.hfst \
					  generated/omorfi-token-separator.regex.hfst
	$(HCAT) $(HFST_FLAGS) generated/omorfi-token.regex.hfst \
		generated/omorfi-token-separator.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) -o generated/omorfi.nondict-token.hfst
	$(HCAT) $(HFST_FLAGS) generated/omorfi-between-tokens.regex.hfst \
		generated/omorfi-token-separator.regex.hfst -o generated/omorfi-token-joiner.hfst
	$(HCAT) $(HFST_FLAGS) generated/omorfi.nondict-token.hfst \
		generated/omorfi-token-joiner.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 -o $@

# hyphenation dictionary
generated/omorfi.hyphenate-dict.hfst: generated/temporary-ftb3.orth.hfst \
						generated/omorfi-hyphenate.twolc.hfst
	cat generated/temporary-ftb3.orth.hfst |\
		$(HPR) -p lower |\
		$(HIC) $(HFST_FLAGS) -2 generated/omorfi-hyphenate.twolc.hfst |\
		$(HF2F) $(HFST_FLAGS) -f olw > $@

generated/omorfi.hyphenate-rules.hfst: generated/omorfi-hyphenate.twolc.hfst
	$(HSPL) generated/omorfi-hyphenate.twolc.hfst --prefix generated/omorfi.hyphenate-rules-
	$(HIX) generated/omorfi.hyphenate-rules-1.hfst generated/omorfi.hyphenate-rules-2.hfst |\
		$(HIX) - generated/omorfi.hyphenate-rules-3.hfst |\
		$(HMIN) |\
		$(HF2F) -f olw > $@

# }}}
# {{{FTB3 compilation

# word-boundary huphens
generated/temporary-ftb3.hyphenated.hfst: generated/omorfi-ftb3.lexc.hfst \
	generated/omorfi-hyphens.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/omorfi-hyphens.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# spelling variations
generated/temporary-ftb3.relaxed.hfst: generated/temporary-ftb3.hyphenated.hfst \
	generated/omorfi-sh.regex.hfst \
	generated/omorfi-zh.regex.hfst \
	generated/omorfi-orthographic-variations.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-orthographic-variations.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T generated/omorfi-sh.regex.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T generated/omorfi-zh.regex.hfst -o $@

# case variations
generated/temporary-ftb3.orth.hfst: generated/temporary-ftb3.relaxed.hfst \
	generated/omorfi-uppercase-first.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/omorfi-uppercase-first.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# make tag adjustments
generated/temporary-ftb3.tagged.hfst: generated/temporary-ftb3.orth.hfst \
	generated/omorfi-ftb3-rewrite-tags.regex.hfst
	cat $< |\
		$(HINV) $(HFST_FLAGS) |\
		$(HCOMP) $(HFST_FLAGS) -2 generated/omorfi-ftb3-rewrite-tags.regex.hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove remaining morph boundaries at this point
generated/temporary-ftb3.unbounded.hfst: generated/temporary-ftb3.tagged.hfst |\
	generated/omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# hand-written weights for ftb3
generated/temporary-ftb3.tagweighted.hfst: generated/temporary-ftb3.unbounded.hfst generated/omorfi-ftb3.reweight
	$(HREW) $(HFST_FLAGS) -T generated/omorfi-ftb3.reweight generated/temporary-ftb3.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# create morphological analyzer
generated/temporary.ftb3.hfst: generated/temporary-ftb3.tagweighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

# finalising
generated/omorfi-ftb3.analyse.hfst: generated/temporary.ftb3.hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
generated/omorfi-ftb3.generate.hfst: generated/temporary-ftb3.hyphenated.hfst \
	generated/omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-remove-boundaries.regex.hfst |\
		$(HF2F) $(HFST_FLAGS) -f olw  -o $@

# }}}
#
# {{{ FTB1 compilation
# The FTB1 Makefile fragment was written by Miikka Silfverberg, with
# file naming changed to match omorfi structure a bit by Flammie.
#
# This Makefile builds morphology.ftb1.ol which is the lookup
# optimized FinnTreeBank 1 version of Omorfi.
#
# The ftb1-version of Omorfi is built from omorfi-omor.analyse.hfst
# which can be found in the directory omorfi/src/generated.  You
# should copy omorfi-omor.analyse.hfst into this directory.
#
# This Makefile was tested using Omorfi revision
# 20141014-213-g12c4345.
#
# Differences between regular Omorfi and the ftb1 version: 
#
# - Ftb1 uses a different label set than Omorfi.
#
# - Compound analyses where some of the parts are proper nouns are
#   filtered out.
#
# - Minen-derivatives are analyzed as nouns with a noun lemma and
#   Lex_Minen tag.
#
# - Sti-derivatives are analyzed as adverbs with an adverb lemma and
#   Lex_Sti tags.
#
# - Only the last part of a compound gets analyzed. The earlier parts
#   remain unanalyzed but a compound border marker '#' is inserted
#   between compound parts.
#
# Author: Miikka Silfverberg 2015

# Convert omorfi to tropical format via sfst format in order
# to get rid of weights and add optional upper casing for all
# words.
generated/ftb1-morphology.omor.hfst: generated/omorfi-omor.analyse.hfst generated/ftb1-capitalize.regex.hfst
	hfst-fst2fst -S $< | \
	hfst-fst2fst -t | \
	hfst-compose -1 generated/ftb1-capitalize.regex.hfst | \
	hfst-minimize -o $@

# Add proper noun analyses with [LEX=MINEN] tags for all
# Minen-derivatives. We need to change the lemma of the
# analysis as well as the tags. Therefore we first need to
# extract stems and re-build the analyses using the stems and
# inflectional suffixes.
generated/ftb1-morphology.omor.hfst.minen: generated/ftb1-morphology.omor.hfst generated/ftb1-minen_analyzer.hfst
	hfst-disjunct -1 generated/ftb1-morphology.omor.hfst -2 generated/ftb1-minen_analyzer.hfst |\
	hfst-minimize > $@

# Get all word forms of the lemma 'miettiminen'.
generated/ftb1-miettiminen_omorfi.hfst: generated/ftb1-morphology.omor.hfst generated/ftb1-miettiminen.regex.hfst
	hfst-compose -F -1 $< -2 generated/ftb1-miettiminen.regex.hfst | \
	hfst-minimize > $@

# Get inflectional suffixes of all front vowel
# Minen-derivatives.
generated/ftb1-front_minen_omorfi.hfst: generated/ftb1-miettiminen_omorfi.hfst generated/ftb1-rm_mietti.regex.hfst \
generated/ftb1-rm_mietti.inv.regex.hfst
	hfst-compose -1 generated/ftb1-rm_mietti.inv.regex.hfst -2 $< |\
	hfst-compose -2 generated/ftb1-rm_mietti.regex.hfst |\
	hfst-minimize > $@

# Get all word forms of the lemma 'avaaminen'.
generated/ftb1-avaaminen_omorfi.hfst: generated/ftb1-morphology.omor.hfst generated/ftb1-avaaminen.regex.hfst
	hfst-compose -F -1 $< -2 generated/ftb1-avaaminen.regex.hfst | \
	hfst-minimize > $@

# Get inflectional suffixes of all back vowel
# Minen-derivatives.
generated/ftb1-back_minen_omorfi.hfst: generated/ftb1-avaaminen_omorfi.hfst generated/ftb1-rm_avaa.regex.hfst \
generated/ftb1-rm_avaa.inv.regex.hfst
	hfst-compose -1 generated/ftb1-rm_avaa.inv.regex.hfst -2 $< |\
	hfst-compose -2 generated/ftb1-rm_avaa.regex.hfst |\
	hfst-minimize > $@

# Get inflectional suffixes of all Minen-derivatives.
generated/ftb1-minen_omorfi.hfst: generated/ftb1-back_minen_omorfi.hfst generated/ftb1-front_minen_omorfi.hfst
	hfst-disjunct -1 generated/ftb1-back_minen_omorfi.hfst -2 generated/ftb1-front_minen_omorfi.hfst | \
	hfst-minimize > $@

# Get all Va-derivatives of verbs.
generated/ftb1-va_derivatives.hfst: generated/ftb1-morphology.omor.hfst generated/ftb1-va_der.regex.hfst
	hfst-compose -F -1 $< -2 generated/ftb1-va_der.regex.hfst | \
	hfst-project -p input | \
	hfst-minimize > $@

# Get the stems of all Va-derivatives of verbs (these stems
# are also stems [minus -minen] for Minen-derivatives).
generated/ftb1-va_stems.hfst: generated/ftb1-va_derivatives.hfst generated/ftb1-rm_va.regex.hfst generated/ftb1-rm_va.regex.inv.hfst
	hfst-compose -2 generated/ftb1-rm_va.regex.hfst -1 $< | \
	hfst-compose -1 generated/ftb1-rm_va.regex.inv.hfst | \
	hfst-minimize > $@

# Form complete analyses for Minen-derivatives by concatenating
# stems, suffixes and markers.
generated/ftb1-minen_analyzer.hfst: generated/ftb1-minen_omorfi.hfst generated/ftb1-va_stems.hfst generated/ftb1-minen_marker.regex.hfst \
generated/ftb1-word_id.regex.hfst
	hfst-concatenate -1 generated/ftb1-va_stems.hfst -2 generated/ftb1-minen_omorfi.hfst |\
	hfst-concatenate -2 generated/ftb1-minen_marker.regex.hfst |\
	hfst-concatenate -1 generated/ftb1-word_id.regex.hfst |\
	hfst-minimize > $@

# Add proper adverb analyses with [LEX=STI] tags for all
# Sti-derivatives. We need to change the lemma of the
# analysis as well as the tags. Therefore we first need to
# extract stems and re-build the analyses using the stems and
# inflectional suffixes.
generated/ftb1-morphology.omor.hfst.minen.sti: generated/ftb1-sti_analyzer.hfst generated/ftb1-morphology.omor.hfst.minen
	hfst-disjunct -1 generated/ftb1-sti_analyzer.hfst -2 generated/ftb1-morphology.omor.hfst.minen |\
	hfst-minimize > $@

# Get all word forms of the lemma 'ikuisesti'.
generated/ftb1-ikuisesti_omorfi.hfst: generated/ftb1-morphology.omor.hfst.minen  generated/ftb1-ikuisesti.regex.hfst
	hfst-compose -1 $< -2 generated/ftb1-ikuisesti.regex.hfst |\
	hfst-minimize > $@

# Get all word forms of the lemma 'pimeästi'.
generated/ftb1-pimeasti_omorfi.hfst: generated/ftb1-morphology.omor.hfst.minen  generated/ftb1-pimeasti.regex.hfst
	hfst-compose -1 $< -2 generated/ftb1-pimeasti.regex.hfst |\
	hfst-minimize > $@

# Get inflectional suffixes of all front vowel
# Sti-derivatives.
generated/ftb1-front_sti_omorfi.hfst: generated/ftb1-pimeasti_omorfi.hfst generated/ftb1-rm_pimea.regex.hfst \
generated/ftb1-rm_pimea.inv.regex.hfst
	hfst-compose -1 generated/ftb1-rm_pimea.inv.regex.hfst -2 $< |\
	hfst-compose -2 generated/ftb1-rm_pimea.regex.hfst |\
	hfst-minimize > $@

# Get inflectional suffixes of all back vowel
# Sti-derivatives.
generated/ftb1-back_sti_omorfi.hfst: generated/ftb1-ikuisesti_omorfi.hfst generated/ftb1-rm_ikuise.regex.hfst \
generated/ftb1-rm_ikuise.inv.regex.hfst
	hfst-compose -1 generated/ftb1-rm_ikuise.inv.regex.hfst -2 $< |\
	hfst-compose -2 generated/ftb1-rm_ikuise.regex.hfst |\
	hfst-minimize > $@

# Get inflectional suffixes of all Sti-derivatives.
generated/ftb1-sti_omorfi.hfst: generated/ftb1-front_sti_omorfi.hfst generated/ftb1-back_sti_omorfi.hfst
	hfst-disjunct -1 generated/ftb1-front_sti_omorfi.hfst -2 generated/ftb1-back_sti_omorfi.hfst |\
	hfst-minimize > $@

# Get all sen (singular genitive) forms of adjective.
generated/ftb1-sen_adjectives.hfst: generated/ftb1-morphology.omor.hfst.minen generated/ftb1-sen_adj.regex.hfst
	hfst-compose -1 $< -2 generated/ftb1-sen_adj.regex.hfst |\
	hfst-project -p input |\
	hfst-minimize > $@

# Get the stems of all singular genitive adjectives (these
# stems are also stems [minus -sti] for Sti-derivatives).
generated/ftb1-sen_stems.hfst: generated/ftb1-sen_adjectives.hfst generated/ftb1-rm_n.regex.hfst generated/ftb1-rm_n.inv.regex.hfst
	hfst-compose -1 $< -2 generated/ftb1-rm_n.regex.hfst |\
	hfst-compose -1 generated/ftb1-rm_n.inv.regex.hfst |\
	hfst-minimize > $@

# Form complete analyses for Sti-derivatives by concatenating
# stems, suffixes and markers.
generated/ftb1-sti_analyzer.hfst: generated/ftb1-sen_stems.hfst generated/ftb1-sti_omorfi.hfst generated/ftb1-sti_marker.regex.hfst \
generated/ftb1-word_id.regex.hfst
	hfst-concatenate -1 generated/ftb1-sen_stems.hfst -2 generated/ftb1-sti_omorfi.hfst |\
	hfst-concatenate -2 generated/ftb1-sti_marker.regex.hfst |\
	hfst-concatenate -1 generated/ftb1-word_id.regex.hfst |\
	hfst-minimize > $@

# 1. Remove compounds where some parts are proper nouns. They are
# problematic for disambiguation and almost never occur.
# 2. Replace dash compound markers so that the type of the dash
# can be identified on the output-level. This is needed for
# recovering the correct dashes later.
# 3. Remove [INF=MINEN] analyses that don't occur in ftb1.
# 4. Remove {hyph?} markers that omorfi contains on the input
# side (they're a bug and shouldn't be there).
generated/ftb1-morphology.omor.lex.hfst: generated/ftb1-morphology.omor.hfst.minen.sti \
generated/ftb1-rm_prop_compound.regex.hfst generated/ftb1-rm_infminen.regex.hfst generated/ftb1-rm_dummy_hyph.regex.hfst \
generated/ftb1-compound0.relabel
	hfst-compose -1 $< -2 generated/ftb1-rm_prop_compound.regex.hfst | \
	hfst-substitute -F generated/ftb1-compound0.relabel |\
	hfst-compose -2 generated/ftb1-rm_infminen.regex.hfst | \
	hfst-compose -1 generated/ftb1-rm_dummy_hyph.regex.hfst | \
	hfst-minimize > $@

# Get prefixes of compounds and subsitute all compound markers
# so that they can be identified both on the input and output
# level.
generated/ftb1-compound_prefixes.hfst: generated/ftb1-morphology.omor.lex.hfst generated/ftb1-input_boundary.regex.hfst \
generated/ftb1-output_boundary.regex.hfst generated/ftb1-compound1.relabel generated/ftb1-compound2.relabel
	hfst-substitute -F generated/ftb1-compound1.relabel $< | \
	hfst-compose -1 generated/ftb1-input_boundary.regex.hfst | \
	hfst-compose -2 generated/ftb1-output_boundary.regex.hfst | \
	hfst-minimize | \
	hfst-substitute -F generated/ftb1-compound2.relabel -o $@

# Get all word forms that arenät compounds.
generated/ftb1-non_compounds.hfst: generated/ftb1-morphology.omor.lex.hfst generated/ftb1-no_compounds.regex.hfst
	hfst-compose -1 $< -2 generated/ftb1-no_compounds.regex.hfst |\
	hfst-minimize > generated/ftb1-non_compounds.hfst

# Compile a transducer where only final parts of compounds are
# analyzed because that's the way ftb1 does it. The initial
# parts should be left as they are.
generated/ftb1-wf_prefix_recovered.hfst: generated/ftb1-compound_prefixes.hfst generated/ftb1-morphology.omor.lex.hfst \
generated/ftb1-no_uppercase.regex.hfst generated/ftb1-compound_final.regex.hfst generated/ftb1-non_compounds.hfst
	hfst-invert generated/ftb1-compound_prefixes.hfst | \
	hfst-concatenate -2 generated/ftb1-compound_final.regex.hfst | \
	hfst-compose -2 generated/ftb1-no_uppercase.regex.hfst | \
	hfst-minimize | \
	hfst-compose -1 generated/ftb1-morphology.omor.lex.hfst | \
	hfst-disjunct -2 generated/ftb1-non_compounds.hfst | \
	hfst-minimize > $@

# 1. Remove word id markers and replace all omorfi labels with
# corresponding ftb1 labels.
# 2. Remove the duplicate marking of number in pronouns.
# 3. Change all Pcle analyses to Adverb analyses.
# 4. Remove duplicate word class markers that result from
# substituting derivation tags.
generated/omorfi-ftb1.analyse.hfst: generated/ftb1-wf_prefix_recovered.hfst generated/ftb1-rm_word_id.regex.hfst \
generated/ftb1-rewrite_pron.regex.hfst generated/ftb1-rewrite_pcle.regex.hfst generated/ftb1-no_double_pos.regex.hfst \
generated/omor2ftb1.relabel
	hfst-compose -1 $< -2 generated/ftb1-rm_word_id.regex.hfst | \
	hfst-substitute -F generated/omor2ftb1.relabel | \
	hfst-compose -2 generated/ftb1-rewrite_pron.regex.hfst | \
	hfst-compose -2 generated/ftb1-rewrite_pcle.regex.hfst | \
	hfst-compose -2 generated/ftb1-no_double_pos.regex.hfst | \
	hfst-minimize |\
	hfst-fst2fst -f olw > $@

# Invert the argument fst.
%.inv.hfst:%.hfst
	hfst-invert $^ > $@

generated/ftb1-capitalize.regex:
	echo '[Q:q|W:w|E:e|R:r|T:t|Y:y|U:u|I:i|O:o|P:p|Å:å|A:a|S:s|D:d|F:f|G:g|H:h|J:j|K:k|L:l|Ö:ö|Ä:ä|Z:z|X:x|C:c|V:v|B:b|N:n|M:m|?]*' > $@

generated/ftb1-rm_prop_compound.regex:
	echo '[\%[BOUNDARY%=COMPOUND%]* %[PROPER%=PROPER%] \%[BOUNDARY%=COMPOUND%]* [%[BOUNDARY%=COMPOUND%] \%[BOUNDARY%=COMPOUND%]* %[POS%=NOUN%] %[PROPER%=PROPER%] \%[BOUNDARY%=COMPOUND%]*]*] | [ \%[PROPER%=PROPER%]* ]' > $@

generated/ftb1-rm_infminen.regex:
	echo '[? - %[INF%=MINEN%]]*' > $@

generated/ftb1-rm_dummy_hyph.regex:
	echo '[? - %{hyph%?%} ]*' > $@

generated/ftb1-input_boundary.regex:
	echo '[[?* [0:%$$COMPOUND%_EPS%$$ | 0:%$$COMPOUND%_DASH1%$$ | 0:%$$COMPOUND%_DASH2%$$ | 0:%$$COMPOUND%_DASH3%$$] [0:? - [0:%$$COMPOUND%_EPS%$$ | 0:%$$COMPOUND%_DASH1%$$ | 0:%$$COMPOUND%_DASH2%$$ | 0:%$$COMPOUND%_DASH3%$$]]*] | [[? - [%$$COMPOUND%_EPS%$$ | %$$COMPOUND%_DASH1%$$ | %$$COMPOUND%_DASH2%$$ | %$$COMPOUND%_DASH3%$$]]*]]' > $@

generated/ftb1-output_boundary.regex:
	echo '[?* [%[BOUNDARY%=COMPOUND%]:0|%[BOUNDARY%=COMPOUND1%]:0|%[BOUNDARY%=COMPOUND2%]:0|%[BOUNDARY%=COMPOUND3%]:0] [?:0 - [%[BOUNDARY%=COMPOUND%]:0|%[BOUNDARY%=COMPOUND1%]:0|%[BOUNDARY%=COMPOUND2%]:0|%[BOUNDARY%=COMPOUND3%]:0 ]]*] | [? - [%[BOUNDARY%=COMPOUND%]|%[BOUNDARY%=COMPOUND1%]|%[BOUNDARY%=COMPOUND2%]|%[BOUNDARY%=COMPOUND3%] ]]*' > $@

generated/ftb1-no_compounds.regex:
	echo '\[%[BOUNDARY%=COMPOUND%] | %[BOUNDARY%=COMPOUND1%] | %[BOUNDARY%=COMPOUND2%] | %[BOUNDARY%=COMPOUND3%] ]*' > $@

generated/ftb1-no_uppercase.regex:
	echo '\[Q|W|E|R|T|Y|U|I|O|P|Å|A|S|D|F|G|H|J|K|L|Ö|Ä|Z|X|C|V|B|N|M|Š|É]*' > $@

generated/ftb1-compound_final.regex:
	echo '[ %[BOUNDARY%=COMPOUND%] | %[BOUNDARY%=COMPOUND1%]| %[BOUNDARY%=COMPOUND2%]| %[BOUNDARY%=COMPOUND3%] ] [ \[ %[BOUNDARY%=COMPOUND%] | %[BOUNDARY%=COMPOUND1%] | %[BOUNDARY%=COMPOUND2%] | %[BOUNDARY%=COMPOUND3%] ] ]*' > $@

generated/ftb1-rm_word_id.regex:
	echo '%[WORD%_ID%= -> 0 || _ .o. %] -> 0 || \%] _ ;' > $@

generated/ftb1-rewrite_pron.regex:
	echo '[% Sg | % Pl] -> 0 || [% Sg3 | % Sg2 | % Sg1 | % Pl3 | % Pl2 | % Pl1 ] _ ;' > $@

generated/ftb1-rewrite_pcle.regex:
	echo '% Pcle % Abbr -> % Adv % Abbr .o. % Pcle -> 0 || _ ? .o. % Pcle -> % Adv ;' > $@

generated/ftb1-no_double_pos.regex:
	echo '[ % A|% Adp|% Adv|% N|% Num|% Pcle|% Pron|% Pun|% V|% N Abbr|% V Neg ] -> 0 || _ [% A|% Adp|% Adv|% N|% Num|% Pcle|% Pron|% Pun|% V|% N Abbr|% V Neg] ;' > $@

generated/ftb1-miettiminen.regex:
	echo '%[WORD%_ID%= m i e t t i m i n e n %] ?*' > $@

generated/ftb1-rm_mietti.regex:
	echo '%[WORD%_ID%=:0 [m:0|M:0] [i:0|I:0] [e:0|E:0] [t:0|T:0] [t:0|T:0] [i:0|I:0] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-rm_mietti.inv.regex:
	echo '[0:m|0:M] [0:i|0:I] [0:e|0:E] [0:t|0:T] [0:t|0:T] [0:i|0:I] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-avaaminen.regex:
	echo '%[WORD%_ID%= a v a a m i n e n %] ?*' > $@

generated/ftb1-rm_avaa.regex:
	echo '%[WORD%_ID%=:0 [a:0|A:0] [v:0|V:0] [a:0|A:0] [a:0|A:0] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-rm_avaa.inv.regex:
	echo '[0:a|0:A] [0:v|0:V] [0:a|0:A] [0:a|0:A] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-va_der.regex:
	echo '\%[BOUNDARY%=COMPOUND%]* %[POS%=VERB%] %[VOICE%=ACT%] %[PCP%=VA%] %[NUM%=SG%] %[CASE%=NOM%]' > $@

generated/ftb1-rm_va.regex:
	echo '?* [v:0|V:0] [a:0|A:0|ä:0|Ä:0]' > $@

generated/ftb1-minen_marker.regex:
	echo '0:%[LEX=%MINEN%]' > $@

generated/ftb1-word_id.regex:
	echo '0:%[WORD%_ID%=' > $@

generated/ftb1-ikuisesti.regex:
	echo '%[WORD%_ID%= i k u i s e s t i %] ?*' > $@

generated/ftb1-pimeasti.regex:
	echo '%[WORD%_ID%= p i m e ä s t i %] ?*' > $@

generated/ftb1-rm_ikuise.regex:
	echo '%[WORD%_ID%=:0 [i:0|I:0] [k:0|K:0] [u:0|U:0] [i:0|I:0] [s:0|S:0] [e:0|E:0] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-rm_ikuise.inv.regex:
	echo '[0:i|0:I] [0:k|0:K] [0:u|0:U] [0:i|0:I] [0:s|0:S] [0:e|0:E] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-rm_pimea.regex:
	echo '%[WORD%_ID%=:0 [p:0|P:0] [i:0|I:0] [m:0|M:0] [e:0|E:0] [ä:0|Ä:0] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-rm_pimea.inv.regex:
	echo '[0:p|0:P] [0:i|0:I] [0:m|0:M] [0:e|0:E] [0:ä|0:Ä] \%[BOUNDARY%=COMPOUND%]*' > $@

generated/ftb1-rm_n.regex:
	echo '?* [n:0 | N:0]' > $@

generated/ftb1-rm_n.inv.regex:
	echo '?* [0:n | 0:N]' > $@

generated/ftb1-sen_adj.regex:
	echo '\%[BOUNDARY%=COMPOUND%]* %[POS%=ADJECTIVE%] %[NUM%=SG%] %[CASE%=GEN%]' > $@

generated/ftb1-sti_marker.regex:
	echo '0:%[LEX=%STI%]' > $@

generated/ftb1-compound0.relabel:
	echo '-:[BOUNDARY=COMPOUND]	-:[BOUNDARY=COMPOUND1]' > $@
	echo '‐:[BOUNDARY=COMPOUND]	‐:[BOUNDARY=COMPOUND2]'	>> $@
	echo '‑:[BOUNDARY=COMPOUND]	‑:[BOUNDARY=COMPOUND3]' >> $@

generated/ftb1-compound1.relabel:
	echo '@_EPSILON_SYMBOL_@:[BOUNDARY=COMPOUND]	$$COMPOUND_EPS$$:[BOUNDARY=COMPOUND]' > $@
	echo '-:[BOUNDARY=COMPOUND1]	$$COMPOUND_DASH1$$:[BOUNDARY=COMPOUND1]' >> $@
	echo '‐:[BOUNDARY=COMPOUND2]	$$COMPOUND_DASH2$$:[BOUNDARY=COMPOUND2]' >> $@
	echo '‑:[BOUNDARY=COMPOUND3]	$$COMPOUND_DASH3$$:[BOUNDARY=COMPOUND3]' >> $@

generated/ftb1-compound2.relabel:
	echo '$$COMPOUND_EPS$$:[BOUNDARY=COMPOUND]	#:[BOUNDARY=COMPOUND]' > $@
	echo '$$COMPOUND_DASH1$$:[BOUNDARY=COMPOUND1]	-:[BOUNDARY=COMPOUND1]' >> $@
	echo '$$COMPOUND_DASH2$$:[BOUNDARY=COMPOUND2]	‐:[BOUNDARY=COMPOUND2]' >> $@
	echo '$$COMPOUND_DASH3$$:[BOUNDARY=COMPOUND3]	‑:[BOUNDARY=COMPOUND3]' >> $@

generated/omor2ftb1.relabel:
	echo '[CASE=ABE]	 Abe' > $@
	echo '[CASE=ABL]	 Abl' >> $@
	echo '[CASE=ACC]	 Acc' >> $@
	echo '[CASE=ADE]	 Ade' >> $@
	echo '[CASE=ALL]	 All' >> $@
	echo '[CASE=COM]	 Com' >> $@
	echo '[CASE=ELA]	 Ela' >> $@
	echo '[CASE=ESS]	 Ess' >> $@
	echo '[CASE=GEN]	 Gen' >> $@
	echo '[CASE=ILL]	 Ill' >> $@
	echo '[CASE=INE]	 Ine' >> $@
	echo '[CASE=INS]	 Ins' >> $@
	echo '[CASE=LAT]	 Lat' >> $@
	echo '[CASE=NOM]	 Nom' >> $@
	echo '[CASE=PAR]	 Par' >> $@
	echo '[CASE=TRA]	 Tra' >> $@
	echo '[CLIT=HAN]	 Han' >> $@
	echo '[CLIT=KAAN]	 Kaan' >> $@
	echo '[CLIT=KA]	 Ka' >> $@
	echo '[CLIT=KIN]	 Kin' >> $@
	echo '[CLIT=KO]	 Ko' >> $@
	echo '[CLIT=PA]	 Pa' >> $@
	echo '[CLIT=S]	 S' >> $@
	echo '[CMP=CMP]	 Cmp' >> $@
	echo '[CMP=SUP]	 Sup' >> $@
	echo '[CONJ=ADVERBIAL]	 CS' >> $@
	echo '[CONJ=COORD]	 CC' >> $@
	echo '[INF=A]	 InfA' >> $@
	echo '[INF=E]	 InfE' >> $@
	echo '[INF=MA]	 InfMa' >> $@
	echo '[INF=MAISILLA]	 InfMaisilla' >> $@
	echo '[MOOD=COND]	 Cond' >> $@
	echo '[MOOD=IMPV]	 Imprt' >> $@
	echo '[MOOD=INDV]	 Ind' >> $@
	echo '[MOOD=OPT]	 Opt' >> $@
	echo '[MOOD=POTN]	 Pot' >> $@
	echo '[NEG=CON]	 ConNeg' >> $@
	echo '[NUM=SG]	 Sg' >> $@
	echo '[NUM=PL]	 Pl' >> $@
	echo '[PCP=AGENT]	 PcpAg' >> $@
	echo '[PCP=NEG]	 PcpNeg' >> $@
	echo '[PCP=NUT]	 PcpNut' >> $@
	echo '[PCP=VA]	 PcpVa' >> $@
	echo '[PERS=SG1]	 Sg1' >> $@
	echo '[PERS=SG2]	 Sg2' >> $@
	echo '[PERS=SG3]	 Sg3' >> $@
	echo '[PERS=PL1]	 Pl1' >> $@
	echo '[PERS=PL2]	 Pl2' >> $@
	echo '[PERS=PL3]	 Pl3' >> $@
	echo '[POS=ADJECTIVE]	 A' >> $@
	echo '[POS=ADPOSITION]	 Adp' >> $@
	echo '[POS=ADVERB]	 Adv' >> $@
	echo '[POS=NOUN]	 N' >> $@
	echo '[POS=NUMERAL]	 Num' >> $@
	echo '[POS=PARTICLE]	 Pcle' >> $@
	echo '[POS=PRONOUN]	 Pron' >> $@
	echo '[POS=PUNCTUATION]	 Pun' >> $@
	echo '[POS=VERB]	 V' >> $@
	echo '[POSITION=PREFIX]	 Prefix' >> $@
	echo '[POSS=PL1]	 PxPl1' >> $@
	echo '[POSS=PL2]	 PxPl2' >> $@
	echo '[POSS=SG1]	 PxSg1' >> $@
	echo '[POSS=SG2]	 PxSg2' >> $@
	echo '[POSS=3]	 Px3' >> $@
	echo '[PROPER=PROPER]	 Prop' >> $@
	echo '[SUBCAT=ABBREVIATION]	 Abbr' >> $@
	echo '[SUBCAT=CARD]	 Card' >> $@
	echo '[SUBCAT=DECIMAL]	 Card' >> $@
	echo '[SUBCAT=DEMONSTRATIVE]	 Dem' >> $@
	echo '[SUBCAT=INTERJECTION]	 Interj' >> $@
	echo '[SUBCAT=INTERROGATIVE]	 Interr' >> $@
	echo '[SUBCAT=NEG]	 Neg' >> $@
	echo '[SUBCAT=ORD]	 Ord' >> $@
	echo '[SUBCAT=PERSONAL]	 Pers' >> $@
	echo '[SUBCAT=RECIPROC]	 Recip' >> $@
	echo '[SUBCAT=REFLEXIVE]	 Refl' >> $@
	echo '[SUBCAT=RELATIVE]	 Rel' >> $@
	echo '[SUBCAT=ROMAN]	 Ord' >> $@
	echo '[SUBCAT=QUANTOR]	 Qnt' >> $@
	echo '[TENSE=PRESENT]	 Pres' >> $@
	echo '[TENSE=PAST]	 Past' >> $@
	echo '[VOICE=ACT]	 Act' >> $@
	echo '[VOICE=PSS]	 Pass' >> $@
	echo '[PERS=PE4]	@_EPSILON_SYMBOL_@' >> $@
	echo '[SUBCAT=CONJUNCTION]	@_EPSILON_SYMBOL_@' >> $@
	echo '[BOUNDARY=CLAUSE]	@_EPSILON_SYMBOL_@' >> $@
	echo '[BOUNDARY=SENTENCE]	@_EPSILON_SYMBOL_@' >> $@
	echo '[BOUNDARY=COMPOUND]	#' >> $@
	echo '[BOUNDARY=COMPOUND1]	-' >> $@
	echo '[BOUNDARY=COMPOUND2]	‐' >> $@
	echo '[BOUNDARY=COMPOUND3]	‐' >> $@
	echo '[CONJ=COMPARATIVE]	@_EPSILON_SYMBOL_@' >> $@
	echo '[DRV=JA]	 N' >> $@
	echo '[DRV=MATON]	 A' >> $@
	echo '[DRV=UUS]	 N' >> $@
	echo '[DRV=MINEN]	 N' >> $@
	echo '[DRV=S]	 A' >> $@
	echo '[DRV=STI]	 Adv' >> $@
	echo '[DRV=U]	 N' >> $@
	echo '[DRV=VA]	 A' >> $@
	echo '[DRV=INEN]	 A' >> $@
	echo '[INF=MINEN]	 InfMinen' >> $@
	echo '[LEX=MINEN]	 Lex_Minen' >> $@
	echo '[LEX=STI]	 Lex_Sti' >> $@
	echo '[POSITION=FINAL]	 Fin' >> $@
	echo '[POSITION=INITIAL]	 Ini' >> $@
	echo '[STYLE=ARCHAIC]	@_EPSILON_SYMBOL_@' >> $@
	echo '[STYLE=DIALECTAL]	@_EPSILON_SYMBOL_@' >> $@
	echo '[STYLE=NONSTANDARD]	@_EPSILON_SYMBOL_@' >> $@
	echo '[STYLE=RARE]	@_EPSILON_SYMBOL_@' >> $@
	echo '[SUBCAT=BRACKET]	@_EPSILON_SYMBOL_@' >> $@
	echo '[SUBCAT=DASH]	@_EPSILON_SYMBOL_@' >> $@
	echo '[SUBCAT=QUOTATION]	 Quo' >> $@
	echo '[MOOD=INDV][TENSE=PAST]	 Ind Past' >> $@
	echo '[MOOD=INDV][TENSE=PRESENT]	 Ind Pres' >> $@
	echo '[POSITION=SUFFIX]	@_EPSILON_SYMBOL_@' >> $@
	echo '[POS=NOUN][SUBCAT=ABBREVIATION]	 N Abbr' >> $@
	echo '[POS=VERB][SUBCAT=NEG]	 V Neg' >> $@
	echo '[SUBCAT=BRACKET][POSITION=FINAL]	@_EPSILON_SYMBOL_@' >> $@
	echo '[SUBCAT=BRACKET][POSITION=INITIAL]	@_EPSILON_SYMBOL_@' >> $@
	echo '[SUBCAT=QUOTATION][POSITION=FINAL]	 Quo Fin' >> $@
	echo '[SUBCAT=QUOTATION][POSITION=INITIAL]	 Quo Ini' >> $@
	echo '[SUBCAT=SPACE]	@_EPSILON_SYMBOL_@' >> $@
	echo '' >> $@
# }}}
#
# {{{OMOR compilation
# word-boundary huphens
generated/temporary-omor.hyphenated.hfst: generated/omorfi-omor.lexc.hfst \
	generated/omorfi-hyphens.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/omorfi-hyphens.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# spelling variations
generated/temporary-omor.relaxed.hfst: generated/temporary-omor.hyphenated.hfst \
	generated/omorfi-sh.regex.hfst \
	generated/omorfi-zh.regex.hfst \
	generated/omorfi-orthographic-variations.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-orthographic-variations.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T generated/omorfi-sh.regex.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T generated/omorfi-zh.regex.hfst -o $@

# remove remaining morph boundaries at this point
generated/temporary-omor.unbounded.hfst: generated/temporary-omor.relaxed.hfst |\
	generated/omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# hand-written weights for omor
generated/temporary-omor.tagweighted.hfst: generated/temporary-omor.unbounded.hfst generated/omorfi-omor.reweight
	$(HREW) $(HFST_FLAGS) -T generated/omorfi-omor.reweight generated/temporary-omor.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# no token weights
generated/temporary-omor.tokenweighted.hfst: generated/temporary-omor.tagweighted.hfst
	cp -v $< $@

# no other weight combinations
generated/temporary-omor.weighted.hfst: generated/temporary-omor.tokenweighted.hfst
	cp -v $< $@

# create morphological analyzer
generated/temporary.omor.hfst: generated/temporary-omor.weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

# finalising
generated/omorfi-omor.analyse.hfst: generated/temporary.omor.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -o $@ -i $<

generated/omorfi-omor_recased.analyse.hfst: generated/temporary.omor.hfst generated/omorfi-recase-any.twolc.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HIC) $(HFST_FLAGS) - generated/omorfi-recase-any.twolc.hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HF2F) -f olw $(HFST_FLAGS) -o $@

# create generator from analyzer
generated/omorfi-omor.generate.hfst: generated/temporary-omor.hyphenated.hfst  generated/omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-remove-boundaries.regex.hfst |\
		$(HF2F) $(HFST_FLAGS) -f olw -o $@

# }}}
#
# {{{APE compilation
generated/fin-autogen.hfst: generated/apertium-fin.fin.lexc.hfst \
	generated/apertium-fin.fin.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/apertium-fin.fin.twolc.hfst -o $@

generated/fin-automorf.hfst: generated/apertium-fin.fin.lexc.hfst \
	generated/apertium-fin.fin.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/apertium-fin.fin.twolc.hfst |\
		$(HINV) $(HFST_FLAGS) -o $@
# }}}
#
# {{{SPELL-CHECKING
# voikko speller HFST beta targets'
generated/errmodel.edit-distance.txt: python/generate-edit-distance.py
	$(PYTHON) $< -o $@

generated/errmodel.edit-distance-1.hfst: generated/errmodel.edit-distance.hfst
	$(HMIN) $< -o $@

generated/errmodel.edit-distance-2.hfst: generated/errmodel.edit-distance.hfst
	$(HMIN) $< |\
		$(HREP) -f 1 -t 2 -o $@

generated/errmodel.edit-distance-3.hfst: generated/errmodel.edit-distance.hfst
	$(HMIN) $< |\
		$(HREP) -f 1 -t 3 -o $@

voikko/acceptor.default.hfst: generated/omorfi.accept.hfst
	$(HF2F) -f olw < $< > $@

voikko/errmodel.default.hfst: generated/errmodel.edit-distance-2.hfst
	$(HF2F) -f olw < $< > $@

voikko/speller-omorfi.zhfst: voikko/index.xml \
	voikko/acceptor.default.hfst voikko/errmodel.default.hfst
	$(ZIP) -j -v -9 $@  $?

# }}}
#
# {{{ VISL CG 3
if CAN_VISLCG3
generated/omorfi.cg3bin: vislcg3/omorfi.cg3
	$(CGCOMP) $< $@
endif
# }}}

CLEAN_FILES=generated/ftb1-avaaminen_omorfi.hfst \
			 generated/ftb1-avaaminen.regex.hfst \
			 generated/ftb1-back_minen_omorfi.hfst \
			 generated/ftb1-back_sti_omorfi.hfst \
			 generated/ftb1-capitalize.regex.hfst \
			 generated/ftb1-compound_final.regex.hfst \
			 generated/ftb1-compound_prefixes.hfst \
			 generated/ftb1-compound0.relabel \
			 generated/ftb1-compound_subst1 \
			 generated/ftb1-compound_subst2 \
			 generated/ftb1-front_minen_omorfi.hfst \
			 generated/ftb1-front_sti_omorfi.hfst \
			 generated/ftb1-ikuisesti_omorfi.hfst \
			 generated/ftb1-ikuisesti.regex.hfst \
			 generated/ftb1-input_boundary.regex.hfst \
			 generated/ftb1-miettiminen_omorfi.hfst \
			 generated/ftb1-miettiminen.regex.hfst \
			 generated/ftb1-minen_analyzer.hfst \
			 generated/ftb1-minen_marker.regex.hfst \
			 generated/ftb1-minen_omorfi.hfst \
			 generated/ftb1-morphology.ftb1.ol \
			 generated/ftb1-morphology.omor.hfst \
			 generated/ftb1-morphology.omor.hfst.minen \
			 generated/ftb1-morphology.omor.hfst.minen.sti \
			 generated/ftb1-morphology.omor.lex.hfst \
			 generated/ftb1-no_compounds.regex.hfst \
			 generated/ftb1-no_double_pos.regex.hfst \
			 generated/ftb1-non_compounds.hfst \
			 generated/ftb1-no_uppercase.regex.hfst \
			 generated/ftb1-omor2ftb1_subst \
			 generated/ftb1-output_boundary.regex.hfst \
			 generated/ftb1-pimeasti_omorfi.hfst \
			 generated/ftb1-pimeasti.regex.hfst \
			 generated/ftb1-rewrite_pcle.regex.hfst \
			 generated/ftb1-rewrite_pron.regex.hfst \
			 generated/ftb1-rm_avaa.inv.regex.hfst \
			 generated/ftb1-rm_avaa.regex.hfst \
			 generated/ftb1-rm_dummy_hyph.regex.hfst \
			 generated/ftb1-rm_ikuise.inv.regex.hfst \
			 generated/ftb1-rm_ikuise.regex.hfst \
			 generated/ftb1-rm_infminen.regex.hfst \
			 generated/ftb1-rm_mietti.inv.regex.hfst\
			 generated/ftb1-rm_mietti.regex.hfst \
			 generated/ftb1-rm_n.inv.regex.hfst \
			 generated/ftb1-rm_n.regex.hfst\
			 generated/ftb1-rm_pimea.inv.regex.hfst \
			 generated/ftb1-rm_pimea.regex.hfst \
			 generated/ftb1-rm_prop_compound.regex.hfst\
			 generated/ftb1-rm_va.regex.hfst \
			 generated/ftb1-rm_va.regex.inv.hfst \
			 generated/ftb1-rm_word_id.regex.hfst\
			 generated/ftb1-sen_adjectives.hfst sen_adj.regex.hfst \
			 generated/ftb1-sen_stems.hfst\
			 generated/ftb1-sti_analyzer.hfst\
			 generated/ftb1-sti_marker.regex.hfst \
			 generated/ftb1-sti_omorfi.hfst\
			 generated/ftb1-va_derivatives.hfst\
			 generated/ftb1-va_der.regex.hfst\
			 generated/ftb1-va_stems.hfst \
			 generated/ftb1-wf_prefix_recovered.hfst\
			 generated/ftb1-word_id.regex.hfst

clean-local:
	rm -rf generated/ keys.*.tsv missing-keys.*.tsv \
		voikko/*hfst
# vim: set foldmethod=marker:
