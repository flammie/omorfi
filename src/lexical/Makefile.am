## Process this file with automake to produce Makefile.in

XML_SRCS=externals/kotus-sanalista_v1.xml externals/joukahainen.xml
LEXEMES=lexemes/lexemes.tsv
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
INFLECTIONS=continuations/acro-inflections.tsv \
			continuations/adjective-inflections.tsv \
			continuations/digit-inflections.tsv \
			continuations/noun-inflections.tsv \
			continuations/numeral-inflections.tsv \
			continuations/particle-inflections.tsv \
			continuations/pronoun-inflections.tsv \
			continuations/symbol-inflections.tsv \
			continuations/verb-inflections.tsv
JOINS=attributes/boundaries.tsv \
	  attributes/origin.tsv \
	  attributes/plurale-tantum.tsv attributes/possessives.tsv \
	  attributes/pronunciation.tsv attributes/proper-classes.tsv \
	  attributes/particle-classes.tsv attributes/pronoun-classes.tsv \
	  attributes/symbol-classes.tsv \
	  attributes/semantic.tsv \
	  attributes/subcategories.tsv \
	  attributes/usage.tsv \
	  attributes/verb-arguments.tsv
SCIRPTS=tsv2lexc.py tsvjoin.py tsv_expand.py
FINNISC=\
		format_output.py \
		gradation.py \
		lexc_string_utils.py \
		parse_csv_data.py \
		plurale_tantum.py \
		stub.py \
		guess_feats.py guess_new_class.py wordmap.py \
		omor_strings_io.py \
		apertium_formatter.py
EXTRA_DIST=$(XML_SRCS) $(LEXEMES) $(JOINS) $(SCIRPTS) $(FINNISC) $(STEMPARTS) $(INFLECTIONS)
TESTS=format_output.py apertium_formatter.py

noinst_DATA=omorfi-$(TAG_FORMAT).lexc omorfi.dix omorfi-sanalista.xml \
			omorfi-$(TAG_FORMAT).reweight gtd-tests-$(TAG_FORMAT).yaml

if CAN_PYTHON
gtd-tests-$(TAG_FORMAT).yaml: $(top_srcdir)/test/gtd-tests.tsv
	$(PYTHON) $(srcdir)/tsv2yaml.py -i $< -o $@ -f=$(TAG_FORMAT) -v

omorfi-$(TAG_FORMAT).reweight: serialise-reweighter.py format_output.py
	$(PYTHON) $(srcdir)/serialise-reweighter.py -v -f=$(TAG_FORMAT_PRECISE)\
		-o $@

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

omorfi-$(TAG_FORMAT).lexc: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/tsv2lexc.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@ -f=$(TAG_FORMAT_PRECISE)

omorfi.dix: master.tsv stemparts.tsv inflections.tsv
	$(PYTHON) $(srcdir)/tsv2monodix.py -v -m master.tsv -p stemparts.tsv \
		-i inflections.tsv -o $@

omorfi-sanalista.xml: master.tsv
	$(PYTHON) $(srcdir)/tsv2kotussanalista.py -v -m master.tsv -o $@
else
gtd-tests-$(TAG_FORMAT).yaml:
	echo "Lexical data preprocessing requires python3"
	false

omorfi-$(TAG_FORMAT).reweight:
	echo "Lexical data preprocessing requires python3"
	false
	false

joint.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

master.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

stemparts.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

inflections.tsv: 
	echo "Lexical data preprocessing requires python3"
	false

omorfi-$(TAG_FORMAT).lexc:
	echo "Lexical data preprocessing requires python3"
	false

omorfi.dix: 
	echo "Lexical data preprocessing requires python3"
	false

omorfi-sanalista.xml: 
	echo "Lexical data preprocessing requires python3"
	false
endif

clean-local:
	-rm -f master.tsv joint.tsv stemparts.tsv inflections.tsv \
		omorfi.lexc omorfi.dix omorfi-sanalista.xml

