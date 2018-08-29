#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stderr, stdin, stdout
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi import Omorfi, Token
#from omorfi.token import get_ud_feats, get_upos, get_lemmas, \
#       format_feats_ud, format_xpos_ftb, format_xpos_tdt, format_misc_ud







def try_analyses_conllu(original, wordn, surf, anals, outfile, hacks=None):
    for anal in anals:
        upos = get_upos(anal)
        if upos == original[3]:
            feats = format_feats_ud(anal)
            if feats == original[5]:
                lemmas = "#".join(get_lemmas(anal))
                if lemmas == original[2]:
                    return print_analyses_conllu(wordn, surf, anal, outfile, hacks)
    # no exact match found (re-try without lemma)
    for anal in anals:
        upos = get_upos(anal)
        if upos == original[3]:
            feats = format_feats_ud(anal)
            if feats == original[5]:
                return print_analyses_conllu(wordn, surf, anal, outfile, hacks)
    # and re-try without feats
    for anal in anals:
        upos = get_upos(anal)
        if upos == original[3]:
            return print_analyses_conllu(wordn, surf, anal, outfile, hacks)
    return print_analyses_conllu(wordn, surf, anals[0], outfile, hacks)


def debug_analyses_conllu(original, wordn, surf, anals, outfile, hacks=None):
    print("# REFERENCE(python):", original, file=outfile)
    for anal in anals:
        print_analyses_conllu(wordn, surf, anal, outfile, hacks)



def print_analyses_conllu(wordn, surf, anal, outfile, hacks=None):
    upos = get_upos(anal)
    if not upos or upos == "":
        upos = 'X'
    if hacks == 'ftb':
        third = format_xpos_ftb(anal)
    else:
        third = format_xpos_tdt(anal)
    print(wordn, surf, "#".join(get_lemmas(anal)),
          upos,
          third,
          format_feats_ud(anal, hacks),
          "_", "_", "_", format_misc_ud(anal), sep="\t", file=outfile)


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-a', '--analyser', metavar='AFILE',
                   help="read analyser model from AFILE")
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE", dest="outfile",
                   help="print output into OUTFILE", type=FileType('w'))
    a.add_argument('-x', '--statistics', metavar="STATFILE", dest="statfile",
                   help="print statistics to STATFILE", type=FileType('w'))
    a.add_argument('-O', '--oracle', action='store_true',
                   help="match to values in input when parsing if possible")
    a.add_argument('-u', '--udpipe', metavar="UDPIPE",
                   help='use UDPIPE for additional guesses (experi-mental)')
    a.add_argument('--hacks', metavar='HACKS',
                   help="mangle analyses to match HACKS version of UD",
                   choices=['ftb'])
    a.add_argument('-X', '--frequencies', metavar="FREQDIR",
                   help="read frequencies from FREQDIR/*.freqs")
    a.add_argument('--debug', action='store_true',
                   help="print lots of debug info while processing")
    options = a.parse_args()
    if options.verbose:
        print("Printing verbosely")
    omorfi = Omorfi(options.verbose)
    if options.analyser:
        if options.verbose:
            print("reading analyser model", options.analyser)
        omorfi.load_analyser(options.analyser)
    else:
        print("analyser is needed to conllu", file=stderr)
        exit(4)
    if options.udpipe:
        if options.verbose:
            print("Loading udpipe", options.udpipe)
        omorfi.load_udpipe(options.udpipe)
    if not options.infile:
        print("reading from <stdin>")
        options.infile = stdin
    if options.verbose:
        print("analysing", options.infile.name)
    if not options.outfile:
        options.outfile = stdout
    if options.verbose:
        print("writing to", options.outfile.name)
    if not options.statfile:
        options.statfile = stdout

    if options.frequencies:
        with open(options.frequencies + '/lexemes.freqs') as lexfile:
            omorfi.load_lexical_frequencies(lexfile)
        with open(options.frequencies + '/omors.freqs') as omorfile:
            omorfi.load_omortag_frequencies(omorfile)

    # statistics
    realstart = perf_counter()
    cpustart = process_time()
    tokens = 0
    unknowns = 0
    sentences = 0
    recognised_comments = ['sent_id =', 'text =', 'doc-name:', 'sentence-text:']
    for sentplus in tokenise_conllu(options.infile):
        for token in sentplus:
            if token.nontoken and token.comment:
                if token.comment == '':
                    print(file=options.outfile)
                else:
                    print("#", token.comment, file=options.outfile)
                continue
            tokens += 1
            anals = omorfi.analyse(token)
            if not anals or len(anals) == 0 or (len(anals) == 1 and
                                                'OOV' in anals[0]):
                unknowns += 1
                anals = omorfi.guess(token)
            if anals and len(anals) > 0:
                if options.debug:
                    debug_analyses_conllu(
                        fields, index, surf, anals, options.outfile, options.hacks)
                elif options.oracle:
                    try_analyses_conllu(fields, index, surf, anals,
                                        options.outfile, options.hacks)
                else:
                    print_analyses_conllu(index, surf, anals[0],
                                          options.outfile, options.hacks)
            else:
                print("???", file=stderr)
                exit(1)
    cpuend = process_time()
    realend = perf_counter()
    print("Tokens:", tokens, "Sentences:", sentences,
          file=options.statfile)
    print("Unknowns / OOV:", unknowns, "=",
          unknowns / tokens * 100 if tokens != 0 else 0,
          "%", file=options.statfile)
    print("CPU time:", cpuend - cpustart, "Real time:", realend - realstart,
          file=options.statfile)
    print("Tokens per timeunit:", tokens / (realend - realstart),
          file=options.statfile)
    exit(0)


if __name__ == "__main__":
    main()
