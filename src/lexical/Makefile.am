## Process this file with automake to produce Makefile.in

XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
LEXEMES=lexemes/fiwn.csv lexemes/joukahainen.csv lexemes/nss.csv \
		lexemes/omorfi.csv lexemes/pronouns.csv lexemes/visk.csv
JOINS=attributes/boundaries.csv attributes/broken-paradigms.csv \
	  attributes/plurale-tantum.csv attributes/possessives.csv \
	  attributes/pronunciation.csv attributes/proper-classes.csv \
	  attributes/usage.csv
SCIRPTS=csv2lexc.py csvjoin.py regenerate-lexicons.sh

EXTRA_DIST=$(XML_SRCS) $(LEXICAL_SRCS) $(SCIRPTS)

lexemes.csv: $(LEXEMES)
	echo "# This file has been generated automatically from lexemes/" > $@
	echo "# Updates to this file will be deleted on next make" >> $@
	cat $^ | sort | uniq >> $@

master.csv: lexemes.csv $(JOINS)
	./csvjoin.py -v -i lexemes.csv -j attributes/boundaries.csv \
		-j attributes/broken-paradigms.csv \
		-j attributes/plurale-tantum.csv -j attributes/possessives.csv \
		-j attributes/pronunciation.csv -j attributes/proper-classes.csv \
		-j attributes/usage.csv -o $@

omor.timestamp: master.csv
	./csv2lexc.py -v -i $< -o $(topsrcdir)/morphology/roots
	touch $@

