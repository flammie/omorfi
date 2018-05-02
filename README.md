# Omorfi–Open morphology of Finnish

This is a free/libre open source morphology of Finnish: a database, tools and
APIs. This package is licenced under [GNU GPL version
3](https://gnu.org/licenses/gpl.html), but *not necessarily later*. Licence can
also be found in the `COPYING` file in the root directory of this package.
Other licences are possible by *all* the authors named in the `AUTHORS` file.

Omorfi has been used for a number of tasks:

* morphological analysis
* morphological segmentation
* spell-checking and correction
* information retrieval
* ontologies
* statistical machine translation
* rule-based machine translation
* language modeling
* tokenisation and sentence boundary detection
* stemming, lemmatisation and shallow morph analysis

The lexical data of omorfi has been acquired from various sources with
different original licences.  The dictionaries used in omorfi are [Nykysuomen
sanalista](http://kaino.kotus.fi) (LGPL),
[Joukahainen](http://joukahainen.lokalisointi.org) (GPL) and
[FinnWordNet](http://www.ling.helsinki.fi/research/finnwordnet) (Princeton
Wordnet licence / GPL; relicenced with kind permission from University of
Helsinki), and [Finnish Wiktionary](http://fi.Wiktionary.org) (Creative Commons
Attribution–ShareAlike). Some words have also been collected by omorfi
developers and contributors and are GPLv3 like the rest of the package.

I hear all the cool kids wear these things these days, sure they are much nicer
than w3c validator stamps:

[![Build Status](https://travis-ci.org/flammie/omorfi.svg?branch=master)](https://travis-ci.org/flammie/omorfi)
[![Coverage Status](https://coveralls.io/repos/github/flammie/omorfi/badge.svg?branch=master)](https://coveralls.io/github/flammie/omorfi?branch=feature/coveralls)

## Downloading and further information

→ See also: [Release policy](https://flammie.github.io/omorfi/pages/Releases.html)

Omorfi is currently hosted at github. [Omorfi's github
repository](https://github.com/flammie/omorfi) contain most of the important
information about omorfi: version control system for source codes, bug tracker
for reporting bugs, and the stable releases as convenient packages. [Omorfi's
gh-pages site](https://flammie.github.io/omorfi/) contain further information not
found in this README.

## Dependencies

*Before you start:* Apertium wiki has installation information for most
dependencies on their [Apertium installation pages, look at section called
pre-requisites](http://wiki.apertium.org/wiki/Installation), e.g., if you are
looking to build *omorfi* on *Ubuntu*, go to: [Pre-requisites for
Ubuntu](http://wiki.apertium.org/wiki/Prerequisites_for_Debian).

Compilation of the morphological analyser, generation, lemmatisation or
spell-checking requires [HFST](https://hfst.github.io/) tools or compatible
installed. For use, you will need the python bindings too, and a relatively
recent version of python 3. Of course standard GNU build tools are needed as
well. You should have versions no older than one or two years. The build is not
guaranteed to work at all with all ancient versions of GNU build tools, HFST or
python. The versions that should work are as follows:

  * **hfst-3.8** or greater, with python bindings
  * **python-3.2** or greater, with hfst python bindings available
  * GNU **autoconf-2.64** and **automake-1.12**

The use of certain automata also requires additional tools:

  * *hfst-ospell-0.2.0* or greater needed for spell-checking

APIs require:

* *Python 3.2* for python API
* *Java 7* for Java API
* *Bash 3*, *coreutils* for bash API
* The C++ API uses C++-11, this is basically available on all modern platforms.

## Installation

Installation uses standard autotools system:

```
./configure && make && make install
```

The compiling may take forever or longer, depending on the hardware and settings
used. You should be prepared with at least 4 gigs of RAM, however, it is possible
to compile a limited vocabulary system with less. This is a limitation of the
HFST system used to compile the language models, and it is only present at
compile time, the final models use perhaps up to hundreds of megabytes in memory.

If configure cannot find HFST tools, you must tell it where to find them:

```
./configure --with-hfst=${HFSTPATH}
```

Autotools system supports installation to e.g. home directory:

```
./configure --prefix=${HOME}
```

With git version you must create the necessary autotools files in the host system
once, after initial checkout:

```
./autogen.sh
```

For further instructions, see `INSTALL`, the GNU standard install instructions
for autotools systems.

There are a number of options that you can pass to `configure` script. The
default configuration leaves lots of features out to speed up the process,
for a full listing:

```
./configure --help
```

Some of the features that build more automata double the time required to
compile and the space used by the automata (approximately). Some features are
to enable or disable the API bindings for Java or other languages. The
`configure` script displays the current setup in the end:

```
* Analysers: yes
    * OMOR yes (flags: --omor-props   --omor-sem)
    * FTB3.1 no
    * apertium no
    * giella: no
    * labeled segmenter: no
* Limits:
    * tiny lexicons:
    * big tests:
* Applications
    * Voikko speller: yes
    * segmenter: no
    * lemmatiser: no
    * hyphenators: no
* Clusters
    * run tests on PBS cluster: false → mailto: no
    * run tests on SLURM cluster: false → mailto: no
```

For fully usable system you may want to turn the applications on.

## Usage

→ See also: [man pages](https://flammie.github.io/omorfi/man/)

Following are basic shell scripts that only use *HFST* tools and GNU
*coreutils*:

- `omorfi-analyse-text.sh`: analyse plain text into ambiguous word-form lists
- `omorfi-analyse-tokenised.sh`: analyse pre-tokenised word-forms one per line
- `omorfi-generate.sh`: generate word-forms from omor descriptions

The following scripts require *python*:

- `omorfi-tokenise.py`: format raw text into tokens (words and puncts).
- `omorfi-conllu.py`: analyse and generate CONLL-U formatted data (Universal
  Dependencies) format
- `omorfi-vislcg.py`: analyse raw texts into VISL CG 3 format

The following requires *python* and *VISL CG 3*

- `omorfi-disambiguate-text.sh`: analyse text and disambiguate using VISL CG-3

The following uses *hfst-ospell*:

- `omorfi-spell.sh`: spell-check and correct word-forms one per line

The following script requires *segmenting* automata enabled:

- `omorfi-segment.sh`: morphologically segment word-forms one per line
- `omorfi-segment.py`: morphologically segment word-forms one per line

The following script uses *all* enabled automata and *python*:

- `omorfi-factorise.py`: analyse raw texts into moses factored format

For further examples please refer to [omorfi man pages](https://flammie.github.io/omorfi/man/)
or [omorfi usage examples in github pages](https://flammie.github.io/omorfi/pages/usage-examples.html)

## Programming APIs

Omorfi can be used via very simple programming APIs, the design is detailed in
[omorfi API design](https://flammie.github.io/omorfi/pages/API-design)

Python API is in `Omorfi` class under `omorfi.omorfi` (may change in the
future), and requires HFST python bindings.

Java API is in `com.github.flammie.omorfi.Omorfi` and uses
hfst-optimized-lookup-java package (bundled or in classpath).

C++ API is in `omorfi::Omorfi` class and uses hfst API.

Bash "API" is in omorfi.bash and uses hfst tools and GNU coreutils.

## Using binary models

The compiled dictionaries are saved in binary files that can be handled with
various tools. Most of them are in HFST optimised format and can be used with
HFST tools. The CG3 binary is for VISL CG 3, the ZHFST file is compatible with
hfst-ospell and voikko, and the tsv file is the lexical database in TSV format.

For usage examples see [our usage
examples](https://flammie.github.io/omorfi/pages/usage-examples.html). The
binaries are installed in `$prefix/share`:

```
master.tsv                   omorfi-omor.analyse.hfst
omorfi.accept.hfst           omorfi-omor.generate.hfst
omorfi.analyse.hfst          omorfi-omor_recased.analyse.hfst
omorfi.cg3bin                omorfi_recased.analyse.hfst
omorfi.describe.hfst         omorfi_recased.describe.hfst
omorfi-ftb3.analyse.hfst     omorfi.tokenise.hfst
omorfi-ftb3.generate.hfst    omorfi.tokenise.pmatchfst
omorfi.generate.hfst         omorfi.tokenise.pmatchfst.debug1
omorfi-giella.analyse.hfst   omorfi.tokenise.pmatchfst.debug2
omorfi-giella.generate.hfst  speller-omorfi.zhfst
```

The actual listing depends on features and tagsets selected in the
[configuration phase](#Installation).

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

Omorfi code and data are free and libre open source, modifiable and
redistributable by anyone. IRC channel [#omorfi on
Freenode](irc://Freenode/#omorfi) is particularly good for immediate discussion
about contributions. Any data or code contributed must be compatible with our
licencing policy, i.e. GNU compatible free licence. In the github, you may use
the "fork this project" button to contribute, read github's documentation for
more information about this work-flow.

We are currently using [git-flow](http://nvie.com/posts/a-successful-git-branching-model/),
but feel free to just send pull-requests as you find comfortable and we'll sort
it out.

### Coding standards

Python code should pass the flake8 style checker and imports should be sorted
in accordance with isort. Ideally, you should integrate these into your editor,
[the development environment section of the python guide has instructions for a
few editors](docs.python-guide.org/en/latest/dev/env/). In addition, you can
install a pre-commit hook to run the checks like so:

```
$ pip install pre-commit
$ pre-commit install
```

I (Flammie) also recommend syntastic, e.g. I use
[vim-syntastic](https://github.com/vim-syntastic/syntastic)
