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

→ See also: https://flammie.github.io/omorfi/meta/Releases.html

Omorfi is currently hosted at github. [Omorfi's github
repository](https://github.com/flammie/omorfi) contain most of the important
information about omorfi: version control system for source codes, bug tracker
for reporting bugs, and the stable releases as convenient packages. [Omorfi's
gh-pages site](https://flammie.github.io/omorfi) contain further information not
found in this README.

## Dependencies

Before you start: Apertium wiki has installation information for most
dependencies on their [Apertium installation pages, look at section called
pre-requisites](http://wiki.apertium.org/wiki/Installation), e.g., if you are
looking to build *omorfi* on *Ubuntu*, go to: [Pre-requisites for
Ubuntu](http://wiki.apertium.org/wiki/Prerequisites_for_Debian).

Compilation of the morphological analyser, generation, lemmatisation or
spell-checking requires [HFST](https://hfst.github.io/) tools or compatible
installed. For use, you will need the python bindings too, and a relatively
recent version of python 3. Of course standard GNU build tools are needed as
well. You should have versions no more than year or two old, the build is not
guaranteed to work at all with ancient versions of GNU build tools, HFST or
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

→ See also: man pages

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
$
```

When testing the instructions, please do not copy/pasdte the dollar sign, it is
not a part of the command, but an command-line prompt indicator!

### Raw text tokenisation

→ See also: https://flammie.github.io/omorfi/man/omorfi-tokenise(1).html

For many tasks you need to tokenise text before using it, this may involve:
splitting punctuation from words, recasing, etc. Also formatting text into word
per line, space-separated or more advanced formats like CONLL-U. There's only
one tool `omorfi-tokenise.py` for this.

```
$ omorfi-tokenise.py -v -i test/newstest2016-fien-ref.fi.text | tail
kokouksessa keskusteltiin myös lakimiesten ammattinharjoittamisoikeuksien takaamisesta sekä ammattituomareiden ja - syyttäjien tukemisesta .
kokoukseen osallistui myös pääministeri Li Keqiang , sekä vanhemmat johtajat Liu Yunshan ja Zhang Gaoli , kerrottiin kokouksen jälkeen julkaistussa lausunnossa .
Lines: 3000 Tokens: 47338 Ratio: 15.779333333333334 tokens/line
CPU time: 0.5221295579999996 Real time: 0.5221478860185016
Tokens per timeunit: 90660.1391436499 Lines per timeunit: 5745.498699373647
```

For CONLL-U and so Universal dependencies, you'd use `-O conllu`:

```
$ omorfi-tokenise.py -v -i test/newstest2016-fien-ref.fi.text -O conllu| tail
# sentence-text: Kokoukseen osallistui myös pääministeri Li Keqiang, sekä vanhemmat johtajat Liu Yunshan ja Zhang Gaoli, kerrottiin kokouksen jälkeen julkaistussa lausunnossa.
1	kokoukseen	_	_	_	_	_	_	_	LOWERCASED=Kokoukseen
2	osallistui	_	_	_	_	_	_	_	ORIGINALCASE
3	myös	_	_	_	_	_	_	_	ORIGINALCASE
4	pääministeri	_	_	_	_	_	_	_	ORIGINALCASE
5	Li	_	_	_	_	_	_	_	ORIGINALCASE
6	Keqiang	_	_	_	_	_	_	_	SpaceBefore=No|SpaceAfter=No
7	,	_	_	_	_	_	_	_	SpaceBefore=No
8	sekä	_	_	_	_	_	_	_	ORIGINALCASE
9	vanhemmat	_	_	_	_	_	_	_	ORIGINALCASE
10	johtajat	_	_	_	_	_	_	_	ORIGINALCASE
11	Liu	_	_	_	_	_	_	_	ORIGINALCASE
12	Yunshan	_	_	_	_	_	_	_	SpaceBefore=No|SpaceAfter=No
13	ja	_	_	_	_	_	_	_	ORIGINALCASE
14	Zhang	_	_	_	_	_	_	_	ORIGINALCASE
15	Gaoli	_	_	_	_	_	_	_	SpaceBefore=No|SpaceAfter=No
16	,	_	_	_	_	_	_	_	SpaceBefore=No
17	kerrottiin	_	_	_	_	_	_	_	ORIGINALCASE
18	kokouksen	_	_	_	_	_	_	_	ORIGINALCASE
19	jälkeen	_	_	_	_	_	_	_	ORIGINALCASE
20	julkaistussa	_	_	_	_	_	_	_	ORIGINALCASE
21	lausunnossa	_	_	_	_	_	_	_	ORIGINALCASE|SpaceAfter=No
22	.	_	_	_	_	_	_	_	SpaceBefore=No

Lines: 3000 Tokens: 47338 Ratio: 15.779333333333334 tokens/line
CPU time: 0.9153448170000003 Real time: 1.1707193159963936
Tokens per timeunit: 40434.96964061865 Lines per timeunit: 2562.5271224355897
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
$ omorfi-analyse-text.sh test/newstest2016-enfi-ref.fi.text |head
Tampereella	[WORD_ID=Tampere][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=ADE]

karkuteillä	[WORD_ID=karkuteillä][UPOS=ADV]
karkuteillä	[WORD_ID=karkuteillä_2][UPOS=ADV]

ollut	[WORD_ID=olla][UPOS=AUX][DRV=NUT][CMP=POS][NUM=SG][CASE=NOM]
ollut	[WORD_ID=olla][UPOS=AUX][DRV=TU][CMP=POS][NUM=PL][CASE=NOM]
ollut	[WORD_ID=olla][UPOS=AUX][VOICE=ACT][MOOD=INDV][TENSE=PAST][NUM=SG][NEG=CON]
ollut	[WORD_ID=olla][UPOS=AUX][VOICE=ACT][PCP=NUT]
ollut	[WORD_ID=olla][UPOS=AUX][VOICE=PSS][PCP=NUT][CMP=POS][CASE=NOM][NUM=PL]
```

If your text is already split into word-forms (one word-form per line), it can
be analysed like this:

```
$ omorfi-analyse-tokenised.sh test/wordforms.list  | head
.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]	0,000000

1	[WORD_ID=1][UPOS=NUM][NUMTYPE=CARD]	0,000000
1	[WORD_ID=1][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM]	0,000000

10	[WORD_ID=10][UPOS=NUM][NUMTYPE=CARD]	0,000000
10	[WORD_ID=10][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM]	0,000000

1000–2000	[WORD_ID=1000][UPOS=NUM][NUMTYPE=CARD][BOUNDARY=COMPOUND][WORD_ID=2000][UPOS=NUM][NUMTYPE=CARD]	0,000000
1000–2000	[WORD_ID=1000][UPOS=NUM][NUMTYPE=CARD][BOUNDARY=COMPOUND][WORD_ID=2000][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM]	0,000000
```

#### VISL CG 3 format


A full pipeline for VISL CG 3 disambiguation is implemented as a convenience
script that works like text analysis script:

```
$ omorfi-disambiguate-text.sh test/newstest2016-enfi-ref.fi.text | tail
"<kokoukseen>"
	"kokouksi" NOUN SG ILL
	"kokouksi_2" NOUN SG ILL
	"kokous" NOUN SG ILL
"<osallistui>"
	"osallistua" VERB ACT INDV PAST SG3
"<myös>"
	"myödä" VERB <DIALECTAL> ACT IMPV SG2 S
"<pääministeri>"
	"pää-ministeri" NOUN TITLE SG NOM
	"pääministeri" NOUN TITLE SG NOM
"<Li>"
	"Li" NUM ROMAN
	"Li" PROPN FIRST SG NOM
	"Li_2" PROPN LAST SG NOM
"<Keqiang>"
	"Keqiang" UNKNOWN <W=65536>
"<,>"
	"," PUNCT CLAUSE COMMA CLB
	",_2" SYM CLB
"<sekä>"
	"sekä" CONJ
"<vanhemmat>"
	"vanha" ADJ MPI CMP PL NOM
	"vanhempi" NOUN PL NOM
"<johtajat>"
	"johtaa" VERB JA PL NOM
	"johtaja" NOUN TITLE PL NOM
"<Liu>"
	"Liu" PROPN LAST SG NOM
"<Yunshan>"
	"Yunshan" UNKNOWN <W=65536>
"<ja>"
	"ja" CONJ
"<Zhang>"
	"Zhang" PROPN LAST SG NOM
"<Gaoli>"
	"Gaoli" UNKNOWN <W=65536>
"<,>"
	"," PUNCT CLAUSE COMMA CLB
	",_2" SYM CLB
"<kerrottiin>"
	"kertoa" VERB PSS INDV PAST PE4
"<kokouksen>"
	"kokouksi" NOUN SG GEN
	"kokouksi_2" NOUN SG GEN
	"kokous" NOUN SG GEN
"<jälkeen>"
	"jälkeen_2" ADV PREP
"<julkaistussa>"
	"julkaistu" ADJ POS SG INE
"<lausunnossa>"
	"lausunto" NOUN SG INE
"<.>"
	"." PUNCT SENTENCE
Tokens: 47338 Unknown: 1982 4.186911149604969 %
CPU time: 3.087152993 Real time: 3.1000033089949284
Tokens per timeunit: 15270.306280849665
```


CG style format can be generated using python based analyser script
`omorfi-vislcg.py`:

```
$ omorfi-vislcg.py -i test/newstest2016-enfi-ref.fi.text | tail
"<,>"
	"," PUNCT CLAUSE COMMA
	",_2" SYM

"<kerrottiin>"
	"kertoa" VERB PSS INDV PAST PE4

"<kokouksen>"
	"kokouksi" NOUN SG GEN
	"kokouksi_2" NOUN SG GEN
	"kokous" NOUN SG GEN

"<jälkeen>"
	"jälkeen" ADP POST
	"jälkeen_2" ADV PREP
	"jälki" NOUN SG ILL

"<julkaistussa>"
	"julkaistu" ADJ POS SG INE

"<lausunnossa>"
	"lausunto" NOUN SG INE

"<.>"
	"." PUNCT SENTENCE

Tokens: 47338 Unknown: 1982 4.186911149604969 %
CPU time: 3.6671915069999996 Real time: 3.66774150999845
Tokens per timeunit: 12906.580213178655
```


#### Moses factored format

Moses factored analysis format can be generated using python script:

```
$ omorfi-factorise.py -i test/newstest2016-enfi-ref.fi.text | tail
Kokouksessa|koko+uksi|UNK|NOUN.SG.INE|0 keskusteltiin|keskustella|UNK|VERB.PSS.INDV.PAST.PE4|0 myös|myödä|UNK|VERB.DIALECTAL.ACT.IMPV.SG2.S|0 lakimiesten|laki+mies|UNK|NOUN.PL.GEN|0 ammattinharjoittamisoikeuksien|ammattinharjoittamisoikeuksien|UNK|UNKNOWN|0 takaamisesta|taata_2|UNK|VERB.MINEN.SG.ELA|0 sekä|sekä|UNK|CONJ|0 ammattituomareiden|ammatti-+tuomari|UNK|NOUN.TITLE.PL.GEN|0 ja|ja|UNK|CONJ|0 -syyttäjien|syyttäjä|UNK|NOUN.TITLE.PL.GEN|0 tukemisesta.|tukemisesta.|UNK|UNKNOWN|0
Kokoukseen|koko+uksi|UNK|NOUN.SG.ILL|0 osallistui|osallistua|UNK|VERB.ACT.INDV.PAST.SG3|0 myös|myödä|UNK|VERB.DIALECTAL.ACT.IMPV.SG2.S|0 pääministeri|pää-+ministeri|UNK|NOUN.TITLE.SG.NOM|0 Li|Li|UNK|NUM.ROMAN|0 Keqiang,|Keqiang,|UNK|UNKNOWN|0 sekä|sekä|UNK|CONJ|0 vanhemmat|vanha|UNK|ADJ.MPI.CMP.PL.NOM|0 johtajat|johtaa|UNK|VERB.JA.PL.NOM|0 Liu|Liu|UNK|PROPN.LAST.SG.NOM|0 Yunshan|Yunshan|UNK|UNKNOWN|0 ja|ja|UNK|CONJ|0 Zhang|Zhang|UNK|PROPN.LAST.SG.NOM|0 Gaoli,|Gaoli,|UNK|UNKNOWN|0 kerrottiin|kertoa|UNK|VERB.PSS.INDV.PAST.PE4|0 kokouksen|koko+uksi|UNK|NOUN.SG.GEN|0 jälkeen|jälkeen|UNK|ADP.POST|0 julkaistussa|julkaistu|UNK|ADJ.POS.SG.INE|0 lausunnossa.|lausunnossa.|UNK|UNKNOWN|0
```

The input should be in format produced by moses's `tokenizer.perl` (truecase or
clean-corpus-n not necessary). The output is readily usable by Moses train
model. *If you don't use tokenizer.perl, the words next to punctuation will not
be analysed.*

#### Universal Dependencies pre-parse format

[Universal Dependencies](http://universaldependencies.org) are the up-and-coming
standard for all your morpho-syntactic needs! Omorfi is currently scheduled to
follow up on Universal dependencies relaeas schedules and analysis and design
principles.

Universal dependencies parsing requires input in pre-tokenised,
CONLL-U format, only fields INDEX, SURF and MISC are made use of in
basic version.

```
$ omorfi-conllu.py -v -i test/UD_Finnish/fi-ud-dev.conllu | tail -n 40
# sentence-text: TGV-junat ajavat toistaiseksi normaalia pikajunan nopeutta muilla rataosuuksilla kuin erityisesti nopeaa liikennettä varten suunnitelluilla aidatuilla osuuksilla, joissa ei ole tasoristeyksiä.
1	TGV-junat	TGV#juna	NOUN	N	Case=Nom|Number=Plur	_	_	_	_
2	ajavat	ajaa	VERB	V	Case=Nom|Degree=Pos|Number=Plur	_	_	_	_
3	toistaiseksi	toistainen	ADJ	A	Case=Tra|Degree=Pos|Number=Sing	_	_	_	_
4	normaalia	normaali	ADJ	A	Case=Par|Degree=Pos|Number=Sing	_	_	_	_
5	pikajunan	pika-#juna	NOUN	N	Case=Gen|Number=Sing	_	_	_	_
6	nopeutta	nopeus	NOUN	N	Case=Par|Number=Sing	_	_	_	_
7	muilla	muu	ADJ	A	Case=Ade|Degree=Pos|Number=Plur	_	_	_	_
8	rataosuuksilla	rata#osuus	NOUN	N	Case=Ade|Number=Plur	_	_	_	_
9	kuin	kuin	SCONJ	C	_	_	_	_	_
10	erityisesti	erityisesti	ADV	Adv	Derivation=Sti	_	_	_	_
11	nopeaa	nopea	ADJ	A	Case=Par|Degree=Pos|Number=Sing	_	_	_	_
12	liikennettä	liikenne	NOUN	N	Case=Par|Number=Sing	_	_	_	_
13	varten	varten	ADV	Adv	_	_	_	_	_
14	suunnitelluilla	suunnitella	VERB	V	Case=Ade|Degree=Pos|Number=Plur	_	_	_	_
15	aidatuilla	aidata	VERB	V	Case=Ade|Degree=Pos|Number=Plur	_	_	_	_
16	osuuksilla	osuus	NOUN	N	Case=Ade|Number=Plur	_	_	_	_
17	,	,	PUNCT	Punct	_	_	_	_	_
18	joissa	joka	PRON	Pron	Case=Ine|Number=Plur|PronType=Rel	_	_	_	_
19	ei	ei	VERB	V	Negative=Neg|Number=Sing|Person=3|VerbForm=Fin|Voice=Act	_	_	__
20	ole	olla	AUX	V	Mood=Imp|Number=Sing|Person=2|VerbForm=Fin|Voice=Act	_	_	_	_
21	tasoristeyksiä	taso#risteys	NOUN	N	Case=Par|Number=Plur	_	_	_	_
22	.	.	PUNCT	Punct	_	_	_	_	_
```

This can be combined with tokenisation to analyse raw corpora:

```
$ omorfi-tokenise.py -O conllu -i test/newstest2016-enfi-ref.fi.text | omorfi-conllu.py | tail -n 40
# sentence-text: Kokoukseen osallistui myös pääministeri Li Keqiang, sekä vanhemmat johtajat Liu Yunshan ja Zhang Gaoli, kerrottiin kokouksen jälkeen julkaistussa lausunnossa.
1	kokoukseen	koko#uksi	NOUN	N	Case=Ill|Number=Sing	_	_	_	_
2	osallistui	osallistua	VERB	V	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|Voice=Act	_	_	_	_
3	myös	myödä	VERB	V	Clitic=S|Mood=Imp|Number=Sing|Person=2|Style=Coll|VerbForm=Fin|Voice=Act	__	_	_
4	pääministeri	pää-#ministeri	NOUN	N	Case=Nom|Number=Sing	_	_	_	_
5	Li	Li	NUM	Num	_	_	_	_	_
6	Keqiang	Keqiang	X	X	_	_	_	_	_
7	,	,	PUNCT	Punct	_	_	_	_	_
8	sekä	sekä	CONJ	C	_	_	_	_	_
9	vanhemmat	vanha	ADJ	A	Case=Nom|Degree=Cmp|Number=Plur	_	_	_	_
10	johtajat	johtaa	VERB	V	Case=Nom|Derivation=Ja|Number=Plur	_	_	_	_
11	Liu	Liu	PROPN	N	Case=Nom|Number=Sing	_	_	_	_
12	Yunshan	Yunshan	X	X	_	_	_	_	_
13	ja	ja	CONJ	C	_	_	_	_	_
14	Zhang	Zhang	PROPN	N	Case=Nom|Number=Sing	_	_	_	_
15	Gaoli	Gaoli	X	X	_	_	_	_	_
16	,	,	PUNCT	Punct	_	_	_	_	_
17	kerrottiin	kertoa	VERB	V	Mood=Ind|Tense=Past|VerbForm=Fin|Voice=Pass	_	_	_	_
18	kokouksen	koko#uksi	NOUN	N	Case=Gen|Number=Sing	_	_	_	_
19	jälkeen	jälkeen	ADP	Adp	AdpType=Post	_	_	_	_
20	julkaistussa	julkaistu	ADJ	A	Case=Ine|Degree=Pos|Number=Sing	_	_	_	_
21	lausunnossa	lausunto	NOUN	N	Case=Ine|Number=Sing	_	_	_	_
22	.	.	PUNCT	Punct	_	_	_	_	_

```

There's a cheat mode that can be used with UD training data to always select
the best match, for evaluation purposes: `--oracle`. There's a debug mode to
print full n-best for each token: `--debug`, this is pseudo CONLL-U.

### Morphological segmentation

The morphological segmentation can be done like this:

```
$ omorfi-segment.py -O segments -i test/newstest2016-enfi-ref.fi.text
Lisäksi ulko→ ←maalais→ ←ten pysyv→ ←i→ ←en asukas→ ←lup→ ←i→ ←en , ” green cardien , ” haku→ ←prosessi→ ←a helpote→ ←taan optimoima→ ←lla vaatimuks→ ←i→ ←a ja keventämä→ ←llä haku→ ←prosessi→ ←a .
Kokouksessa keskustel→ ←tiin myös lakimies→ ←ten ammattinharjoittamisoikeuksien takaamise→ ←sta sekä ammatti→ ←tuomare→ ←i→ ←den ja - syyttäj→ ←i→ ←en tukemise→ ←sta .
Kokoukseen osallistu→ ←i myös pää→ ←ministeri Li Keqiang , sekä vanhemma→ ←t johtaja→ ←t Liu Yunshan ja Zhang Gaoli , kerrot→ ←tiin kokoukse→ ←n jälkeen julkaistu→ ←ssa lausunno→ ←ssa .
```

**Preliminary** support for labeled segmentation is also available but not
guaranteed to work.

### Spell-Checking and correction

Spelling correction may be done if hfst-ospell is installed:

```
$ omorfi-spell.sh test/wordforms.list | tail
"äyräässä" is in the lexicon...
"äänestys" is in the lexicon...
"äänioikeus" is in the lexicon...
"öykkärein" is in the lexicon...
"öykkäri" is in the lexicon...
"öykkärimpi" is in the lexicon...
"öykkäröi" is in the lexicon...
"öykkäröidä" is in the lexicon...
```

### Morphological generation

Generating word-forms can be done using:

```
$ omorfi-generate.sh
[WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=NOM]
[WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=NOM]	bisse	0,000000

[WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=INE]
[WORD_ID=bisse][UPOS=NOUN][NUM=SG][CASE=INE]	bissessä	0,000000
```

The input for generator is simply the output of the raw analyser.

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
(('[WORD_ID=koira][UPOS=NOUN][NUM=SG][CASE=NOM]', 0.0),)
>>> for analysis in anlyses:
...     print(analysis[0], analysis[1])
...
[WORD_ID=alku][UPOS=NOUN][NUM=SG][CASE=ELA] 0.0
[WORD_ID=alunen][UPOS=NOUN][NUM=SG][CASE=PAR] 0.0
[WORD_ID=alus][UPOS=NOUN][NUM=SG][CASE=PAR] 0.0
[WORD_ID=alusta][UPOS=NOUN][NUM=SG][CASE=NOM] 0.0
[WORD_ID=alusta_2][UPOS=ADV] 0.0
[WORD_ID=alusta_3][UPOS=ADV] 0.0
[WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=IMPV][PERS=SG2] 0.0
[WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON] 0.0
[WORD_ID=Alku_2][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=ELA] 0.0
[WORD_ID=Alku_3][UPOS=PROPN][PROPER=LAST][NUM=SG][CASE=ELA] 0.0
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

The installed files are in `$prefix/share/omorfi` (my installation is in linux
default: `/usr/local`)

```
$ ls /usr/local/share/omorfi/
fin-autogen.hfst    omorfi-ftb1.analyse.hfst	 omorfi.labelsegment.hfst	   omorfi.tokenise.hfst
fin-automorf.hfst   omorfi-ftb3.analyse.hfst	 omorfi-omor.analyse.hfst	   omorfi.tokenise.pmatchfst
master.tsv	    omorfi-ftb3.generate.hfst	 omorfi-omor.generate.hfst	   omorfi.tokenise.pmatchfst.debug1
omorfi.accept.hfst  omorfi-giella.analyse.hfst	 omorfi-omor_recased.analyse.hfst  omorfi.tokenise.pmatchfst.debug2
omorfi.cg3bin	    omorfi-giella.generate.hfst  omorfi.segment.hfst		   speller-omorfi.zhfst
```

The naming is probably not gonna be same forever.

### HFST tools

You can directly access specific automata using finite-state tools from the HFST
project (details can be found on their individual man pages and
[HFST wiki](https://kitwiki.csc.fi/):

```
$ hfst-lookup /usr/local/share/omorfi/omorfi.segment.hfst
> talossani
talossani	talo{DB}s{MB}sa{MB}ni	0,000000
talossani	talo{MB}ssa{MB}ni	0,000000

> on
on	on	0,000000

> hirveä
hirveä	hirve{MB}ä	0,000000
hirveä	hirveä	0,000000

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
