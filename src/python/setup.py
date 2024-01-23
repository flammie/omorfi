#!/usr/bin/env python3
"""Python setup for some pypi stuff?"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="omorfi",
    version="0.9.10",
    author="Flammie A Pirinen",
    author_email="flammie@iki.fi",
    description="Open morphology for Finnish, python bindings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flammie/omorfi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords="finnish nlp morphology",
    python_requires=">=3.5",
    scripts=["omorfi-download.py",
             "omorfi-conllu.py",
             "omorfi-convert.py",
             "omorfi-disamparsulate.py",
             "omorfi-download.py",
             "omorfi-factorise.py",
             "omorfi-freq-evals.py",
             "omorfi-ftb3.py",
             "omorfi-segment.py",
             "omorfi-sigmorphons.py",
             "omorfi-tokenise.py",
             "omorfi-unimorph.py",
             "omorfi-vislcg.py",
             "omorfi-wikitable.py"],
    install_requires=["hfst"],
)
