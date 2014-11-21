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
				   serialise-reweighter.py \
				   generate-twolcs.py generate-regexes.py
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

if WANT_HFST
if WANT_FTB3
FTB3_AUTOMATA=omorfi-ftb3.analyse.hfst \
			  omorfi-ftb3.lemmatise.hfst \
			  omorfi-ftb3.generate.hfst \
			  omorfi-ftb3.accept.hfst \
			  omorfi-ftb3.tokenise.hfst \
			  omorfi-ftb3.hyphenate.hfst
FTB3_GENERATED=omorfi-ftb3.lexc omorfi-ftb3.reweight omorfi-ftb3-tests.yaml \
			   omorfi-ftb3-phon.twolc omorfi-ftb3-uppercase-any.twolc \
			   omorfi-ftb3-hyphens.twolc \
			   omorfi-ftb3-orthographic-variations.regex \
			   omorfi-ftb3-zh.regex omorfi-ftb3-sh.regex \
			   omorfi-ftb3-rewrite-tags.regex \
			   omorfi-ftb3-between-tokens.regex.hfst \
			   omorfi-ftb3-token.regex.hfst \
			   omorfi-ftb3-remove-boundaries.regex

endif
endif

hfstfidata_DATA=$(FTB3_AUTOMATA)
#voikkoshare_DATA=speller-omorfi.zhfst

EXTRA_DIST=\
		   $(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) \
		   $(STEMPARTS) $(INFLECTIONS) \
		   voikko-fi_FI.pro index.xml

TESTS=tagset_formatter.py apertium_formatter.py

noinst_DATA=$(FTB3_GENERATED) omorfi.dix omorfi-sanalista.xml
if CAN_PYTHON
omorfi-ftb3-tests.yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/tsv2yaml.py -i $< -o $@ -f=ftb3 -v

omorfi-ftb3.reweight: serialise-reweighter.py
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

omorfi-ftb3.lexc: master.tsv stemparts.tsv inflections.tsv tsv2lexc.py
	$(PYTHON) $(srcdir)/tsv2lexc.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=ftb3

omorfi-ftb3-phon.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r stub-phon -o $@

omorfi-ftb3-uppercase-any.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r uppercase-any -o $@

omorfi-ftb3-hyphens.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r hyphens -o $@

omorfi-ftb3-orthographic-variations.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r orthographic-variations -o $@

omorfi-ftb3-zh.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r zh -o $@

omorfi-ftb3-sh.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r sh -o $@

omorfi-ftb3-rewrite-tags.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r rewrite-tags -o $@

omorfi-ftb3-remove-boundaries.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r remove-boundaries -o $@

omorfi-ftb3-between-tokens.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r between-tokens -o $@

omorfi-ftb3-token.regex:
	$(PYTHON) $(srcdir)/generate-regexes.py -f=ftb3 \
		-r token -o $@

omorfi-ftb3-hyphenate.twolc:
	$(PYTHON) $(srcdir)/generate-twolcs.py -f=ftb3 -r hyphenate -o $@

omorfi.dix: master.tsv stemparts.tsv inflections.tsv $(FORMAT_SCIRPTS)
	$(PYTHON) $(srcdir)/tsv2monodix.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@

omorfi-sanalista.xml: master.tsv $(FORMAT_SCIRPTS)
	$(PYTHON) $(srcdir)/tsv2kotussanalista.py -v -m master.tsv -o $@
endif

# compile lexc
%.lexc.hfst: %.lexc
	$(HLEXC) --Werror -o $@ $<

# compile twolc
%.twolc.hfst: %.twolc
	$(HTWOLC) $(HFST_FLAGS) --resolve -o $@ $<

%.regex.hfst: %.regex
	$(HREGEX) $(HFST_FLAGS) --semicolon -j -i $< |\
		$(HMIN) $(HFST_FLAGS) -o $@

# combine lexical data with phonology
temporary-ftb3.phon.hfst: omorfi-ftb3.lexc.hfst omorfi-ftb3-phon.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-ftb3-phon.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

# make orthographical adjustments to phonemic version
temporary-ftb3.hyphenated.hfst: temporary-ftb3.phon.hfst \
	omorfi-ftb3-hyphens.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-ftb3-hyphens.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

temporary-ftb3.relaxed.hfst: temporary-ftb3.hyphenated.hfst \
	omorfi-ftb3-sh.regex.hfst \
	omorfi-ftb3-zh.regex.hfst \
	omorfi-ftb3-orthographic-variations.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-ftb3-orthographic-variations.regex.hfst |\
		$(HMIN) $(HFST_FLAGS) |\
		$(HSUB) $(HFST_FLAGS) -f š -T omorfi-ftb3-sh.regex.hfst |\
		$(HSUB) $(HFST_FLAGS) -f ž -T omorfi-ftb3-zh.regex.hfst -o $@

temporary-ftb3.orth.hfst: temporary-ftb3.relaxed.hfst \
	omorfi-ftb3-uppercase-any.twolc.hfst
	$(HIC) $(HFST_FLAGS) -1 $< -2 omorfi-ftb3-uppercase-any.twolc.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# make tag adjustments to orthographical version
temporary-ftb3.tagged.hfst: temporary-ftb3.orth.hfst \
	omorfi-ftb3-rewrite-tags.regex.hfst
	cat $< |\
		$(HINV) $(HFST_FLAGS) |\
		$(HCOMP) $(HFST_FLAGS) -2 omorfi-ftb3-rewrite-tags.regex.hfst |\
		$(HINV) $(HFST_FLAGS) |\
		$(HMIN) $(HFST_FLAGS) > $@

# remove word boundaries at this point
temporary-ftb3.unbounded.hfst: temporary-ftb3.tagged.hfst |\
	omorfi-ftb3-remove-boundaries.regex.hfst
	$(HCOMP) $(HFST_FLAGS) -1 $< -2 omorfi-ftb3-remove-boundaries.regex.hfst  |\
		$(HMIN) $(HFST_FLAGS) > $@

# hand-written weights
temporary-ftb3.tagweighted.hfst: temporary-ftb3.unbounded.hfst omorfi-ftb3.reweight
	$(HREW) $(HFST_FLAGS) -T omorfi-ftb3.reweight temporary-ftb3.unbounded.hfst |\
		$(HMIN) $(HFST_FLAGS) > $@

temporary-ftb3.tokenweighted.hfst: temporary-ftb3.tagweighted.hfst
	cp -v $< $@

temporary-ftb3.weighted.hfst: temporary-ftb3.tokenweighted.hfst
	cp -v $< $@

# create morphological analyzer
temporary.ftb3.hfst: temporary-ftb3.weighted.hfst
	$(HINV) $(HFST_FLAGS) $< |\
		$(HMIN) $(HFST_FLAGS) > $@

omorfi-ftb3.analyse.hfst: temporary.ftb3.hfst
	$(HF2F) -f olw -o $@ -i $<

# create generator from analyzer
omorfi-ftb3.generate.hfst: temporary-ftb3.unbounded.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

# lemmatization is a special case of tagset variant
omorfi-ftb3.lemmatise.hfst: temporary.ftb3.hfst taghacks/lemmatize-ftb3.relabel
	$(HSUB) $(HFST_FLAGS) -F $(srcdir)/taghacks/lemmatize-ftb3.relabel -i $< -o $@

# create one tape spell checker
omorfi-ftb3.accept.hfst: temporary.ftb3.hfst
	$(HPR) $(HFST_FLAGS) --project=upper -i $< -o $@

# create basic corpus tokeniser
# Should split at even-odd boundaries of word punct* word punct*
omorfi-ftb3.tokenise.hfst: omorfi-ftb3.accept.hfst \
						omorfi-ftb3-between-tokens.regex.hfst \
						omorfi-ftb3-token.regex.hfst
	echo '0:"\n" ;' | $(HREGEX) -o omorfi-ftb3.token-separator.hfst
	$(HCAT) $(HFST_FLAGS) omorfi-ftb3-token.regex.hfst \
		omorfi-ftb3.token-separator.hfst |\
		$(HMIN) $(HFST_FLAGS) -o omorfi-ftb3.nondict-token.hfst
	$(HCAT) $(HFST_FLAGS) omorfi-ftb3-between-tokens.regex.hfst \
		omorfi-ftb3.token-separator.hfst -o omorfi-ftb3-token-joiner.hfst
	$(HCAT) $(HFST_FLAGS) omorfi-ftb3.nondict-token.hfst \
		omorfi-ftb3-token-joiner.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 -o $@

# hyphenation dictionary
omorfi-ftb3.hyphenate.hfst: temporary-ftb3.orth.hfst \
						omorfi-ftb3-hyphenate.twolc.hfst
	cat temporary-ftb3.orth.hfst |\
		$(HIC) $(HFST_FLAGS) -2 omorfi-ftb3-hyphenate.twolc.hfst > $@

# voikko speller HFST beta targets
speller-omorfi.zhfst: omorfi-ftb3.accept.hfst \
					spell-checking/error.edit-distance-2.hfst index.xml
	$(HF2F) -f olw < omorfi-ftb3.accept.hfst > acceptor.default.hfst
	$(HF2F) -f olw < spell-checking/error.edit-distance-2.hfst > errmodel.default.hfst
	$(ZIP) -v -9 $@ index.xml acceptor.default.hfst errmodel.default.hfst
	-rm -f acceptor.default.hfst errmodel.default.hfst


clean-local:
	-rm -f temporary-ftb3.*.hfst \
		master.tsv joint.tsv stemparts.tsv inflections.tsv \
		omorfi-ftb3.lexc omorfi.dix omorfi-sanalista.xml

