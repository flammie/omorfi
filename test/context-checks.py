#!/usr/bin/env -O python3
from omorfi import load_omorfi, omorfi_lookup
from glob  import glob
from sys import stdout, argv
import re
import gc

previous = list()
sent = list()
max_window_size = 256

adposition_complements = dict()
adposition_complement_cases = ['CASE=GENITIVE', 'CASE=PARTITIVE']

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
        print("ERROR! Too long sentence chopped:", end='')
        for coh in sent[:50]:
            for tag in coh:
                if tag.startswith("SURF="):
                    print(tag[len("SURF="):], end=' ')
        parse_sentence()
        sent = list()
        previous = list()
        gc.collect()

def extract_word_ids(word_pos):
    word_ids = ''
    for tag in sent[word_pos]:
        if tag.startswith('WORD_ID'):
            word_ids += tag[len('WORD_ID='):] + '/'
    return word_ids

def extract_surf(word_pos):
    for tag in sent[word_pos]:
        if tag.startswith("SURF"):
            return tag[len("SURF="):]

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
        if 'POSS=1STSINGULAR' in sent[word_pos] or 'POSS=2NDSINGULAR' in sent[word_pos] or 'POSS=3RDAMBIGUOUS' in sent[word_pos] or 'POSS=2NDPLURAL' in sent[word_pos] or 'POSS=1STPLURAL' in sent[word_pos]:
            if not 'poss' in apdposition_complements[word]:
                adposition_complements[word]['poss'] = 1
            else:
                adposition_complements[word]['poss'] += 1
            comp_found = True
        if not comp_found:
            if not 'none' in adposition_complements[word]:
                adposition_complements[word]['none'] = 1
            else:
                adposition_complements[word]['none'] += 1

def parse_sentence():
    for word_pos in range(len(sent)):
        if 'SUBCAT=ADPOSITION' in sent[word_pos]:
            context_adposition_complement(word_pos)

def test_adposition_complements(logfile):
    for lemma, comps in adposition_complements.items():
        if not 'left' in comps and not 'right' in comps:
            print("ERROR! no comps for", lemma, file=logfile)
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
                print("ERROR! mostly no comps for", lemma, file=logfile)

def print_adposition_stats(logfile):
    for lemma, comps in adposition_complements.items():
        totals = 0
        lefts = 0
        rights = 0
        nones = 0
        if 'left' in comps:
            for case in adposition_complements[lemma]['left']:
                lefts += adposition_complements[lemma]['left'][case]
        if 'right' in comps:
            for case in adposition_complements[lemma]['right']:
                rights += adposition_complements[lemma]['right'][case]
        if 'none' in comps:
            nones += adposition_complements[lemma]['none']
        totals = lefts + rights + nones
        print(lemma, lefts/totals, nones/totals, rights/totals, totals,
                file=logfile, sep='\t')

def main():
    if len(argv) > 1 and argv[1] == 'debug':
        test_corpora_files = ["fast_test.notatext"]
    else:
        test_corpora_files = glob("*.text")
    adposition_log = open('adposition_complements.log', 'w')
    adposition_stats = open('adposition_complements_full.log', 'w')
    omorfi = load_omorfi('../src/morphology.omor.hfst')
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
                #print(token)
                analyses = omorfi_lookup(omorfi, token)
                add_to_sent(analyses, token)
        print("Flushing! because this is too memory intensive")
        previous = list()
        sent = list()
        omorfi = None
        omorfi = load_omorfi('../src/morphology.omor.hfst')
        gc.collect()
    test_adposition_complements(adposition_log)
    print_adposition_stats(adposition_stats)
    exit(0)

if __name__ == '__main__':
    main()
