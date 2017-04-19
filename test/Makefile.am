## Process this file with automake to produce Makefile.in

TESTS=rough-tests.sh scripts-runnable.sh \
	  tools-all-quick.bash \
	  faithfulness-ftb-3.1-quick.sh \
	  coverages-all-quick.sh \
	  faithfulness-ftb-3.1.sh \
	  conllu-fi-ud-test.sh \
	  conllu-fi-ftb-ud-test.sh
if WANT_BIG_TESTS
TESTS+=coverages-all-slow.bash
endif
XFAIL_TESTS=tools-all-quick.bash
if WANT_SMALL_LEXICONS
TESTS+=rougher-tests.bash coverages-less-quick.bash
XFAIL_TESTS+=rough-tests.sh coverages-all-quick.sh
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

