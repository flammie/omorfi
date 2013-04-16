#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple python interface for omorfi using libhfst-python.
"""


import libhfst
from argparse import ArgumentParser

from sys import stderr, stdin
from os import getenv, access, F_OK

def omor2ftc(omorstring):
    anals = dict()
    ftc = ''
    omors = omorstring.split("][")
    for omor in omors:
        kv = omor.split("=")
        k = kv[0].lstrip("[")
        v = kv[1].rstrip("]")
        if k in anals:
            anals[k] = anals[k] + [v]
        else:
            anals[k] = [v]
    # WORD ID comes first as lemma
    for w in anals['WORD_ID']:
        ftc += w
    # word Case NUM P POSS
    if 'CASE' in anals:
        casesfrom = [["Par", "Part"], ["Ine", "In"], ["Ela", "El"]]
        case = anals['CASE'][-1].title()
        for c in casesfrom:
            case = case.replace(c[0], c[1])
        ftc += ' ' + case
    if 'NUM' in anals:
        ftc += ' ' + anals['NUM'][-1].upper()
    # Verb is Tense Genus Mood P PERS
    if 'TENSE' in anals:
        tensef = [['PRESENT', 'Pr'], ['PAST', 'Imp']]
        tense = anals['TENSE'][-1]
        for c in tensef:
            tense = tense.replace(c[0], c[1])
        ftc += ' ' + tense
    if 'VOICE' in anals:
        voice = anals['VOICE'][-1].title()
        ftc += ' ' + voice
    if 'MOOD' in anals:
        moodf = [['INDV', 'Ind'], ['COND', 'Cond'], ['POTN', 'Pot'], ['IMPV', 'Imper']]
        mood = anals['MOOD'][-1]
        for c in moodf:
            mood = mood.replace(c[0], c[1])
        ftc += ' ' + mood
    if 'PRS' in anals:
        possfrom = [["SG1", "S 1P"], ["SG2", "S 2P"], ["SG3", "S 3P"], ["PL1", "P 1P"], ["PL2", "P 2P"], ["PL3", "P 3P"], ['PE4', '']]
        poss = anals['PRS'][-1].upper()
        for c in possfrom:
            poss = poss.replace(c[0], c[1])
        if poss:
            ftc += ' ' + poss
    if 'POSS' in anals:
        possfrom = [["SG1", "S 1P"], ["SG2", "S 2P"], ["SG3", "3P"], ["PL1", "P 1P"], ["PL2", "P 2P"], ["PL3", "3P"]]
        poss = anals['POSS'][-1].upper()
        for c in possfrom:
            poss = poss.replace(c[0], c[1])
        ftc += ' ' + poss
    if ftc == ':':
        ftc = '_COLON'
    elif ftc == ',':
        ftc = '_COMMA'
    elif ftc == '.':
        ftc = '_PERIOD'
    elif ftc == '(':
        ftc = '_LEFTPARENTH'
    elif ftc == '-':
        ftc = '_HYPHEN'
    elif ftc == ')':
        ftc = '_RIGHTPARENTH'
    elif ftc == '?':
        ftc = '_QUESTION'
    elif ftc == '+':
        ftc = '_PLUS'
    elif ftc == '/':
        ftc = '_SLASH'
    elif ftc == '!':
        ftc = '_EXCLAMATION'
    elif ftc == '*':
        ftc = '_ASTERISK'
    elif ftc == ';':
        ftc = '_SEMICOLON'
    elif ftc == '%':
        ftc = '_RIGHTP'
    elif ftc == '...':
        ftc = '_THREEPOINTS'
    return ftc

def load_omorfi(path=None):
    stdpaths = ['/usr/local/share/hfst/fi/morphology.omor.hfst',
            '/usr/share/hfst/fi/morphology.omor.hfst',
            '/usr/local/share/omorfi/morphology.omor.hfst',
            '/usr/share/omorfi/morphology.hfst']
    if getenv('HOME'):
        home = getenv('HOME')
        stdpaths += [home + '/.hfst/fi/morphology.omor.hfst',
                home + '/.omorfi/morphology.omor.hfst' ]
    if path:
        if access(path, F_OK):
            res = libhfst.HfstTransducer(libhfst.HfstInputStream(path))
    else:
        for sp in stdpaths:
            if access(sp, F_OK):
                res = libhfst.HfstTransducer(libhfst.HfstInputStream(sp))
    return res

def omorfi_lookup(omorfi, token, can_titlecase=True, can_uppercase=True):
    titlecased = False
    uppercased = False
    res = libhfst.detokenize_paths(omorfi.lookup_fd(token))
    if len(res) == 0 and can_titlecase:
        res = libhfst.detokenize_paths(omorfi.lookup_fd(token[0].lower() + token[1:]))
        titlecased = True
        if len(res) == 0 and can_uppercase:
            res = libhfst.detokenize_paths(omorfi.lookup_fd(token.lower()))
            uppercased = True
    if uppercased:
        for r in res:
            r.output = r.output + '[CASECHANGE=LOWERED]'
    elif titlecased:
        for r in res:
            r.output = r.output + '[CASECHANGE=DOWNFIRST]'
    return res

def main():
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAFILE',
            help="HFST's optimised lookup binary data for the transducer to be applied")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
            dest="infile", help="source of analysis data")
    options = a.parse_args()
    omorfi = load_omorfi(options.fsa)
    if not options.infile:
        options.infile = stdin
    for line in options.infile:
        surf = line.strip()
        if not surf or surf == '':
            continue
        anals = omorfi_lookup(omorfi, surf)
        print(surf, end='')
        for anal in anals:
            print("\t", anal.output, '[WEIGHT=', anal.weight, ']', sep='', end='')
        print('\n')
    exit(0)

if __name__ == "__main__":
    main()
