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
LEXEMES=lexemes/lexemes.tsv
# lexical features
LEMMA_JOINS=lexemes/adjective-classes.tsv \
			lexemes/boundaries.tsv \
			lexemes/homonyms.tsv \
			lexemes/noun-classes.tsv \
			lexemes/numeral-classes.tsv \
			lexemes/origin.tsv \
			lexemes/plurale-tantum.tsv \
			lexemes/possessives.tsv \
			lexemes/pronunciation.tsv \
			lexemes/proper-classes.tsv \
			lexemes/particle-classes.tsv \
			lexemes/pronoun-classes.tsv \
			lexemes/symbol-classes.tsv \
			lexemes/semantic.tsv \
			lexemes/usage.tsv \
			lexemes/verb-arguments.tsv
# paradigm features
PARADIGM_JOINS=paradigms/morphophonology.tsv

# Morphology
# stem variants by deletion and concatenations
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
# suffixes by concatenations
INFLECTIONS=stub-stem-inflection/acro-inflections.tsv \
			stub-stem-inflection/adjective-inflections.tsv \
			stub-stem-inflection/digit-inflections.tsv \
			stub-stem-inflection/noun-inflections.tsv \
			stub-stem-inflection/numeral-inflections.tsv \
			stub-stem-inflection/particle-inflections.tsv \
			stub-stem-inflection/pronoun-inflections.tsv \
			stub-stem-inflection/symbol-inflections.tsv \
			stub-stem-inflection/verb-inflections.tsv

# }}}
#
# {{{Scripts (variable name = SCIRPTS cause automagic _SCRIPTS)
# tag formats
FORMAT_SCIRPTS=apertium_formatter.py \
			   ftb3_formatter.py \
			   omor_formatter.py \
			   tdt_formatter.py
# file formats
GENERATOR_SCIRPTS=generate-lexcs.py \
				  generate-twolcs.py \
				  generate-regexes.py \
				  generate-reweights.py \
				  generate-edit-distance.py \
				  generate-monodix.py \
				  generate-yaml.py \
				  generate-kotus-sanalista.py
# Raw-ish database handling
DATABASE_SCIRPTS=tsvjoin.py tsv_expand.py
# Finnish specific lot
FIN_SCIRPTS=gradation.py \
			parse_csv_data.py \
			plurale_tantum.py \
			stub.py \
			guess_feats.py \
			guess_new_class.py \
			wordmap.py \
			omor_strings_io.py
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

endif # HFST
# }}}
# {{{Autotools install
# destnations directories for this stuff at the top of the file
hfstfidata_DATA=$(GENERIC_AUTOMATA) $(FTB3_AUTOMATA) $(OMOR_AUTOMATA) \
				$(APE_AUTOMATA)
voikkoshare_DATA=voikko/speller-omorfi.zhfst

bin_SCRIPTS=scripts/omorfi-analyse-text.sh \
			scripts/omorfi-analyse-tokenised.sh \
			scripts/omorfi-generate.sh \
			scripts/omorfi-hyphenate.sh \
			scripts/omorfi-spell.sh \
			scripts/omorfi-segment.sh \
			scripts/omorfi-interactive.sh

python_PYTHON=scripts/omorfi.py scripts/convert_tag_format.py


# These go into dist tarballs... which we no longer make
# N.B. for distcheck anyways
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(LEMMA_JOINS) $(SCIRPTS) \
		   $(STEMPARTS) $(INFLECTIONS) \
		   voikko/voikko-fi_FI.pro voikko/index.xml

# These are ran with make check. All modules should have stuff
TESTS=$(FORMAT_SCIRPTS) $(FIN_SCIRPTS)
XFAIL_TESTS=tdt_formatter.py

# These aren't installed but generated
noinst_DATA=generated/omorfi.dix generated/omorfi-sanalista.xml

# Things that make clean isn't smart enought to wipe
CLEANFILES=$(GENERIC_GENERATED) $(FTB3_GENERATED)
# }}}
#
# {{{GENERATING
if CAN_PYTHON
generated/timestamp:
	mkdir -p generated
	touch $@

# database to database
generated/joint.tsv: lexemes/lexemes.tsv $(LEMMA_JOINS) generated/timestamp
	$(PYTHON) $(srcdir)/tsvjoin.py -v -i $< \
		-j $(srcdir)/lexemes/adjective-classes.tsv \
		-j $(srcdir)/lexemes/boundaries.tsv \
		-j $(srcdir)/lexemes/origin.tsv \
		-j $(srcdir)/lexemes/homonyms.tsv \
		-j $(srcdir)/lexemes/noun-classes.tsv \
		-j $(srcdir)/lexemes/numeral-classes.tsv \
		-j $(srcdir)/lexemes/plurale-tantum.tsv \
		-j $(srcdir)/lexemes/possessives.tsv \
		-j $(srcdir)/lexemes/pronunciation.tsv \
		-j $(srcdir)/lexemes/particle-classes.tsv \
		-j $(srcdir)/lexemes/proper-classes.tsv \
		-j $(srcdir)/lexemes/pronoun-classes.tsv \
		-j $(srcdir)/lexemes/semantic.tsv \
		-j $(srcdir)/lexemes/symbol-classes.tsv \
		-j $(srcdir)/lexemes/usage.tsv \
		-j $(srcdir)/lexemes/verb-arguments.tsv -o $@

generated/master.tsv: generated/joint.tsv
	$(PYTHON) $(srcdir)/tsv_expand.py \
		-j $(srcdir)/paradigms/morphophonology.tsv -v -i $< -o $@.unsrt
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
	$(PYTHON) $(srcdir)/generate-lexcs.py -v -m generated/master.tsv -p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=generic

generated/omorfi-phon.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/generate-twolcs.py -r phon -o $@

generated/omorfi-recase-any.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/generate-twolcs.py -r recase-any -o $@

generated/omorfi-uppercase-first.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/generate-twolcs.py -r uppercase-first -o $@

generated/omorfi-hyphens.twolc: generated/timestamp
	$(PYTHON) $(srcdir)/generate-twolcs.py -r hyphens -o $@

generated/omorfi-orthographic-variations.regex: generated/timestamp
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r orthographic-variations -o $@

generated/omorfi-zh.regex: generated/timestamp
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r zh -o $@

generated/omorfi-sh.regex: generated/timestamp
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r sh -o $@

generated/omorfi-remove-boundaries.regex: generated/timestamp
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r remove-boundaries -o $@

generated/omorfi-between-tokens.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r between-tokens -o $@

generated/omorfi-token.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r token -o $@

generated/omorfi-hyphenate.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r hyphenate -o $@

# database to omor 
generated/omorfi-omor-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/generate-yamls.py -i $< -o $@ -f=omor -v

generated/omorfi-omor.reweight: generate-reweights.py
	$(PYTHON) $(srcdir)/generate-reweights.py -v -f=omor -o $@

generated/omorfi-omor.lexc: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/generate-lexcs.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=omor

generated/omorfi-omor-rewrite-tags.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=omor \
		-r rewrite-tags -o $@

# database to ftb3 
generated/omorfi-ftb3-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/generate-yamls.py -i $< -o $@ -f=ftb3 -v

generated/omorfi-ftb3.reweight: generate-reweights.py
	$(PYTHON) $(srcdir)/generate-reweights.py -v -f=ftb3 -o $@

generated/omorfi-ftb3.lexc: generated/master.tsv generated/stemparts.tsv generated/inflections.tsv
	$(PYTHON) $(srcdir)/generate-lexcs.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=ftb3

generated/omorfi-ftb3-rewrite-tags.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r rewrite-tags -o $@

generated/omorfi-ftb3-lemmatise.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r lemmatise -o $@

# database to apertium
generated/apertium-fin.fin.lexc: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/generate-lexcs.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@ -f=apertium

generated/apertium-fin.fin.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -v -f=apertium -r apertium -o $@

generated/omorfi.dix: generated/master.tsv generated/stemparts.tsv \
	generated/inflections.tsv
	$(PYTHON) $(srcdir)/generate-monodix.py -v -m generated/master.tsv \
		-p generated/stemparts.tsv \
		-i generated/inflections.tsv -o $@

# database (back) to kotus
generated/omorfi-sanalista.xml: generated/master.tsv
	$(PYTHON) $(srcdir)/generate-kotus-sanalista.py -v -m generated/master.tsv -o $@
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

# spelling variations
generated/temporary.relaxed.hfst: generated/temporary.hyphenated.hfst \
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

# make tag adjustments
generated/temporary.tagged.hfst: generated/temporary.orth.hfst
	cp -vf $< $@

# remove remaining morph boundaries at this point
generated/temporary.unbounded.hfst: generated/temporary.tagged.hfst |\
	generated/omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 generated/omorfi-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# no tag weights
generated/temporary.tagweighted.hfst: generated/temporary.unbounded.hfst
	cp -v $< $@

# no token weights
generated/temporary.tokenweighted.hfst: generated/temporary.tagweighted.hfst
	cp -v $< $@

# no other weight combinations
generated/temporary.weighted.hfst: generated/temporary.tokenweighted.hfst
	cp -v $< $@

# lemmatisation is now built by messing with ftb3
generated/omorfi.lemmatise.hfst: generated/temporary.ftb3.hfst generated/omorfi-ftb3-lemmatise.regex.hfst
	$(HCOMP) $(HFST_FLAGS) $< generated/omorfi-ftb3-lemmatise.regex.hfst -o $@

# 
generated/omorfi.segment.hfst: generated/temporary.weighted.hfst
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
generated/omorfi-ftb3.generate.hfst: generated/temporary-ftb3.unbounded.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

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

# case variations
generated/temporary-omor.orth.hfst: generated/temporary-omor.relaxed.hfst \
	generated/omorfi-recase-any.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 generated/omorfi-recase-any.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# remove remaining morph boundaries at this point
generated/temporary-omor.unbounded.hfst: generated/temporary-omor.orth.hfst |\
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
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
generated/omorfi-omor.generate.hfst: generated/temporary-omor.unbounded.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

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
generated/errmodel.edit-distance.txt: generate-edit-distance.py
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
