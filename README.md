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

The lexical data of omorfi has been acquired from various sources with
different original licences.  The dictionaries used in omorfi are [Nykysuomen
sanalista](http://kaino.kotus.fi) (LGPL),
[Joukahainen](http://joukahainen.lokalisointi.org) (GPL) and
[FinnWordNet](http://www.ling.helsinki.fi/research/finnwordnet) (Princeton
Wordnet licence / GPL; relicenced with kind permission from University of
Helsinki), and [Finnish Wiktionary](http://fi.Wiktionary.org) (Creative Commons
Attribution–ShareAlike). Some words have also been collected by omorfi
developers and contributors and are GPLv3 like the rest of the package.

## Downloading and further information

Omorfi is currently hosted at github. [Omorfi's github
pages](https://github.com/flammie/omorfi) contain most of the important
information about omorfi: wiki for additional documentation, version control
system for source codes, bug tracker for reporting bugs, and the stable
releases as convenient packages.

## Dependencies

Compilation of the morphological analyser, generation, lemmatisation or
spell-checking requires [HFST](http://hfst.sf.net) tools or compatible
installed, including the python bindings and relatively recent python. Of
course standard GNU build tools are needed as well. You should have versions no
more than year or two old, the build is not guaranteed to work at all with
ancient versions of GNU build tools, HFST or python. The versions that should
work are as follows:

  * **hfst-3.8** or greater, with python bindings
  * **python-3.2** or greater, with hfst python bindings available
  * GNU **autoconf-2.64** and **automake-1.12**

The use of certain automata also requires additional tools:

  * *hfst-ospell-0.2.0* or greater needed for spell-checking

APIs require:

* *Python 3.2* for python API
* *Java 7* for Java API

For bash tools, recent GNU coreutils etc. should be more than enough.

## Installation

Installation uses standard autotools system:

```
./configure && make && make install
```

The compiling may take forever or more depending on the hardware and settings.
You should be prepared with at least 4 gigs of RAM or such.  The stable release
versions should be compilable on average end-user systems.  You should be able
to make use of the `-j` switch of make to speed it up.

If configure cannot find HFST tools, you must tell it where to find them:

```
./configure --with-hfst=${HFSTPATH}
```

Autotools system supports installation to e.g. home directory:

```
./configure --prefix=${HOME}
```

With git version you must create necessary autotools files in the host system
once, after initial checkout:

```
./autogen.sh
```

For further instructions, see `INSTALL`, the GNU standard install instructions
for autotools systems.

## Usage

For basic, beginner end-user usage, omorfi provides helper scripts:

- `omorfi-analyse-text.sh`: analyse plain text into ambiguous word-form lists
- `omorfi-analyse-tokenised.sh`: analyse pre-tokenised word-forms one per line
- `omorfi-generate.sh`: generate word-forms from omor descriptions
- `omorfi-segment.sh`: morphologically segment word-forms one per line
- `omorfi-spell.sh`: spell-check and correct word-forms one per line
- `omorfi-disambiguate-text.sh`: analyse text and disambiguate using VISL CG-3

These scripts are enough for basic usage including scientific use for
re-production of published results, but lack many additional features like more
fine-grained control of tokenisation, case-folding.

Most commonly you will probably want to turn text files into FTB3.1 lists into
xerox format analyses:

```
$ omorfi-analyse-text.sh kalevala.txt
!! Warning: Transducer contains one or more multi-character symbols made up of
ASCII characters which are also available as single-character symbols. The
input stream will always be tokenised using the longest symbols available.
Use the -t option to view the tokenisation. The problematic symbol(s):
SS
Ensimmäinen	
Ensimmäinen	Ensimmäinen N Nom Sg
Ensimmäinen	Ensimmäinen Num Ord Nom Sg

runo	
runo	runo N Nom Sg

Mieleni	
Mieleni	Miele N Prop Gen Sg PxSg1
Mieleni	Miele N Prop Nom Pl PxSg1
Mieleni	Miele N Prop Nom Sg PxSg1
Mieleni	Mieli N Gen Sg PxSg1
Mieleni	Mieli N Nom Pl PxSg1
Mieleni	Mieli N Nom Sg PxSg1

minun	
minun	minä Pron Pers Gen Sg

tekevi	
tekevi	tehdä V Prs Act Sg3

...
```

If your text is already split into word-forms (one word-form per line), it can
be analysed like this:

```
$ omorfi-analyse-tokenised.sh test/wordforms.list 
> 1	1 Num Digit Nom Sg	0,000000

> 10	10 Num Digit Nom Sg	0,000000

> 11	11 Num Digit Nom Sg	0,000000

> 12	12 Num Digit Nom Sg	0,000000

> 13	13 Num Digit Nom Sg	0,000000

> 14	14 Num Digit Nom Sg	0,000000

> 15	15 Num Digit Nom Sg	0,000000

> 16	16 Num Digit Nom Sg	0,000000

> 17	17 Num Digit Nom Sg	0,000000

> 18	18 Num Digit Nom Sg	0,000000

> 19	19 Num Digit Nom Sg	0,000000

> 2	2 Num Digit Nom Sg	0,000000
```

The morphological segmentation can be done like this:

```
$ omorfi-segment.sh kalevala.wordlist | head -n 100

Ensimmäinen	ensimmäinen	0,000000

runo	runo	0,000000

Mieleni	Miele ni	0,000000
Mieleni	miele ni	0,000000

minun	minu n	0,000000

tekevi	teke vi	0,000000

aivoni	aivo ni	0,000000

ajattelevi	ajattele vi	0,000000
```


Spelling correction may be done if hfst-ospell is installed:

```
omorfi-spell.sh kalevala.wordlist
```

Generating word-forms can be done using:

```
omorfi-generate.sh
$ omorfi-generate.sh 
> [WORD_ID=talo][POS=NOUN][NUM=SG][CASE=INE]
[WORD_ID=talo][POS=NOUN][NUM=SG][CASE=INE]	talossa	0,000000
```

Moses factored analysis format can be generated using python script:

```
omorfi-factorise.py
tämä kyllä toimii oikein.
tämä|tämä|PRONOUN|PRONOUN.DEMONSTRATIVE.SG.NOM|0 kyllä|kyllä|ADVERB|ADVERB|0 toimii|toimia|VERB|VERB.ACT.INDV.PRESENT.SG3|.i oikein.|oikein.|UNK|UNKNOWN|0 
```

The input should be in format produced by moses's `tokenizer.perl` (truecase or
clean-corpus-n not necessary). 

CG style format can be generated using python based analyser script 
`omorfi-analyse.py`:

```
"<Ensimmäinen>"
        "ensimmäinen" <DETITLECASED> NOUN SG NOM <W=0>
        "ensimmäinen" <DETITLECASED> NUMERAL ORD SG NOM <W=0>
        "ensimmäinen" <LOWERCASED> NOUN SG NOM <W=0>
        "ensimmäinen" <LOWERCASED> NUMERAL ORD SG NOM <W=0>

"<runo>"
        "runo" NOUN SG NOM <W=0>
        "Runo" <TITLECASED> NOUN PROPER SG NOM <W=0>

"<Mieleni>"
        "Miele" NOUN PROPER PL NOM SG1 <W=0>
        "Miele" NOUN PROPER SG GEN SG1 <W=0>
        "Miele" NOUN PROPER SG NOM SG1 <W=0>
        "mieli" <DETITLECASED> NOUN PL NOM SG1 <W=0>
        "mieli" <DETITLECASED> NOUN SG GEN SG1 <W=0>
        "mieli" <DETITLECASED> NOUN SG NOM SG1 <W=0>
        "mieli" <LOWERCASED> NOUN PL NOM SG1 <W=0>
        "mieli" <LOWERCASED> NOUN SG GEN SG1 <W=0>
        "mieli" <LOWERCASED> NOUN SG NOM SG1 <W=0>

"<minun>"
        "minä" PRONOUN PERSONAL SG1 SG GEN <W=0>

"<tekevi>"
        "tehdä" VERB ACT INDV PRESENT SG3 <ARCHAIC> <W=1600>

"<,>"
        "," PUNCTUATION CLAUSE <W=0>

"<aivoni>"
        "aivo" NOUN PL NOM SG1 <W=0>
        "aivo" NOUN SG GEN SG1 <W=0>
        "aivo" NOUN SG NOM SG1 <W=0>
        "aivot" NOUN PL NOM SG1 <W=0>

"<ajattelevi>"
        "ajatella" VERB ACT INDV PRESENT SG3 <ARCHAIC> <W=1600>
```

A full pipeline for VISL CG 3 disambiguation is implemented as a convenience
script that works like text analysis script:

```
$ omorfi-disambiguate-text.sh kalevala.txt
"<Ensimmäinen>"
        "ensimmäinen" <DETITLECASED> NOUN SG NOM <W=0>
        "ensimmäinen" <DETITLECASED> NUMERAL ORD SG NOM <W=0>
        "ensimmäinen" <LOWERCASED> NOUN SG NOM <W=0>
        "ensimmäinen" <LOWERCASED> NUMERAL ORD SG NOM <W=0>
"<runo>"
        "runo" NOUN SG NOM <W=0>
"<Mieleni>"
        "mieli" <LOWERCASED> NOUN SG NOM SG1 <W=0>
        "mieli" <DETITLECASED> NOUN SG NOM SG1 <W=0>
"<minun>"
        "minä" PRONOUN PERSONAL SG1 SG GEN <W=0>
"<tekevi>"
        "tehdä" VERB ACT INDV PRESENT SG3 <ARCHAIC> <W=1600>
"<,>"
        "," PUNCTUATION CLAUSE <W=0> CLB
"<aivoni>"
        "aivo" NOUN SG NOM SG1 <W=0>
"<ajattelevi>"
        "ajatella" VERB ACT INDV PRESENT SG3 <ARCHAIC> <W=1600>
```

The use of disambiguation requires working omorfi python installation.

*In order for python scripts to work you need to install them to same prefix as
 python, or define PYTHONPATH*:

```
$ PYTHONPATH=/usr/local/lib/python3.4/site-packages/ omorfi-disambiguate-text.sh kalevala.txt
```

You will also want to have *python3* as the system python in case I forget to
set the whole shebang right. You can work around this by:

```
python3 $(which omorfi-analyse.py )
```

### Advanced usage

For serious business, the convenience shell-scripts are not usually sufficient.
We offer bindings to several popular programming languages as well as low-level
access to the automata either via command-line or the external programming
libraries from the toolkit generating the automata.

#### Python

Python interface (check wiki page Python API for details):

```
$ python
Python 3.4.1 (default, Oct 16 2014, 03:32:31) 
[GCC 4.7.3] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from omorfi.omorfi import Omorfi
>>> omorfi = Omorfi()
>>> omorfi.load_from_dir()
>>> omorfi.analyse("koira")
(<libhfst.HfstPath; proxy of <Swig Object of type 'HfstPath *' at 0x7f640b7c0420> >, <libhfst.HfstPath; proxy of <Swig Object of type 'HfstPath *' at 0x7f640b7c0750> >)
>>> analyses = omorfi.analyse("koira")
>>> for analysis in analyses:
...     print(analysis.output, analysis.weight)
... 
[WORD_ID=Koira][POS=NOUN][PROPER=PROPER][NUM=SG][CASE=NOM][WEIGHT=0.000000] 0.0
[WORD_ID=koira][POS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.000000] 0.0

```

#### Java

Java class (check wiki page Java API api for details):

```
java -Xmx1024m com.github.flammie.omorfi.Omorfi
```

Especially loading all automata from system paths requires more memory than
java typically gives you, so use `-Xmx` switch.

#### Raw automata

The installed files are in `$prefix/hfst/fi`:

```
$ ls /usr/local/share/hfst/fi/
omorfi.accept.hfst       omorfi-omor.generate.hfst
fin-autogen.hfst         omorfi-ftb3.analyse.hfst   omorfi.segment.hfst
fin-automorf.hfst        omorfi-ftb3.generate.hfst  omorfi.tokenise.hfst
omorfi.hyphenate.hfst    omorfi.lemmatise.hfst      omorfi-omor.analyse.hfst
```

The naming *has changed* in 2014–2015 cycle! This was made because people seem
to distribute automata over the net without attributions, at least the default
filenames for most automata are now `omorfi*.hfst`. The system is: 
omorfi.`function`.hfst, or omorfi-`variant`.`function`.hfst. The variants
other than `omor` are for convenience and interoperability, and have recasing
built in, but since they encode existing standards, will also be more
stable between versions.

#### HFST tools

You can directly access specific automata with HFST tools (detailed in their
man pages and [HFST wiki](https://kitwiki.csc.fi/):

```
$ hfst-lookup /usr/local/share/hfst/fi/omorfi.segment.hfst 
> talossani
talossani	talo{STUB}{MB}ssa{MB}ni	0,000000

> on
on	{STUB}on	0,000000

> hirveä
hirveä	hirve{STUB}ä	0,000000
hirveä	hirv{STUB}e{MB}ä	0,000000

> kissakoira-apina
kissakoira-apina	kiss{STUB}a{wB}koir{STUB}a{wB}apin{STUB}a	0,000000

> 
```

## Troubleshooting

Mac OS X may cause problems with its Unicode encoding (NFD), or with its
non-GNU command-line tools.

### hfst-lexc: Unknown option

This may happen when compiling the system with make:

```
hfst-lexc --Werror -o generated/omorfi-ftb3.lexc.hfst generated/omorfi-ftb3.lexc
Try ``/usr/local/bin/hfst-lexc --help'' for more information.
/usr/local/bin/hfst-lexc: Unknown option
```

It means your hfst-lexc is too old. You need at least version 3.8 to handle
`--Werror` switch. You can workaround by removing `--Werror` from
`src/Makefile.am`, although this is not recommended, as the newer versions of
HFST have provided this option to ensure the data is not broken.

## Contributing

Omorfi code and data are free and libre open source, modifiable and
redistributable by anyone. IRC channel [#omorfi on
Freenode](irc://Freenode/#omorfi) is particularly good for immediate discussion
about contributions. Any data or code contributed must be compatible with our
licencing policy, i.e. GNU compatible free licence.
