## Process this file with automake to produce Makefile.in

SUBDIRS=lexical-data

# lexc data
LEXC_MAIN=definitions.lexc
MORPHOLOGY_SRCS=\
				pos.lexc \
				compounding.hlexc \
				stems/adjectives.lexc \
				stems/digits.lexc \
				stems/nouns.lexc \
				stems/numerals.lexc \
				stems/proper-nouns.lexc \
				stems/verbs.lexc \
				inflection/acronyms.lexc \
				inflection/adjectives.lexc \
				inflection/commons.lexc \
				inflection/digits.lexc \
				inflection/nouns.lexc \
				inflection/verbs.lexc
LEXICAL_SRCS=\
			lexical-data/abbreviation-stubs.hlexc \
			lexical-data/acronym-stubs.hlexc \
			lexical-data/adjective-stubs.hlexc \
			lexical-data/adpositions.hlexc \
			lexical-data/adverbs.hlexc \
			lexical-data/conjunctions.hlexc \
			lexical-data/digit-stubs.hlexc \
			lexical-data/exceptions.hlexc \
			lexical-data/interjections.hlexc \
			lexical-data/noun-stubs.hlexc \
			lexical-data/numeral-stubs.hlexc \
			lexical-data/particles.hlexc \
			lexical-data/prefixes.hlexc \
			lexical-data/suffixes.hlexc \
			lexical-data/pronouns.hlexc \
			lexical-data/proper-noun-stubs.hlexc \
			lexical-data/punctuation.hlexc \
			lexical-data/verb-stubs.hlexc \
			lexical-data/51.hlexc
LEXC_SRCS=$(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS)
EXTRA_DIST=$(LEXC_MAIN) $(MORPHOLOGY_SRCS)

LEXICAL_TARGETS=omorfi.lexc.hfst #guess-universal.lexc.hfst

noinst_DATA=omorfi.lexc.hfst #guess-universal.lexc.hfst

# lexical transducer
omorfi.lexc.hfst: $(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS)
	$(HLEXC) -o $@.foma $^
	$(HF2F) -f openfst -o $@ $@.foma
	rm $@.foma

omorfi.lexc.foma: $(LEXC_MAIN) $(LEXICAL_SRCS) $(MORPHOLOGY_SRCS)
	cat $^ > combined.lexc
	printf "read lexc combined.lexc\nsave stack $@" | foma

clean-local:
	-rm -f *.hfst *.ol

