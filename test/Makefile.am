## Process this file with automake to produce Makefile.in

TESTS=rough-tests.sh scripts-runnable.sh ftb-test.sh
#XFAIL_TESTS=

EXTRA_DIST=rough-tests.sh scripts-runnable.sh ftb-test.sh \
		   wordforms.list ftb-test.py

if CAN_YAML_TEST
yaml-tests.yaml: test-header.yaml $(top_builddir)/src/lexical/gtd-tests.yaml
	cat test-header.yaml gtd-tests.yaml > $@

TESTS+=yaml-tests.sh
endif

clean-local:
	-rm -f wordforms.anals
