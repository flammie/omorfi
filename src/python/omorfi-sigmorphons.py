#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test omorfi - unimorph compatibility
"""


from argparse import ArgumentParser, FileType
from sys import stderr, stdout, stdin
from time import perf_counter, process_time

from omorfi import Omorfi

u2o = {'pos=N': '[UPOS=NOUN]',
       'pos=V': '[UPOS=VERB]',
       'pos=ADJ': '[UPOS=ADJ]',
       'case=NOM': '[CASE=NOM]',
       'case=ON+ESS': '[CASE=ADE]',
       'case=ON+ABL': '[CASE=ABL]',
       'case=PRIV': '[CASE=ABE]',
       'case=IN+ESS': '[CASE=INE]',
       'case=IN+LAT': '[CASE=ILL]',
       'case=IN+ABL': '[CASE=ELA]',
       'case=ACC': '[CASE=ACC]',
       'case=PRT': '[CASE=PAR]',
       'case=COM': '[CASE=COM]',
       'case=GEN': '[CASE=GEN]',
       'case=INS': '[CASE=INS]',
       'case=FRML': '[CASE=ESS]',
       'case=TRANS': '[CASE=TRA]',
       'case=ON+ALL': '[CASE=ALL]',
       'polar=POS': '',
       'mood=IMP': '[MOOD=IMPV]',
       'mood=IND': '[MOOD=INDV]',
       'mood=COND': '[MOOD=COND]',
       'mood=POT': '[MOOD=POTN]',
       'mood=PURP': '[INF=A][CASE=TRA][POSS=3]',
       'aspect=PROSP': '[DRV=MAISILLA][POSS=3]',
       'finite=NFIN': '[INF=A][NUM=SG][CASE=LAT]',
       'tense=PRS': '[TENSE=PRESENT]',
       'tense=PST': '[TENSE=PAST]',
       'voice=ACT': '[VOICE=ACT]',
       'voice=PASS': '[VOICE=PSS]',
       'comp=SPRL': '[DRV=IN²][CMP=SUP]',
       'comp=CMPR': '[DRV=MPI][CMP=CMP]',
       'per=1': '[PERS=__1]',
       'per=2': '[PERS=__2]',
       'per=3': '[PERS=__3]',
       'num=SG': '[NUM=SG]',
       'num=PL': '[NUM=PL]'
       }


def unimorph2omor(unimorphstring):
    unimorphs = unimorphstring.split(',')
    omors = ''
    for unimorph in unimorphs:
        if 'pos' not in unimorph:
            continue
        if unimorph in u2o:
            omors += u2o[unimorph]
        else:
            print("missing", unimorph)
            exit(1)
    for unimorph in unimorphs:
        if 'comp' not in unimorph and 'voice' not in unimorph:
            continue
        if unimorph in u2o:
            omors += u2o[unimorph]
        else:
            print("missing", unimorph)
            exit(1)
    for unimorph in unimorphs:
        if 'mood' not in unimorph and 'aspect' not in unimorph and 'finite' \
                not in unimorph:
            continue
        if unimorph in u2o:
            omors += u2o[unimorph]
        else:
            print("missing", unimorph)
            exit(1)
    for unimorph in unimorphs:
        if 'tense' not in unimorph:
            continue
        if unimorph in u2o:
            omors += u2o[unimorph]
        else:
            print("missing", unimorph)
            exit(1)
    for unimorph in unimorphs:
        if 'per' not in unimorph:
            continue
        if unimorph in u2o:
            omors += u2o[unimorph]
        else:
            print("missing", unimorph)
            exit(1)
    for unimorph in unimorphs:
        if 'num' not in unimorph:
            continue
        if unimorph in u2o:
            omors += u2o[unimorph]
        else:
            print("missing", unimorph)
            exit(1)
    for unimorph in unimorphs:
        if 'case' not in unimorph:
            continue
        if unimorph in u2o:
            omors += u2o[unimorph]
        else:
            print("missing", unimorph)
            exit(1)
    omors = omors.replace("UPOS=ADJ][NUM", "UPOS=ADJ][CMP=POS][NUM")
    omors = omors.replace("UPOS=VERB][MOOD", "UPOS=VERB][VOICE=ACT][MOOD")
    omors = omors.replace("PERS=__1][NUM=SG]", "PERS=SG1]")
    omors = omors.replace("PERS=__2][NUM=SG]", "PERS=SG2]")
    omors = omors.replace("PERS=__3][NUM=SG]", "PERS=SG3]")
    omors = omors.replace("PERS=__1][NUM=PL]", "PERS=PL1]")
    omors = omors.replace("PERS=__2][NUM=PL]", "PERS=PL2]")
    omors = omors.replace("PERS=__3][NUM=PL]", "PERS=PL3]")
    omors = omors.replace("COND][TENSE=PAST]", "COND]")
    omors = omors.replace("IMPV][TENSE=PAST]", "IMPV]")
    omors = omors.replace("POTN][TENSE=PAST]", "POTN]")
    omors = omors.replace("IMPV][TENSE=PRESENT]", "IMPV]")
    omors = omors.replace("POTN][TENSE=PRESENT]", "POTN]")
    omors = omors.replace("COND][TENSE=PRESENT]", "COND]")
    omors = omors.replace("NUM=PL][CASE=COM]", "CASE=COM]")
    if 'VOICE=PSS' in omors:
        omors += '[PERS=PE4]'
    if 'CMP=SUP' in omors or 'CMP=CMP' in omors:
        omors += '[NUM=SG][CASE=NOM]'
    if 'CASE=ACC' in omors:
        if 'NUM=SG' in omors:
            omors = omors.replace("CASE=ACC", "CASE=GEN")
        elif "NUM=PL" in omors:
            omors = omors.replace("CASE=ACC", "CASE=NOM")
        else:
            print("ARGEG¤EFREAF¤EFFWA")
            exit(2)
    if 'CASE=COM' in omors and 'UPOS=NOUN' in omors:
        # nonsense but argh
        omors += '[POSS=3]'
    return omors


def main():
    """Command-line interface for omorfi's sort | uniq -c tester."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='FSAFILE', required=True,
                   help="load analyser from FSAFILE")
    a.add_argument('-g', '--generator', metavar='FSAFILE', required=True,
                   help="load analyser from FSAFILE")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-o', '--output', metavar="OUTFILE",
                   type=FileType('w'),
                   dest="outfile", help="log outputs to OUTFILE")
    a.add_argument('-X', '--statistics', metavar="STATFILE",
                   type=FileType('w'),
                   dest="statfile", help="statistics")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
                   help="Print verbosely while processing")
    a.add_argument('-C', '--no-casing', action="store_true", default=False,
                   help="Do not try to recase input and output when matching")
    a.add_argument('-t', '--threshold', metavar="THOLD", default=99,
                   help="if coverage is less than THOLD exit with error")
    a.add_argument('-F', '--format', metavar="FMT", required=True,
                   help="which SIGMORHON shared task format is used")

    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    try:
        if options.analyser:
            if options.verbose:
                print("reading analyser from", options.analyser)
            omorfi.load_analyser(options.analyser)
        if options.generator:
            if options.verbose:
                print("reading generator from", options.generator)
            omorfi.load_generator(options.generator)
        if not options.infile:
            options.infile = stdin
            print("reading from <stdin>")
        if not options.statfile:
            options.statfile = stdout
        if not options.outfile:
            options.outfile = stdout
    except IOError:
        print("Could not process file", options.analyser, file=stderr)
        exit(2)
    # basic statistics
    correct = 0
    incorrect = 0
    oov = 0
    lines = 0
    # for make check target
    realstart = perf_counter()
    cpustart = process_time()
    for line in options.infile:
        fields = line.strip().split('\t')
        if len(fields) < 3:
            print("ERROR: Skipping line", fields, file=stderr)
            continue
        omors = None
        lemma = None
        print("<<<", fields)
        if options.format == '1':
            lemma = fields[0]
            omors = unimorph2omor(fields[1])
        elif options.format == '2':
            srcomors = unimorph2omor(fields[0])
            srchyps = omorfi.analyse(fields[1])
            for srchyp in srchyps:
                if srcomors in srchyp.raw and len(srchyp.get_lemmas()) == 1:
                    lemma = srchyp.get_lemmas()[0]
            if not lemma:
                lemma = ''.join(srchyps[0].get_lemmas())
            omors = unimorph2omor(fields[2])
        elif options.format == '3':
            srchyps = omorfi.analyse(fields[0])
            for srchyp in srchyps:
                if len(srchyp.get_lemmas()) == 1:
                    lemma = srchyp.get_lemmas()[0]
            if not lemma:
                lemma = ''.join(srchyps[0].get_lemmas())
            omors = unimorph2omor(fields[1])
        else:
            print("format fail", options.format)
            exit(1)
        genomor = '[WORD_ID=' + lemma + ']' + omors
        print(">>> ", genomor)
        generations = omorfi.generate(genomor)
        if not generations or '[' in generations:
            oov += 1
            genat1 = lemma
            print("OOV", genat1)
        else:
            genat1 = generations.split('/')[0]
            print("@1 ", genat1)
        if options.format == '1':
            if genat1 == fields[2]:
                correct += 1
            else:
                print("MIS", genat1, "!=", fields[2])
                incorrect += 1
        elif options.format == '2':
            if genat1 == fields[3]:
                correct += 1
            else:
                print("MIS", genat1, "!=", fields[2])
                incorrect += 1
        elif options.format == '3':
            if genat1 == fields[2]:
                correct += 1
            else:
                print("MIS", genat1, "!=", fields[2])
                incorrect += 1
        lines += 1
        if options.verbose and lines % 1000 == 0:
            print(lines, '...')
    realend = perf_counter()
    cpuend = process_time()
    print("CPU time:", cpuend - cpustart, "real time:", realend - realstart)
    if lines == 0:
        print("Needs more than 0 lines to determine something",
              file=stderr)
        exit(2)
    print("Lines", "Corect", "OOV", sep="\t", file=options.statfile)
    print(lines, correct, oov, sep="\t", file=options.statfile)
    print(lines / lines * 100 if lines != 0 else 0,
          correct / lines * 100 if lines != 0 else 0,
          oov / lines * 100,
          sep="\t", file=options.statfile)
    exit(0)


if __name__ == "__main__":
    main()
