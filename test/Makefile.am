## Process this file with automake to produce Makefile.in

TESTS=rough-tests.sh scripts-runnable.sh ftb-3.1-faithfulness-quick.sh
#XFAIL_TESTS=
BIG_TESTS=europarl-coverage.sh gutenberg-coverage.sh jrc-acquis-coverage.sh \
		  ftb31-coverage.sh fiwiki-coverage.sh \
		  ftb-test.sh
EXTRA_DIST=rough-tests.sh scripts-runnable.sh \
		   wordforms.list ftb-test.py \
		   $(BIG_TESTS)

if CAN_YAML_TEST
#yaml-tests.yaml: test-header.yaml $(top_builddir)/src/lexical/gtd-tests.yaml
#	cat test-header.yaml gtd-tests.yaml > $@

endif

if WANT_BIG_TESTS
TESTS+=$(BIG_TESTS)
endif

clean-local:
	-rm -f wordforms.anals
