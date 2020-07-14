# Omorfi–Open morphology of Finnish

This is a free/libre open source morphology of Finnish: a database, tools and
APIs. Everything you need to build NLP applications processing Finnish language
words and texts.

[![Build Status](https://travis-ci.org/flammie/omorfi.svg?branch=develop)](https://travis-ci.org/flammie/omorfi)
(stable master branch:
[![Build Status](https://travis-ci.org/flammie/omorfi.svg?branch=master)](https://travis-ci.org/flammie/omorfi)
)
![CI](https://github.com/flammie/omorfi/workflows/CI/badge.svg)

## Documentation

For more detailed information, see [github pages for
omorfi](//flammie.github.io/omorfi/).

## Citing and academic works

Citation information can be found in file
[CITATION](https://github.com/flammie/omorfi/blob/develop/CITATION). For further
details, see [omorfi articles](//flammie.github.io/omorfi/pages/Articles.html).

## Downloading and further information

Omorfi packages can be downloaded from github:

* [omorfi releases](https://github.com/flammie/omorfi/releases)

or the most current version using git. For more information, see
[Release policy](https://flammie.github.io/omorfi/pages/Releases.html)

## Dependencies

* **hfst-3.15** or greater,
* **python-3.5** or greater,
* **libhfst-python**,
* **C++** compiler and **libtool**
* GNU **autoconf-2.64**, **automake-1.12**; compatible **pkg-config**
  implementation

Optionally:

* *VISL CG 3*
* *hfst-ospell-0.2.0* or greater needed for spell-checking
* *Java 7*, or greater, for Java bindings

For further information, see [Installation
instructions](//flammie.github.io/omorfi/install.html)

## Installation

It is possible to download the language models from previous release from the
internet (Minimal installation) or compile them from the database (Normal
installation), the former is recommended for new users and latter for advanced
users.

### Minimal installation

```
autoreconf -i
./configure
src/bash/omorfi-download.bash
```

This will download some of the pre-compiled dictionaries into your current
working directory.

### Normal installation

```
./configure
make
make install
```

For further instructions, see [Intallation
instructions](//flammie.github.io/omorfi/install.html).

## Usage

Omorfi can be used from command line using following commands:

1. `omorfi-disambiguate-text.sh`: analyse and disambiguate
1. `omorfi-analyse-text.sh`: analyse
1. `omorfi-spell.sh`: spell-check and correct
1. `omorfi-segment.sh`: morphologically segment
1. `omorfi-conllu.bash`: analyse in CONLL-U format
1. `omorfi-freq-evals.bash`: analyse coverage and statistics
1. `omorfi-ftb3.bash`: analyse in FTB-3 format (CONLL-X)
1. `omorfi-factorise.bash`: analyse in Moses-SMT factorised format
1. `omorfi-vislcg.bash`: analyse in VISL CG 3 format
1. `omorfi-analyse-tokenised.sh`: analyse word per line (faster)
1. `omorfi-generate.sh`: generate word-forms from omor descriptions
1. `omorfi-download.bash`: download language models from latest release

For further details please refer to:
* [omorfi usage examples in github
   pages](https://flammie.github.io/omorfi/pages/usage-examples.html)
* [omorfi man pages](https://flammie.github.io/omorfi/man/)

## Programming APIs

Omorfi can be used via very simple programming APIs, the design is detailed in
[omorfi API design](https://flammie.github.io/omorfi/pages/API-design)

## Using binary models

There are various binaries for language models that can be used with specialised
tools like HFST. For further details, see [our usage
examples](https://flammie.github.io/omorfi/pages/usage-examples.html).

## Troubleshooting

For full descriptions and archived problems, see: [Troubleshooting in github
pages](https://flammie.github.io/omorfi/pages/troubleshooting.html)

### hfst-lexc: Unknown option

Update HFST.

### ImportError (or other Python problems)

In order for python scripts to work you need to install them to same prefix as
python, or define PYTHONPATH, e.g. `export
PYTHONPATH=/usr/local/lib/python3.4/site-packages/`

### Processing text gets stuck / takes long

This can easily happen for legit reasons. It can be reduced by filtering
overlong tokens out. Or processing texts in smaller pieces.

### Make gets killed

Get more RAM or swap space.

## Contributing

Omorfi code and data are free and libre open source, and community-driven, to
participate, read further information in
[CONTRIBUTING](https://github.com/flammie/omorfi/blob/develop/CONTRIBUTING.md)

## Contact

* Issues and problems may be filed in github issue tracker, including support
  questions
* [IRC channel #omorfi on Freenode](irc://Freenode/#omorfi) is particularly good
  for live chat for support questions, suggestions and discussions
* [omorfi-devel mailing
  list](https://groups.google.com/forum/#!forum/omorfi-devel) is good for longer
  more involved discussions

You can always discuss in English or Finnish on any of the channels.

## Code of conduct

See [our code of conduct](//flammie.github.io/omorfi/CODE_OF_CONDUCT.html).

## Donations

A lot of omorfi development has been done on spare time and by volunteers, if
you want to support [Flammie](https://flammie.github.io) you can use the
github's ❤️Sponsor button, or any of the services below:

<a href="https://liberapay.com/Flammie/donate"><img alt="Donate using Liberapay"
src="https://liberapay.com/assets/widgets/donate.svg"></a>

<a href="https://www.patreon.com/bePatron?u=9479606" data-patreon-widget-type="become-patron-button">Become a Patron!</a>

