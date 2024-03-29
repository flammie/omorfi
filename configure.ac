#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([omorfi],[0.9.10],[https://github.com/flammie/omorfi/issues],[https://github.com/flammie/omorfi/])
LT_PREREQ([2.2.6])
AC_CONFIG_AUX_DIR([config-aux])
AM_INIT_AUTOMAKE([1.12 -Wall -Wno-portability -Werror foreign dist-xz color-tests subdir-objects])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_SRCDIR([src/cpp/omorfi.cc])
AC_CONFIG_HEADERS([config.h])

PACKAGE=omorfi
VERSION=0.9.10

# Options
AC_ARG_WITH([hfst],
            [AS_HELP_STRING([--with-hfst=DIRECTORY],
            [define HFST binary path if not in PATH @<:@default=PATH@:>@])],
            [],
            [with_hfst=yes])
AM_CONDITIONAL([WANT_HFST], [test "x$with_hfst" != "xno"])
AC_ARG_ENABLE([voikko],
              [AS_HELP_STRING([--enable-voikko],
                              [compile voikko support @<:@default=yes@:>@])],
                              [enable_voikko=$enableval],
                              [enable_voikko=yes])
AM_CONDITIONAL([WANT_VOIKKO], [test "x$enable_voikko" != xno])

# main tagset switches
AC_ARG_ENABLE([omor],
              [AS_HELP_STRING([--enable-omor],
                              [generate omor automata @<:@default=enable@:>@])],
                             [enable_omor=$enableval],
                             [enable_omor=yes])
AM_CONDITIONAL([WANT_OMOR], [test "x$enable_omor" = xyes])
AC_ARG_ENABLE([omor_paradigms],
              [AS_HELP_STRING([--enable-omor-paradigms],
                              [include new_para feature in omors @<:@default=disable@:>@])],
                              [enable_omor_paradigms=$enableval],
                              [enable_omor_paradigms=no])
AS_IF([test x$enable_omor_paradigms != xno],
      [AC_SUBST([OMORPARAFLAG], ["--omor-new-para"])])
AC_ARG_ENABLE([omor_allomorphs],
              [AS_HELP_STRING([--enable-omor-allomorphs],
                              [include allomorph feature in omors @<:@default=disable@:>@])],
                              [enable_omor_allomorphs=$enableval],
                              [enable_omor_allomorphs=no])
AS_IF([test x$enable_omor_allomorphs != xno],
      [AC_SUBST([OMORALLOFLAG], ["--omor-allo"])])
AC_ARG_ENABLE([omor_proper_classes],
              [AS_HELP_STRING([--enable-omor-proper-classes],
                              [include proper feature in omors @<:@default=enable@:>@])],
                              [enable_omor_proper_classes=$enableval],
                              [enable_omor_proper_classes=yes])
AS_IF([test enable_omor_proper_classes != xno],
      [AC_SUBST([OMORPROPFLAG], ["--omor-props"])])
AC_ARG_ENABLE([omor_semantics],
              [AS_HELP_STRING([--enable-omor-semantics],
                              [include sem feature in omors @<:@default=enable@:>@])],
                              [enable_omor_semantics=$enableval],
                              [enable_omor_semantics=yes])
AS_IF([test x$enable_omor_semantics != xno],
      [AC_SUBST([OMORSEMFLAG], ["--omor-sem"])])

# generic tagset switch to override (for lexc serialisation)
AC_ARG_ENABLE([ftb1],
              [AS_HELP_STRING([--enable-ftb1],
                              [generate ftb1 automata @<:@default=disable@:>@])],
                             [enable_ftb1=$enableval],
                             [enable_ftb1=no])
AM_CONDITIONAL([WANT_FTB1], [test "x$enable_ftb1" = xyes])
AC_ARG_ENABLE([ftb3],
              [AS_HELP_STRING([--enable-ftb3],
                              [generate ftb3 automata @<:@default=disable@:>@])],
                             [enable_ftb3=$enableval],
                             [enable_ftb3=no])
AM_CONDITIONAL([WANT_FTB3], [test "x$enable_ftb3" = xyes])
AC_ARG_ENABLE([apertium],
              [AS_HELP_STRING([--enable-apertium],
                              [generate apertium automata @<:@default=enable@:>@])],
                             [enable_apertium=$enableval],
                             [enable_apertium=no])
AM_CONDITIONAL([WANT_APERTIUM], [test "x$enable_apertium" = xyes])
AC_ARG_ENABLE([giella],
              [AS_HELP_STRING([--enable-giella],
                              [generate giella automata @<:@default=disable@:>@])],
                             [enable_giella=$enableval],
                             [enable_giella=no])
AM_CONDITIONAL([WANT_GIELLA], [test "x$enable_giella" = xyes])
AC_ARG_ENABLE([labeled_segments],
              [AS_HELP_STRING([--enable-labeled-segments],
                              [generate labeled segmenter @<:@default=disable@:>@])],
                             [enable_labeled_segments=$enableval],
                             [enable_labeled_segments=no])
AM_CONDITIONAL([WANT_LABELED_SEGMENTS], [test "x$enable_labeled_segments" = xyes])


# applications
# segmenter currently based on FTB 3
AC_ARG_ENABLE([lemmatiser],
              [AS_HELP_STRING([--enable-lemmatiser],
                              [generate lemmatiser @<:@default=disable@:>@])],
                             [enable_lemmatiser=$enableval],
                             [enable_lemmatiser=no])
AM_CONDITIONAL([WANT_LEMMATISE], [test x$enable_lemmatiser != xno])
AC_ARG_ENABLE([segmenter],
              [AS_HELP_STRING([--enable-segmenter],
                              [generate segmenter @<:@default=disable@:>@])],
                             [enable_segmenter=$enableval],
                             [enable_segmenter=no])
AM_CONDITIONAL([WANT_SEGMENTS], [test x$enable_segmenter != xno])
AC_ARG_ENABLE([hyphenator],
              [AS_HELP_STRING([--enable-hyphenator],
                              [generate hyphenator @<:@default=disable@:>@])],
                             [enable_hyphenator=$enableval],
                             [enable_hyphenator=no])
AM_CONDITIONAL([WANT_HYPHENATE], [test x$enable_hyphenator != xno])

# libraries
AC_ARG_WITH([java],
            [AS_HELP_STRING([--without-java],
                            [do not build java library])],
            [with_java=$withval],
            [with_java=no])
AC_ARG_WITH([cpp],
            [AS_HELP_STRING([--without-cpp],
                            [do not build cpp library])],
            [with_cpp=$withval],
            [with_cpp=yes])

# run some things on clusters
AC_ARG_WITH([pbs-mail],
            [AS_HELP_STRING([--with-pbs-mail],
                            [set email for pbs job @<:@default=disable pbs@:>@])],
            [with_pbs_mail=$withval],
            [with_pbs_mail=no])
AC_SUBST([PBS_EMAIL], [$with_pbs_mail])
AC_ARG_WITH([slurm-mail],
            [AS_HELP_STRING([--with-slurm-mail],
                            [set email for slurm job @<:@default=disable pbs@:>@])],
            [with_slurm_mail=$withval],
            [with_slurm_mail=no])
AC_SUBST([SLURM_EMAIL], [$with_slurm_mail])
# Control heaviness of builds and tests
AC_ARG_ENABLE([small-lexicons],
              [AS_HELP_STRING([--enable-small-lexicons],
                              [whether to greatly reduce lexicon sizes @<:@default=no@:>@])],
                             [small_lexicons=$enableval],
                             [small_lexicons=no])
AM_CONDITIONAL([ONLY_SMALL_LEXICONS], [test "x$small_lexicons" != xno])
AC_ARG_ENABLE([big-tests],
              [AS_HELP_STRING([--enable-big-tests],
                              [whether to run large corpus tests @<:@default=no@:>@])],
                             [big_tests=$enableval],
                             [big_tests=no])
AM_CONDITIONAL([WANT_BIG_TESTS], [test "x$big_tests" != xno])

# hum dee dum
AC_MSG_CHECKING([if plans for world domination have succeeded yet])
AC_MSG_RESULT([we are the new world order])

# Checks for programs
AM_PROG_AR
AC_PROG_CC
AC_PROG_CXX
LT_INIT
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PATH_PROG([TIME], [time], [false])
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
       AC_PATH_PROG([HPROC], [hfst-proc hfst-apertium-proc], [no])
       AS_IF([test "x$HPROC" = "xno"],
             [AC_MSG_WARN([hfst-proc is needed for some corpus analysis])])
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
       AC_PATH_PROG([HOSPELL], [hfst-ospell], [no])
       AS_IF([test "x$HOSPELL" = "xno"],
             [AC_MSG_WARN([hfst-ospell is needed for spell-checking])])
       AC_PATH_PROG([HLOOKUP], [hfst-lookup], [no])
       AS_IF([test "x$HLOOKUP" = "xno"],
             [AC_MSG_WARN([hfst-lookup is needed for bash scripts])])
       AC_PATH_PROG([ADT], [apertium-destxt], [cat])
       AS_IF([test x$ADT = xcat],
          [AC_MSG_WARN([corpus analysis script works better with apertium tools])])],
    [AS_IF([test x$with_hfst != xno],
           [AC_CHECK_FILES([$with_hfst/hfst-lexc $with_hfst/hfst-twolc $with_hfst/hfst-compose-intersect $with_hfst/hfst-invert $with_hfst/hfst-project $with_hfst/hfst-fst2fst $with_hfst/hfst-regexp2fst $with_hfst/hfst-substitute $with_hfst/hfst-minimize $with_hfst/hfst-compose $with_hfst/hfst-txt2fst $with_hfst/hfst-split $with_hfst/hfst-conjunct $with_hfst/hfst-proc $with_hfst/hfst-repeat $with_hfst/hfst-concatenate $with_hfst/hfst-disjunct $with_hfst/hfst-strings2fst $with_hfst/hfst-subtract $with_hfst/hfst-reweight], [HAVE_HFST=1], [AC_MSG_ERROR([HFST commandline tools are needed in $with_hfst])])
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
    AC_SUBST([HAPROC], $with_hfst/hfst-apertium-proc)
    AC_SUBST([HREP], $with_hfst/hfst-repeat)
    AC_SUBST([HCAT], $with_hfst/hfst-concatenate)
    AC_SUBST([HUN], $with_hfst/hfst-disjunct)
    AC_SUBST([HS2F], $with_hfst/hfst-strings2fst)
    AC_SUBST([HMINUS], $with_hfst/hfst-subtract)
    AC_SUBST([HOSPELL], $with_hfst/hfst-ospell)
    AC_SUBST([HLOOKUP], $with_hfst/hfst-lookup)
    AC_SUBST([HREW], $with_hfst/hfst-reweight)])
])
AC_PATH_PROG([CGCOMP], [cg-comp], [false])
AC_PATH_PROG([CGPROC], [cg-proc], [false])
AM_CONDITIONAL([CAN_VISLCG3], [test x$CGCOMP != xfalse])

AS_IF([test "x$enable_voikko" = "xyes"],
      [AC_PATH_PROG([ZIP], [zip], [false])
       AS_IF([test "x$ZIP" = "xfalse"],
             [AC_MSG_ERROR([zip is required for voikko speller packages])])])
AC_PATH_PROGS([THEREARENOEASTEREGGS], [toilet figlet cowsay], [echo])
AC_PATH_PROGS([WGET], [wget])
# insist on gnu stuff on mac :-/
AC_PATH_PROGS([TAR], [gtar gnutar tar])
AC_PATH_PROGS([WC], [gwc wc])
AC_PATH_PROGS([DATE], [gdate date])

# require python for stuff
AM_PATH_PYTHON([3.2])
AM_CONDITIONAL([CAN_PYTHON], [test x$PYTHON != x:])
AX_PYTHON_MODULE([libhfst], [true])
AC_PATH_PROG([JEKYLL], [jekyll], [false])
AC_PATH_PROG([DOXYGEN], [doxygen], [false])
AM_CONDITIONAL([CAN_DOC], [test "x$doxygen" != xfalse])
AC_PATH_PROGS([HFSTTESTER], [HfstTester.py HfstTester], [false])
AM_CONDITIONAL([CAN_YAML_TEST], [test "x$HFSTTESTER" != xfalse])

# check java when not disabled
AS_IF([test "x$with_java" != xno], [
    AX_CHECK_CLASSPATH
    AX_PROG_JAVA
    AX_PROG_JAVAC
    AX_CHECK_CLASS([net.sf.hfst.Transducer])
    ])
AS_IF([test "x$with_java" = xyes], [
    AS_IF([test "x$HAVE_net_sf_hfst_Transducer" = xno],
          [AC_MSG_WARN(Building java with bundled hfst then)
          AC_SUBST([HFSTCLASSPATH], [java])
          ])
    ], [AC_SUBST([HFSTCLASSPATH], [$with_java])])
AM_CONDITIONAL([CAN_JAVA], [test x$with_java != xno])

# separated my scripts for corpora fetching, some preprocessing
AC_PATH_PROG([FETCH_EUROPARL], [fetch-europarl.bash], [false])
AC_PATH_PROG([FETCH_WIKIMEDIA], [fetch-wikimedia.bash], [false])
AC_PATH_PROG([FETCH_GUTENBERG], [fetch-gutenberg.bash], [false])
AC_PATH_PROG([FETCH_JRC_ACQUIS], [fetch-jrc-acquis.bash], [false])
AC_PATH_PROG([CLEAN_EUROPARL], [unpack-europarl.bash], [false])
AC_PATH_PROG([CLEAN_WIKIMEDIA], [unpack-wikimedia.bash], [false])
AC_PATH_PROG([CLEAN_GUTENBERG], [unpack-gutenbergs.bash], [false])
AC_PATH_PROG([CLEAN_JRC_ACQUIS], [unpack-jrc-acquis.bash], [false])
AM_CONDITIONAL([CAN_BIG_CORPORA], [test x$FETCH_EUROPARL != xfalse])

# big cluster stuff
AC_PATH_PROG([QSUB], [qsub], [false])
AC_PATH_PROG([SBATCH], [sbatch], [false])


AC_LANG([C++])
# Checks for libraries
PKG_CHECK_MODULES([LIBHFST], [hfst >= 3.15],
                  [AC_DEFINE([HAVE_LIBHFST], [1], [Use libhfst])])
AM_CONDITIONAL([WANT_CPP], [test x$with_cpp != xno])

# Checks for header files
# Checks for typedefs, structures and compiler characteristics
AX_CXX_COMPILE_STDCXX_11
# Checks for library functions

AC_CONFIG_FILES([Makefile src/Makefile src/voikko/index.xml
                 test/Makefile test/test-header.yaml
                 omorfi.pc man/Makefile docs/Makefile docs/Doxyfile])
AC_CONFIG_FILES([src/bash/omorfi.bash])
AC_CONFIG_FILES([test/unimorph-test.bash],
                [chmod +x test/unimorph-test.bash])
AC_CONFIG_FILES([test/ftb-3.1-test.bash],
                [chmod +x test/ftb-3.1-test.bash])
AC_CONFIG_FILES([test/ftb-3.1-quick-test.bash],
                [chmod +x test/ftb-3.1-quick-test.bash])
AC_CONFIG_FILES([test/vislcg-fi-ud-test.sh],
                [chmod +x test/vislcg-fi-ud-test.sh])
AC_CONFIG_FILES([test/conllu-fi-tdt-ud-test.bash],
                [chmod +x test/conllu-fi-tdt-ud-test.bash])
AC_CONFIG_FILES([test/conllu-fi-ftb-ud-test.sh],
                [chmod +x test/conllu-fi-ftb-ud-test.sh])
AC_CONFIG_FILES([test/finer-test.bash],
                [chmod +x test/finer-test.bash])
AC_CONFIG_FILES([test/speed-test.sh],
                [chmod +x test/speed-test.sh])
AC_CONFIG_FILES([test/coverages-all-quick.bash],
                [chmod +x test/coverages-all-quick.bash])
AC_CONFIG_FILES([test/coverages-less-quick.bash],
                [chmod +x test/coverages-less-quick.bash])
AC_CONFIG_FILES([test/coverages-all-slow.bash],
                [chmod +x test/coverages-all-slow.bash])
AC_CONFIG_FILES([test/tools-python.bash],
                [chmod +x test/tools-python.bash])
AC_CONFIG_FILES([docs/generate-statistics.bash],
                [chmod +x docs/generate-statistics.bash])
AS_IF([test x$with_pbs_mail != xno],
      [AC_CONFIG_FILES([test/clusterstuff.pbs])])
AS_IF([test x$with_slurm_mail != xno],
      [AC_CONFIG_FILES([test/clusterstuff.slurm])])

AC_OUTPUT

cat <<EOF
Configured $PACKAGE_STRING:
=======
* Analysers: $with_hfst
    * OMOR $enable_omor (flags: $OMORPROPFLAG $OMORALLOFLAG $OMORPARAFLAG $OMORSEMFLAG)
    * FTB3.1 $enable_ftb3
    * apertium $enable_apertium
    * giella: $enable_giella
    * labeled segmenter: $enable_labeled_segments
* Limits:
    * tiny lexicons: $enable_small_lexicons
    * big tests: $enable_big_tests
* Applications
    * Voikko speller: $enable_voikko
    * segmenter: $enable_segmenter
    * lemmatiser: $enable_lemmatiser
    * hyphenators: $enable_hyphenator
* Libraries
    * Python 3: yes
    * Java: $with_java
    * C++: $with_cpp
* Clusters
    * run tests on PBS cluster: $QSUB → mailto: $with_pbs_mail
    * run tests on SLURM cluster: $SBATCH → mailto: $with_slurm_mail
EOF
AS_IF([test x$TIME = xfalse], [AC_MSG_WARN([GNU time is missing, tests will fail])])
AS_IF([test x$PYTHON = x:], [AC_MSG_WARN([python3 is required for lexical database use])])
$THEREARENOEASTEREGGS say make, make check and make install to proceed
