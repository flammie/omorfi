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


def print_nominals_(omorfi, word, upos, outfile, inject=''):
    print("| *Case* | _Singular_ | _Plural_ | _Possessive_ | _Clitic_ |",
          file=outfile)
    print("|:-------|:-----------|:---------|:-------------|:---------|",
          file=outfile)
    print("| _Nominative_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=NOM]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=NOM]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=NOM][POSS=SG1]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=NOM][CLIT=HAN]") + " |",
          file=outfile)
    print("| _Genitive_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=GEN]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=GEN]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=GEN][POSS=SG2]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=GEN][CLIT=KO]") + " |",
          file=outfile)
    print("| _Partitive_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=PAR]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=PAR]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=PAR][POSS=3]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=PAR][CLIT=PA]") + " |",
          file=outfile)
    print("| _Inessive_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=INE]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=INE]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=INE][POSS=PL1]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=INE][CLIT=KAAN]") + " |",
          file=outfile)
    print("| _Elative_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ELA]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ELA]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ELA][POSS=PL2]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ELA][CLIT=KIN]") + " |",
          file=outfile)
    print("| _Illative_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ILL]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ILL]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ILL][POSS=3]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ILL][CLIT=KO]") + " |",
          file=outfile)
    print("| _Adessive_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ADE]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ADE]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ADE][POSS=SG1]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ADE][CLIT=PA]") + " |",
          file=outfile)
    print("| _Ablative_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ABL]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ABL]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ABL][POSS=SG2]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ABL][CLIT=KAAN]") + " |",
          file=outfile)
    print("| _Allative_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ALL]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ALL]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ALL][POSS=3]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ALL][CLIT=HAN]") + " |",
          file=outfile)
    print("| _Essive_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ESS]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ESS]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ESS][POSS=PL1]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ESS][CLIT=KO]") + " |",
          file=outfile)
    print("| _Translative_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=TRA]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=TRA]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=TRA][POSS=PL2]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=TRA][CLIT=PA]") + " |",
          file=outfile)
    print("| _Abessive_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ABE]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ABE]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=ABE][POSS=3]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=ABE][CLIT=KAAN]") + " |",
          file=outfile)
    print("| _Instructive_ | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=INS]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=INS]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=SG][CASE=INS][POSS=SG1]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[NUM=PL][CASE=INS][CLIT=KO]") + " |",
          file=outfile)
    print("| _Comitative_ | " +
          generate(omorfi, word, upos, inject +
                   "[CASE=COM]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[CASE=COM]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[CASE=COM][POSS=SG2]") + " | " +
          generate(omorfi, word, upos, inject +
                   "[CASE=COM][CLIT=HAN]") + " |",
          file=outfile)


def print_nominals(omorfi, word, upos, outfile):
    print("#### Nominal cases", file=outfile)
    print(file=outfile)
    print_nominals_(omorfi, word, upos, outfile, '')


def print_numerals(omorfi, word, upos, outfile):
    print("#### Nominal cases", file=outfile)
    print(file=outfile)
    if word.endswith('s') or word.endswith('nen'):
        tags = '[NUMTYPE=ORD]'
    else:
        tags = '[NUMTYPE=CARD]'
    print_nominals_(omorfi, word, upos, outfile, tags)

def print_comparatives(omorfi, word, upos, comp, outfile):
    if comp == 'POS':
        print("#### Nominal cases", file=outfile)
        tags = "[CMP=POS]"
    elif comp == 'CMP':
        print("#### Comparative cases", file=outfile)
        tags = "[DRV=MPI][CMP=CMP]"
    elif comp == 'SUP':
        print("#### Superlative cases", file=outfile)
        tags = "[DRV=IN²][CMP=SUP]"
    print(file=outfile)
    print_nominals_(omorfi, word, upos, outfile, tags)


def print_finites(omorfi, word, upos, outfile):
    print(file=outfile)
    print("#### Finite forms", file=outfile)
    print(file=outfile)
    print("| *Person* | _Present_ | _Past_ | _Conditional_ |" +
          " _Potential_ | _Imperative_ |", file=outfile)
    print("|:---------|:----------|:-------|:--------------|"
          ":------------|:-------------|", file=outfile)
    print("| _1st singular_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][PERS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][PERS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][PERS=SG1]") + " |",
          file=outfile)
    print("| _2nd singular_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][PERS=SG2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][PERS=SG2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][PERS=SG2]") + " |",
          file=outfile)
    print("| _3rd singular_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][PERS=SG3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][PERS=SG3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][PERS=SG3]") + " |",
          file=outfile)
    print("| _1st plural_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=PL1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=PL1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][PERS=PL1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][PERS=PL1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][PERS=PL1]") + " |",
          file=outfile)
    print("| _2nd plural_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=PL2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=PL2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][PERS=PL2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][PERS=PL2]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][PERS=PL2]") + " |",
          file=outfile)
    print("| _3rd plural_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=PL3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=PL3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][PERS=PL3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][PERS=PL3]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][PERS=PL3]") + " |",
          file=outfile)
    print("| _Impersonal_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=INDV][TENSE=PRESENT][PERS=PE4]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=INDV][TENSE=PAST][PERS=PE4]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=COND][PERS=PE4]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=POTN][PERS=PE4]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=IMPV][PERS=PE4]") + " |",
          file=outfile)
    print("| _Connegative singular_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][NUM=SG][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][NEG=CON]") + " |",
          file=outfile)
    print("| _Connegative plural_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=INDV][TENSE=PAST][NUM=PL][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=COND][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=POTN][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][MOOD=IMPV][NEG=CON]") + " |",
          file=outfile)
    print("| _Connegative impersonal_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=INDV][TENSE=PRESENT][PERS=PE4]" +
                   "[NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=INDV][TENSE=PAST][PERS=PE4]" +
                   "[NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=COND][PERS=PE4][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=POTN][PERS=PE4][NEG=CON]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][MOOD=IMPV][PERS=PE4][NEG=CON]") + " |",
          file=outfile)


def print_infinites(omorfi, word, upos, outfile):
    print("#### Non-finite forms", file=outfile)
    print(file=outfile)
    print("| *Form* | _Active_ | _Passive_ | _Possessive_ | _Clitic_ |",
          file=outfile)
    print("|:-------|:---------|:----------|:-------------|:---------|",
          file=outfile)
    print("| _infinitive A lative_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=A][NUM=SG][CASE=LAT]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=A][NUM=SG][CASE=LAT]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=A][NUM=SG][CASE=LAT][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=A][NUM=SG][CASE=LAT][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive A translative_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=A][CASE=TRA]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=A][CASE=TRA]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=A][CASE=TRA][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=A][CASE=TRA][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive E inessive_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=E][NUM=SG][CASE=INE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=E][NUM=SG][CASE=INE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=E][NUM=SG][CASE=INE][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=E][NUM=SG][CASE=INE][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive E instructive_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=E][NUM=SG][CASE=INS]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=E][NUM=SG][CASE=INS]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=E][NUM=SG][CASE=INS][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=E][NUM=SG][CASE=INS][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive MA inessive_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=INE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=INE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=INE][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=INE][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive MA elative_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ELA]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ELA]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ELA][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ELA][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive MA illative_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ILL]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ILL]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ILL][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ILL][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive MA adessive_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ADE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ADE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ADE][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ADE][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive MA abessive_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ABE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ABE]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=ABE][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=ABE][CLIT=KO]") + " |",
          file=outfile)
    print("| _infinitive MA instructive_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=INS]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=INS]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][INF=MA][NUM=SG][CASE=INS][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MA][NUM=SG][CASE=INS][CLIT=KO]") + " |",
          file=outfile)
    print("| _derivation MINEN_ | " +
          generate(omorfi, word, upos,
                   "[INF=MINEN]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][INF=MINEN]") + " | " +
          generate(omorfi, word, upos,
                   "[DRV=MINEN][NUM=SG][CASE=NOM][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[DRV=MINEN][NUM=SG][CASE=NOM][CLIT=KO]") + " |",
          file=outfile)
    print("| _derivation MAISILLA_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][DRV=MAISILLA]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][DRV=MAISILLA]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][DRV=MAISILLA][POSS=SG1]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][DRV=MAISILLA][CLIT=KO]") + " |",
          file=outfile)
    print("| _participle NUT_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][PCP=NUT][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][PCP=NUT][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][PCP=NUT][CMP=POS][NUM=SG][CASE=INE]" +
                   "[POSS=SG1]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][PCP=NUT][CMP=POS][NUM=SG][CASE=ADE][" +
                   "CLIT=KO]") + " |", file=outfile)
    print("| _participle VA_ | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][PCP=VA][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][PCP=VA][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=ACT][PCP=VA][CMP=POS][NUM=SG][CASE=ELA]" +
                   "[POSS=SG1]") + " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][PCP=VA][CMP=POS][NUM=SG][CASE=ABL][" +
                   "CLIT=KO]") + " |", file=outfile)
    print("| _participle MA_ | " +
          generate(omorfi, word, upos,
                   "[PCP=AGENT][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][PCP=AGENT][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[PCP=AGENT][CMP=POS][NUM=SG][CASE=ELA]" +
                   "[POSS=SG1]") + " | " +
          generate(omorfi, word, upos,
                   "[PCP=AGENT][CMP=POS][NUM=SG][CASE=ABL][" +
                   "CLIT=KO]") + " |", file=outfile)
    print("| _participle MATON_ | " +
          generate(omorfi, word, upos,
                   "[PCP=NEG][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[VOICE=PSS][PCP=NEG][CMP=POS][NUM=SG][CASE=NOM]") +
          " | " +
          generate(omorfi, word, upos,
                   "[PCP=NEG][CMP=POS][NUM=SG][CASE=ELA]" +
                   "[POSS=SG1]") + " | " +
          generate(omorfi, word, upos,
                   "[PCP=NEG][CMP=POS][NUM=SG][CASE=ABL][" +
                   "CLIT=KO]") + " |", file=outfile)


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
    if options.upos == 'NOUN':
        print_nominals(omorfi, options.word, options.upos, options.outfile)
    elif options.upos == 'ADJ':
        print_comparatives(omorfi, options.word, options.upos, 'POS',
                           options.outfile)
        # comparisons
        print(file=options.outfile)
        print_comparatives(omorfi, options.word, options.upos, "CMP",
                           options.outfile)
        print(file=options.outfile)
        print_comparatives(omorfi, options.word, options.upos, "SUP",
                           options.outfile)
    elif options.upos == 'NUM':
        print_numerals(omorfi, options.word, options.upos, options.outfile)
    elif options.upos == 'VERB':
        print_finites(omorfi, options.word, options.upos, options.outfile)
        print(file=options.outfile)
        print_infinites(omorfi, options.word, options.upos, options.outfile)
    print(file=options.outfile)
    print("_Note:_ the inflection tables cover small percentage of the " +
          "whole inflectional paradigm, for full list, see [" +
          options.word + " full form list](" + options.word + ".html)",
          file=options.outfile)
    print(file=options.outfile)
    realend = perf_counter()
    cpuend = process_time()
    print("CPU time:", cpuend - cpustart, "real time:", realend - realstart)
    exit(0)


if __name__ == "__main__":
    main()
