## Process this file with automake to produce Makefile.in

XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
LEXEMES=lexemes/fiwn.csv lexemes/joukahainen.csv lexemes/nss.csv \
		lexemes/omorfi.csv lexemes/pronouns.csv lexemes/visk.csv \
		lexemes/propers-unihu-proj.csv lexemes/fiwikt.csv
JOINS=attributes/boundaries.csv attributes/broken-paradigms.csv \
	  attributes/plurale-tantum.csv attributes/possessives.csv \
	  attributes/pronunciation.csv attributes/proper-classes.csv \
	  attributes/usage.csv
SCIRPTS=csv2lexc.py csvjoin.py
FINNISC=\
		format_output.py \
		gradation.py \
		lexc_string_utils.py \
		parse_csv_data.py \
		plurale_tantum.py \
		stub.py
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) $(FINNISC)

noinst_DATA=omor.timestamp

lexemes.csv: $(LEXEMES)
	echo "# This file has been generated automatically from lexemes/" > $@
	echo "# Updates to this file will be deleted on next make" >> $@
	cat $^ | sort | uniq >> $@

master.csv: lexemes.csv $(JOINS)
	$(PYTHON) $(srcdir)/csvjoin.py -v -i lexemes.csv \
		-j $(srcdir)/attributes/boundaries.csv \
		-j $(srcdir)/attributes/broken-paradigms.csv \
		-j $(srcdir)/attributes/plurale-tantum.csv \
		-j $(srcdir)/attributes/possessives.csv \
		-j $(srcdir)/attributes/pronunciation.csv \
		-j $(srcdir)/attributes/proper-classes.csv \
		-j $(srcdir)/attributes/usage.csv -o $@

omor.timestamp: master.csv
	if test ! -d $(top_builddir)/src/morphology/roots ; then \
		mkdir -p $(top_builddir)/src/morphology/roots ; \
	fi
	$(PYTHON) $(srcdir)/csv2lexc.py -v -i $< -o $(top_builddir)/src/morphology/roots -x NUMERAL -x PRONOUN
	touch $@

clean-local:
	-rm -f omor.timestamp master.csv lexemes.csv

