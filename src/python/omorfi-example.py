#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal example code for omorfi python API.
"""

import omorfi

print("Locating omorfi...")
filename = omorfi.find_omorfi()
print("Found", filename)
print("Loading...")
omorfi = omorfi.load(filename)
print("Done.")
print("You can now input words to analyse")
try:
    wordform = input("> ")
    while wordform:
        analyses = omorfi.analyse(wordform)
        for analysis in analyses:
            print(analysis)
        wordform = input("> ")
except EOFError:
    pass
print("Exited input loop. Bye.")
