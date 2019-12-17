#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create wiktionary-like inflection tables for omorfi paradigms and words.
"""


from argparse import ArgumentParser, FileType
from sys import stderr, stdout
from time import perf_counter, process_time

from omorfi import Omorfi


def generate(generator, word, upos, omors=""):
    """Generate word-form."""
    wf = generator.generate("[WORD_ID=" + word + "][UPOS=" + upos + "]" +
                            omors)
    if not wf:
        return '---'
    else:
        return wf


def main():
    """Command-line interface for omorfi's sort | uniq -c tester."""
    a = ArgumentParser()
    a.add_argument('-g', '--generator', metavar='FSAFILE', required=True,
                   help="load generator from FSAFILE")
    a.add_argument('-w', '--word', metavar="WORD_ID", required=True,
                   help="generate forms of word WORD_ID")
    a.add_argument('-o', '--output', metavar="OUTFILE",
                   type=FileType('w'),
                   dest="outfile", help="log outputs to OUTFILE")
    a.add_argument('-X', '--statistics', metavar="STATFILE",
                   type=FileType('w'),
                   dest="statfile", help="statistics")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
                   help="Print verbosely while processing")
    a.add_argument('-O', '--output-format', metavar="OFORMAT",
                   default="markdown",
                   help="Create output table in OFORMAT")
    a.add_argument('-u', '--upos', metavar="UPOS", required=True,
                   choices=["ADJ", "NOUN", "VERB", "NUM", "X"],
                   help="generate inflection table for UPOS")

    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    try:
        if options.generator:
            if options.verbose:
                print("reading generator from", options.generator)
            omorfi.load_generator(options.generator)
        if not options.statfile:
            options.statfile = stdout
        if not options.outfile:
            options.outfile = stdout
    except IOError:
        print("Could not process file", options.generator, file=stderr)
        exit(2)
    # for make check target
    realstart = perf_counter()
    cpustart = process_time()
    print("### Inflection of", options.word, file=options.outfile)
    print(file=options.outfile)
    if options.upos in ['NOUN', 'NUM', 'ADJ']:
        print(file=options.outfile)
        print("#### Nominal cases", file=options.outfile)
        print(file=options.outfile)
        print("| *Case* | _Singular_ | _Plural_ | _Possessive_ | _Clitic_ |",
              file=options.outfile)
        print("|:-------|:-----------|:---------|:-------------|:---------|",
              file=options.outfile)
        print("| _Nominative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=NOM]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=NOM]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=NOM][POSS=SG1]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=NOM][CLIT=HAN]") + " |",
              file=options.outfile)
        print("| _Genitive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=GEN]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=GEN]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=GEN][POSS=SG2]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=GEN][CLIT=KO]") + " |",
              file=options.outfile)
        print("| _Partitive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=PAR]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=PAR]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=PAR][POSS=3]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=PAR][CLIT=PA]") + " |",
              file=options.outfile)
        print("| _Inessive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=INE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=INE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=INE][POSS=PL1]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=INE][CLIT=KAAN]") + " |",
              file=options.outfile)
        print("| _Elative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ELA]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ELA]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ELA][POSS=PL2]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ELA][CLIT=KIN]") + " |",
              file=options.outfile)
        print("| _Illative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ILL]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ILL]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ILL][POSS=3]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ILL][CLIT=KO]") + " |",
              file=options.outfile)
        print("| _Adessive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ADE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ADE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ADE][POSS=SG1]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ADE][CLIT=PA]") + " |",
              file=options.outfile)
        print("| _Ablative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ABL]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ABL]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ABL][POSS=SG2]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ABL][CLIT=KAAN]") + " |",
              file=options.outfile)
        print("| _Allative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ALL]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ALL]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ALL][POSS=3]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ALL][CLIT=HAN]") + " |",
              file=options.outfile)
        print("| _Essive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ESS]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ESS]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ESS][POSS=PL1]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ESS][CLIT=KO]") + " |",
              file=options.outfile)
        print("| _Translative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=TRA]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=TRA]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=TRA][POSS=PL2]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=TRA][CLIT=PA]") + " |",
              file=options.outfile)
        print("| _Abessive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ABE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ABE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=ABE][POSS=3]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=ABE][CLIT=KAAN]") + " |",
              file=options.outfile)
        print("| _Instructive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=INS]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=INS]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=SG][CASE=INS][POSS=SG1]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[NUM=PL][CASE=INS][CLIT=KO]") + " |",
              file=options.outfile)
        print("| _Comitative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[CASE=COM]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[CASE=COM]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[CASE=COM][POSS=SG2]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[CASE=COM][CLIT=HAN]") + " |",
              file=options.outfile)
    elif options.upos == 'VERB':
        print(file=options.outfile)
        print("#### Finite forms", file=options.outfile)
        print(file=options.outfile)
        print("| *Person* | _Present_ | _Past_ | _Conditional_ |" +
              " _Potential_ | _Imperative_ |", file=options.outfile)
        print("|:---------|:----------|:-------|:--------------|"
              ":------------|:-------------|", file=options.outfile)
        print("| _1st singular_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][PERS=SG1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][PERS=SG1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][PERS=SG1]") + " |",
              file=options.outfile)
        print("| _2nd singular_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][PERS=SG2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][PERS=SG2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][PERS=SG2]") + " |",
              file=options.outfile)
        print("| _3rd singular_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][PERS=SG3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][PERS=SG3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][PERS=SG3]") + " |",
              file=options.outfile)
        print("| _1st plural_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=PL1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=PL1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][PERS=PL1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][PERS=PL1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][PERS=PL1]") + " |",
              file=options.outfile)
        print("| _2nd plural_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=PL2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=PL2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][PERS=PL2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][PERS=PL2]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][PERS=PL2]") + " |",
              file=options.outfile)
        print("| _3rd plural_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=PL3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=PL3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][PERS=PL3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][PERS=PL3]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][PERS=PL3]") + " |",
              file=options.outfile)
        print("| _Impersonal_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=INDV][TENSE=PRESENT][PERS=PE4]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=INDV][TENSE=PAST][PERS=PE4]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=COND][PERS=PE4]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=POTN][PERS=PE4]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=IMPV][PERS=PE4]") + " |",
              file=options.outfile)
        print("| _Connegative singular_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][NUM=SG][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][NEG=CON]") + " |",
              file=options.outfile)
        print("| _Connegative plural_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=INDV][TENSE=PAST][NUM=PL][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=COND][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=POTN][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][MOOD=IMPV][NEG=CON]") + " |",
              file=options.outfile)
        print("| _Connegative impersonal_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=INDV][TENSE=PRESENT][PERS=PE4]" +
                       "[NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=INDV][TENSE=PAST][PERS=PE4]" +
                       "[NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=COND][PERS=PE4][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=POTN][PERS=PE4][NEG=CON]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][MOOD=IMPV][PERS=PE4][NEG=CON]") + " |",
              file=options.outfile)
        print(file=options.outfile)
        print("#### Non-finite forms", file=options.outfile)
        print(file=options.outfile)
        print("| *Form* | _Active_ | _Passive_ | _Possessive_ | _Clitic_ |",
              file=options.outfile)
        print("|:-------|:---------|:----------|:-------------|:---------|",
              file=options.outfile)
        print("| _infinitive A lative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=A][NUM=SG][CASE=LAT]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][INF=A][NUM=SG][CASE=LAT]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=A][NUM=SG][CASE=LAT][POSS=SG1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=A][NUM=SG][CASE=LAT][CLIT=KO]") + " |",
              file=options.outfile)
        print("| _infinitive A translative_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=A][CASE=TRA]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][INF=A][CASE=TRA]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=A][CASE=TRA][POSS=SG1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=A][CASE=TRA][CLIT=KO]") + " |",
              file=options.outfile)
        print("| _infinitive E inessive_ | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=E][CASE=INE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][INF=E][CASE=INE]") + " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=ACT][INF=E][CASE=INE][POSS=SG1]") +
              " | " +
              generate(omorfi, options.word, options.upos,
                       "[VOICE=PSS][INF=E][CASE=INE][CLIT=KO]") + " |",
              file=options.outfile)
    if options.upos == 'ADJ':
        # comparisons
        print(file=options.outfile)
        print("#### Comparative forms", file=options.outfile)
        print(file=options.outfile)
    realend = perf_counter()
    cpuend = process_time()
    print("CPU time:", cpuend - cpustart, "real time:", realend - realstart)
    exit(0)


if __name__ == "__main__":
    main()
