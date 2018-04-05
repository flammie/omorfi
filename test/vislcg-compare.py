#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare two conllu files for matches on each field.
"""


from argparse import ArgumentParser, FileType
from sys import stderr


def main():
    a = ArgumentParser()
    a.add_argument('-H', '--hypothesis', metavar="HYPFILE", type=open, required=True,
                   dest="hypfile", help="analysis results")
    a.add_argument('-r', '--reference', metavar="REFFILE", type=open,
                   required=True,
                   dest="reffile", help="reference data")
    a.add_argument('-l', '--log', metavar="LOGFILE", required=True,
                   type=FileType('w'),
                   dest="logfile", help="result file")
    a.add_argument('-X', '--realign', action="store_true", default=False,
                   help="Allow fuzzy matches if tokenisation differs")
    a.add_argument('-v', '--verbose', action="store_true", default=False,
                   help="Print verbosely while processing")
    a.add_argument('-t', '--thresholds', metavar='THOLDS', default=99, type=int,
                   help="require THOLD % for lemma, UPOS and UFEAT or exit 1 (for testing)")
    options = a.parse_args()
    #
    lines = 0
    tokens = 0
    hypotheses = 0
    # count this
    lemmas_miss = 0
    lemmas_miss_total = 0
    lemmas_match = 0
    lemmas_match_total = 0
    tags_miss = 0
    tags_miss_total = 0
    tags_match = 0
    tags_match_total = 0
    compounding_fails = 0
    hypline = False
    in_hyps = False
    for refline in options.reffile:
        lines += 1
        refline = refline.rstrip()
        if not refline or refline == '':
            continue
        elif refline.startswith("#") or refline.startswith("<"):
            continue
        elif refline.startswith('"<') and refline.endswith('>"'):
            refsurf = refline[2:-2]
            continue
        elif refline.startswith(';'):
            continue
        elif refline.startswith('\t"'):
            refs = refline.strip().split()
            reflemma = refs[0][1:-1]
            reftags = refs[1:]
            reftags = list(filter(lambda x: '<' not in x, reftags))
            tokens += 1
        else:
            print("Unparsable in reference:", refline, file=stderr)
            exit(2)
        hyps_done = False
        lemma_found = False
        tags_found = False
        lemma_hyps = []
        tag_hyps = []
        while not hyps_done:
            try:
                hypline = next(options.hypfile)
                hypline = hypline.rstrip()
            except StopIteration:
                hyps_done = True
            if not hypline or hypline == '':
                pass
            elif hypline.startswith('"<') and hypline.endswith('>"'):
                if not in_hyps:
                    in_hyps = True
                else:
                    hyps_done = True
            elif hypline.startswith("#") or hypline.startswith("<"):
                pass
            elif hypline.startswith(';'):
                pass
            elif hypline.startswith('\t'):
                hyps = hypline.strip().split()
                hyplemma = hyps[0][1:-1]
                hyptags = hyps[1:]
                hyptags = list(filter(lambda x : '<' not in x, hyptags))
                hypotheses += 1
                if hyplemma == reflemma:
                    lemmas_match_total += 1
                    lemma_found = True
                elif hyplemma.replace('#', '') == reflemma.replace('#', ''):
                    lemmas_match_total += 1
                    lemma_found = True
                    compounding_fails += 1
                else:
                    lemmas_miss_total += 1
                lemma_hyps += [hyplemma]
                mismatch = False
                for reftag in reftags:
                    if reftag.startswith('<') and reftag.endswith('>'):
                        continue
                    if ':' in reftag or '=' in reftag:
                        continue
                    tagmatched = False
                    for hyptag in hyptags:
                        if hyptag == reftag:
                            tagmatched = True
                            break
                    if not tagmatched:
                        mismatch = True
                        break
                tag_hyps += [set(hyptags)]
                if mismatch:
                    tags_miss_total += 1
                else:
                    tags_match_total += 1
                    tags_found = True
            else:
                print("Unparsable in hyps:", hypline, file=stderr)
                exit(2)
        if lemma_found:
            lemmas_match += 1
            print("LEMMAOK", reflemma, file=options.logfile)
        else:
            lemmas_miss += 1
            print("LEMMAMISS", reflemma, '(', reftags, ')', refsurf,
                  'HYPS:', lemma_hyps, file=options.logfile)
        if tags_found:
            tags_match += 1
            print("TAGOK", reftags, file=options.logfile)
        else:
            tags_miss += 1
            print("TAGMISS", reftags, '(', reflemma, ')', refsurf,
                  'HYPS:', tag_hyps, file=options.logfile)
    print("Metric\\Stuff", "Tokens", "Lemmas", "Taglists", sep="\t")
    print("Freq", tokens, lemmas_match, tags_match, sep="\t")
    print("Rec", tokens / tokens * 100,
          (lemmas_match) / tokens * 100,
          (tags_match) / tokens * 100, sep='\t')
    print("Freq", hypotheses, lemmas_match_total, tags_match_total, sep="\t")
    print("Pr", hypotheses / hypotheses * 100,
          (lemmas_match_total) / hypotheses * 100,
          (tags_match_total) / hypotheses * 100, sep='\t')
    print("Lemmas with mismatched #'s:", compounding_fails, "(",
          compounding_fails / tokens * 100, "%)")
    print("Ambiguity left:", hypotheses / tokens)
    if tokens == 0 or \
            ((lemmas_match / tokens * 100) < options.thresholds) or\
            ((tags_match / tokens * 100) < options.thresholds):
        print("needs to have", options.thresholds,
              "% matches to pass regress test\n",
              file=stderr)
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
