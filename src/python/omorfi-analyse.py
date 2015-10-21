#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stderr, stdin, stdout
from argparse import ArgumentParser, FileType
from omorfi.omorfi import Omorfi

import re

def get_lemmas(anal):
    re_lemma = re.compile("\[WORD_ID=([^]]*)\]")
    lemmas = re_lemma.finditer(anal.output)
    rv = []
    for lemma in lemmas:
        rv += [lemma.group(1)]
    return rv

def get_last_feat(feat, anal):
    re_feat = re.compile("\[" + feat + "=([^]]*)\]")
    feats = re_feat.finditer(anal.output)
    rv = ""
    for feat in feats:
        rv = feat.group(1)
    return rv

def get_last_feats(anal):
    re_feats = re.compile("\[[^]]*\]")
    rvs = list()
    feats = re_feats.finditer(anal[0].output)
    for feat in feats:
        if 'BOUNDARY=' in feat.group(0) or 'WORD_ID=' in feat.group(0):
            rvs = list()
        else:
            rvs.append(feat.group(0))
    return rvs


def format_feats_ud(anal):
    feats = get_last_feats(anal)
    rvs = dict()
    for f in feats:
        key = f.split("=")[0].lstrip("[")
        value = f.split("=")[1].rstrip("]")
        if key == 'CASE':
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
            rvs['Mood'] = value[0] + value[1:].lower()
        elif key == 'VOICE':
            rvs['Voice'] = value[0] + value[1:].lower()
        elif key == 'PERS':
            rvs['VerbForm'] = 'Fin'
            if 'SG' in value:
                rvs['Number'] = 'Sing'
            elif 'PL' in value:
                rvs['Number'] = 'Sing'
            if '1' in value:
                rvs['Person'] = '1'
            elif '2' in value:
                rvs['Person'] = '2'
            elif '3' in value:
                rvs['Person'] = '3'
        elif key == 'POSS':
            rvs['VerbForm'] = 'Fin'
            if 'SG' in value:
                rvs['Number[psor]'] = 'Sing'
            elif 'PL' in value:
                rvs['Number[psor]'] = 'Sing'
            if '1' in value:
                rvs['Person[psor]'] = '1'
            elif '2' in value:
                rvs['Person[psor]'] = '2'
            elif '3' in value:
                rvs['Person[psor]'] = '3'
        elif key == 'NEG':
            if value == 'CON':
                rvs['Connegative'] = 'Yes'
            elif value == 'NEG':
                rvs['Negative'] = 'Yes'
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
            elif value == 'MA':
                rvs['InfForm'] = '3'
            elif value == 'MINEN':
                rvs['InfForm'] = '4'
            elif value == 'MAISILLA':
                rvs['InfForm'] = '5'
        elif key == 'CMP':
            if value == 'SUP':
                rvs['degree'] = 'Sup'
            elif value == 'CMP':
                rvs['degree'] = 'Cmp'
        elif key == 'SUBCAT':
            if value == 'NEG':
                rvs['Negative'] = 'Yes'
            elif value == 'QUANTIFIER':
                rvs['PronType'] = 'Ind'
            elif value in ['COMMA', 'DASH', 'QUOTATION', 'BRACKET']:
                # not annotated in UD feats: 
                # * punctuation classes
                continue
            elif value in ['REFLEXIVE', 'DECIMAL', 'ROMAN']:
                # not annotated in UD feats:
                # * reflexive PronType
                # * decimal, roman NumType
                continue
            else:
                print("Unhandled subcat: ", value)
                print("in", anal[0].output)
                exit(1)
        elif key == 'ABBR':
            rvs['Abbr'] = value[0] + value[1:].lower()
        elif key == 'NUMTYPE':
            rvs['NumType'] = value[0] + value[1:].lower()
        elif key == 'PRONTYPE':
            rvs['PronType'] = value[0] + value[1:].lower()
        elif key == 'CLIT':
            rvs['Clitic'] = value[0] + value[1:].lower()
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
                print("in", anal[0].output)
                exit(1)
        elif key in ['DRV', 'LEX']:
            if value in ['MINEN', 'STI']:
                rvs['Derivation'] = value[0] + value[1:].lower()
            elif value in ['TTAIN', 'foo']:
                continue
            else:
                print("Unknown non-inflectional affix", key, '=', value)
                print("in", anal[0].output)
                exit(1)
        elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE',
                'GUESS', 'PROPER', 'POSITION']:
            # Not feats in UD:
            # * UPOS is another field
            # * Allomorphy is ignored
            # * Weight = no probabilities
            # * No feats for recasing
            # * FIXME: lexicalised inflection usually not a feat
            # * Guessering not a feat
            # * Proper noun classification not a feat
            # * punct sidedness is not a feat
            continue
        else:
            print("Unhandled", key, '=', value)
            print("in", anal[0].output)
            exit(1)
    rv = ''
    for k,v in rvs.items():
        rv += k + '=' + v + '|'
    return rv.rstrip('|')

def format_upos_tdt(upos):
    if upos in ['NOUN', 'PROPN']:
        return 'N'
    elif upos == 'ADJ':
        return 'A'
    elif upos == 'VERB':
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
    else:
        return 'X'

def print_analyses(wordn, surf, anals, format, outfile):
    if format == 'xerox':
        print_analyses_xerox(surf, anals, outfile)
    elif format == 'apertium':
        print_analyses_apertium(surf, anals, outfile)
    elif format == 'vislcg3':
        print_analyses_vislcg3(surf, anals, outfile)
    elif format == 'conllx':
        print_analyses_conllx(wordn, surf, anals, outfile)
    elif format == 'conllu':
        print_analyses_conllu(wordn, surf, anals, outfile)
    else:
        print("format unknown:", format, file=stderr)
        exit(2)

def print_analyses_xerox(surf, anals, outfile):
    for anal in anals:
        print(surf, anal.output, sep='\t', file=outfile)
    print

def print_analyses_apertium(surf, anals, outfile):
    print("^", surf, sep='')
    for anal in anals:
        print("/", anal.output, sep='', file=outfile)
    print("$")

def print_analyses_vislcg3(surf, anals, outfile):
    print('"<', surf, '>"', sep='', file=outfile)
    re_lemma = re.compile("\[WORD_ID=([^]]*)\]")
    re_pos = re.compile("\[POS=([^]]*)\]")
    re_mrd = re.compile("\[([^=]*)=([^]]*)]")
    for anal in anals:
        pos_matches = re_pos.finditer(anal.output)
        pos = "UNK"
        mrds = []
        lemmas = []
        for pm in pos_matches:
            pos = pm.group(1)
        lemmas = get_lemmas(anal)
        mrd_matches = re_mrd.finditer(anal.output)
        for mm in mrd_matches:
            if mm.group(1) == 'WORD_ID':
                mrds = []
            elif mm.group(1) == 'CASECHANGE' and mm.group(2) != 'NONE':
                mrds = ['<' + mm.group(2) + '>'] + mrds
            elif mm.group(1) == 'ALLO':
                mrds = ['<' + mm.group(2) + '>'] + mrds
            elif mm.group(1) == 'WEIGHT' and mm.group(2) != 'inf':
                    mrds += ['<W=' + str(int(float(mm.group(2)) * 100)) + '>']
            elif mm.group(1) == 'WEIGHT' and mm.group(2) == 'inf':
                    mrds += ['<W=65536>']
            elif mm.group(1) in ['STYLE']:
                mrds += ['<' + mm.group(2) + '>']
            else:
                mrds += [mm.group(2)]
        print('\t"', ''.join(lemmas).replace('"', '\\"'), '" ',
                ' '.join(mrds), sep='', file=outfile)
    print(file=outfile)

def print_analyses_conllx(wordn, surf, anals, outfile):
    print(wordn, surf, "#".join(get_lemmas(anals[0])),
            "-", "-", anals[0].output,
            "-", "-", "-", "-", sep="\t", file=outfile)

def print_analyses_conllu(wordn, surf, anals, outfile):
    print(wordn, surf, "#".join(get_lemmas(anals[0])), 
            get_last_feat("UPOS", anals[0]), 
            format_upos_tdt(get_last_feat("UPOS", anals[0])),
            format_feats_ud(anals),
            "-", "-", "-", "-", sep="\t", file=outfile)

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
    a.add_argument('-F', '--format', metavar='FORMAT', required=True,
            help="Output in format compatible with FORMAT",
            choices=['xerox', 'apertium', 'vislcg3', 'conllx', 'conllu'])
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.fsa:
        if options.verbose:
            print("reading language models in", options.fsa)
        omorfi.load_from_dir(options.fsa, analyse=True, accept=True)
    else:
        if options.verbose:
            print("reading language models in default dirs")
        omorfi.load_from_dir()
    if not options.infile:
        options.infile = stdin
    if options.verbose:
        print("analysing", options.infile.name)
    if not options.outfile:
        options.outfile = stdout
    if options.verbose:
        print("writing to", options.outfile.name)
    for line in options.infile:
        line = line
        if not line or line == '':
            continue
        surfs = omorfi.tokenise(line)
        i = 0
        if options.format == 'conllu':
            print("# sentence-text: ", line.strip(), file=options.outfile)
        for surf in surfs:
            i += 1
            anals = omorfi.analyse(surf)
            print_analyses(i, surf, anals, options.format, options.outfile)
        if options.format in ['conllx', 'conllu']:
            print(file=options.outfile)
    exit(0)

if __name__ == "__main__":
    main()
