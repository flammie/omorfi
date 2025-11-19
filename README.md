# 🇫🇮Omorfi–Open morphology of Finnish

This is a free/libre open source morphology of Finnish: a database, tools and
APIs. Everything you need to build NLP applications processing Finnish language
words and texts.

* 🇫🇮 high-quality Finnish text analysis and generation
* 🩸 bleeding edge
* ⚡ blazing fast

[![Build Status](https://travis-ci.org/flammie/omorfi.svg?branch=develop)](https://travis-ci.org/flammie/omorfi)
![CI](https://github.com/flammie/omorfi/workflows/CI/badge.svg)

## Documentation

I try to keep this `README` very condensed for github.
For more detailed information, see [github pages for
omorfi](//flammie.github.io/omorfi/).

## Licence

Omorfi is licenced [GNU GPLv3](COPYING) (not later). The bundled HFST in the
java API demo is [Apache](COPYING-hfst-java).

* [Further information about licence and copyright in
  documentation](//flammie.github.io/omorfi/licence.html)

## Citing and academic works

Citation information is available in github's *cite this repository* function,
backed by the
[CITATION.cff](https://github.com/flammie/omorfi/blob/CITATION.cff). For further
details, see [omorfi articles](//flammie.github.io/omorfi/articles.html).

## Downloading and further information

Omorfi source packages can be downloaded from github:

* [omorfi releases](https://github.com/flammie/omorfi/releases)

or the most current version using git. For more information, see
[Release policy](https://flammie.github.io/omorfi/releases.html)

## Dependencies

* **hfst-3.15** or greater,
* **python-3.5** or greater,
* **hfst-python**,
* **C++** compiler and **libtool**
* GNU **autoconf-2.64**, **automake-1.12**; compatible **pkg-config**
  implementation

Optionally:

* *VISL CG 3*
* *hfst-ospell-0.2.0* or greater needed for spell-checking
* *Java 7*, or greater, for Java bindings

## Installation

For detailed instructions and explanations of different options, see
[Installation instructions](//flammie.github.io/omorfi/install.html) on the
github pages site. This readme is a quick reference.

### Full installation

Requires *all* dependencies to be installed.

```
autoreconf -i
./configure
make
make install
```

Will install binaries and scripts for all users on typical environments

### Minimal "installation"

To skip language model building and use some of the scripts locally.

```
autoreconf -i
./configure
src/bash/omorfi-download.bash
```

This will download some of the pre-compiled dictionaries into your current
working directory.

### Python installation

It is possible to install within python via `pip` or `anaconda`. The
dependencies that are not available in pip or anaconda will not be usable, e.g.
syntactic analysis and disambiguation using VISL CG 3.

```
pip install omorfi
```

[![Anaconda](https://anaconda.org/flammie/omorfi/badges/installer/conda.svg)](https://anaconda.org/flammie/omorfi/)

```
conda install -c flammie omorfi
```

**NB: since conda does not have new version of hfst buildable with recent
pythons or something, only older versions are available on conda.**

### Docker

It is possible to use omorfi with a ready-made docker container, there is a
Dockerfile in `src/docker/Dockerfile` for that.

```
docker build -t "omorfi:Dockerfile" .
docker run -it "omorfi:Dockerfile" bash
```

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
   pages](https://flammie.github.io/omorfi/usage.html)
* [omorfi man pages](https://flammie.github.io/omorfi/man/)

## Programming APIs

Omorfi can be used via very simple programming APIs, the design is detailed in
[omorfi API design](https://flammie.github.io/omorfi/API-design.html)

## Using binary models

There are various binaries for language models that can be used with specialised
tools like HFST. For further details, see [our usage
examples](https://flammie.github.io/omorfi/usage.html).

## Troubleshooting

For full descriptions and archived problems, see: [Troubleshooting in github
pages](https://flammie.github.io/omorfi/troubleshooting.html)

### hfst-lexc: Unknown option

Update HFST.

### ImportError (or other Python problems)

In order for python scripts to work you need to install them to same prefix as
python, or define PYTHONPATH, e.g. `export
PYTHONPATH=/usr/local/lib/python3.11/site-packages/`

### Processing text gets stuck / takes long

This can easily happen for legit reasons. It can be reduced by filtering
overlong tokens out. Or processing texts in smaller pieces.

### Make gets killed

Get more RAM or swap space.

## Contributing

Omorfi code and data are free and libre open source, and community-driven, to
participate, read further information in
[CONTRIBUTING](https://flammie.github.io/omorfi/CONTRIBUTING.html)

## Contact

* Issues and problems may be filed in [our github issue
  tracker](https://github.com/flammie/omorfi/issues), including support
  questions
* [Matrix channel omorfi](https://matrix.to/#/#omorfi:matrix.org) is
  particularly good for live chat for support questions, suggestions and
  discussions
* [omorfi-devel mailing
  list](https://groups.google.com/forum/#!forum/omorfi-devel) is good for longer
  more involved discussions

You can always discuss in English or Finnish on any of the channels.

## Code of conduct

See [our code of conduct](//flammie.github.io/omorfi/CODE_OF_CONDUCT.html).

## Donations

A lot of omorfi development has been done on spare time and by volunteers, if
you want to support [Flammie](https://flammie.github.io) you can use the
github's [❤️Sponsor](https://github.com/sponsors/flammie) button, or any of the
services below:

<a href="https://liberapay.com/Flammie/donate"><img alt="Donate using Liberapay"
src="https://liberapay.com/assets/widgets/donate.svg"></a>

<a href="https://www.patreon.com/bePatron?u=9479606" data-patreon-widget-type="become-patron-button">Become a Patron!</a>

