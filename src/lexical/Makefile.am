## Process this file with automake to produce Makefile.in

XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
LEXEMES=lexemes/fiwn.csv lexemes/joukahainen.csv lexemes/nss.csv \
		lexemes/omorfi.csv lexemes/visk.csv lexemes/chemistry.csv \
		lexemes/propers-unihu-proj.csv lexemes/fiwikt.csv
STEMPARTS=continuations/acronym-stems.tsv \
		  continuations/adjective-stems.tsv \
		  continuations/digit-stems.tsv \
		  continuations/noun-stems.tsv \
		  continuations/numeral-stems.tsv \
		  continuations/pronoun-stems.tsv \
		  continuations/verb-stems.tsv
INFLECTIONS=continuations/acro-inflections.tsv \
			continuations/adjective-inflections.tsv \
			continuations/digit-inflections.tsv \
			continuations/noun-inflections.tsv \
			continuations/numeral-inflections.tsv \
			continuations/particle-inflections.tsv \
			continuations/pronoun-inflections.tsv \
			continuations/verb-inflections.tsv
JOINS=attributes/boundaries.csv \
	  attributes/plurale-tantum.csv attributes/possessives.csv \
	  attributes/pronunciation.csv attributes/proper-classes.csv \
	  attributes/particle-classes.csv attributes/pronoun-classes.csv \
	  attributes/semantic.csv attributes/subcategories.csv attributes/usage.csv
SCIRPTS=csv2lexc.py csvjoin.py csv_expand.py
FINNISC=\
		format_output.py \
		gradation.py \
		lexc_string_utils.py \
		parse_csv_data.py \
		plurale_tantum.py \
		stub.py \
		guess_feats.py guess_new_class.py wordmap.py \
		omor_strings_io.py
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) $(FINNISC)
TESTS=format_output.py

noinst_DATA=omor.timestamp


kotus-style.csv: $(LEXEMES)
	echo "# This file has been generated automatically from lexemes/" > $@
	echo "# Updates to this file will be deleted on next make" >> $@
	cat $^ | sort | uniq >> $@

joint.tsv: kotus-style.csv $(JOINS)
	$(PYTHON) $(srcdir)/csvjoin.py -v -i $< \
		-j $(srcdir)/attributes/boundaries.csv \
		-j $(srcdir)/attributes/plurale-tantum.csv \
		-j $(srcdir)/attributes/possessives.csv \
		-j $(srcdir)/attributes/pronunciation.csv \
		-j $(srcdir)/attributes/particle-classes.csv \
		-j $(srcdir)/attributes/proper-classes.csv \
		-j $(srcdir)/attributes/pronoun-classes.csv \
		-j $(srcdir)/attributes/semantic.csv \
		-j $(srcdir)/attributes/subcategories.csv \
		-j $(srcdir)/attributes/usage.csv -o $@

master.tsv: joint.tsv
	$(PYTHON) $(srcdir)/csv_expand.py -i $< -o $@

stemparts.tsv: $(STEMPARTS)
	cat $^ | grep -v '^#' | sort > $@

inflections.tsv: $(INFLECTIONS)
	cat $^ | grep -v '^#' | sort> $@

omor.timestamp: master.tsv stemparts.tsv inflections.tsv
	if test ! -d $(top_builddir)/src/morphology/roots ; then \
		mkdir -p $(top_builddir)/src/morphology/roots ; \
	fi
	if test ! -d $(top_builddir)/src/morphology/stems ; then \
		mkdir -p $(top_builddir)/src/morphology/stems ; \
	fi
	if test ! -d $(top_builddir)/src/morphology/inflection ; then \
		mkdir -p $(top_builddir)/src/morphology/inflection ; \
	fi
	$(PYTHON) $(srcdir)/csv2lexc.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv \
		-s $(top_builddir)/src/morphology/roots \
		-S $(top_builddir)/src/morphology/stems \
		-X $(top_builddir)/src/morphology/inflection \
		-R $(top_builddir)/src/morphology/definitions.lexc \
		-f=$(TAG_FORMAT)
	touch $@

clean-local:
	-rm -f omor.timestamp master.tsv joint.tsv kotus-style.csv stemparts.tsv inflections.tsv

