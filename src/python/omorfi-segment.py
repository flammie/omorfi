#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import stderr, stdin, stdout

from omorfi import Omorfi


def print_moses_factor_segments(token, outfile, options):
    labelsegments = None
    for anal in token.labelsegmentations:
        if anal.rawtype == "labelsegments":
            labelsegments = anal
            break
    if not labelsegments:
        print("Missing labelsegments for token", token, file=stderr)
        exit(1)
    segs = labelsegments.get_moses_factor_segments()
    print(options.segment_marker.join(segs), end=' ', file=outfile)


def print_segments(token, outfile, options):
    if options.show_ambiguous:
        sep = ''
        for segmenteds in token.segmentations:
            print(sep, end='', file=outfile)
            print(options.segment_marker.join(
                segmenteds.get_segments(
                    options.split_morphs, options.split_words,
                    options.split_new_words, options.split_derivs,
                    options.split_nonwords)),
                  end='', file=outfile)
            sep = options.show_ambiguous
    else:
        segmented = None
        for anal in token.segmentations:
            if anal.rawtype == "segments":
                segmented = anal
                break
        if not segmented:
            print("Missing segments for token", file=stderr)
            exit(1)
        print(options.segment_marker.join(
            segmented.get_segments(
                options.split_morphs, options.split_words,
                options.split_new_words, options.split_derivs,
                options.split_nonwords)),
              end='', file=outfile)
    print(' ', end='', file=outfile)


def main():
    """Segment text in some formats."""
    a = ArgumentParser()
    a.add_argument('-s', '--segmenter', metavar='SFILE',
                   help="load segmenter from SFILE", required=True)
    a.add_argument('-S', '--labeller', metavar='LSFILE',
                   help="load labelsegmenter from LSFILE", required=True)
    a.add_argument('-i', '--input', metavar="INFILE", type=open,
                   dest="infile", help="source of analysis data")
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    a.add_argument('-o', '--output', metavar="OUTFILE",
                   help="print segments into OUTFILE")
    a.add_argument('-O', '--output-format', metavar="OFORMAT",
                   help="format output suitable for OFORMAT",
                   required=True,
                   choices=["moses-factors", "segments"])
    a.add_argument('--no-split-words', action="store_false", default=True,
                   dest="split_words",
                   help="split on word boundaries")
    a.add_argument('--no-split-new-words', action="store_false", default=True,
                   dest="split_new_words",
                   help="split on new word boundaries " +
                   "(prev. unattested compounds)")
    a.add_argument('--no-split-morphs', action="store_false", default=True,
                   dest="split_morphs",
                   help="split on morph boundaries")
    a.add_argument('--split-derivs', action="store_true", default=False,
                   help="split on derivation boundaries")
    a.add_argument('--split-nonwords', action="store_true", default=False,
                   help="split on other boundaries")
    a.add_argument('--segment-marker', default='→ ←', metavar='SEG',
                   help="mark segment boundaries with SEG")
    a.add_argument('--show-ambiguous', default=False, metavar='ASEP',
                   help="separate ambiguous segmentations with SEG")
    options = a.parse_args()
    omorfi = Omorfi(options.verbose)
    if options.segmenter:
        if options.verbose:
            print("Reading segmenter", options.segmenter)
        omorfi.load_segmenter(options.segmenter)
    else:
        print("segmenter is needed for segmenting", file=stderr)
        exit(2)
    if options.labeller:
        if options.verbose:
            print("Reading labelsegmenter", options.labeller)
        omorfi.load_labelsegmenter(options.labeller)
    if not omorfi.can_segment or not omorfi.can_labelsegment:
        print("Could not load segmenter(s), re-compile them or use -f option")
        print()
        print("To compile segmenter, use --enable-segmenter, and/or",
              "--enable-labeled-segments")
        exit(1)
    if options.infile:
        infile = options.infile
    else:
        options.infile = stdin
        infile = stdin
    if options.output:
        outfile = open(options.output, 'w')
    else:
        options.output = "<stdout>"
        outfile = stdout
    if options.segment_marker is None:
        if options.verbose:
            print("Default segment marker is → ←")
        options.segment_marker = '→ ←'
    if options.verbose:
        print("reading from", options.infile.name)
    if options.verbose:
        print("writign to", options.output)

    linen = 0
    for line in infile:
        line = line.strip()
        linen += 1
        if options.verbose and linen % 10000 == 0:
            print(linen, '...')
        if not line or line == '':
            print(file=outfile)
            continue
        tokens = omorfi.tokenise(line)
        for token in tokens:
            omorfi.segment(token)
            omorfi.labelsegment(token)
            if options.output_format == 'moses-factors':
                print_moses_factor_segments(token, outfile, options)
            elif options.output_format == 'segments':
                print_segments(token, outfile, options)
        print(file=outfile)
    exit(0)


if __name__ == "__main__":
    main()
