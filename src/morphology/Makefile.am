## Process this file with automake to produce Makefile.in

if WANT_FTB3
MAYBE_FTB3_HACKS=hacks/digits-ftb3.lexc \
				 hacks/51-ftb3.lexc
else
MAYBE_OMOR_HACKS=hacks/digits.lexc \
				 hacks/51.lexc
endif

if WANT_TAGGER_HACKS
MAYBE_TAGGER_HACKS=hacks/tagger-hacks.lexc
endif

# lexc data
LEXC_MAIN=omorfi.lexc
NOTGENERATED_SRCS=\
				  $(MAYBE_FTB3_HACKS) $(MAYBE_OMOR_HACKS) \
				  $(MAYBE_TAGGER_HACKS)

LEXC_SRCS=$(LEXC_MAIN) \
		  $(LEXICAL_SRCS) \
		  $(MORPHOLOGY_SRCS) \
		  $(MAYBE_OMOR_HACKS) \
		  $(MAYBE_FTB3_HACKS) \
		  $(NOTGENERATED_SRCS)
EXTRA_DIST=$(NOTGENERATED_SRCS)

LEXICAL_TARGETS=omorfi.lexc.hfst

noinst_DATA=omorfi.lexc.hfst

# lexical transducer
omorfi.lexc: $(top_builddir)/src/lexical/omorfi.lexc
	-cp -v $< $@

omorfi.lexc.hfst: $(LEXC_MAIN) \
				  $(MAYBE_FTB3_HACKS) $(MAYBE_OMOR_HACKS) $(MAYBE_TAGGER_HACKS)
	$(HLEXC) -v -f foma -o $@.foma $^
	$(HF2F) -v -f openfst -o $@ $@.foma
	-rm -v $@.foma

omorfi.lexc.foma: $(LEXC_MAIN) \
				  $(MAYBE_FTB3_HACKS) $(MAYBE_OMOR_HACKS) $(MAYBE_TAGGER_HACKS)
	cat $^ > combined.lexc
	printf "read lexc combined.lexc\nsave stack $@" | foma

if WANT_FTB3
hacks/51-ftb3.lexc: hacks/51.lexc
	$(top_builddir)/src/scripts/convert_tag_format.py -t ftb3 -r '^(\[[^]]+\])+' -i $< -o $@.tmp
	echo "!!! AUTOMATICALLY GENERATED FROM $< - CHANGES WILL BE LOST AT NEXT COMPILATION!" > $@
	cat $@.tmp >> $@
	-rm -v $@.tmp
endif

clean-local:
	-rm -f *.hfst *.ol $(LEXICAL_SRCS) $(LEXC_MAIN)
