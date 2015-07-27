#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.64)
AC_INIT([omorfi], [20150401_alpha], [https://code.google.com/p/omorfi/issues/list], [http://code.google.com/p/omorfi/])
AC_CONFIG_AUX_DIR([config-aux])
AM_INIT_AUTOMAKE([1.12 -Wall -Wno-portability -Werror foreign dist-xz color-tests])

PACKAGE=omorfi
VERSION=20150401_alpha

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

# generic tagset switch to override (for lexc serialisation)
AC_ARG_ENABLE([ftb3],
              [AS_HELP_STRING([--enable-ftb3],
                              [generate ftb3 automata @<:@default=enable@:>@])],
                             [enable_ftb3=$enableval],
                             [enable_ftb3=yes])
AM_CONDITIONAL([WANT_FTB3], [test "x$enable_ftb3" = xyes])
AC_ARG_ENABLE([omor],
              [AS_HELP_STRING([--enable-omor],
                              [generate omor automata @<:@default=enable@:>@])],
                             [enable_omor=$enableval],
                             [enable_omor=yes])
AM_CONDITIONAL([WANT_OMOR], [test "x$enable_omor" = xyes])
AC_ARG_ENABLE([apertium],
              [AS_HELP_STRING([--enable-apertium],
                              [generate apertium automata @<:@default=enable@:>@])],
                             [enable_apertium=$enableval],
                             [enable_apertium=yes])
AM_CONDITIONAL([WANT_APERTIUM], [test "x$enable_apertium" = xyes])
AC_ARG_ENABLE([giella],
              [AS_HELP_STRING([--enable-giella],
                              [generate giella automata @<:@default=enable@:>@])],
                             [enable_giella=$enableval],
                             [enable_giella=yes])
AM_CONDITIONAL([WANT_GIELLA], [test "x$enable_giella" = xyes])

AC_ARG_WITH([pbs-mail],
            [AS_HELP_STRING([set email for pbs job @<:@default=disable pbs@:>@])],
            [with_pbs_mail=$withval],
            [with_pbs_mail=no])
AC_SUBST([PBS_EMAIL], [$with_pbs_mail])
AC_ARG_WITH([slurm-mail],
            [AS_HELP_STRING([set email for slurm job @<:@default=disable pbs@:>@])],
            [with_slurm_mail=$withval],
            [with_slurm_mail=no])
AC_SUBST([SLURM_EMAIL], [$with_slurm_mail])
AC_ARG_ENABLE([big-tests],
              [AS_HELP_STRING([--enable-big-tests],
                              [whether to run large corpus tests @<:@default=no@:>@])],
                             [big_tests=$enableval],
                             [big_tests=no])
AM_CONDITIONAL([WANT_BIG_TESTS], [test "x$big_tests" != xno])

# hum dee dum
AC_MSG_CHECKING([if plans for world domination have succeeded yet])
AC_MSG_RESULT([40 seconds to mars])

# Checks for programs
AC_PROG_LN_S
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
    AC_SUBST([HREP], $with_hfst/hfst-repeat)
    AC_SUBST([HCAT], $with_hfst/hfst-concatenate)
    AC_SUBST([HUN], $with_hfst/hfst-disjunct)
    AC_SUBST([HS2F], $with_hfst/hfst-strings2fst)
    AC_SUBST([HMINUS], $with_hfst/hfst-subtract)
    AC_SUBST([HREW], $with_hfst/hfst-reweight)])
])
AC_PATH_PROG([CGCOMP], [cg-comp], [false])
AM_CONDITIONAL([CAN_VISLCG3], [test x$CGCOMP != xfalse])

AS_IF([test "x$enable_voikko" = "xyes"], 
      [AC_PATH_PROG([ZIP], [zip], [false])
       AS_IF([test "x$ZIP" = "xfalse"],
             [AC_MSG_ERROR([zip is required for voikko speller packages])])])
AC_PATH_PROG([THEREARENOEASTEREGGS], [cowsay], [echo])

# require python for stuff
AM_PATH_PYTHON([3.2],, [:])
AM_CONDITIONAL([CAN_PYTHON], [test x$PYTHON != x:])
AC_PATH_PROG([DOXYGEN], [doxygen], [false])
AM_CONDITIONAL([CAN_DOC], [test "x$doxygen" != xfalse])
AC_PATH_PROGS([HFSTTESTER], [HfstTester.py HfstTester], [false])
AM_CONDITIONAL([CAN_YAML_TEST], [test "x$HFSTTESTER" != xfalse])

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

# we are not using any traditional programming so as to need these standard
# sections:
# Checks for libraries
# Checks for header files
# Checks for typedefs, structures and compiler characteristics
# Checks for library functions

AC_CONFIG_FILES([Makefile src/Makefile src/voikko/index.xml
                 doc/Makefile test/Makefile test/test-header.yaml
                 omorfi.pc man/Makefile])
AC_CONFIG_FILES([src/bash/omorfi-analyse-text.sh],
                [chmod +x src/bash/omorfi-analyse-text.sh])
AC_CONFIG_FILES([src/bash/omorfi-segment.sh],
                [chmod +x src/bash/omorfi-segment.sh])
AC_CONFIG_FILES([src/bash/omorfi-generate.sh],
                [chmod +x src/bash/omorfi-generate.sh])
AC_CONFIG_FILES([src/bash/omorfi-hyphenate.sh],
                [chmod +x src/bash/omorfi-hyphenate.sh])
AC_CONFIG_FILES([src/bash/omorfi-spell.sh],
                [chmod +x src/bash/omorfi-spell.sh])
AC_CONFIG_FILES([src/bash/omorfi-analyse-tokenised.sh],
                [chmod +x src/bash/omorfi-analyse-tokenised.sh])
AC_CONFIG_FILES([test/coverage-europarl.sh],
                [chmod +x test/coverage-europarl.sh])
AC_CONFIG_FILES([test/coverage-fiwiki.sh],
                [chmod +x test/coverage-fiwiki.sh])
AC_CONFIG_FILES([test/coverage-gutenberg.sh],
                [chmod +x test/coverage-gutenberg.sh])
AC_CONFIG_FILES([test/coverage-jrc-acquis.sh],
                [chmod +x test/coverage-jrc-acquis.sh])
AC_CONFIG_FILES([test/coverage-ftb-3.1.sh],
                [chmod +x test/coverage-ftb-3.1.sh])
AC_CONFIG_FILES([test/faithfulness-ftb-3.1.sh],
                [chmod +x test/faithfulness-ftb-3.1.sh])
AC_CONFIG_FILES([test/faithfulness-ftb-3.1-quick.sh],
                [chmod +x test/faithfulness-ftb-3.1-quick.sh])
AC_CONFIG_FILES([test/speed-test.sh],
                [chmod +x test/speed-test.sh])
AC_CONFIG_FILES([test/coverages-all-quick.sh],
                [chmod +x test/coverages-all-quick.sh])
AS_IF([test x$with_pbs_mail != xno],
      [AC_CONFIG_FILES([test/clusterstuff.pbs])])
AS_IF([test x$with_slurm_mail != xno],
      [AC_CONFIG_FILES([test/clusterstuff.slurm])])

AC_OUTPUT

cat <<EOF
Configured $PACKAGE_STRING:
=======
* Analysers: $with_hfst
    * OMOR $enable_omor
    * FTB3.1 $enable_ftb3
    * apertium $enable_apertium
    * giella: $enable_giella
* Voikko speller: $enable_voikko
* 
    * run tests on PBS cluster: $QSUB → mailto: $with_pbs_mail
    * run tests on SLURM cluster: $SBATCH → mailto: $with_slurm_mail
EOF
AS_IF([test x$TIME = xfalse], [AC_MSG_WARN([GNU time is missing, tests will fail])])
AS_IF([test x$PYTHON = x:], [AC_MSG_WARN([python3 is required for lexical database use])])
$THEREARENOEASTEREGGS say make, make check and make install to proceed
