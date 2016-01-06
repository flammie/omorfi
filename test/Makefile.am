## Process this file with automake to produce Makefile.in

TESTS=rough-tests.sh scripts-runnable.sh \
	  faithfulness-ftb-3.1-quick.sh \
	  coverages-all-quick.sh \
	  coverage-europarl.sh \
	  coverage-gutenberg.sh \
	  coverage-jrc-acquis.sh \
	  coverage-ftb-3.1.sh \
	  coverage-fiwiki.sh \
	  coverage-fi-ud.sh \
	  coverage-fi-ftb-ud.sh \
	  faithfulness-ftb-3.1.sh
#XFAIL_TESTS=
EXTRA_DIST=rough-tests.sh \
		   scripts-runnable.sh \
		   wordforms.list \
		   coverage.py \
		   faithfulness.py 

CLEANFILES=wordforms.anals

if CAN_YAML_TEST
#yaml-tests.yaml: test-header.yaml $(top_builddir)/src/lexical/gtd-tests.yaml
#	cat test-header.yaml gtd-tests.yaml > $@

endif

