## Process this file with automake to produce Makefile.in

if WANT_TAGGER_HACKS
MAYBE_TAGGER_HACKS=hacks/tagger-hacks.lexc
endif

# lexc data
LEXC_MAIN=omorfi-$(TAG_FORMAT).lexc
NOTGENERATED_SRCS=\
				  $(MAYBE_TAGGER_HACKS)

LEXC_SRCS=$(LEXC_MAIN) \
		  $(LEXICAL_SRCS) \
		  $(MORPHOLOGY_SRCS) \
		  $(NOTGENERATED_SRCS)
EXTRA_DIST=$(NOTGENERATED_SRCS)

LEXICAL_TARGETS=omorfi.lexc.hfst

noinst_DATA=omorfi.lexc.hfst

# lexical transducer
$(LEXC_MAIN): $(top_builddir)/src/lexical/omorfi-$(TAG_FORMAT).lexc
	-cp -v $< $@

omorfi.lexc.hfst: $(LEXC_MAIN) $(MAYBE_TAGGER_HACKS)
	$(HLEXC) -v -f foma -o $@.foma $^
	$(HF2F) -v -f openfst -o $@ $@.foma
	-rm -v $@.foma

omorfi.lexc.foma: $(LEXC_MAIN) $(MAYBE_TAGGER_HACKS)
	cat $^ > combined.lexc
	printf "read lexc combined.lexc\nsave stack $@" | foma

clean-local:
	-rm -f *.hfst *.ol $(LEXICAL_SRCS) $(LEXC_MAIN)

