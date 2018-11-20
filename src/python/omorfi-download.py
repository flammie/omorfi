#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Download models from github."""

import tarfile
import io
import urllib.request
# string munging
from argparse import ArgumentParser


def main():
    """Command-line interface to omorfi downloads."""
    a = ArgumentParser()
    a.add_argument('-m', '--models', metavar="MODELS", required=True,
                   help="download omorfi-usable MODELS",
                   choices=["hfst", "hunspell", "zhfst"])
    a.add_argument('-v', '--verbose', action='store_true',
                   help="print verbosely while processing")
    options = a.parse_args()
    if options.models == "hfst":
        tarball = "omorfi-hfst-binaries-20181111.tar.xz"
    downloadlink = "https://github.com/flammie/omorfi/releases/download/" +\
                   "2018111/" + tarball
    if options.verbose:
        print("Fetching:", downloadlink)
    response = urllib.request.urlopen(downloadlink)
    data = response.read()
    z = tarfile.open("mode=r|xz", fileobj=io.BytesIO(data))
    z.extractall()
    exit(0)


if __name__ == "__main__":
    main()
