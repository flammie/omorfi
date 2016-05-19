#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string munging
import re
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stderr, stdin, stdout
# statistics
from time import perf_counter, process_time

# omorfi
from omorfi.omorfi import Omorfi


def get_lemmas(anal):
    re_lemma = re.compile("\[WORD_ID=([^]]*)\]")
    lemmas = re_lemma.finditer(anal[0])
    rv = []
    for lemma in lemmas:
        rv += [lemma.group(1)]
    return rv


def get_last_feat(feat, anal):
    re_feat = re.compile("\[" + feat + "=([^]]*)\]")
    feats = re_feat.finditer(anal[0])
    rv = ""
    for feat in feats:
        rv = feat.group(1)
    return rv


def get_last_feats(anal):
    re_feats = re.compile("\[[^]]*\]")
    rvs = list()
    feats = re_feats.finditer(anal[0])
    for feat in feats:
        if 'BOUNDARY=' in feat.group(0) or 'WORD_ID=' in feat.group(0):
            rvs = list()
        else:
            rvs.append(feat.group(0))
    return rvs


def format_feats_ud(anal, hacks=None):
    feats = get_last_feats(anal)
    rvs = dict()
    for f in feats:
        key = f.split("=")[0].lstrip("[")
        value = f.split("=")[1].rstrip("]")
        if key == 'CASE':
            if value == 'LAT':
                # XXX: hack to retain compability
                rvs['Number'] = 'Sing'
            else:
                rvs['Case'] = value[0] + value[1:].lower()
        elif key == 'NUM':
            if value == 'SG':
                rvs['Number'] = 'Sing'
            elif value == 'PL':
                rvs['Number'] = 'Plur'
        elif key == 'TENSE':
            if 'PRESENT' in value:
                rvs['Tense'] = 'Pres'
            elif 'PAST' in value:
                rvs['Tense'] = 'Past'
        elif key == 'MOOD':
            if not hacks:
                rvs['VerbForm'] = 'Fin'
            if value == 'INDV':
                rvs['Mood'] = 'Ind'
            elif value == 'COND':
                rvs['Mood'] = 'Cnd'
            elif value == 'IMPV':
                rvs['Mood'] = 'Imp'
            else:
                rvs['Mood'] = value[0] + value[1:].lower()
        elif key == 'VOICE':
            if value == 'PSS':
                rvs['Voice'] = 'Pass'
            elif value == 'ACT':
                rvs['Voice'] = 'Act'
        elif key == 'PERS':
            if 'SG' in value:
                rvs['Number'] = 'Sing'
            elif 'PL' in value:
                rvs['Number'] = 'Plur'
            if '1' in value:
                rvs['Person'] = '1'
            elif '2' in value:
                rvs['Person'] = '2'
            elif '3' in value:
                rvs['Person'] = '3'
        elif key == 'POSS':
            if 'SG' in value:
                rvs['Number[psor]'] = 'Sing'
            elif 'PL' in value:
                rvs['Number[psor]'] = 'Plur'
            if '1' in value:
                rvs['Person[psor]'] = '1'
            elif '2' in value:
                rvs['Person[psor]'] = '2'
            elif '3' in value:
                rvs['Person[psor]'] = '3'
        elif key == 'NEG':
            if value == 'CON':
                rvs['Connegative'] = 'Yes'
                # XXX
                rvs.pop('Voice')
            elif value == 'NEG':
                rvs['Negative'] = 'Neg'
                if not hacks:
                    rvs['VerbForm'] = 'Fin'
        elif key == 'PCP':
            rvs['VerbForm'] = 'Part'
            if value == 'VA':
                rvs['PartForm'] = 'Pres'
            elif value == 'NUT':
                rvs['PartForm'] = 'Past'
            elif value == 'MA':
                rvs['PartForm'] = 'Agent'
            elif value == 'MATON':
                rvs['PartForm'] = 'Neg'
        elif key == 'INF':
            rvs['VerbForm'] = 'Inf'
            if value == 'A':
                rvs['InfForm'] = '1'
            elif value == 'E':
                rvs['InfForm'] = '2'
                # XXX
                rvs['Number'] = 'Sing'
            elif value == 'MA':
                rvs['InfForm'] = '3'
                # XXX
                rvs['Number'] = 'Sing'
            elif value == 'MINEN':
                rvs['InfForm'] = '4'
            elif value == 'MAISILLA':
                rvs['InfForm'] = '5'
        elif key == 'CMP':
            if value == 'SUP':
                rvs['Degree'] = 'Sup'
            elif value == 'CMP':
                rvs['Degree'] = 'Cmp'
            elif value == 'POS':
                rvs['Degree'] = 'Pos'
        elif key == 'SUBCAT':
            if value == 'NEG':
                rvs['Negative'] = 'Neg'
                if not hacks:
                    rvs['VerbForm'] = 'Fin'
            elif value == 'QUANTIFIER':
                rvs['PronType'] = 'Ind'
            elif value == 'REFLEXIVE':
                rvs['Reflexive'] = 'Yes'
            elif value in ['COMMA', 'DASH', 'QUOTATION', 'BRACKET']:
                # not annotated in UD feats:
                # * punctuation classes
                continue
            elif value in ['DECIMAL', 'ROMAN']:
                # not annotated in UD feats:
                # * decimal, roman NumType
                continue
            else:
                print("Unhandled subcat: ", value)
                print("in", anal[0][0])
                exit(1)
        elif key == 'ABBR':
            # XXX?
            rvs['Abbr'] = 'Yes'
        elif key == 'NUMTYPE':
            rvs['NumType'] = value[0] + value[1:].lower()
        elif key == 'PRONTYPE':
            rvs['PronType'] = value[0] + value[1:].lower()
        elif key == 'ADPTYPE':
            rvs['AdpType'] = value[0] + value[1:].lower()
        elif key == 'CLIT':
            rvs['Clitic'] = value[0] + value[1:].lower()
        elif key == 'FOREIGN':
            rvs['Foreign'] = value[0] + value[1:].lower()
        elif key == 'STYLE':
            if value in ['DIALECTAL', 'COLLOQUIAL']:
                rvs['Style'] = 'Coll'
            elif value == 'NONSTANDARD':
                # XXX: Non-standard spelling is kind of a typo?
                # e.g. seitsämän -> seitsemän
                rvs['Typo'] = 'Yes'
            elif value == 'ARCHAIC':
                rvs['Style'] = 'Arch'
            elif value == 'RARE':
                continue
            else:
                print("Unknown style", value)
                print("in", anal[0])
                exit(1)
        elif key in ['DRV', 'LEX']:
            if value in ['INEN', 'JA', 'LAINEN', 'LLINEN', 'MINEN', 'STI',
                         'TAR', 'TON', 'TTAA', 'TTAIN', 'U', 'VS']:
                # values found in UD finnish Derivs
                rvs['Derivation'] = value[0] + value[1:].lower()
            elif value in ['S', 'MAISILLA', 'VA', 'MATON', 'UUS',
                           'ADE', 'INE', 'ELA', 'ILL']:
                # valuse not found in UD finnish Derivs
                continue
            else:
                print("Unknown non-inflectional affix", key, '=', value)
                print("in", anal[0])
                exit(1)
        elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE',
                     'GUESS', 'PROPER', 'POSITION', 'SEM', 'CONJ']:
            # Not feats in UD:
            # * UPOS is another field
            # * Allomorphy is ignored
            # * Weight = no probabilities
            # * No feats for recasing
            # * FIXME: lexicalised inflection usually not a feat
            # * Guessering not a feat
            # * Proper noun classification not a feat
            # * punct sidedness is not a feat
            # * XXX: sem has not been used as a feat?
            # * special CONJ comparative is not used in UD
            continue
        else:
            print("Unhandled", key, '=', value)
            print("in", anal[0])
            exit(1)
    rv = ''
    for k, v in sorted(rvs.items()):
        rv += k + '=' + v + '|'
    if len(rvs) != 0:
        return rv.rstrip('|')
    else:
        return '_'


def format_third_ftb(anal):
    upos = get_last_feat("UPOS", anal)
    return upos


def format_third_tdt(upos):
    if upos in ['NOUN', 'PROPN']:
        return 'N'
    elif upos == 'ADJ':
        return 'A'
    elif upos in ['VERB', 'AUX']:
        return 'V'
    elif upos in ['CONJ', 'SCONJ']:
        return 'C'
    elif upos == 'ADP':
        return 'Adp'
    elif upos == 'ADV':
        return 'Adv'
    elif upos == 'PRON':
        return 'Pron'
    elif upos == 'PUNCT':
        return 'Punct'
    elif upos == 'SYM':
        return 'Symb'
    elif upos == 'INTJ':
        return 'Interj'
    elif upos == 'NUM':
        return 'Num'
    else:
        return 'X'


def get_upos(anal):
    upos = get_last_feat("UPOS", anal)
    drv = get_last_feat("DRV", anal)
    if upos == 'VERB' and drv == 'MINEN':
        upos = 'NOUN'
    return upos


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
    upos = get_last_feat("UPOS", anal)
    if not upos or upos == "":
        upos = 'X'
    if hacks == 'ftb':
        third = format_third_ftb(anal)
    else:
        third = format_third_tdt(upos)
    print(wordn, surf, "#".join(get_lemmas(anal)),
          upos,
          third,
          format_feats_ud(anal, hacks),
          "_", "_", "_", "_", sep="\t", file=outfile)


def main():
    """Invoke a simple CLI analyser."""
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAPATH',
                   help="Path to directory of HFST format automata")
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
    a.add_argument('--hacks', metavar='HACKS',
                   help="mangle anaelyses to match HACKS version of UD",
                   choices=['ftb'])
    a.add_argument('--debug', action='store_true',
                   help="print lots of debug info while processing")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.fsa:
        if options.verbose:
            print("reading language models in", options.fsa)
        omorfi.load_from_dir(options.fsa, analyse=True)
    else:
        if options.verbose:
            print("reading language models in default dirs")
        omorfi.load_from_dir()
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
    # statistics
    realstart = perf_counter()
    cpustart = process_time()
    tokens = 0
    unknowns = 0
    sentences = 0
    for line in options.infile:
        fields = line.strip().split('\t')
        if len(fields) == 10:
            # conllu is 10 field format
            tokens += 1
            try:
                index = int(fields[0])
            except ValueError:
                if '-' in fields[0]:
                    continue
                else:
                    print(
                        "Cannot figure out token index", fields[0], file=stderr)
                    exit(1)
            surf = fields[1]
            anals = omorfi.analyse(surf)
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
            if not anals or len(anals) == 0 or (len(anals) == 1 and
                                                'UNKNOWN' in anals[0][0]):
                unknowns += 1
        elif line.startswith('# doc-name:') or line.startswith('# sentence-text:'):
            # these comments I know need to be retained as-is
            print(line.strip(), file=options.outfile)
        elif line.startswith('#'):
            # unknown comment
            print(line.strip(), file=options.outfile)
            if options.verbose:
                print("Warning! Unrecognised comment line:", line, sep='\n')
        elif not line or line.strip() == '':
            # retain exactly 1 empty line between sents
            print(file=options.outfile)
            sentences += 1
        else:
            print("Error in conllu format:", line, sep='\n', file=stderr)
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
