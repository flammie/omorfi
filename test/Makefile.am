## Process this file with automake to produce Makefile.in

TESTS=rough-tests.sh scripts-runnable.sh
#XFAIL_TESTS=
BIG_TESTS=europarl-coverage.sh gutenberg-coverage.sh jrc-acquis-coverage.sh \
		  ftb31-coverage.sh ftb-test.sh
EXTRA_DIST=rough-tests.sh scripts-runnable.sh ftb-test.sh \
		   wordforms.list ftb-test.py yaml-tests.sh \
		   $(BIG_TESTS)

if CAN_YAML_TEST
yaml-tests.yaml: test-header.yaml $(top_builddir)/src/lexical/gtd-tests.yaml
	cat test-header.yaml gtd-tests.yaml > $@

TESTS+=yaml-tests.sh
endif

if WANT_BIG_TESTS
TESTS+=$(BIG_TESTS)
endif

clean-local:
	-rm -f wordforms.anals
