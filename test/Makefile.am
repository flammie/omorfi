## Process this file with automake to produce Makefile.in

# order in slowness order
TESTS=rough-tests.sh \
	  rougher-tests.bash \
	  scripts-runnable.sh \
	  regressions.sh \
	  tokenisation-test.bash \
	  tools-python.bash \
	  ftb-3.1-quick-test.bash \
	  coverages-all-quick.bash \
	  coverages-less-quick.bash \
	  ftb-3.1-test.bash \
	  conllu-fi-tdt-ud-test.bash \
	  conllu-fi-ftb-ud-test.sh \
	  vislcg-fi-ud-test.sh \
	  finer-test.bash \
	  unimorph-test.bash
XFAIL_TESTS=
if WANT_BIG_TESTS
TESTS+=coverages-all-slow.bash
endif

TESTDATAFILES=wordforms.list \
			  wordforms-common.list \
			  test.text \
			  test.conllu \
			  test.cg3text

EXTRA_DIST=rough-tests.sh \
		   rougher-tests.bash \
		   regressions.sh \
		   scripts-runnable.sh \
		   faithfulness.py \
		   conllu-compare.py \
		   $(TESTDATAFILES)

CLEANFILES=wordforms.anals wordforms-common.anals

if CAN_YAML_TEST
#yaml-tests.yaml: test-header.yaml $(top_builddir)/src/lexical/gtd-tests.yaml
#	cat test-header.yaml gtd-tests.yaml > $@

endif


coverage-fast-alls.freqs: corpora/5grams.uniq.freqs \
						  corpora/fiwiki-latest-pages-articles.uniq.freqs \
						  corpora/OpenSubtitles2016.fi.uniq.freqs \
						  corpora/ftb1-2014.uniq.freqs \
						  corpora/tatoeba-fi.uniq.freqs \
						  corpora/europarl-v7.fi-en.fi.uniq.freqs \
						  corpora/ftb3.1.uniq.freqs \
						  corpora/fi_ftb-ud.uniq.freqs \
						  corpora/gutenberg-fi.uniq.freqs \
						  corpora/vks.uniq.freqs \
						  corpora/fi_tdt-ud.uniq.freqs \
						  corpora/jrc-fi.uniq.freqs \
						  corpora/vns.uniq.freqs \
						  corpora/finer.uniq.freqs
	$(PYTHON) sum-uniq-freqs.py -o $@ -t 1000 $^

