#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CLI stuff
from sys import stderr, stdin, stdout
from argparse import ArgumentParser, FileType
# omorfi
from omorfi.omorfi import Omorfi
# statistics
from time import perf_counter, process_time
# string munging
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
    feats = re_feats.finditer(anal.output)
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
            if value == 'INDV':
                rvs['Mood'] = 'Ind'
            else:
                rvs['Mood'] = value[0] + value[1:].lower()
        elif key == 'VOICE':
            if value == 'PSS':
                rvs['Voice'] = 'Pass'
            elif value == 'ACT':
                rvs['Voice'] = 'Act'
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
                rvs['Degree'] = 'Sup'
            elif value == 'CMP':
                rvs['Degree'] = 'Cmp'
            elif value == 'POS':
                rvs['Degree'] = 'Pos'
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
                print("in", anal.output)
                exit(1)
        elif key in ['DRV', 'LEX']:
            if value in ['MINEN', 'STI']:
                rvs['Derivation'] = value[0] + value[1:].lower()
            elif value in ['TTAIN', 'foo']:
                continue
            else:
                print("Unknown non-inflectional affix", key, '=', value)
                print("in", anal.output)
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
            print("in", anal.output)
            exit(1)
    rv = ''
    for k,v in sorted(rvs.items()):
        rv += k + '=' + v + '|'
    if len(rvs) != 0:
        return rv.rstrip('|')
    else:
        return '_'

def format_upos_tdt(upos):
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

def try_analyses_conllu(original, wordn, surf, anals, outfile):
    for anal in anals:
        upos = get_last_feat("UPOS", anal)
        if upos == original[3]:
            feats = format_feats_ud(anal)
            if feats == original[5]:
                lemmas = "#".join(get_lemmas(anal))
                if lemmas == original[2]:
                    return print_analyses_conllu(wordn, surf, anal, outfile)
    # no exact match found (re-try without lemma)
    for anal in anals:
        upos = get_last_feat("UPOS", anal)
        if upos == original[3]:
            feats = format_feats_ud(anal)
            if feats == original[5]:
                return print_analyses_conllu(wordn, surf, anal, outfile)
    # and re-try without feats
    for anal in anals:
        upos = get_last_feat("UPOS", anal)
        if upos == original[3]:
            return print_analyses_conllu(wordn, surf, anal, outfile)
    return print_analyses_conllu(wordn, surf, anals[0], outfile)

def print_analyses_conllu(wordn, surf, anal, outfile):
    upos = get_last_feat("UPOS", anal)
    if not upos or upos == "":
        upos = 'X'
    print(wordn, surf, "#".join(get_lemmas(anal)), 
            upos, 
            format_upos_tdt(upos),
            format_feats_ud(anal),
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
            index = int(fields[0])
            surf = fields[1]
            anals = omorfi.analyse(surf)
            if options.oracle:
                try_analyses_conllu(fields, index, surf, anals, options.outfile)
            else:
                print_analyses_conllu(index, surf, anals[0], options.outfile)
            if len(anals) == 0 or (len(anals) == 1 and 
                    'UNKNOWN' in anals[0].output):
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
    print("CPU time:", cpuend-cpustart, "Real time:", realend-realstart,
            file=options.statfile)
    print("Tokens per timeunit:", tokens/(realend-realstart), 
            file=options.statfile)
    exit(0)

if __name__ == "__main__":
    main()
