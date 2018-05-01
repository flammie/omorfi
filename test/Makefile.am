## Process this file with automake to produce Makefile.in

TESTS=rough-tests.sh scripts-runnable.sh \
	  tools-all-quick.bash \
	  ftb-3.1-quick-test.bash \
	  coverages-all-quick.sh \
	  ftb-3.1-test.bash \
	  conllu-fi-tdt-ud-test.bash \
	  conllu-fi-ftb-ud-test.sh \
	  regressions.sh \
	  vislcg-fi-ud-test.sh \
	  rougher-tests.bash \
	  coverages-less-quick.bash
XFAIL_TESTS=
if WANT_BIG_TESTS
TESTS+=coverages-all-slow.bash
endif
EXTRA_DIST=rough-tests.sh \
		   scripts-runnable.sh \
		   wordforms.list \
		   wordforms-common.list \
		   coverage.py \
		   faithfulness.py \
		   conllu-compare.py

CLEANFILES=wordforms.anals

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

