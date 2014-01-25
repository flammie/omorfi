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
JOINS=attributes/boundaries.tsv \
	  attributes/origin.tsv \
	  attributes/plurale-tantum.tsv attributes/possessives.tsv \
	  attributes/pronunciation.tsv attributes/proper-classes.tsv \
	  attributes/particle-classes.tsv attributes/pronoun-classes.tsv \
	  attributes/semantic.tsv attributes/subcategories.tsv attributes/usage.tsv
SCIRPTS=tsv2lexc.py tsvjoin.py tsv_expand.py
FINNISC=\
		format_output.py \
		gradation.py \
		lexc_string_utils.py \
		parse_csv_data.py \
		plurale_tantum.py \
		stub.py \
		guess_feats.py guess_new_class.py wordmap.py \
		omor_strings_io.py
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) $(FINNISC) $(STEMPARTS) $(INFLECTIONS)
TESTS=format_output.py

noinst_DATA=omorfi.lexc # omorfi.dix omorfi-sanalista.xml


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
		-j $(srcdir)/attributes/usage.tsv -o $@

master.tsv: joint.tsv
	$(PYTHON) $(srcdir)/tsv_expand.py \
		-j $(srcdir)/attributes/paradigm-data.tsv -v -i $< -o $@.unsrt
	head -n 1 < $@.unsrt > $@
	tail -n +2 < $@.unsrt | sort >> $@
	-rm -f $@.unsrt

stemparts.tsv: $(STEMPARTS)
	cat $^ | grep -v '^#' | fgrep -v 'HEADERS' | sort > $@

inflections.tsv: $(INFLECTIONS)
	cat $^ | grep -v '^#' | fgrep -v 'HEADERS' | sort > $@

omorfi.lexc: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/tsv2lexc.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=$(TAG_FORMAT_PRECISE)

omorfi.dix: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/tsv2monodix.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@

omorfi-sanalista.xml: master.tsv
	$(PYTHON) $(srcdir)/tsv2kotussanalista.py -v -m master.tsv -o $@

clean-local:
	-rm -f master.tsv joint.tsv stemparts.tsv inflections.tsv

