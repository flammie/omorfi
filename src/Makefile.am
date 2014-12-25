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
GENERIC_AUTOMATA=omorfi.accept.hfst \
				 omorfi.lemmatise.hfst \
				 omorfi.tokenise.hfst \
				 omorfi.hyphenate.hfst \
				 omorfi.segment.hfst
GENERIC_GENERATED=omorfi-uppercase-any.twolc \
				  omorfi-phon.twolc \
				  omorfi-zh.regex omorfi-sh.regex \
				  omorfi-orthographic-variations.regex \
				  omorfi-remove-boundaries.regex
				  omorfi-hyphens.twolc \
				  omorfi-between-tokens.regex.hfst \
				  omorfi-token.regex.hfst
if WANT_FTB3
FTB3_AUTOMATA=omorfi-ftb3.analyse.hfst \
			  omorfi-ftb3.generate.hfst
FTB3_GENERATED=omorfi-ftb3.lexc omorfi-ftb3.reweight omorfi-ftb3-tests.yaml \
			   omorfi-ftb3-rewrite-tags.regex

endif
if WANT_FTB3
OMOR_AUTOMATA=omorfi-omor.analyse.hfst \
			  omorfi-omor.generate.hfst
OMOR_GENERATED=omorfi-omor.lexc omorfi-omor.reweight omorfi-omor-tests.yaml \
			   omorfi-omor-rewrite-tags.regex \
			   omorfi-omor-between-tokens.regex.hfst \
			   omorfi-omor-token.regex.hfst

endif
endif
# }}}
# {{{Autotools install
# destnations directories for this stuff at the top of the file
hfstfidata_DATA=$(GENERIC_AUTOMATA) $(FTB3_AUTOMATA) $(OMOR_AUTOMATA)
voikkoshare_DATA=speller-omorfi.zhfst

# These go into dist tarballs... which we no longer make
# N.B. for distcheck anyways
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) \
		   $(STEMPARTS) $(INFLECTIONS) \
		   voikko-fi_FI.pro index.xml

# These are ran with make check. All modules should have stuff
TESTS=tagset_formatter.py apertium_formatter.py

# These aren't installed but generated
noinst_DATA=omorfi.dix omorfi-sanalista.xml

# Things that make clean isn't smart enought to wipe
CLEANFILES=$(GENERIC_GENERATED) $(FTB3_GENERATED)
# }}}
#
# {{{GENERATING
if CAN_PYTHON
# database to database
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

# database to generic
omorfi.lexc: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/generate-lexcs.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=generic

omorfi-phon.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -r recase-any -o $@

omorfi-recase-any.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -r recase-any -o $@

omorfi-uppercase-first.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -r uppercase-first -o $@

omorfi-hyphens.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -r hyphens -o $@

omorfi-orthographic-variations.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r orthographic-variations -o $@

omorfi-zh.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r zh -o $@

omorfi-sh.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r sh -o $@

omorfi-remove-boundaries.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r remove-boundaries -o $@

omorfi-between-tokens.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r between-tokens -o $@

omorfi-token.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py \
		-r token -o $@

omorfi-hyphenate.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r hyphenate -o $@

# database to omor 
omorfi-omor-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/generate-yamls.py -i $< -o $@ -f=omor -v

omorfi-omor.reweight: generate-reweights.py
	$(PYTHON) $(srcdir)/generate-reweights.py -v -f=omor -o $@

omorfi-omor.lexc: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/generate-lexcs.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=omor

omorfi-omor-rewrite-tags.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=omor \
		-r rewrite-tags -o $@

# database to ftb3 
omorfi-ftb3-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/generate-yamls.py -i $< -o $@ -f=ftb3 -v

omorfi-ftb3.reweight: generate-reweights.py
	$(PYTHON) $(srcdir)/generate-reweights.py -v -f=ftb3 -o $@

omorfi-ftb3.lexc: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/generate-lexcs.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=ftb3

omorfi-ftb3-rewrite-tags.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r rewrite-tags -o $@

omorfi-ftb3-lemmatise.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r lemmatise -o $@

# database to apertium
omorfi.dix: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/generate-monodix.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@

# database (back) to kotus
omorfi-sanalista.xml: master.tsv
	$(PYTHON) $(srcdir)/generate-kotus-sanalista.py -v -m master.tsv -o $@
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
temporary.phon.hfst: omorfi.lexc.hfst omorfi-phon.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-phon.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# word-boundary huphens
temporary.hyphenated.hfst: temporary.phon.hfst \
	omorfi-hyphens.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-hyphens.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# spelling variations
temporary.relaxed.hfst: temporary.hyphenated.hfst \
	omorfi-sh.regex.hfst \
	omorfi-zh.regex.hfst \
	omorfi-orthographic-variations.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-orthographic-variations.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T omorfi-sh.regex.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T omorfi-zh.regex.hfst -o $@

# case variations
temporary.orth.hfst: temporary.relaxed.hfst \
	omorfi-uppercase-first.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-uppercase-first.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# make tag adjustments
temporary.tagged.hfst: temporary.orth.hfst
	cp -vf $< $@

# remove remaining morph boundaries at this point
temporary.unbounded.hfst: temporary.tagged.hfst |\
	omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# no tag weights
temporary.tagweighted.hfst: temporary.unbounded.hfst
	cp -v $< $@

# no token weights
temporary.tokenweighted.hfst: temporary.tagweighted.hfst
	cp -v $< $@

# no other weight combinations
temporary.weighted.hfst: temporary.tokenweighted.hfst
	cp -v $< $@

# lemmatisation is now built by messing with ftb3
omorfi.lemmatise.hfst: temporary.ftb3.hfst omorfi-ftb3-lemmatise.regex.hfst
	$(HCOMP) $(HFST_FLAGS) $< omorfi-ftb3-lemmatise.regex.hfst -o $@

# 
omorfi.segment.hfst: temporary.weighted.hfst
	$(HINV) $< -o $@

# create one tape spell checker
omorfi.accept.hfst: temporary.ftb3.hfst
	$(HPR) $(HFST_FLAGS) --project=upper -i $< -o $@

# create basic corpus tokeniser
# Should split at even-odd boundaries of word punct* word punct*
omorfi.token-separator.hfst:
	echo '0:"\n" ;' | $(HREGEX) -o omorfi.token-separator.hfst

omorfi.tokenise.hfst: omorfi.accept.hfst \
					  omorfi-between-tokens.regex.hfst \
					  omorfi-token.regex.hfst \
					  omorfi.token-separator.hfst
	$(HCAT) $(HFST_FLAGS) omorfi-token.regex.hfst \
		omorfi.token-separator.hfst |\
		$(HMIN) $(HFST_FLAGS) -o omorfi.nondict-token.hfst
	$(HCAT) $(HFST_FLAGS) omorfi-between-tokens.regex.hfst \
		omorfi.token-separator.hfst -o omorfi-token-joiner.hfst
	$(HCAT) $(HFST_FLAGS) omorfi.nondict-token.hfst \
		omorfi-token-joiner.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 -o $@

# hyphenation dictionary
omorfi.hyphenate.hfst: temporary-ftb3.orth.hfst \
						omorfi-ftb3-hyphenate.twolc.hfst
	cat temporary-ftb3.orth.hfst |\
		$(HIC) $(HFST_FLAGS) -2 omorfi-ftb3-hyphenate.twolc.hfst > $@

# }}}
# {{{FTB3 compilation
# combine lexical data with phonology
temporary-ftb3.phon.hfst: omorfi-ftb3.lexc.hfst omorfi-phon.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-phon.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# word-boundary huphens
temporary-ftb3.hyphenated.hfst: temporary-ftb3.phon.hfst \
	omorfi-hyphens.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-hyphens.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# spelling variations
temporary-ftb3.relaxed.hfst: temporary-ftb3.hyphenated.hfst \
	omorfi-sh.regex.hfst \
	omorfi-zh.regex.hfst \
	omorfi-orthographic-variations.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-orthographic-variations.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T omorfi-sh.regex.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T omorfi-zh.regex.hfst -o $@

# case variations
temporary-ftb3.orth.hfst: temporary-ftb3.relaxed.hfst \
	omorfi-uppercase-first.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-uppercase-first.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# make tag adjustments
temporary-ftb3.tagged.hfst: temporary-ftb3.orth.hfst \
	omorfi-ftb3-rewrite-tags.regex.hfst
	cat $< |\
		$(HINV) $(HFST_FLAGS) |\
		$(HCOMP) $(HFST_FLAGS) -2 omorfi-ftb3-rewrite-tags.regex.hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove remaining morph boundaries at this point
temporary-ftb3.unbounded.hfst: temporary-ftb3.tagged.hfst |\
	omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# hand-written weights for ftb3
temporary-ftb3.tagweighted.hfst: temporary-ftb3.unbounded.hfst omorfi-ftb3.reweight
	$(HREW) $(HFST_FLAGS) -T omorfi-ftb3.reweight temporary-ftb3.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# no token weights
temporary-ftb3.tokenweighted.hfst: temporary-ftb3.tagweighted.hfst
	cp -v $< $@

# no other weight combinations
temporary-ftb3.weighted.hfst: temporary-ftb3.tokenweighted.hfst
	cp -v $< $@

# create morphological analyzer
temporary.ftb3.hfst: temporary-ftb3.weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

# finalising
omorfi-ftb3.analyse.hfst: temporary.ftb3.hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
omorfi-ftb3.generate.hfst: temporary-ftb3.unbounded.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

# }}}
#
# {{{OMOR compilation
# combine lexical data with phonology
temporary-omor.phon.hfst: omorfi-omor.lexc.hfst omorfi-phon.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-phon.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# word-boundary huphens
temporary-omor.hyphenated.hfst: temporary-omor.phon.hfst \
	omorfi-hyphens.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-hyphens.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# spelling variations
temporary-omor.relaxed.hfst: temporary-omor.hyphenated.hfst \
	omorfi-sh.regex.hfst \
	omorfi-zh.regex.hfst \
	omorfi-orthographic-variations.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-orthographic-variations.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T omorfi-sh.regex.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T omorfi-zh.regex.hfst -o $@

# case variations
temporary-omor.orth.hfst: temporary-omor.relaxed.hfst \
	omorfi-recase-any.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-recase-any.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# make tag adjustments
temporary-omor.tagged.hfst: temporary-omor.orth.hfst \
	omorfi-omor-rewrite-tags.regex.hfst
	cat $< |\
		$(HINV) $(HFST_FLAGS) |\
		$(HCOMP) $(HFST_FLAGS) -2 omorfi-omor-rewrite-tags.regex.hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove remaining morph boundaries at this point
temporary-omor.unbounded.hfst: temporary-omor.tagged.hfst |\
	omorfi-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# hand-written weights for omor
temporary-omor.tagweighted.hfst: temporary-omor.unbounded.hfst omorfi-omor.reweight
	$(HREW) $(HFST_FLAGS) -T omorfi-omor.reweight temporary-omor.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# no token weights
temporary-omor.tokenweighted.hfst: temporary-omor.tagweighted.hfst
	cp -v $< $@

# no other weight combinations
temporary-omor.weighted.hfst: temporary-omor.tokenweighted.hfst
	cp -v $< $@

# create morphological analyzer
temporary.omor.hfst: temporary-omor.weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

# finalising
omorfi-omor.analyse.hfst: temporary.omor.hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
omorfi-omor.generate.hfst: temporary-omor.unbounded.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

# }}}
#
#
# {{{SPELL-CHECKING
# voikko speller HFST beta targets'
errmodel.edit-distance.txt: generate-edit-distance.py
	$(PYTHON) $< -o $@

errmodel.edit-distance-1.hfst: errmodle.edit-distance.hfst
	$(HMIN) $< -o $@

errmodel.edit-distance-2.hfst: errmodel.edit-distance.hfst
	$(HMIN) $< |\
		$(HREP) -f 1 -t 2 -o $@

errmodel.edit-distance-3.hfst: errmodel.edit-distance.hfst
	$(HMIN) $< |\
		$(HREP) -f 1 -t 3 -o $@

speller-omorfi.zhfst: omorfi.accept.hfst \
					errmodel.edit-distance-2.hfst index.xml
	$(HF2F) -f olw < omorfi.accept.hfst > acceptor.default.hfst
	$(HF2F) -f olw < errmodel.edit-distance-2.hfst > errmodel.default.hfst
	$(ZIP) -v -9 $@ index.xml acceptor.default.hfst errmodel.default.hfst
	-rm -f acceptor.default.hfst errmodel.default.hfst

# }}}
# vim: set foldmethod=marker:
