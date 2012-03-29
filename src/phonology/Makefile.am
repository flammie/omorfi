## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose
HTWOLC_FLAGS=$(HFST_FLAGS) --resolve $(WEIGHTFLAG)

PHONOLOGY_SRCS=omorfi.twolc
PHONOLOGY_TARGETS=omorfi.twolc.hfst

EXTRA_DIST=$(PHONOLOGY_SRCS)
noinst_DATA=omorfi.twolc.hfst

omorfi.twolc.hfst: omorfi.twolc
	$(HTWOLC) $(HTWOLC_FLAGS) -o $@ -i $<

clean-local:
	-rm -f *.hfst *.ol

