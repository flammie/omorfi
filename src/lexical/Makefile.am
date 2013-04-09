## Process this file with automake to produce Makefile.in

XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
LEXEMES=lexemes/fiwn.csv lexemes/joukahainen.csv lexemes/nss.csv \
		lexemes/omorfi.csv lexemes/visk.csv \
		lexemes/propers-unihu-proj.csv lexemes/fiwikt.csv
JOINS=attributes/boundaries.csv \
	  attributes/plurale-tantum.csv attributes/possessives.csv \
	  attributes/pronunciation.csv attributes/proper-classes.csv \
	  attributes/usage.csv
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

noinst_DATA=omor.timestamp

if WANT_PROPER_SUBCLASSES
MAYBE_PROPER_CLASSES = -j $(srcdir)/attributes/proper-classes.csv
endif

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
		$(MAYBE_PROPER_CLASSES) \
		-j $(srcdir)/attributes/usage.csv -o $@

master.tsv: joint.tsv
	$(PYTHON) $(srcdir)/csv_expand.py -i $< -o $@

omor.timestamp: master.tsv
	if test ! -d $(top_builddir)/src/morphology/roots ; then \
		mkdir -p $(top_builddir)/src/morphology/roots ; \
	fi
	$(PYTHON) $(srcdir)/csv2lexc.py -v -i $< -o $(top_builddir)/src/morphology/roots \
              -f=$(TAG_FORMAT) -x NUMERAL -x PRONOUN
	touch $@

clean-local:
	-rm -f omor.timestamp master.tsv joint.tsv kotus-style.csv

