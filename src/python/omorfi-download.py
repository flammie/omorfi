#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A command-line utility to fetch released omorfi language models.

Mainly a helper for pip package, normal users can use the bash version
`omorfi-download.bash`, which I think is easier and better. 57 % of this
script was yoinked from Turku NLP's neural parser pipeline:

https://github.com/TurkuNLP/Turku-neural-parser-pipeline/blob/master/fetch_models.py
"""

# string munging
from argparse import ArgumentParser, FileType
# CLI stuff
from sys import stderr, stdin, stdout
# statistics
from time import perf_counter, process_time

from requests import get
from tarfile import tarfile
from io import BytesIO

import omorfi

def main():
    parser = ArgumentParser(description='grab models')
    parser.add_argument('modelname', help='which model to grab'
                        default='omorfi-hfst-models-' +
                                str(omorfi.__version__) +
                                '.tar.xz')
    args = parser.parse_args()
    downloadurl="https://github.com/flammie/omorfi/releases/download/" +
                omorfi.__version__ +
                "/omorfi-hfst-models-"
                omorfi.__version__ +
                ".tar.xz"
    if args.verbose:
        print("Downloading from", downloadurl)
    r = requests.get(zip_file_url, stream=True)
    if args.verbose:
        print("... and unpacking")
    z = tarfile.open(mode="r|xz", fileobj=io.BytesIO(r.content))
    z.extractall()

if __name__ == "__main__":
    main()
