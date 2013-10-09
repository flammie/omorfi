#!/usr/bin/env -O python3
from omorfi import Omorfi
from glob  import glob
from sys import stdout, argv
import re
import gc

from argparse import ArgumentParser, FileType

# context list
previous = list()
sent = list()
max_window_size = 256

adjective_agreements = dict()
adposition_complements = dict()
adposition_complement_cases = ['CASE=GENITIVE', 'CASE=PARTITIVE', \
        'CASE=ELATIVE', 'CASE=ILLATIVE', 'CASE=ALLATIVE', 'CASE=ABLATIVE']

# contextless
whitelist_props = True
lemma_freqs = dict()
lemmas = set()
tsv_borked = True # while is_proper fails?

nominal_case_freqs = dict()
nominal_case_freqs_per_lemma = dict()

adjective_comps_per_lemma = dict()

# background information

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

# context parsing

def add_to_sent(analyses, surf):
    global sent
    tags = set()
    for analysis in analyses:
        parts = analysis.output.split('][')
        for part in parts:
            tag = part.rstrip(']').lstrip('[')
            tags.add(tag)
        tags.add("SURF=" + surf)
    sent.append(tags)
    if 'BOUNDARY=SENTENCE' in tags:
        parse_sentence()
        previous = sent
        sent = list()
        gc.collect()
    elif len(sent) >= max_window_size:
        print("ERROR! Too long sentence skipped from start:")
        for coh in sent[:20]:
            for tag in coh:
                if tag.startswith("SURF="):
                    print(tag[len("SURF="):], end=' ')
        print('restarting at [...]:')
        for tag in sent[-1]:
            if tag.startswith("SURF="):
                print(tag[len("SURF="):])
        sent = list()
        previous = list()
        gc.collect()

# analysis mangling

def harvest_word_ids(analysis):
    word_ids = re.search(r"\[WORD_ID=([^]]*)\]", analysis.output)
    return "#".join(word_ids.groups())

def extract_word_ids(word_pos):
    word_ids = ''
    for tag in sent[word_pos]:
        if tag.startswith('WORD_ID'):
            word_ids += tag[len('WORD_ID='):] + '/'
    return word_ids

def extract_surf(word_pos):
    return extract_tag(word_pos, 'SURF=')[len('SURF='):]

def extract_tag(word_pos, tagstart):
    for s in sent[word_pos]:
        if s.startswith(tagstart):
            return s

# contextless statistics

def stat_word_ids(token, analyses):
    for analysis in analyses:
        for word_id in re.finditer(r"\[WORD_ID=([^]]*)\]", analysis.output):
            if not word_id.group(1) in lemma_freqs:
                lemma_freqs[word_id.group(1)] = 1
            else:
                lemma_freqs[word_id.group(1)] += 1



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

# context checks

def context_adjective_agreement(word_pos):
    word = extract_surf(word_pos)
    if not word in adjective_agreements:
        adjective_agreements[word] = dict()
    case = extract_tag(word_pos, 'CASE=')
    comp_found = False
    if 'SUBCAT=ADJECTIVE' in sent[word_pos]:
        if word_pos < len(sent) - 1:
            #right_word = extract_word_ids(word_pos + 1)
            if 'POS=NOUN' in sent[word_pos + 1] and case in sent[word_pos + 1]:
                if not 'right' in adjective_agreements[word]:
                    adjective_agreements[word]['right'] = 1
                else:
                    adjective_agreements[word]['right'] += 1
            else:
                if not 'none' in adjective_agreements[word]:
                    adjective_agreements[word]['none'] = 1
                else:
                    adjective_agreements[word]['none'] += 1

def context_adposition_complement(word_pos):
    word = extract_surf(word_pos)
    if not word in adposition_complements:
        adposition_complements[word] = dict()
    comp_found = False
    if 'SUBCAT=ADPOSITION' in sent[word_pos]:
        if word_pos > 0:
            #left_word = extract_word_ids(word_pos - 1)
            for case in adposition_complement_cases:
                if 'POS=NOUN' in sent[word_pos - 1] and case in sent[word_pos - 1]:
                    if not 'left' in adposition_complements[word]:
                        adposition_complements[word]['left'] = dict()
                        adposition_complements[word]['left'][case] = 1
                    elif not case in adposition_complements[word]['left']:
                        adposition_complements[word]['left'][case] = 1
                    else:
                        adposition_complements[word]['left'][case] += 1
                    comp_found = True
        if word_pos < len(sent) - 1:
            #right_word = extract_word_ids(word_pos + 1)
            for case in adposition_complement_cases:
                if 'POS=NOUN' in sent[word_pos + 1] and case in sent[word_pos + 1]:
                    if not 'right' in adposition_complements[word]:
                        adposition_complements[word]['right'] = dict()
                        adposition_complements[word]['right'][case] = 1
                    elif not case in adposition_complements[word]['right']:
                        adposition_complements[word]['right'][case] = 1
                    else:
                        adposition_complements[word]['right'][case] += 1
                    comp_found = True
        if 'POSSESSIVE=1STSINGULAR' in sent[word_pos] or 'POSSESSIVE=2NDSINGULAR' in sent[word_pos] or 'POSSESSIVE=3RDAMBIGUOUS' in sent[word_pos] or 'POSSESSIVE=2NDPLURAL' in sent[word_pos] or 'POSSESSIVE=1STPLURAL' in sent[word_pos]:
            if not 'poss' in adposition_complements[word]:
                adposition_complements[word]['poss'] = 1
            else:
                adposition_complements[word]['poss'] += 1
            comp_found = True
        if not comp_found:
            if not 'none' in adposition_complements[word]:
                adposition_complements[word]['none'] = 1
            else:
                adposition_complements[word]['none'] += 1

# all context tests per word
def parse_sentence():
    for word_pos in range(len(sent)):
        if 'SUBCAT=ADPOSITION' in sent[word_pos]:
            context_adposition_complement(word_pos)
        elif 'SUBCAT=ADJECTIVE' in sent[word_pos]:
            context_adjective_agreement(word_pos)

# post-processing statistic mangling (short logs, simple)

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



def test_adposition_complements(logfile):
    for lemma, comps in adposition_complements.items():
        if not 'left' in comps and not 'right' in comps:
            print(lemma, "0 complements", file=logfile)
        biggest = 0
        if 'left' in comps:
            lefts = 0
            for case in adposition_complements[lemma]['left']:
                lefts += adposition_complements[lemma]['left'][case]
            biggest = lefts
        if 'right' in comps:
            rights = 0
            for case in adposition_complements[lemma]['right']:
                lefts += adposition_complements[lemma]['right'][case]
            if rights > biggest:
                biggest = rights
        if 'none' in comps and ('right' in comps or 'left' in comps):
            if adposition_complements[lemma]['none'] > biggest:
                print(lemma, biggest, "with complements", adposition_complements[lemma]['none'], "without", file=logfile)

def test_adjective_agreements(logfile):
    for lemma, comps in adjective_agreements.items():
        if not 'right' in comps:
            print(lemma, "without agreeing NPs", file=logfile)
        elif 'none' in comps and 'right' in comps:
            if adjective_agreements[lemma]['right'] < adjective_agreements[lemma]['none']:
                print(lemma, adjective_agreements[lemma]['right'], "agreements",
                        adjective_agreeements[lemma]['none'], 'without',
                        file=logfile)

# long logs

def print_adposition_stats(logfile):
    print("surcface", "left", "poss", "right", "none", "total", sep='\t',
            file=logfile)
    for lemma, comps in adposition_complements.items():
        totals = {'all': 0}
        lefts = {'all': 0}
        poss = 0
        rights = {'all': 0}
        nones = 0
        for case in adposition_complement_cases:
            totals[case] = 0
            lefts[case] = 0
            rights[case] = 0
        if 'left' in comps:
            for case in adposition_complements[lemma]['left']:
                lefts['all'] += adposition_complements[lemma]['left'][case]
                totals[case] += adposition_complements[lemma]['left'][case]
                lefts[case] = adposition_complements[lemma]['left'][case]
        if 'right' in comps:
            for case in adposition_complements[lemma]['right']:
                rights['all'] += adposition_complements[lemma]['right'][case]
                totals[case] += adposition_complements[lemma]['right'][case]
                rights[case] = adposition_complements[lemma]['right'][case]
        if 'poss' in comps:
            poss += adposition_complements[lemma]['poss']
        if 'none' in comps:
            nones += adposition_complements[lemma]['none']
        totals['all'] = lefts['all'] + poss + rights['all'] + nones
        print(lemma,
                lefts['all'], poss, rights['all'], nones, totals['all'],
                file=logfile, sep='\t')
        print(lemma, 
                "%.2f %%" % (lefts['all'] / totals['all'] * 100), 
                "%.2f %%" % (poss / totals['all'] * 100), 
                "%.2f %%" % (rights['all'] / totals['all'] * 100),
                "%.2f %%" % (nones / totals['all'] * 100), 
                "%.2f %%" % (totals['all'] / totals['all'] * 100),
                file=logfile, sep='\t')
        for case in adposition_complement_cases:
            if totals[case] > 0:
                print("%s %s" %(lemma, case),
                        lefts[case], "–", rights[case], "–", totals[case],
                        file=logfile, sep='\t')
                print("%s %s %%" %(lemma, case), 
                        "%.2f %%" % (lefts[case] / totals[case] * 100), 
                        "–", 
                        "%.2f %%" % (rights[case] / totals[case] * 100),
                        "–", 
                        "%.2f %%" % (totals[case] / totals[case] * 100),
                        file=logfile, sep='\t')

# statistiscs for use in analysers etc.

def print_lemma_stats(statfile):
    for lemma in sorted(lemma_freqs, key=lemma_freqs.get):
        print(lemma, lemma_freqs[lemma], sep='\t', file=statfile)

def print_case_stats(statfile):
    for case, freq in nominal_case_freqs.items():
        print(case, freq, sep='\t', file=statfile)


# main loop

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
    # hard-coded logs for now
    lemma_log = open('missing_word_ids.log', 'w')
    case_log = open('missing_nominal_cases.log', 'w')
    comp_log = open('missing_comparatives.log', 'w')
    adposition_log = open('adposition_complements.log', 'w')
    adposition_stats = open('adposition_complements_full.log', 'w')
    adjective_log = open('adjective_agreements.log', 'w')
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
            if (linen % 1000000) == 0:
                print(linen, "...! Time to reload everything because memory is leaking very badly indeed!")
                previous = list()
                sent = list()
                omorfi = None
                omorfi = Omorfi()
                omorfi.load_filename(opts.fsa)
                gc.collect()

            if (linen % 10000) == 0:
                print(linen, "...")
            for punct in ".,:;?!()":
                line = line.replace(punct, " " + punct + " ")
            for token in line.split():
                analyses = omorfi.analyse(token)
                add_to_sent(analyses, token)
                stat_word_ids(token, analyses)
                stat_nominal_cases(token, analyses, case_log)
                stat_adjective_comps(token, analyses, comp_log)
    test_zero_lemmas(lemma_log) 
    test_zero_cases(case_log)
    test_zero_comps(comp_log)
    #test_case_deviations()
    test_adposition_complements(adposition_log)
    print_adposition_stats(adposition_stats)
    test_adjective_agreements(adjective_log)
    print_lemma_stats(open('../src/probabilistics/lemmas.freqs', 'w'))
    print_case_stats(open('../src/probabilistics/cases.freqs', 'w'))
    exit(0)

if __name__ == '__main__':
    main()
