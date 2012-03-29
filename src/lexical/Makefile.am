## Process this file with automake to produce Makefile.in

XML_SRCS=kotus-sanalista_v1.xml joukahainen.xml

SCIRPTS=csv2lexc.py pronouns2lexc.py regenerate-lexicons.sh

LEXICAL_SRCS=\
	abbreviation-stubs.hlexc \
	acronym-stubs.hlexc \
	adjective-stubs.hlexc \
	adpositions.hlexc \
	adverbs.hlexc \
	codified-expressions.hlexc \
	conjunctions.hlexc \
	digit-stubs.hlexc \
	exceptions.hlexc \
	interjections.hlexc \
	noun-stubs.hlexc \
	numeral-stubs.hlexc \
	particles.hlexc \
	prefixes.hlexc \
	pronouns.hlexc \
	proper-noun-stubs.hlexc \
	punctuation.hlexc \
	suffixes.hlexc \
	verb-stubs.hlexc

EXTRA_DIST=$(XML_SRCS) $(LEXICAL_SRCS) $(SCIRPTS)

all-local:
	@echo  \* to regenerate lexicons use regenerate targets manually

regenerate:
	$(MAKE) regenerate-csv
	$(MAKE) regenerate-lexc

regenerate-lexc:
	sh regenerate-lexicons.sh

regenerate-csv:
	false
