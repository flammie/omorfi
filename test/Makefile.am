## Process this file with automake to produce Makefile.in

# order in slowness order
TESTS=rough-tests.sh \
	  rougher-tests.bash \
	  scripts-runnable.sh \
	  regressions.sh \
	  tools-python.bash \
	  ftb-3.1-quick-test.bash \
	  coverages-all-quick.bash \
	  coverages-less-quick.bash \
	  ftb-3.1-test.bash \
	  conllu-fi-tdt-ud-test.bash \
	  conllu-fi-ftb-ud-test.sh \
	  vislcg-fi-ud-test.sh \
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


coverage-fast-alls.freqs: 5grams.uniq.freqs \
						  fiwiki-latest-pages-articles.uniq.freqs \
						  OpenSubtitles2016.fi.uniq.freqs \
						  ftb1-2014.uniq.freqs \
						  tatoeba-fi.uniq.freqs \
						  europarl-v7.fi-en.fi.uniq.freqs \
						  ftb3.1.uniq.freqs \
						  fi_ftb-ud.uniq.freqs \
						  gutenberg-fi.uniq.freqs \
						  vks.uniq.freqs \
						  fi-ud.uniq.freqs \
						  jrc-fi.uniq.freqs \
						  vns.uniq.freqs
	$(PYTHON) sum-uniq-freqs.py -o $@ -t 1000 $^

