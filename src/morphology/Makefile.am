## Process this file with automake to produce Makefile.in

if WANT_FTB3
MAYBE_FTB3_HACKS=hacks/punctuation-ftb3.lexc \
				 hacks/digits-ftb3.lexc \
				 hacks/51-ftb3.lexc
else
MAYBE_OMOR_HACKS=hacks/digits.lexc \
				 hacks/punctuation.lexc \
				 hacks/51.lexc
endif

# lexc data
LEXC_MAIN=definitions.lexc
MORPHOLOGY_SRCS=\
				stems/acronyms.lexc \
				stems/adjectives.lexc \
				stems/nouns.lexc \
				stems/numerals.lexc \
				stems/pronouns.lexc \
				stems/verbs.lexc \
				inflection/acronyms.lexc \
				inflection/adjectives.lexc \
				inflection/nouns.lexc \
				inflection/numerals.lexc \
				inflection/particles.lexc \
				inflection/pronouns.lexc \
				inflection/verbs.lexc
LEXICAL_SRCS=\
			roots/acronyms.lexc \
			roots/adjectives.lexc \
			roots/nouns.lexc \
			roots/numerals.lexc \
			roots/particles.lexc \
			roots/pronouns.lexc \
			roots/verbs.lexc
NOTGENERATED_SRCS=\
			hacks/digits.lexc \
			hacks/punctuation.lexc \
			hacks/51.lexc \
			hacks/ftb3-hacks.lexc \
			compounding/compounding-ftb3.lexc

LEXC_SRCS=$(LEXC_MAIN) \
		  $(LEXICAL_SRCS) \
		  $(MORPHOLOGY_SRCS) \
		  $(MAYBE_OMOR_HACKS) \
		  $(MAYBE_FTB3_HACKS) \
		  $(NOTGENERATED_SRCS)
EXTRA_DIST=$(LEXC_MAIN) $(NOTGENERATED_SRCS)

LEXICAL_TARGETS=omorfi.lexc.hfst #guess-universal.lexc.hfst

noinst_DATA=omorfi.lexc.hfst #guess-universal.lexc.hfst

# lexical transducer
omorfi.lexc.hfst: $(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS) \
				  $(MAYBE_FTB3_HACKS) $(MAYBE_OMOR_HACKS)
	$(HLEXC) -f foma -o $@.foma $^
	$(HF2F) -f openfst -o $@ $@.foma
	rm $@.foma

omorfi.lexc.foma: $(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS) \
				  $(MAYBE_FTB3_HACKS) $(MAYBE_OMOR_HACKS)
	cat $^ > combined.lexc
	printf "read lexc combined.lexc\nsave stack $@" | foma

clean-local:
	-rm -f *.hfst *.ol $(LEXICAL_SRCS)
