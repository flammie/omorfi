#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A command-line utility to fetch released omorfi language models.

Mainly a helper for pip package, normal users can use the bash version
`omorfi-download.bash`, which I think is easier and better. 57 % of this
script was yoinked from Turku NLP's neural parser pipeline:

https://github.com/TurkuNLP/Turku-neural-parser-pipeline/blob/master/fetch_models.py
"""

# string munging
from argparse import ArgumentParser

import tarfile
import io
import requests

import omorfi


def main():
    """CLI for downloading omorfi language models."""
    parser = ArgumentParser(description="download omorfi binaries")
    parser.add_argument("-m", "--model-version",  metavar="MFILE",
                        help="download models MFILE",
                        default=str(omorfi.__version__))
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="print verbosely")
    args = parser.parse_args()
    downloadurl = "https://github.com/flammie/omorfi/releases/download/v" + \
                  args.model_version + \
                  "/omorfi-hfst-models-" + \
                  args.model_version + \
                  ".tar.xz"
    print("Downloading from", downloadurl, "and unpacking to .")
    if args.verbose:
        print("Downloading...")
    r = requests.get(downloadurl, stream=True)
    if args.verbose:
        print("opening...")
    with tarfile.open(mode="r|xz", fileobj=io.BytesIO(r.content)) as z:
        if args.verbose:
            print("unpackin...")
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(z)


if __name__ == "__main__":
    main()
