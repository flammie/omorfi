#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.64)
AC_INIT([omorfi],[20141332],[flammie@iki.fi], [http://code.google.com/p/omorfi/])
AC_CONFIG_AUX_DIR([config-aux])
AM_INIT_AUTOMAKE([1.11 -Wall -Wno-portability -Werror foreign dist-xz color-tests])

PACKAGE=omorfi
VERSION=20131332

# Options
AC_ARG_WITH([hfst],
            [AS_HELP_STRING([--with-hfst=DIRECTORY],
            [define HFST binary path if not in PATH @<:@default=PATH@:>@])],
            [],
            [with_hfst=yes])
AS_IF([test "x$with_hfst" = "xno"], 
      [AC_MSG_ERROR([--without-hfst not supported!])])

AC_SUBST([UPPERCASING], [$enable_uppercasing])
AC_ARG_ENABLE([uppercasing],
              [AS_HELP_STRING([--enable-uppercasing=STYLE],
                              [uppercase surface strings with STYLE @<:@default=any@:>@])],
              [enable_uppercasing=$enableval],
              [enable_uppercasing=any])
AC_SUBST([UPPERCASING], [$enable_uppercasing])
AC_ARG_ENABLE([tokenweights],
              [AS_HELP_STRING([--enable-tokenweights=WEIGHTS],
                              [use word form frequencies from WEIGHTS @<:@default=no@:>@])],
              [enable_tokenweights=$enableval],
              [enable_tokenweights=no])
AM_CONDITIONAL([WANT_TOKENWEIGHTS], [test "x$enable_tokenweights" != xno])
AC_ARG_ENABLE([tagweights],
              [AS_HELP_STRING([--enable-tagweights=WEIGHTS],
                              [use tag likelihoods from WEIGTS @<:@default=no@:>@])],
                              [enable_tagweights=$enableval],
                              [enable_tagweights=no])
AM_CONDITIONAL([WANT_TAGWEIGHTS], [test "x$enable_tagweights" != xno])
AC_SUBST([TOKENWEIGHTS], [$enable_tokenweights])
AC_SUBST([TAGWEIGHTS], [$enable_tagweights])
AC_ARG_ENABLE([error_model],
              [AS_HELP_STRING([--enable-error-model=ERROR],
                              [create suggestion transducer from ERROR model @<:@default=edit-distance-2@:>@])],
                              [enable_error_model=$enableval],
                              [enable_error_model=edit-distance-2])
AC_SUBST([ERROR_MODEL], [$enable_error_model])
AC_ARG_ENABLE([filter],
              [AS_HELP_STRING([--enable-filter=FILTER],
                              [filter morphology with FILTER rule @<:@default=no@:>@])],
                              [enable_filter=$enableval],
                              [enable_filter=no])
AC_SUBST([FILTER], [$enable_filter])
AM_CONDITIONAL([WANT_FILTERS], [test "x$enable_filter" != xno])
AC_ARG_ENABLE([doc],
              [AS_HELP_STRING([--enable-doc],
                              [enable building of documentation using docutils @<:@default=yes@<:@])],
              [enable_doc=$enableval],
              [enable_doc=yes])
AC_ARG_ENABLE([morphology],
              [AS_HELP_STRING([--enable-morphology],
                              [compile morphological analyser @<:@default=yes@:>@])],
                              [enable_morphology=$enableval],
                              [enable_morphology=yes])
AM_CONDITIONAL([WANT_MORPHOLOGY], [test "x$enable_morphology" != xno])
AC_ARG_ENABLE([generation],
              [AS_HELP_STRING([--enable-generation],
                              [compile morphological generation @<:@default=yes@:>@])],
                              [enable_generation=$enableval],
                              [enable_generation=yes])
AM_CONDITIONAL([WANT_GENERATION], [test "x$enable_generation" != xno])
AC_ARG_ENABLE([dictionary],
              [AS_HELP_STRING([--enable-dictionary],
                              [compile dicitonaries @<:@default=yes@:>@])],
                              [enable_dictionary=$enableval],
                              [enable_dictionary=yes])
AM_CONDITIONAL([WANT_DICTIONARY], [test "x$enable_dictionary" != xno])
AC_ARG_ENABLE([hyphenation],
              [AS_HELP_STRING([--enable-hyphenation],
                              [compile hyphenators @<:@default=no@:>@])],
                              [enable_hyphenation=$enableval],
                              [enable_hyphenation=no])
AM_CONDITIONAL([WANT_HYPHENATION], [test "x$enable_hyphenation" != xno])
AC_ARG_ENABLE([voikko],
              [AS_HELP_STRING([--enable-voikko],
                              [compile voikko support @<:@default=yes@:>@])],
                              [enable_voikko=$enableval],
                              [enable_voikko=yes])
AM_CONDITIONAL([WANT_VOIKKO], [test "x$enable_voikko" != xno])

# generic tagset switch to override (for lexc serialisation)
AC_ARG_ENABLE([multichar_format],
              [AS_HELP_STRING([--enable-multichar-format],
                              [use other formats for multichar symbols @<:@default=ftb3@:>@])],
                             [tag_format=$enableval],
                             [tag_format=ftb3])
AM_CONDITIONAL([WANT_FTB3], [test "x$tag_format" = xftb3])
AC_SUBST([FTB3], [$enable_ftb3])
AM_CONDITIONAL([WANT_TAGGER_HACKS], [test "$tag_format" != ${tag_format/+taggerhacks/}])
AC_SUBST([TAG_FORMAT_PRECISE], [$tag_format])
AC_SUBST([TAG_FORMAT], [${tag_format%%[[+-]]*}])

# hum dee dum
AC_MSG_CHECKING([if plans for world domination have succeeded yet])
AC_MSG_RESULT([getting there])

# Checks for programs
AC_PROG_LN_S
AS_IF([test "x$with_hfst" = "xyes" ], [
       AC_PATH_PROG([HLEXC], [hfst-lexc], [no])
       AS_IF([test "x$HLEXC" = "xno"],
             [AC_MSG_ERROR([hfst-lexc is needed])])
       AC_PATH_PROG([HTWOLC], [hfst-twolc], [no])
       AS_IF([test "x$HTWOLC" = "xno"],
             [AC_MSG_ERROR([hfst-twolc is needed])])
       AC_PATH_PROG([HIC], [hfst-compose-intersect], [no])
       AS_IF([test "x$HIC" = "xno"],
             [AC_MSG_ERROR([hfst-compose-intersect is needed])])
       AC_PATH_PROG([HINV], [hfst-invert], [no])
       AS_IF([test "x$HINV" = "xno"],
            [AC_MSG_ERROR([hfst-invert is needed])])
       AC_PATH_PROG([HREGEX], [hfst-regexp2fst], [no])
       AS_IF([test "x$HREGEX" = "xno"],
             [AC_MSG_ERROR([hfst-regexp2fst is needed])])
       AC_PATH_PROG([HSUB], [hfst-substitute], [no])
       AS_IF([test "x$HSUB" = "xno"],
             [AC_MSG_ERROR([hfst-substitute is needed])])
       AC_PATH_PROG([HPR], [hfst-project], [no])
       AS_IF([test "x$HPR" = "xno"],
             [AC_MSG_ERROR([hfst-project is needed for speller automata])])
       AC_PATH_PROG([HMIN], [hfst-minimize], [no])
       AS_IF([test "x$HMIN" = "xno"],
             [AC_MSG_ERROR([hfst-minimize is needed])])
       AC_PATH_PROG([HF2F], [hfst-fst2fst], [no])
       AS_IF([test "x$HF2F" = "xno"],
             [AC_MSG_ERROR([hfst-fsts2fst is needed for optimized automata])])
       AC_PATH_PROG([HRUNR], [hfst-lookup], [no])
       AS_IF([test "x$HRUNR" = "xno"],
             [AC_MSG_ERROR([hfst-lookup is needed for regression tests])])
       AC_PATH_PROG([HCOMP], [hfst-compose], [no])
       AS_IF([test "x$HCOMP" = "xno"],
             [AC_MSG_ERROR([hfst-compose is needed])])
       AC_PATH_PROG([HT2F], [hfst-txt2fst], [no])
       AS_IF([test "x$HT2F" = "xno"],
             [AC_MSG_ERROR([hfst-txt2fst is needed])])
       AC_PATH_PROG([HSPL], [hfst-split], [no])
       AS_IF([test "x$HSPL" = "xno"],
             [AC_MSG_ERROR([hfst-split is needed])])
       AC_PATH_PROG([HIX], [hfst-conjunct], [no])
       AS_IF([test "x$HIX" = "xno"],
             [AC_MSG_ERROR([hfst-conjunct is needed])])
       AC_PATH_PROG([HPROC], [hfst-proc], [no])
       AS_IF([test "x$HPROC" = "xno"],
             [AC_MSG_ERROR([hfst-proc is needed for testing])])
       AC_PATH_PROG([HREP], [hfst-repeat], [no])
       AS_IF([test "x$HREP" = xno],
             [AC_MSG_ERROR([hfst-repeat is needed for edit distance repetition])])
       AC_PATH_PROG([HCAT], [hfst-concatenate], [no])
       AS_IF([test "x$HCAT" = xno],
             [AC_MSG_ERROR([hfst-concatenate is needed])])
       AC_PATH_PROG([HUN], [hfst-disjunct], [no])
       AS_IF([test "x$HCAT" = xno],
             [AC_MSG_ERROR([hfst-disjunct is needed])])
       AC_PATH_PROG([HS2F], [hfst-strings2fst], [no])
       AS_IF([test "x$HCAT" = xno],
             [AC_MSG_ERROR([hfst-strings2fst is needed])])
       AC_PATH_PROG([HMINUS], [hfst-subtract], [no])
       AS_IF([test "x$HCAT" = xno],
             [AC_MSG_ERROR([hfst-subtract is needed])])
       AC_PATH_PROG([HREW], [hfst-reweight], [no])
       AS_IF([test "x$HREW" = xno],
             [AC_MSG_ERROR([hfst-reweight is needed for weights])])
       AC_PATH_PROG([ADT], [apertium-destxt], [cat])
       AS_IF([test x$ADT = xcat],
          [AC_MSG_WARN([corpus analysis script works better with apertium tools])])],
    [
    AC_CHECK_FILES([$with_hfst/hfst-lexc $with_hfst/hfst-twolc $with_hfst/hfst-compose-intersect $with_hfst/hfst-invert $with_hfst/hfst-project $with_hfst/hfst-fst2fst $with_hfst/hfst-regexp2fst $with_hfst/hfst-substitute $with_hfst/hfst-minimize $with_hfst/hfst-compose $with_hfst/hfst-txt2fst $with_hfst/hfst-split $with_hfst/hfst-conjunct $with_hfst/hfst-proc $with_hfst/hfst-repeat $with_hfst/hfst-concatenate $with_hfst/hfst-disjunct $with_hfst/hfst-strings2fst $with_hfst/hfst-subtract $with_hfst/hfst-reweight], [HAVE_HFST=1], [AC_MSG_ERROR([HFST commandline tools are needed in $with_hfst])])
    AC_SUBST([HLEXC], $with_hfst/hfst-lexc)
    AC_SUBST([HTWOLC], $with_hfst/hfst-twolc)
    AC_SUBST([HIC], $with_hfst/hfst-compose-intersect)
    AC_SUBST([HINV], $with_hfst/hfst-invert)
    AC_SUBST([HU2W], $with_hfst/hfst-unweighted2weighted)
    AC_SUBST([HF2F], $with_hfst/hfst-fst2fst)
    AC_SUBST([HPR], $with_hfst/hfst-project)
    AC_SUBST([HRUNR], $with_hfst/hfst-lookup)
    AC_SUBST([HREGEX], $with_hfst/hfst-regexp2fst)
    AC_SUBST([HSUB], $with_hfst/hfst-substitute)
    AC_SUBST([HMIN], $with_hfst/hfst-minimize)
    AC_SUBST([HCOMP], $with_hfst/hfst-compose)
    AC_SUBST([HT2F], $with_hfst/hfst-txt2fst)
    AC_SUBST([HIX], $with_hfst/hfst-conjunct)
    AC_SUBST([HSPL], $with_hfst/hfst-split)
    AC_SUBST([HPROC], $with_hfst/hfst-proc)
    AC_SUBST([HREP], $with_hfst/hfst-repeat)
    AC_SUBST([HCAT], $with_hfst/hfst-concatenate)
    AC_SUBST([HUN], $with_hfst/hfst-disjunct)
    AC_SUBST([HS2F], $with_hfst/hfst-strings2fst)
    AC_SUBST([HMINUS], $with_hfst/hfst-subtract)
    AC_SUBST([HREW], $with_hfst/hfst-reweight)
])

AS_IF([test "x$enable_voikko" = "xyes"], 
      [AC_PATH_PROG([ZIP], [zip], [false])
       AS_IF([test "x$ZIP" = "xfalse"],
             [AC_MSG_ERROR([zip is required for voikko speller packages])])])
# require python for stuff
AM_PATH_PYTHON([3.2])

# test RST scripts without python since python tests do not work in all platforms
AC_PATH_PROG([RST], [rst], [false])
AC_PATH_PROGS([RST2HTML], [rst2html.py rst2html], [false])
AC_PATH_PROGS([RST2PDF], [rst2pdf.py rst2pdf], [false])
AC_PATH_PROGS([RST2TEX], [rst2tex.py rst2tex], [false])
AC_PATH_PROGS([HFSTTESTER], [HfstTester.py HfstTester], [false])
AM_CONDITIONAL([CAN_RST], [test "x$RST" != xfalse -o \( "x$RST2HTML" != xfalse -a "x$RST2PDF" != xfalse \) ])
AM_CONDITIONAL([WANT_DOC], [test "x$enable_doc" != xfalse])

# we are not using any traditional programming so as to need these standard
# sections:
# Checks for libraries
# Checks for header files
# Checks for typedefs, structures and compiler characteristics
# Checks for library functions

AC_CONFIG_FILES([Makefile src/Makefile src/index.xml
                 src/morphology/Makefile src/lexical/Makefile 
                 src/hyphenation/Makefile src/orthography/Makefile
                 src/phonology/Makefile src/spell-checking/Makefile
                 src/probabilistics/Makefile src/taghacks/Makefile
                 doc/Makefile test/Makefile 
                 src/scripts/Makefile src/scripts/omorfi-analyse.sh
                 src/scripts/omorfi-generate.sh src/scripts/omorfi-hyphenate.sh
                 src/scripts/omorfi-spell.sh
                 src/scripts/omorfi-interactive.sh
                 man/Makefile], 
                 [chmod +x src/scripts/omorfi-analyse.sh src/scripts/omorfi-generate.sh src/scripts/omorfi-hyphenate.sh src/scripts/omorfi-spell.sh src/scripts/omorfi-interactive.sh])
AC_OUTPUT

cat <<EOF
Configured $PACKAGE_STRING:
    * Uppercasing ruleset: $enable_uppercasing
    * Weighting method: $enable_tagweights + $enable_tokenweights
    * Default error model: $enable_error_model
    * Filter analyses: $enable_filter
    * Default tagset: $enable_tagset
    * Create optimised lookup format: $enable_optimisations
    * Morphological analyser: $enable_morphology
    * Morphological generator: $enable_generation
    * Dictionaries: $enable_dictionary
    * Hyphenation: $enable_hyphenation
    * Voikko support: $enable_voikko
    * Tag format: $tag_format
EOF
