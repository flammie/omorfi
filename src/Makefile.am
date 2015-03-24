## Process this file with automake to produce Makefile.in

# Settings
HFST_FLAGS=--verbose
hfstfidatadir=$(datadir)/hfst/fi/
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
PARADIGM_JOINS=paradigms/morphophonology.tsv

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
			   python/omorfi/tdt_formatter.py
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
			python/omorfi/omor_strings_io.py
SCIRPTS=$(FORMAT_SCIRPTS) $(GENERATOR_SCIRPTS) $(DATABASE_SCIRPTS) \
		$(FIN_SCIRPTS)
# }}}
#
# {{{Generated files
if WANT_HFST
GENERIC_AUTOMATA=generated/omorfi.accept.hfst \
				 generated/omorfi.lemmatise.hfst \
				 generated/omorfi.tokenise.hfst \
				 generated/omorfi.hyphenate.hfst \
				 generated/omorfi.segment.hfst
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
				  generated/omorfi-token.regex.hfst
if WANT_FTB3
FTB3_AUTOMATA=generated/omorfi-ftb3.analyse.hfst \
			  generated/omorfi-ftb3.generate.hfst
FTB3_GENERATED=generated/omorfi-ftb3.lexc \
			   generated/omorfi-ftb3.reweight \
			   generated/omorfi-ftb3-tests.yaml \
			   generated/omorfi-ftb3-rewrite-tags.regex

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
			  generated/apertium-fin.fin.twolc
endif
DB_GENERATED=generated/master.tsv generated/joint.tsv

endif # HFST
# }}}
# {{{Autotools install
# destnations directories for this stuff at the top of the file
hfstfidata_DATA=$(GENERIC_AUTOMATA) $(FTB3_AUTOMATA) $(OMOR_AUTOMATA) \
				$(APE_AUTOMATA)
voikkoshare_DATA=voikko/speller-omorfi.zhfst
pkgdata_DATA=generated/master.tsv

bin_SCRIPTS=bash/omorfi-analyse-text.sh \
			bash/omorfi-analyse-tokenised.sh \
			bash/omorfi-generate.sh \
			bash/omorfi-hyphenate.sh \
			bash/omorfi-spell.sh \
			bash/omorfi-segment.sh

pkgpython_PYTHON=python/omorfi/__init__.py \
				 python/omorfi/omorfi.py


# These go into dist tarballs... which we no longer make
# N.B. for distcheck anyways
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(LEMMA_JOINS) $(SCIRPTS) \
		   $(STEMPARTS) $(INFLECTIONS) \
		   voikko/voikko-fi_FI.pro voikko/index.xml

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
CLEANFILES=$(GENERIC_GENERATED) $(FTB3_GENERATED) $(DB_GENERATED)
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

generated/omorfi-hyphenate.twolc:
	$(PYTHON) $(srcdir)/python/generate-twolcs.py -f=ftb3 -r hyphenate -o $@

generated/omorfi-boundary.reweight: 
	$(PYTHON) $(srcdir)/python/generate-reweights.py -v -f=boundary -o $@

# database to omor 
generated/omorfi-omor-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/python/generate-yamls.py -i $< -o $@ -f=omor -v

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
	$(PYTHON) $(srcdir)/python/generate-yamls.py -i $< -o $@ -f=ftb3 -v

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

generated/omorfi.dix: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/python/generate-monodix.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@

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
	$(HPR) $(HFST_FLAGS) --project=upper -i $< -o $@

# create basic corpus tokeniser
# Should split at even-odd boundaries of word punct* word punct*
generated/omorfi.token-separator.hfst:
	echo '0:"\n" ;' | $(HREGEX) -o generated/omorfi.token-separator.hfst

generated/omorfi.tokenise.hfst: generated/omorfi.accept.hfst \
					  generated/omorfi-between-tokens.regex.hfst \
					  generated/omorfi-token.regex.hfst \
					  generated/omorfi.token-separator.hfst
	$(HCAT) $(HFST_FLAGS) generated/omorfi-token.regex.hfst \
		generated/omorfi.token-separator.hfst |\
		$(HMIN) $(HFST_FLAGS) -o generated/omorfi.nondict-token.hfst
	$(HCAT) $(HFST_FLAGS) generated/omorfi-between-tokens.regex.hfst \
		generated/omorfi.token-separator.hfst -o generated/omorfi-token-joiner.hfst
	$(HCAT) $(HFST_FLAGS) generated/omorfi.nondict-token.hfst \
		generated/omorfi-token-joiner.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 -o $@

# hyphenation dictionary
generated/omorfi.hyphenate.hfst: generated/temporary-ftb3.orth.hfst \
						generated/omorfi-hyphenate.twolc.hfst
	cat generated/temporary-ftb3.orth.hfst |\
		$(HIC) $(HFST_FLAGS) -2 generated/omorfi-hyphenate.twolc.hfst > $@

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

voikko/speller-omorfi.zhfst: generated/omorfi.accept.hfst \
					generated/errmodel.edit-distance-2.hfst voikko/index.xml
	$(HF2F) -f olw < generated/omorfi.accept.hfst > voikko/acceptor.default.hfst
	$(HF2F) -f olw < generated/errmodel.edit-distance-2.hfst > voikko/errmodel.default.hfst
	$(ZIP) -j -v -9 $@ voikko/*

# }}}
# vim: set foldmethod=marker:
