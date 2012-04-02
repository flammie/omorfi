## Process this file with automake to produce Makefile.in

# lexc data
LEXC_MAIN=definitions.lexc
MORPHOLOGY_SRCS=\
				pos.lexc \
				compounding/compounding.lexc \
				stemparts/adjectives.lexc \
				stemparts/digits.lexc \
				stemparts/nouns.lexc \
				stemparts/numerals.lexc \
				stemparts/proper-nouns.lexc \
				stemparts/verbs.lexc \
				inflection/acronyms.lexc \
				inflection/adjectives.lexc \
				inflection/commons.lexc \
				inflection/digits.lexc \
				inflection/nouns.lexc \
				inflection/verbs.lexc
LEXICAL_SRCS=\
			roots/abbreviations.lexc \
			roots/acronyms.lexc \
			roots/adjectives.lexc \
			roots/adpositions.lexc \
			roots/adverbs.lexc \
			roots/conjunctions.lexc \
			roots/interjections.lexc \
			roots/nouns.lexc \
			roots/particles.lexc \
			roots/prefixes.lexc \
			roots/suffixes.lexc \
			roots/proper-nouns.lexc \
			roots/verbs.lexc
NOTGENERATED_SRCS=\
			roots/digits.lexc \
			roots/exceptions.lexc \
			roots/numerals.lexc \
			roots/pronouns.lexc \
			roots/punctuation.lexc \
			roots/51.lexc

LEXC_SRCS=$(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS) $(NOTGENERATED_SRCS)
EXTRA_DIST=$(LEXC_MAIN) $(MORPHOLOGY_SRCS) $(NOTGENERATED_SRCS)

LEXICAL_TARGETS=omorfi.lexc.hfst #guess-universal.lexc.hfst

noinst_DATA=omorfi.lexc.hfst #guess-universal.lexc.hfst

# lexical transducer
omorfi.lexc.hfst: $(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS) $(NONGENERATED_SRCS)
	$(HLEXC) -f foma -o $@.foma $^
	$(HF2F) -f openfst -o $@ $@.foma
	rm $@.foma

omorfi.lexc.foma: $(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS) $(NONGENERATED_SRCS)
	cat $^ > combined.lexc
	printf "read lexc combined.lexc\nsave stack $@" | foma

clean-local:
	-rm -f *.hfst *.ol

