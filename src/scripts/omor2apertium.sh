#!/bin/bash
lexcdir=src/morphology
if test $# -ge 1 ; then
    lexcdir=$1
fi
cat $lexcdir/definitions.lexc $lexcdir/pos.lexc \
    $lexcdir/compounding/compounding.lexc \
    $lexcdir/roots/51.lexc \
    $lexcdir/roots/abbreviations.lexc \
    $lexcdir/roots/acronyms.lexc \
    $lexcdir/roots/adjectives.lexc \
    $lexcdir/roots/adpositions.lexc \
    $lexcdir/roots/adverbs.lexc \
    $lexcdir/roots/conjunctions.lexc \
    $lexcdir/roots/digits.lexc \
    $lexcdir/roots/interjections.lexc \
    $lexcdir/roots/nouns.lexc \
    $lexcdir/roots/numerals.lexc \
    $lexcdir/roots/particles.lexc \
    $lexcdir/roots/prefixes.lexc \
    $lexcdir/roots/pronouns.lexc \
    $lexcdir/roots/proper-nouns.lexc \
    $lexcdir/roots/punctuation.lexc \
    $lexcdir/roots/suffixes.lexc \
    $lexcdir/roots/verbs.lexc \
    $lexcdir/stemparts/acronyms.lexc \
    $lexcdir/stemparts/adjectives.lexc \
    $lexcdir/stemparts/digits.lexc \
    $lexcdir/stemparts/nouns.lexc \
    $lexcdir/stemparts/numerals.lexc \
    $lexcdir/stemparts/verbs.lexc \
    $lexcdir/inflection/acronyms.lexc \
    $lexcdir/inflection/adjectives.lexc \
    $lexcdir/inflection/adpositions.lexc \
    $lexcdir/inflection/adverbs.lexc \
    $lexcdir/inflection/digits.lexc \
    $lexcdir/inflection/nouns.lexc \
    $lexcdir/inflection/numerals.lexc \
    $lexcdir/inflection/prefixes.lexc \
    $lexcdir/inflection/pronouns.lexc \
    $lexcdir/inflection/verbs.lexc \
    | sed -f $(dirname $0)/omor2apertium.sed \
    | fgrep -v '%<del%>'
