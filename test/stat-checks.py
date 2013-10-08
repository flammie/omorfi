#!/usr/bin/env -O python3
from omorfi import Omorfi
from glob  import glob
from sys import stdout, argv
import re

from argparse import ArgumentParser, FileType

whitelist_props = True
lemma_freqs = dict()
lemmas = set()
tsv_borked = True # while is_proper fails?

nominal_case_freqs = dict()
nominal_case_freqs_per_lemma = dict()

adjective_comps_per_lemma = dict()

def gather_lemmas(master_tsv):
    for line in master_tsv:
        fields = line.split('\t')
        if len(fields) < 16:
            continue
        if whitelist_props and fields[10] == 'True':
            continue
        elif whitelist_props and fields[0][0].isupper() and tsv_borked:
            continue
        else:
            lemmas.add(fields[0])

def stat_word_ids(token, analyses):
    for analysis in analyses:
        for word_id in re.finditer(r"\[WORD_ID=([^]]*)\]", analysis.output):
            if not word_id.group(1) in lemma_freqs:
                lemma_freqs[word_id.group(1)] = 1
            else:
                lemma_freqs[word_id.group(1)] += 1

def harvest_word_ids(analysis):
    word_ids = re.search(r"\[WORD_ID=([^]]*)\]", analysis.output)
    return "#".join(word_ids.groups())

def stat_nominal_cases(token, analyses, logfile):
    for analysis in analyses:
        if '[POS=NOUN]' in analysis.output:
            word_id = harvest_word_ids(analysis)
            case = re.search(r"\[CASE=([^]]*)\]", analysis.output)
            if not case:
                print("ERROR! missing case in", token, analysis.output, 
                        file=logfile)
                continue
            if not case.group(1) in nominal_case_freqs:
                nominal_case_freqs[case.group(1)] = 1
            else:
                nominal_case_freqs[case.group(1)] += 1
            if not word_id in nominal_case_freqs_per_lemma:
                nominal_case_freqs_per_lemma[word_id] = dict()
            if not case.group(1) in nominal_case_freqs_per_lemma:
                nominal_case_freqs_per_lemma[word_id][case.group(1)] = 1
            else:
                nominal_case_freqs_per_lemma[word_id][case.group(1)] += 1

def stat_adjective_comps(token, analyses, logfile):
    for analysis in analyses:
        if '[SUBCAT=ADJECTIVE]' in analysis.output:
            word_id = harvest_word_ids(analysis)
            comp = re.search(r"\[COMPARISON=([^]]*)\]", analysis.output)
            if not comp:
                print("ERROR! missing comp in", token, analysis.output,
                        file=logfile)
                continue
            if not word_id in adjective_comps_per_lemma:
                adjective_comps_per_lemma[word_id] = dict()
            if not comp.group(1) in adjective_comps_per_lemma:
                adjective_comps_per_lemma[word_id][comp.group(1)] = 1
            else:
                adjective_comps_per_lemma[word_id][comp.group(1)] += 1

def test_zero_lemmas(logfile):
    for lemma in lemmas - lemma_freqs.keys():
        print("WARNING! word not in:", lemma, file=logfile)

def test_zero_cases(logfile):
    cases = nominal_case_freqs.keys()
    for lemma in nominal_case_freqs_per_lemma:
        for case in cases - nominal_case_freqs_per_lemma[lemma].keys():
            print("WARNING!", lemma, "without", case, file=logfile)
        if len(nominal_case_freqs_per_lemma[lemma].keys()) == 1 and \
                'NOMINATIVE' in nominal_case_freqs_per_lemma[lemma]:
            print("ERROR!", lemma, "without inflectional cases, consider PARTICLE", file=logfile)

def test_zero_comps(logfile):
    for lemma in adjective_comps_per_lemma.keys():
        if not '[COMPARISON=COMPARATIVE]' in adjective_comps_per_lemma[lemma]:
            print("WARNING!", lemma, "missing comparative forms", file=logfile)
        if not '[COMPARISON=SUPERLATIVE]' in adjective_comps_per_lemma[lemma]:
            print("WARNING!", lemma, "missing superlative", file=logfile)
        if not '[COMPARISON=COMPARATIVE]' in adjective_comps_per_lemma[lemma] \
                and not '[COMPARISON=SUPERLATIVE]' in adjective_comps_per_lemma[lemma]:
            print("ERROR!", lemma, "has no comparison, consider NOUN", file=logfile)

def print_lemma_stats(statfile):
    for lemma in sorted(lemma_freqs, key=lemma_freqs.get):
        print(lemma, lemma_freqs[lemma], sep='\t', file=statfile)

def print_case_stats(statfile):
    for case, freq in nominal_case_freqs.items():
        print(case, freq, sep='\t', file=statfile)

def main():
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAFILE', required=True,
            help="HFST's optimised lookup binary data for the transducer to be applied")
    a.add_argument('-i', '--input', metavar="INFILE", type=str, required=True,
            dest="infile", help="source of analysis data")
    a.add_argument('-m', '--master', metavar="TSVFILE", type=str, required=True,
            dest="tsvfile", help="source of existing lexical data")
    opts = a.parse_args()
    if opts.infile:
        test_corpora_files = [opts.infile]
    else:
        test_corpora_files = glob("*.text")
    
    lemma_log = open('missing_word_ids.log', 'w')
    case_log = open('missing_nominal_cases.log', 'w')
    comp_log = open('missing_comparatives.log', 'w')
    omorfi = Omorfi()
    omorfi.load_filename(opts.fsa)
    gather_lemmas(open(opts.tsvfile))
    test_corpora = list()
    for test_corpus_file in test_corpora_files:
        try:
            test_corpora.append(open(test_corpus_file))
        except IOError as ioe:
            print("Failed to open corpus ", test_corpus_file, ":", ioe)
    for test_corpus in test_corpora:
        print('lines from', test_corpus)
        linen = 0
        for line in test_corpus:
            linen += 1
            if (linen % 10000) == 0:
                print(linen, "...")
            for punct in ".,:;?!()":
                line = line.replace(punct, " " + punct)
            for token in line.split():
                analyses = omorfi.analyse(token)
                stat_word_ids(token, analyses)
                stat_nominal_cases(token, analyses, case_log)
                stat_adjective_comps(token, analyses, comp_log)
    test_zero_lemmas(lemma_log) 
    test_zero_cases(case_log)
    test_zero_comps(comp_log)
    #test_case_deviations()
    print_lemma_stats(open('../src/probabilistics/lemmas.freqs', 'w'))
    print_case_stats(open('../src/probabilistics/cases.freqs', 'w'))
    exit(0)

if __name__ == '__main__':
    main()
