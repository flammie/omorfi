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

These are the obligatory stamps of the day:

[![Build Status](https://travis-ci.org/flammie/omorfi.svg?branch=master)](https://travis-ci.org/flammie/omorfi)

## Downloading and further information

Omorfi is currently hosted at github. [Omorfi's github
repository](https://github.com/flammie/omorfi) contain most of the important
information about omorfi: version control system for source codes, bug tracker
for reporting bugs, and the stable releases as convenient packages. [Omorfi's
gh-pages site](https://flammie.github.io/omorfi) contain further information not
found in this README.

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

Omorfi comes with several simple scripts for basic functionalities. These 
scripts cover the most basic usage with minimal amount of required extra
tools, however, for advanced usage you may want to check the APIs or bindings
for python and Java.

Following are basic shell scripts that only use *HFST* tools and GNU
*coreutils*:

- `omorfi-analyse-text.sh`: analyse plain text into ambiguous word-form lists
- `omorfi-analyse-tokenised.sh`: analyse pre-tokenised word-forms one per line
- `omorfi-generate.sh`: generate word-forms from omor descriptions
- `omorfi-segment.sh`: morphologically segment word-forms one per line

The following requires *python* and *VISL CG 3* 

- `omorfi-disambiguate-text.sh`: analyse text and disambiguate using VISL CG-3

The following uses *hfst-ospell*:

- `omorfi-spell.sh`: spell-check and correct word-forms one per line

The following are *python* scripts:
vi
- `omorfi-tokenise.py`: format raw text into tokens (words and puncts).
- `omorfi-conllu.py`: analyse and generate CONLL-U formatted data (Universal
  Dependencies) format
- `omorfi-vislcg.py`: analyse raw texts into VISL CG 3 format
- `omorfi-factorise.py`: analyse raw texts into moses factored format

The following examples have been run in the omorfi source dir after succesful
installation. The command lines look like this:

```
[tpirinen@c305 omorfi]$ 
```

for taito-shell.csc.fi. This is a thing that works in CSC-maintained taito
cluster easily. The command line like:

```
$ 
```

was executed on my laptop or work desktop because it didn't work on taito
cluster. This is a hint that something requires more software to be installed.

### Raw text tokenisation

For many tasks you need to tokenise text before using it, this may involve:
splitting punctuation from words, recasing, etc. Also formatting text into word
per line, space-separated or more advanced formats like CONLL-U. There's only
one tool `omorfi-tokenise.py` for this.

```
$ omorfi-tokenise.py -v -i test/newstest2015-fien-src.fi.text | tail
kaupungin tiedotteen mukaan lähetys ei ole mahdollinen teknisten ongelmien vuoksi .
Kouvolan kaupunki pahoittelee tilannetta .
jälkitallenteen voi katsoa parin päivän päästä kokouksesta .
Kouvolan kaupunginvaltuuston kokouksia on voinut katsoa internetin kautta vuoden alusta .
seuraavan kerran päätöksentekoa voi seurata suorana 13.10.2014.
valtuuston kokousvideot löytyvät osoitteesta http://www.kouvola.fi/index/aikuisvaestolle/paatoksenteko/valtuustoverkossa.html ja Kouvolan kaupungin YouTube-kanavalta .
Lines: 1370 Tokens: 19755 Ratio: 14.41970802919708 tokens/line
CPU time: 0.183332214 Real time: 0.30890897917561233
Tokens per timeunit: 63950.87657445347 Lines per timeunit: 4434.963346342761
```

For CONLL-U and so Universal dependencies, you'd use `-O conllu`:

```
$ omorfi-tokenise.py -v -i test/newstest2015-fien-src.fi.text -O conllu| tail
# sentence-text: Valtuuston kokousvideot löytyvät osoitteesta http://www.kouvola.fi/index/aikuisvaestolle/paatoksenteko/valtuustoverkossa.html ja Kouvolan kaupungin YouTube-kanavalta.
1   valtuuston  _   _   _   _   _   _   _   LOWERCASED=Valtuuston
2   kokousvideot    _   _   _   _   _   _   _   ORIGINALCASE
3   löytyvät    _   _   _   _   _   _   _   ORIGINALCASE
4   osoitteesta _   _   _   _   _   _   _   ORIGINALCASE
5   http://www.kouvola.fi/index/aikuisvaestolle/paatoksenteko/valtuustoverkossa.html    _   __  _   _   _   _   SpaceBefore=No|SpaceAfter=No
6   ja  _   _   _   _   _   _   _   ORIGINALCASE
7   Kouvolan    _   _   _   _   _   _   _   ORIGINALCASE
8   kaupungin   _   _   _   _   _   _   _   ORIGINALCASE
9   YouTube-kanavalta   _   _   _   _   _   _   _   ORIGINALCASE|SpaceAfter=No
10  .   _   _   _   _   _   _   _   SpaceBefore=No

Lines: 1370 Tokens: 19755 Ratio: 14.41970802919708 tokens/line
CPU time: 0.234918811 Real time: 0.2349290030542761
```

### Morphological analysis

Different kinds of morphological analysis use cases: traditional linguitsics
with Xerox-style analysis, followed by constraitn grammars, or Universal
dependency pre-parses, or factorised analysis for statistical machine
ranslations.

#### Xerox / Finite-State Morphology format

Most commonly you will probably want to turn text files into FTB3.1 lists into
xerox format analyses:

```
[tpirinen@c305 omorfi]$ omorfi-analyse-text.sh \
    test/newstest2015-fien-src.fi.text | head
Juankosken	[WORD_ID=Juankoski][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Juankosken	[WORD_ID=juan][UPOS=NOUN][SEM=CURRENCY][NUM=SG][CASE=NOM][BOUNDARY=COMPOUND][WORD_ID=koski][UPOS=NOUN][NUM=SG][CASE=GEN]

kaupunki	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=NOM]

liittyy	[WORD_ID=liittyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG3]

Kuopion	[WORD_ID=Kuopio][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Kuopion	[WORD_ID=kuopia][UPOS=VERB][VOICE=ACT][MOOD=OPT][PERS=SG1][STYLE=ARCHAIC]
```

If your text is already split into word-forms (one word-form per line), it can
be analysed like this:

```
[tpirinen@c305 omorfi]$ omorfi-analyse-tokenised.sh test/wordforms.list | head
.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]	133.099609

1	[WORD_ID=1][UPOS=NUM][NUMTYPE=CARD]	133.099609

10	[WORD_ID=10][UPOS=NUM][NUMTYPE=CARD]	133.099609

1000–2000	[WORD_ID=1000][UPOS=NUM][NUMTYPE=CARD][BOUNDARY=COMPOUND][WORD_ID=2000][UPOS=NUM][NUMTYPE=CARD]	134.099609

1 000	[WORD_ID=1 000][UPOS=NUM][NUMTYPE=CARD]	133.099609
```

#### VISL CG 3 format


A full pipeline for VISL CG 3 disambiguation is implemented as a convenience
script that works like text analysis script:

```
$ omorfi-disambiguate-text.sh test/newstest2015-fien-src.fi.text | head
"<Juankosken>"
	"Juankoski" PROPN GEO SG GEN
"<kaupunki>"
	"kaupunki" NOUN SG NOM
"<liittyy>"
	"liittyä" VERB ACT INDV PRESENT SG3
"<Kuopion>"
	"Kuopio" PROPN GEO SG GEN
"<kaupunkiin>"
	"kaupunki" NOUN SG ILL
```


CG style format can be generated using python based analyser script 
`omorfi-vislcg.py`:

```
[tpirinen@c305 omorfi]$ omorfi-vislcg.py -i test/newstest2015-fien-src.fi.text | head
"<Juankosken>"
	"Juankoski" PROPN GEO SG GEN

"<kaupunki>"
	"kaupunki" NOUN SG NOM

"<liittyy>"
	"liittyä" VERB ACT INDV PRESENT SG3

"<Kuopion>"
```


#### Moses factored format

Moses factored analysis format can be generated using python script:

```
$ omorfi-factorise.py -i test/newstest2015-fien-src.fi.text | head
Juankosken|Juankoski|UNK|PROPN.GEO.SG.GEN|0 kaupunki|kaupunki|UNK|NOUN.SG.NOM|0 liittyy|liittyä|UNK|VERB.ACT.INDV.PRESENT.SG3|0 Kuopion|Kuopio|UNK|PROPN.GEO.SG.GEN|0 kaupunkiin|kaupunki|UNK|NOUN.SG.ILL|0 vuoden|vuosi|UNK|NOUN.SG.GEN|0 2017|2017|UNK|NUM.CARD|0 alussa.|alussa.|UNK|UNKNOWN|0 
Kuopion|Kuopio|UNK|PROPN.GEO.SG.GEN|0 kaupunginvaltuusto|kaupunginvaltuusto|UNK|NOUN.SG.NOM|0 hyväksyi|hyväksyä|UNK|VERB.ACT.INDV.PAST.SG3|0 liitoksen|liitos|UNK|NOUN.SG.GEN|0 yksimielisesti|yksimielisesti|UNK|ADV.STI|0 maanantaina.|maanantaina.|UNK|UNKNOWN|0 
Juankosken|Juankoski|UNK|PROPN.GEO.SG.GEN|0 kaupunginvaltuusto|kaupunginvaltuusto|UNK|NOUN.SG.NOM|0 hyväksyi|hyväksyä|UNK|VERB.ACT.INDV.PAST.SG3|0 liitoksen|liitos|UNK|NOUN.SG.GEN|0 viime|viime|UNK|ADV|0 viikolla.|viikolla.|UNK|UNKNOWN|0 
Kuntaliitoksen|kuntaliitos|UNK|NOUN.SG.GEN|0 selvittämisessä|selvittäminen|UNK|NOUN.SG.INE|0 oli|olla|UNK|AUX.ACT.INDV.PAST.SG3|0 mukana|mukana|UNK|ADP.POST|0 myös|myös|UNK|ADV|0 Tuusniemen|Tuusniemi|UNK|PROPN.GEO.SG.GEN|0 kunta,|kunta,|UNK|UNKNOWN|0 mutta|mutta|UNK|ADP|0 sen|se|UNK|DET.SG.GEN|0 valtuusto|valtuusto|UNK|NOUN.SG.NOM|0 päätti,|päätti,|UNK|UNKNOWN|0 että|että|UNK|INTJ|0 Tuusniemi|Tuusniemi|UNK|PROPN.GEO.SG.NOM|0 jatkaa|jatkaa|UNK|VERB.ACT.A.LAT|0 itsenäisenä.|itsenäisenä.|UNK|UNKNOWN|0 
```

The input should be in format produced by moses's `tokenizer.perl` (truecase or
clean-corpus-n not necessary). The output is readily usable by Moses train
model.

#### Universal Dependencies pre-parse format

[Universal Dependencies](http://universaldependencies.org) TODO

Universal dependencies parsing requires input in pre-tokenised,
CONLL-U format, only fields INDEX, SURF and MISC are made use of in
basic version.

```
$ python3 src/python/omorfi-conllu.py -v -i test/UD_Finnish/fi-ud-dev.conllu | tail -n 40
# sentence-text: Onnettomuuspaikkaa ja kyseistä rataosaa ei ollut vielä uudistettu TGV-junia varten.
1   Onnettomuuspaikkaa  onnettomuuspaikka   NOUN    N   Case=Par|Number=Sing    _   __  _
2   ja  ja  ADV Adv _   _   _   _   _
3   kyseistä    kyse    NOUN    N   Case=Ela|Number=Plur    _   _   _   _
4   rataosaa    rataosa NOUN    N   Case=Par|Number=Sing    _   _   _   _
5   ei  ei  VERB    V   Negative=Neg|Number=Sing|Person=3|VerbForm=Fin|Voice=Act    __  _   _
6   ollut   olla    AUX V   Case=Nom|Degree=Pos|Number=Plur|PartForm=Past|VerbForm=Part|Voice=Pass  _   _   _   _
7   vielä   vielä   ADV Adv _   _   _   _   _
8   uudistettu  uudistaa    VERB    V   Connegative=Yes|Mood=Ind|Tense=Past|VerbForm=Fin    _   _   _   _
9   TGV-junia   TGV#juna    NOUN    N   Case=Par|Number=Plur    _   _   _   _
10  varten  varten  ADP Adp AdpType=Post    _   _   _   _
11  .   .   PUNCT   Punct   _   _   _   _   _
```

This can be combined with tokenisation to analyse raw corpora:

```
$ python3 src/python/omorfi-tokenise.py -O conllu -i test/newstest2015-fien-src.fi.text | python3 src/python/omorfi-conllu.py | tail -n 40
# sentence-text: Valtuuston kokousvideot löytyvät osoitteesta http://www.kouvola.fi/index/aikuisvaestolle/paatoksenteko/valtuustoverkossa.html ja Kouvolan kaupungin YouTube-kanavalta.
1   valtuuston  valtuusto   NOUN    N   Case=Gen|Number=Sing    _   _   _   _
2   kokousvideot    kokous#video    NOUN    N   Case=Nom|Number=Plur    _   _   _   _
3   löytyvät    löytyä  VERB    V   Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act _   _   _   _
4   osoitteesta osoite  NOUN    N   Case=Ela|Number=Sing    _   _   _   _
5   http://www.kouvola.fi/index/aikuisvaestolle/paatoksenteko/valtuustoverkossa.html    http://www.kouvola.fi/index/aikuisvaestolle/paatoksenteko/valtuustoverkossa.html    X   X   _   __  _   _
6   ja  ja  ADV Adv _   _   _   _   _
7   Kouvolan    Kouvola PROPN   N   Case=Gen|Number=Sing    _   _   _   _
8   kaupungin   kaupunki    NOUN    N   Case=Gen|Number=Sing    _   _   _   _
9   YouTube-kanavalta   YouTube#kanava  NOUN    N   Case=Abl|Number=Sing    _   _   __
10  .   .   PUNCT   Punct   _   _   _   _   _
```

There's a cheat mode that can be used with UD training data to always select
the best match, for evaluation purposes: `--oracle`. There's a debug mode to
print full n-best for each token: `--debug`, this is pseudo CONLL-U.

### Morphological segmentation

The morphological segmentation can be done like this:

```
[tpirinen@c305 omorfi]$ omorfi-segment.sh test/wordforms.list | tail -n 30

äristä	ärist→ ←ä	0.000000
äristä	äris→ ←tä	0.000000

äyräs	äyräs	0.000000

äyräässä	äyrää→ ←ssä	0.000000

äänestys	äänestys	0.000000

äänioikeus	ääni→ ←oikeus	0.000000
```

### Spell-Checking and correction

Spelling correction may be done if hfst-ospell is installed:

```
[tpirinen@c305 omorfi]$ omorfi-spell.sh test/wordforms.list | head
"." is in the lexicon...
"1" is in the lexicon...
"10" is in the lexicon...
"1000–2000" is in the lexicon...
"1 000" is in the lexicon...
"11" is in the lexicon...
"12" is in the lexicon...
"13" is in the lexicon...
"14" is in the lexicon...
"15" is in the lexicon...
```

### Morphological generation

Generating word-forms can be done using:

```
[tpirinen@c305 omorfi]$ omorfi-generate.sh
> [WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=NOM]
[WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=NOM]	bisse	0.000000

> [WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=INE]
[WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=INE]	bissessä	0.000000
```

## Advanced usage

For serious business, the convenience shell-scripts are not usually sufficient.
We offer bindings to several popular programming languages as well as low-level
access to the automata either via command-line or the external programming
libraries from the toolkit generating the automata.

### Python

Python interface (more details on python API page):

```
[tpirinen@c305 omorfi]$ python3
Python 3.4.0 (default, Mar 18 2014, 16:02:57) 
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from omorfi.omorfi import Omorfi
>>> omorfi = Omorfi()
>>> omorfi.load_from_dir()
>>> omorfi.analyse("koira")
(('[WORD_ID=koira][UPOS=NOUN][NUM=SG][CASE=NOM]', 133.099609375),)
>>> analyses = omorfi.analyse("koira")
>>> for analysis in analyses:
...     print(analysis[0], analysis[1])
... 
[WORD_ID=koira][UPOS=NOUN][NUM=SG][CASE=NOM] 133.099609375
>>> 
```

### Java

Java class (more details on java API pages):

```
$ CLASSPATH=$HOME/Koodit/hfst-optimized-lookup/hfst-optimized-lookup-java/hfst-ol.jar:. java com.github.flammie.omorfi.Omorfi 
...
Read all.
> talo
Analysing talo
{omorfi-omor_recased=net.sf.hfst.WeightedTransducer@63947c6b, omorfi-giella=net.sf.hfst.WeightedTransducer@2b193f2d, omorfi-ftb3=net.sf.hfst.WeightedTransducer@355da254, omorfi-omor=net.sf.hfst.WeightedTransducer@4dc63996}
Analysing talo with omorfi-omor
[WORD_ID=talo][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=133.09961]
[WORD_ID=talo][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=133.09961[CASECHANGE=LOWERCASED]]
```

Especially loading all automata from system paths requires more memory than
java typically gives you, so use `-Xmx` switch.

### Raw automata

The installed files are in `$prefix/share/omorfi` (my taito installation is
--prefix=$HOME)

```
[tpirinen@c305 java]$ ls ~/share/omorfi/
master.tsv		    omorfi-giella.generate.hfst  omorfi-omor.generate.hfst	   omorfi.tokenise.hfst
omorfi.accept.hfst	    omorfi.labelsegment.hfst	 omorfi-omor_recased.analyse.hfst  speller-omorfi.zhfst
omorfi-giella.analyse.hfst  omorfi-omor.analyse.hfst	 omorfi.segment.hfst



$ ls /usr/local/share/omorfi/
master.tsv		  omorfi-ftb3.generate.hfst    omorfi-omor.analyse.hfst		 omorfi.tokenise.hfst
omorfi.accept.hfst	  omorfi-giella.analyse.hfst   omorfi-omor.generate.hfst	 speller-omorfi.zhfst
omorfi.cg3bin		  omorfi-giella.generate.hfst  omorfi-omor_recased.analyse.hfst
omorfi-ftb3.analyse.hfst  omorfi.labelsegment.hfst     omorfi.segment.hfst
```

The naming *was changed* back in 2014–2015 cycle! This was made because people
seem to distribute automata over the net without attributions, at least the
default filenames for most automata are now `omorfi*.hfst`. The system is:
omorfi.`function`.hfst, or omorfi-`variant`.`function`.hfst. The variants other
than `omor` are for convenience and interoperability, and have recasing built
in, but since they encode existing standards, will also be more stable between
versions.

### HFST tools

You can directly access specific automata using finite-state tools from the HFST
project (details can be found on their individual man pages and 
[HFST wiki](https://kitwiki.csc.fi/):

```
[tpirinen@c305 omorfi]$ hfst-lookup ~/share/omorfi/omorfi.segment.hfst 
> talossani
talossani	talo{MB}ssa{MB}ni	0.000000

> on
on	on	0.000000

> hirveä
hirveä	hirve{MB}ä	0.000000
hirveä	hirveä	0.000000

> kissakoira-apina
kissakoira-apina	kissa{hyph?}koira{hyph?}apina	0.000000
```

When using `hfst-lookup` with large unclean material, it may get stuck at odd
looking long strings, consider using `-t` switch to set timeout for individual
analyses; omorfi bash API sets this to 15 seconds.

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

### ImportError (or other Python problems)

E.g. error message of form:

```
ImportError: No module named 'omorfi'
```

In order for python scripts to work you need to install them to same prefix as
python, or define PYTHONPATH, e.g.:

```
$ PYTHONPATH=/usr/local/lib/python3.4/site-packages/ omorfi-disambiguate-text.sh kalevala.txt
```

The scripts require *python3* as the system python, in case I forget to
set the whole shebang right. You can work around this by, e.g.,:

```
python3 $(which omorfi-analyse.py )
```

This should not affect release versions but keep in mind if you are using a
python2-based system and development versions.

### Missing FILENAME

When omorfi files are not where bash scripts are looking for them.

If you have moved your installation manually after make install, you may need to
modify paths in omorfi.bash or set environment variable OMORFI_PATH.

If the file missing is `omorfi.cg3bin`, it may mean that the vislcg3 was missing
at the time of the installation. Similarly may happen with omorfi-speller.zhfst,
it will only be created when hfst-ospell and it's dependencies and zip are all
available.

### Processing text gets stuck / takes long

Occasionally some tokens yield very complicated analyses and take a lot of
memory or time. This happens especially with long strings that can be analysed
as combinations of interjections like ahahaha...ha (in theory, each ah, aha, ha
and hah within the string are ambiguous wrt. compounding), while current
versions have blacklisted most such combinations some may still exist. When
using hfst tools directly this can be solved using `-t` option to set the
timeout. While these workarounds will slowly trickle to all parts of HFST and
omorfi, it is often a good idea to pre-process text to remove or normalise
offending strings as they will trip other NLP tools too.

Some operations of omorfi legitly take a lot of memory, and most tools are
suspectible to memory leaks. It may be often beneficial to `split` your data
and process it in smaller chunks.

## Contributing

Omorfi code and data are free and libre open source, modifiable and
redistributable by anyone. IRC channel [#omorfi on
Freenode](irc://Freenode/#omorfi) is particularly good for immediate discussion
about contributions. Any data or code contributed must be compatible with our
licencing policy, i.e. GNU compatible free licence. In the github, you may use
the "fork this project" button to contribute, read github's documentation for
more information about this work-flow.

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
