#!/usr/bin/env -O python3
from omorfi import load_omorfi, omorfi_lookup
from glob  import glob
import re


#test_corpora_files = glob("*.text")
test_corpora_files = ["fast_test.notatext"]

lemma_freqs = dict()

def stat_word_ids(token, analyses):
    for analysis in analyses:
        for word_id in re.finditer(r"\[WORD_ID=([^]]*)\]", analysis.output):
            if not word_id.group(1) in lemma_freqs:
                lemma_freqs[word_id.group(1)] = 1
            else:
                lemma_freqs[word_id.group(1)] += 1

def main():
    omorfi = load_omorfi('../src/morphology.omor.hfst')
    test_corpora = list()
    for test_corpus_file in test_corpora_files:
        try:
            test_corpora.append(open(test_corpus_file))
        except IOError as ioe:
            print("Failed to open corpus ", test_corpus_file, ":", ioe)
    for test_corpus in test_corpora:
        for line in test_corpus:
            for token in line.split():
                analyses = omorfi_lookup(omorfi, token)
                stat_word_ids(token, analyses)
    for lemma in sorted(lemma_freqs, key=lemma_freqs.get):
        print(lemma, lemma_freqs[lemma], sep='\t')
    exit(0)

if __name__ == '__main__':
    main()
