## Process this file with automake to produce Makefile.in

TESTS=rough-tests.sh scripts-runnable.sh \
	  faithfulness-ftb-3.1-quick.sh \
	  coverages-all-quick.sh \
	  faithfulness-ftb-3.1.sh \
	  conllu-fi-ud-test.sh \
	  conllu-fi-ftb-ud-test.sh \
	  coverages-all-slow.bash
#XFAIL_TESTS=
EXTRA_DIST=rough-tests.sh \
		   scripts-runnable.sh \
		   wordforms.list \
		   coverage.py \
		   faithfulness.py \
		   conllu-compare.py

CLEANFILES=wordforms.anals

if CAN_YAML_TEST
#yaml-tests.yaml: test-header.yaml $(top_builddir)/src/lexical/gtd-tests.yaml
#	cat test-header.yaml gtd-tests.yaml > $@

endif

