#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string munging
import re
# CLI stuff
from argparse import ArgumentParser, FileType
from sys import stderr, stdin, stdout
# statistics
from time import perf_counter, process_time

def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-i', '--input', metavar="INFILE", type=open, required=True,
                   dest="infile", help="conllu files to count")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--statistics', metavar="STATDIR", dest="statdir",
                   help="print statistics to STATDIR/*.freqs",
                   required=True)
    a.add_argument('-l', '--lexemes', metavar="LEXFILE", type=open,
                   help="read known lexemes from LEXFILE")
    a.add_argument('--debug', action='store_true',
                   help="print lots of debug info while processing")
    options = a.parse_args()
    if options.verbose:
        print("Printing verbosely")
    if not options.infile:
        print("reading from <stdin>")
        options.infile = stdin
    elif options.verbose:
        print("reading from", options.infile.name)
    lexstatfile = open(options.statdir + '/lexemes.freqs', 'w')
    tagstatfile = open(options.statdir + '/omors.freqs', 'w')
    lexemes = dict()
    if options.lexemes:
        if options.verbose:
            print("reading lexemes from", options.lexemes.name)
        for line in options.lexemes:
            fields = line.split('\t')
            if len(fields) < 4:
                print("Should have 4 fields per line in lexeme file, skipping:",
                      fields)
                continue
            if fields[0] == 'lemma':
                # first line
                continue
            lexemes[fields[0]] = 0
        if verbose:
            print("initialised", len(lexemes), "unseen lexemes")
    tags = dict()
    n_lexemes = 0
    n_tags = 0
    lines = 0
    for line in options.infile:
        lines += 1
        if options.verbose and lines % 5000 == 0:
            print(lines, "...", end=' ')
        fields = line.strip().split('\t')
        if len(fields) != 10:
            if line.startswith('#') or line.strip() == '':
                # ignore all comments, good or bad
                continue
            else:
                print("Unrecognisable conllu line:", fields)
                exit(1)
        lemmas = fields[2].split('#')
        for lemma in lemmas:
            if lemma.strip() == '':
                continue
            elif lemma in lexemes:
                lexemes[lemma] += 1
            else:
                lexemes[lemma] = 1
            n_lexemes += 1
        upos = fields[3]
        ufeats = fields[5].split('|')
        omors = ['[UPOS=' + upos +']']
        for ufeat in ufeats:
            uke, eq, uval = ufeat.partition('=')
            if uke == 'Number':
                if uval == 'Sing':
                    omors += ['[NUM=SG]']
                elif uval == 'Plur':
                    omors += ['[NUM=PL]']
                else:
                    print("number?", uval)
            elif uke == 'Case':
                omors += ['[CASE=' + uval.upper() + ']']
            elif uke == 'Voice':
                if uval == 'Act':
                    omors += ['[VOICE=ACT]']
                elif uval == 'Pass':
                    omors += ['[VOICE=PSS]']
                else:
                    print("voice", uval)
            elif uke == 'Mood':
                if uval == 'Ind':
                    omors += ['[MOOD=INDV]']
                elif uval == 'Cnd':
                    omors += ['[MOOD=COND]']
                elif uval == 'Imp':
                    omors += ['[MOOD=IMPV]']
                elif uval == 'Pot':
                    omors += ['[MOOD=POTN]']
                else:
                    print("mood?", uval)
            elif uke == 'Tense':
                if uval == 'Pres':
                    omors += ['[TENSE=PRES]']
                elif uval == 'Past':
                    omors += ['[TENSE=PAST]']
            elif uke == 'Person':
                if uval == '1':
                    if 'Number=Sing' in ufeats:
                        omors += ['[PERS=SG1]']
                    elif 'Number=Plur' in ufeats:
                        omors += ['[PERS=PL1]']
                    else:
                        print("Person needs Number", ufeats)
                elif uval == '2':
                    if 'Number=Sing' in ufeats:
                        omors += ['[PERS=SG2]']
                    elif 'Number=Plur' in ufeats:
                        omors += ['[PERS=PL2]']
                    else:
                        print("Person needs Number", ufeats)
                elif uval == '3':
                    if 'Number=Sing' in ufeats:
                        omors += ['[PERS=SG3]']
                    elif 'Number=Plur' in ufeats:
                        omors += ['[PERS=PL3]']
                    else:
                        print("Person needs Number", ufeats)
                elif uval == '0':
                    # XXX: for now 0 -> 3
                    if 'Number=Sing' in ufeats:
                        omors += ['[PERS=SG3]']
                    elif 'Number=Plur' in ufeats:
                        omors += ['[PERS=PL3]']
                    else:
                        print("Person needs Number", ufeats)
                else:
                    print('person?', uval)
            elif uke == 'Person[psor]':
                if uval == '1':
                    if 'Number[psor]=Sing' in ufeats:
                        omors += ['[POSS=SG1]']
                    elif 'Number[psor]=Plur' in ufeats:
                        omors += ['[POSS=PL1]']
                    else:
                        print("Person[psor] = 1 needs Number", ufeats)
                elif uval == '2':
                    if 'Number[psor]=Sing' in ufeats:
                        omors += ['[POSS=SG2]']
                    elif 'Number[psor]=Plur' in ufeats:
                        omors += ['[POSS=PL2]']
                    else:
                        print("Person[psor]=2 needs Number", ufeats)
                elif uval == '3':
                    if 'Number[psor]=Sing' in ufeats:
                        omors += ['[POSS=SG3]']
                    elif 'Number[psor]=Plur' in ufeats:
                        omors += ['[POSS=PL3]']
                    else:
                        omors += ['[POSS=3]']
                else:
                    print('person[psor]?', uval)
            elif uke == 'Number[psor]':
                # see above
                continue
            elif uke == 'Connegative':
                omors += ['[NEG=CON]']
            elif uke == 'Polarity':
                omors += ['[SUBCAT=NEG]']
            elif uke == 'PartForm':
                if uval == 'Past':
                    omors += ['[PCP=NUT]']
                elif uval == 'Pres':
                    omors += ['[PCP=VA]']
                elif uval == 'Agt':
                    omors += ['[PCP=MA]']
                elif uval == 'Neg':
                    omors += ['[PCP=MATON]']
                else:
                    print("partform?", uval)
            elif uke == 'InfForm':
                if uval == '3':
                    omors += ['[INF=MA]']
                elif uval == '2':
                    omors += ['[INF=E]']
                elif uval == '1':
                    omors += ['[INF=A]']
                else:
                    print('inffform?', uval)
            elif uke == 'Degree':
                if uval == 'Pos':
                    omors += ['[CMP=POS]']
                elif uval == 'Cmp':
                    omors += ['[CMP=CMP]']
                elif uval == 'Sup':
                    omors += ['[CMP=SUP]']
                else:
                    print('degree?', uval)
            elif uke == 'Clitic':
                omors += ['[CLIT=' + uval.upper() + ']']
            elif uke == 'Derivation':
                omors += ['[DRV=' + uval.upper() + ']']
            elif uke == 'Abbr':
                # not counting abbrs
                continue
            elif uke == 'Style':
                # not counting foreigns
                continue
            elif uke == 'Foreign':
                # not counting foreigns
                continue
            elif uke == 'Typo':
                # not counting typos
                continue
            elif uke == 'VerbForm':
                # not counting infinitivititity
                continue
            elif uke == 'Reflex':
                # not gonna count numtypes
                continue
            elif uke == 'PronType':
                # not gonna count numtypes
                continue
            elif uke == 'NumType':
                # not gonna count numtypes
                continue
            elif uke == 'AdpType':
                # not gonna count adptypes
                continue
            elif uke == '_':
                # no feats
                continue
            else:
                print("Unhandled", uke, eq, uval)
        for omor in omors:
            if omor in tags:
                tags[omor] += 1
            else:
                tags[omor] = 1
            n_tags += 1
    if options.verbose:
        print("writing lexeme statistiscs to", lexstatfile.name)
    for lexeme, freq in lexemes.items():
        print(freq, lexeme, sep='\t', file=lexstatfile)
    for tag, freq in tags.items():
        print(freq, tag, sep='\t', file=tagstatfile)

if __name__ == "__main__":
    main()

