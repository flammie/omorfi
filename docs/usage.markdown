# Omorfi usage

Omorfi can be used with convenience command-line scripts, manually, using
programming language bindings / APIs, etc. This page gives you few basic
examples to get going. We assume here you have done [full
installation](install.html), if you did a *python only* installation you can
only use python examples (skip the bash section).

## Bash-based tools

The bash-based command line tools are easiest to use, as they combine multiple
operations into pipeline, select language models automatically and so forth. The
following pipelines are described in this document:

1. omorfi-download.bash
1. omorfi-disambiguate-text.sh
1. omorfi-vislcg.sh
1. omorfi-analyse-text.sh
1. omorfi-analyse-tokenised.sh
1. omorfi-conllu.sh
1. omorfi-ftb3.sh
1. omorfi-freq-evals.sh
1. omorfi-tokenise.sh
1. omorfi-segment.sh
1. omorfi-spell.sh
1. omorfi-factorise.sh

The following examples have been run in the omorfi source dir after succesful
installation. The command lines look like this:

```console
$
```

When following the instructions, please do not copy/paste the dollar sign, it is
not a part of the command, but a command-line prompt indicator! Furthermore, a
line-wrap symbol '↲' is used to soft-wrap the lines for this web-page, this is not a
part of console output:

```
123456789 123456789 123456789 123456789 123456789 123456789 123456789 ↲
  123456789 123456789
```

The example texts used here are part of omorfi distribution:

```console
$ cat test/test.text
Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa.
Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina.
Juankosken kaupunginvaltuusto hyväksyi liitoksen viime viikolla.
Kuntaliitoksen selvittämisessä oli mukana myös Tuusniemen kunta, mutta sen↲
valtuusto päätti, että Tuusniemi jatkaa itsenäisenä.
Kuopio ja Juankoski päättävät seuraavien kuntavaalien toteuttamisesta erikseen.
Kunnallisvaalit järjestetään seuraavan kerran vuonna 2016.
Juankosken liittymisen jälkeen Kuopion väkiluku on noin 111 000.
Intian ja Japanin pääministerit tapaavat Tokiossa
Intian uusi pääministeri Narendra Modi tapaa japanilaisen kollegansa Shinzo↲
Aben Tokiossa, keskustellakseen talous- ja turvallisuussuhteista, ensimmäisellä↲
merkittävällä ulkomaanvierailullaan toukokuun vaalivoiton jälkeen.
Modin viisipäiväisen Japaniin suuntautuvan vierailun tarkoituksena on vahvistaa↲
taloussuhteita maailman kolmanneksi suurimpaan talouteen.
```

This newspaper text originates from [Shared task of 1st International Conference
on Machine Translation](http://statmt.org/wmt16/)

**NB:** The examples below use the extended dictionary, for more
information of this, see the [Notes about lexicon sizes](Smaller-lexicons.html).
If you are looking for limited dictionary analyses add `-Z` to every bash
command or replace `describe` with `analyse` in langauge model file names.

The output in examples is re-wrapped to fit browser windows and editors, some of
the lines in the real world output will be very long. I use the ↲ symbol to
indicate such wraps.

### omorfi-download.bash

If you haven't built omorfi manually with `./configure && make && make install`,
it is possible to get some of the models for analysis from the internet (the
long URLs redacted from output, note this was on pre-release version so your
output should be slightly different):

```console
$ omorfi-download.bash
--2018-11-16 12:57:07--
https://github.com/flammie/omorfi/releases/download/...
Auflösen des Hostnamens github.com… 192.30.253.113, 192.30.253.112
Verbindungsaufbau zu github.com|192.30.253.113|:443 … verbunden.
HTTP-Anforderung gesendet, auf Antwort wird gewartet … 302 Found
Platz: https://github-production-release-asset-[...] [folgend]
--2018-11-16 12:57:08--  https://github-production-release-asset-[...]
Auflösen des Hostnamens github-production-release-asset-… 52.216.226.192
Verbindungsaufbau zu github-production-release-asset-...|52.216.226.192|:443↲
… verbunden.
HTTP-Anforderung gesendet, auf Antwort wird gewartet … 200 OK
Länge: 13756036 (13M) [application/octet-stream]
Wird in »omorfi-hfst-models-20191111.tar.xz« gespeichert.

omorfi-hfst-models-20191111.t 100%[===========>]  13,12M  4,86MB/s    in 2,7s

2019-11-16 12:57:11 (4,86 MB/s) - »omorfi-hfst-models-2019111.tar.xz«↲
gespeichert [13756036/13756036]

omorfi.accept.hfst
omorfi.analyse.hfst
omorfi.describe.hfst
omorfi.generate.hfst
omorfi.labelsegment.hfst
omorfi.segment.hfst

```

The binaries are unpacked in current directory and are from the previous
release. If you work within the omorfi git directory, you may want to download
the binaries in the directory called `src/generated/`.

### omorfi-disambiguate-text.sh

This is probably what most users want.

```console
$ omorfi-disambiguate-text.sh test/test.text
Lines: 10 Tokens: 110 Ratio: 11.0 tokens/line
CPU time: 0.005696905999999988 Real time: 0.005708508950192481
Tokens per timeunit: 19269.480167196896 Lines per timeunit: 1751.7709242906271
"<Juankosken>"
  "Juankoski" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunki>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<liittyy>"
	"liittyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Pres Number=Sing ↲
 Person=3 <CMP=1> <W=0>
"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunkiin>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Ill <CMP=1> <W=0>
"<vuoden>"
	"vuoden" UPOS=ADV <CMP=1> <W=0>
	"vuosi" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<2017>"
	"2017" UPOS=NUM NumType=Card <NumType=Digit> <CMP=1> <W=0>
	"2017" UPOS=NUM NumType=Card Number=Sing Case=Nom <NumType=Digit> <CMP=1> <W=0>
"<alussa>"
	"alku" UPOS=NOUN Number=Sing Case=Ine <CMP=1> <W=0>
	"alussa" UPOS=ADP AdpType=Post <CMP=1> <W=0>
	"alussa" UPOS=ADV <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>

"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Past Number=Sing ↲
 Person=3 <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<yksimielisesti>"
	"yksimielisesti" UPOS=ADV <Lexicalised=Sti> <CMP=1> <W=0>
"<maanantaina>"
	"maanantaina" UPOS=ADV <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>

"<Juankosken>"
	"Juankoski" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Past Number=Sing ↲
 Person=3 <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<viime>"
	"viime" UPOS=ADJ Degree=Pos Number=Sing Case=Nom <CMP=1> <W=0>
	"viime" UPOS=ADV <CMP=1> <W=0>
"<viikolla>"
	"viikko" UPOS=NOUN Number=Sing Case=Ade <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>

# Tokens: 110
# Unknown: 1 0.9090909090909091 %
# CPU time: 0.014630929999999986
# Real time: 0.018005268997512758
# Tokens per timeunit: 6109.32277741562
```

Compare this to the [Analyses without disambiguation](#Analyses without
disambiguation (VISL-CG3 format)) below to determine which one is more suitable
for your research.

For advanced usage options there is `omorfi-vislcg.py` python script.

#### omorfi-vislcg.bash

It is possible to view the full ambiguous analyses in this format as well, i.e.
before the CG rules try to remove most unlikely things. To do so, use
omorfi-vislcg3.bash script:

```console
$ omorfi-vislcg.bash test/test.text
...
"<Juankosken>"
	"Juankoski" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
	"juan#koski" UPOS=NOUN Number=Sing Case=Gen <CMP=2> <W=10000>
"<kaupunki>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<liittyy>"
	"liittyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Pres Number=Sing ↲
 Person=0 <CMP=1> <W=0>
	"liittyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Pres Number=Sing ↲
 Person=3 <CMP=1> <W=0>
"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunkiin>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Ill <CMP=1> <W=0>
"<vuoden>"
	"vuoden" UPOS=ADV <CMP=1> <W=0>
	"vuosi" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<2017>"
	"2017" UPOS=NUM NumType=Card <NumType=Digit> <CMP=1> <W=0>
	"2017" UPOS=NUM NumType=Card Number=Sing Case=Nom <NumType=Digit> ↲
 <CMP=1> <W=0>
"<alussa>"
	"alku" UPOS=NOUN Number=Sing Case=Ine <CMP=1> <W=0>
	"alunen" UPOS=NOUN Number=Sing Case=Ess Style=Arch <CMP=1> <W=0>
	"alussa" UPOS=ADP AdpType=Post <CMP=1> <W=0>
	"alussa" UPOS=ADV <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>


"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
	"kuopia" UPOS=VERB Voice=Act VerbForm=Fin Number=Sing Person=1 Style=Arch ↲
 <Mood=Opt> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
	"kaupunki#valtuus#to" UPOS=NOUN Number=Sing Case=Nom <CMP=3> <W=20000>
	"kaupunki#valtuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=2> <W=10000>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Past Number=Sing ↲
 Person=0 <CMP=1> <W=0>
	"hyväksyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Past Number=Sing ↲
 Person=3 <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<yksimielisesti>"
	"yksi#-mielinen" UPOS=ADJ Degree=Pos Derivation=Sti <AffixType=Suffix> ↲
 <CMP=2> <W=15000>
	"yksi#-mielinen#es#ti" UPOS=NOUN Number=Sing Case=Nom <SemType=Time> ↲
 <CMP=4> <W=35000>
	"yksi#-mielisesti" UPOS=ADV <AffixType=Suffix> <Lexicalised=Sti> ↲
 <CMP=2> <W=10000>
	"yksimielinen" UPOS=ADJ Degree=Pos Derivation=Sti <CMP=1> <W=5000>
	"yksimielinen#es#ti" UPOS=NOUN Number=Sing Case=Nom <SemType=Time> ↲
 <CMP=3> <W=25000>
	"yksimielisesti" UPOS=ADV <Lexicalised=Sti> <CMP=1> <W=0>
"<maanantaina>"
	"maanantai" UPOS=NOUN Number=Plur Case=Ess <CMP=1> <W=0>
	"maanantai" UPOS=NOUN Number=Sing Case=Ess <CMP=1> <W=0>
	"maanantaina" UPOS=ADV <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>


"<Juankosken>"
	"Juankoski" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
	"juan#koski" UPOS=NOUN Number=Sing Case=Gen <CMP=2> <W=10000>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
	"kaupunki#valtuus#to" UPOS=NOUN Number=Sing Case=Nom <CMP=3> <W=20000>
	"kaupunki#valtuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=2> <W=10000>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Past Number=Sing ↲
 Person=0 <CMP=1> <W=0>
	"hyväksyä" UPOS=VERB Voice=Act VerbForm=Fin Mood=Ind Tense=Past Number=Sing ↲
 Person=3 <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<viime>"
	"viime" UPOS=ADJ Degree=Pos Number=Sing Case=Nom <CMP=1> <W=0>
	"viime" UPOS=ADV <CMP=1> <W=0>
"<viikolla>"
	"viikko" UPOS=NOUN Number=Sing Case=Ade <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>
...
```

### omorfi-analyse-text.sh

Traditional Finite-State Morphology produces all possible hypotheses of each
input token in tabular format. This format uses so-called raw omorfi style
analysis strings. This can be created with `omorfi-analyse-text.sh`:

```console
$ omorfi-analyse-text.sh test/test.text
Juankosken	[WORD_ID=Juankoski][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Juankosken	[WORD_ID=juan][UPOS=NOUN][SEM=CURRENCY][NUM=SG][CASE=NOM]↲
            [BOUNDARY=COMPOUND][WORD_ID=koski][UPOS=NOUN][NUM=SG][CASE=GEN]

kaupunki	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=NOM]

liittyy	[WORD_ID=liittyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT]↲
        [PERS=SG0]
liittyy	[WORD_ID=liittyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT]↲
        [PERS=SG3]

Kuopion	[WORD_ID=Kuopio][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Kuopion	[WORD_ID=kuopia][UPOS=VERB][VOICE=ACT][MOOD=OPT][PERS=SG1]↲
        [STYLE=ARCHAIC]

kaupunkiin	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=ILL]

vuoden	[WORD_ID=vuoden][UPOS=ADV]
vuoden	[WORD_ID=vuosi][UPOS=NOUN][NUM=SG][CASE=GEN]

2017	[WORD_ID=2017][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD]
2017	[WORD_ID=2017][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD][NUM=SG][CASE=NOM]

alussa	[WORD_ID=alku][UPOS=NOUN][NUM=SG][CASE=INE]
alussa	[WORD_ID=alunen][UPOS=NOUN][NUM=SG][CASE=ESS][STYLE=ARCHAIC]
alussa	[WORD_ID=alussa][UPOS=ADP][ADPTYPE=POST]
alussa	[WORD_ID=alussa_2][UPOS=ADV]

.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]

Kuopion	[WORD_ID=Kuopio][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Kuopion	[WORD_ID=kuopia][UPOS=VERB][VOICE=ACT][MOOD=OPT][PERS=SG1]↲
        [STYLE=ARCHAIC]

kaupunginvaltuusto	[WORD_ID=kaupunginvaltuusto][UPOS=NOUN][NUM=SG][CASE=NOM]
kaupunginvaltuusto	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=GEN]↲
                    [BOUNDARY=COMPOUND][WORD_ID=valtuusto][UPOS=NOUN]↲
                    [NUM=SG][CASE=NOM]

hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST]↲
            [PERS=SG0]
hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST]↲
            [PERS=SG3]

liitoksen	[WORD_ID=liitos][UPOS=NOUN][NUM=SG][CASE=GEN]

yksimielisesti	[WORD_ID=yksi][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM]↲
                [BOUNDARY=COMPOUND][WORD_ID=-mielinen][UPOS=ADJ]↲
                [SUBCAT=SUFFIX][CMP=POS][CMP=POS][DRV=STI]
yksimielisesti	[WORD_ID=yksi][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM]↲
                [BOUNDARY=COMPOUND][WORD_ID=-mielisesti][UPOS=ADV]↲
                [SUBCAT=SUFFIX][LEX=STI]
yksimielisesti	[WORD_ID=yksimielinen][UPOS=ADJ][CMP=POS][CMP=POS][DRV=STI]
yksimielisesti	[WORD_ID=yksimielisesti][UPOS=ADV][LEX=STI]

maanantaina	[WORD_ID=maanantai][UPOS=NOUN][NUM=PL][CASE=ESS]
maanantaina	[WORD_ID=maanantai][UPOS=NOUN][NUM=SG][CASE=ESS]
maanantaina	[WORD_ID=maanantaina][UPOS=ADV]

.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]

Juankosken	[WORD_ID=Juankoski][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Juankosken	[WORD_ID=juan][UPOS=NOUN][SEM=CURRENCY][NUM=SG][CASE=NOM]↲
            [BOUNDARY=COMPOUND][WORD_ID=koski][UPOS=NOUN][NUM=SG][CASE=GEN]

kaupunginvaltuusto	[WORD_ID=kaupunginvaltuusto][UPOS=NOUN][NUM=SG][CASE=NOM]
kaupunginvaltuusto	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=GEN]↲
                    [BOUNDARY=COMPOUND][WORD_ID=valtuusto][UPOS=NOUN]↲
                    [NUM=SG][CASE=NOM]

hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST]↲
            [PERS=SG0]
hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST]↲
            [PERS=SG3]

liitoksen	[WORD_ID=liitos][UPOS=NOUN][NUM=SG][CASE=GEN]

viime	[WORD_ID=viime][UPOS=ADV]
viime	[WORD_ID=viime_2][UPOS=ADJ][CMP=POS][NUM=SG][CASE=NOM]

viikolla	[WORD_ID=viikko][UPOS=NOUN][NUM=SG][CASE=ADE]

.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]
```

### omorfi-analyse-tokenised.sh

If your text is already split into word-forms (one word-form per line), it can
be analysed faster with `omorfi-analyse-tokenised.sh` tool:

```
$ omorfi-analyse-tokenised.sh test/wordforms.list
.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]	0,000000

1	[WORD_ID=1][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD]	0,000000
1	[WORD_ID=1][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD][NUM=SG][CASE=NOM]↲
	0,000000

10	[WORD_ID=10][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD]	0,000000
10	[WORD_ID=10][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD][NUM=SG][CASE=NOM]↲
	0,000000

1 000	[WORD_ID=1 000][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD]	0,000000
1 000	[WORD_ID=1 000][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD][NUM=SG][CASE=NOM]↲
	0,000000
...
Strings	Found	Missing	Results
6285	6285	0	11307
Coverage	Ambiguity
1,000000	1,799045
```


### omorfi-conllu.bash

[Universal Dependencies](http://universaldependencies.org) are the up-and-coming
standard for all your morpho-syntactic needs! Omorfi is currently scheduled to
follow up on Universal dependencies relaeas schedules and analysis and design
principles. Omorfi can fill in the LEMMA, UPOS, and UFEAT morphological feature
field, also the MISC field is used for omorfi data that is not covered by
CONLL-U.

Use `omorfi-conllu.bash` for basic parsing:

```console
$ omorfi-conllu.bash test/test.text
reading from <stdin>
# new doc id= <stdin>
# sent_id = 1
# text = Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa.
1	Juankosken	Juankoski	PROPN	N	Case=Gen|Number=Sing	_	_	_↲
	Weight=0.0
2	kaupunki	kaupunki	NOUN	N	Case=Nom|Number=Sing	_	_	_↲
	Weight=0.0
3	liittyy	liittyä	VERB	V	Mood=Ind|Number=Sing|Person=0|Tense=Pres|↲
VerbForm=Fin|Voice=Act  _	_	_	Weight=0.0
4	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
5	kaupunkiin	kaupunki	NOUN	N	Case=Ill|Number=Sing	_	_	_↲
	Weight=0.0
6	vuoden	vuoden	ADV	Adv	_	_	_	_	Weight=0.0
7	2017	2017	NUM	Num	NumType=Card	_	_	_	Weight=0.0
8	alussa	alku	NOUN	N	Case=Ine|Number=Sing	_	_	_	Weight=0.0
9	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0

# sent_id = 2
# text = Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti↲
# maanantaina.
1	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
2	kaupunginvaltuusto	kaupunginvaltuusto	NOUN	N	Case=Nom|Number=Sing↲
	_	_	_	Weight=0.0
3	hyväksyi	hyväksyä	VERB	V	Mood=Ind|Number=Sing|Person=0|↲
Tense=Past|VerbForm=Fin|Voice=Act\
_	_	_	Weight=0.0
4	liitoksen	liitos	NOUN	N	Case=Gen|Number=Sing	_	_	_↲
	Weight=0.0
5	yksimielisesti	yksimielisesti	ADV	Adv	_	_	_	_	Weight=0.0
6	maanantaina	maanantai	NOUN	N	Case=Ess|Number=Plur	_	_	_↲
	Weight=0.0
7	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0

# sent_id = 3
# text = Juankosken kaupunginvaltuusto hyväksyi liitoksen viime viikolla.
1	Juankosken	Juankoski	PROPN	N	Case=Gen|Number=Sing	_	_	_↲
	Weight=0.0
2	kaupunginvaltuusto	kaupunginvaltuusto	NOUN	N	Case=Nom|Number=Sing↲
	_	_	_	Weight=0.0
3	hyväksyi	hyväksyä	VERB	V	Mood=Ind|Number=Sing|Person=0|↲
Tense=Past|VerbForm=Fin|Voice=Act   _	_	_	Weight=0.0
4	liitoksen	liitos	NOUN	N	Case=Gen|Number=Sing	_	_	_↲
	Weight=0.0
5	viime	viime	ADV	Adv	_	_	_	_	Weight=0.0
6	viikolla	viikko	NOUN	N	Case=Ade|Number=Sing	_	_	_↲
	Weight=0.0
7	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0
```

For more options there is a python script `omorfi-conllu.py`.

### omorfi-ftb3.bash

Omorfi can output FTB3.1-compatible format with `omorfi-ftb3.bash`:

```console
$ omorfi-ftb3.bash test/test.text
reading from <stdin>
<s><loc file="<stdin>" line="1" />
1	Juankosken	Juankoski	N	N	N Prop Sg Gen Prop	_	_	_	_
2	kaupunki	kaupunki	N	N	N Sg Nom	_	_	_	_
3	liittyy	liittyä	V	V	V Act Prs Sg3	_	_	_	_
4	Kuopion	Kuopio	N	N	N Prop Sg Gen Prop	_	_	_	_
5	kaupunkiin	kaupunki	N	N	N Sg Ill	_	_	_	_
6	vuoden	vuoden	Adv	Adv	Adv	_	_	_	_
7	2017	2017	Num	Num	Num Digit	_	_	_	_
8	alussa	alku	N	N	N Sg Ine	_	_	_	_
9	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="2" />
1	Kuopion	Kuopio	N	N	N Prop Sg Gen Prop	_	_	_	_
2	kaupunginvaltuusto	kaupunginvaltuusto	N	N	N Sg Nom	_	_	_	_
3	hyväksyi	hyväksyä	V	V	V Act Prt Sg3	_	_	_	_
4	liitoksen	liitos	N	N	N Sg Gen	_	_	_	_
5	yksimielisesti	yksimielisesti	Adv	Adv	Adv Pos Man	_	_	_	_
6	maanantaina	maanantai	N	N	N Pl Ess	_	_	_	_
7	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="3" />
1	Juankosken	Juankoski	N	N	N Prop Sg Gen Prop	_	_	_	_
2	kaupunginvaltuusto	kaupunginvaltuusto	N	N	N Sg Nom	_	_	_	_
3	hyväksyi	hyväksyä	V	V	V Act Prt Sg3	_	_	_	_
4	liitoksen	liitos	N	N	N Sg Gen	_	_	_	_
5	viime	viime	Adv	Adv	Adv	_	_	_	_
6	viikolla	viikko	N	N	N Sg Ade	_	_	_	_
7	.	.	Punct	Punct	Punct	_	_	_	_
</s>
```

### omorfi-freq-evals.bash

It is possible to get naïve coverage estimates with `omorfi-freq-evals.bash`:

```console
$ omorfi-freq-evals.bash test/test.text
reading from <stdin>
1	OOV	Shinzo
CPU time: 0.01207244099999999 real time: 0.025647345988545567
Lines	Covered	OOV
110	109	1
100.0	99.0909090909091	0.9090909090909091
Types	Covered	OOV
87	86	1
100.0	98.85057471264368	1.1494252873563218
```

The python script `omorfi-freq-evals.py` has further options including
Precision/Recall analysis over string matches.

### omorfi-tokenise.bash

Most tools will handle tokenisation internally, if you want to see the
intermediate steps or just tokenise, you can invoke
`omorfi-tokenise.bash` directly:

```console
$ omorfi-tokenise.bash -X test/test.text
Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa .
Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina .
Juankosken kaupunginvaltuusto hyväksyi liitoksen viime viikolla .

```

For more output formats and options, the python script `omorfi-tokenise.py` is
available.

### omorfi-segment.bash

Omorfi can be used to segment word-forms into sub-word units with
`omorfi-segment.sh`:

```console
$ omorfi-segment.sh test/test.text
Juankosken kaupunki liitty→ ←y Kuopion kaupunki→ ←in vuode→ ←n 2017 alussa.
Kuopion kaupungin→ ←valtuusto hyväksy→ ←i liitokse→ ←n yksi→ ←mielisesti↲
 maanantaina.
Juankosken kaupungin→ ←valtuusto hyväksy→ ←i liitokse→ ←n viime viikolla.
...
```

For further options there is a `omorfi-segment.py` python script.

**Preliminary** support for labeled segmentation is also available but not
guaranteed to work.

### omorfi-spell.sh

Spelling correction may be done if hfst-ospell is installed using
`omorfi-spell.sh`:

```console
$ omorfi-spell.sh test/wordforms.list | tail
"äristä" is in the lexicon...
"äyräs" is in the lexicon...
"äyräässä" is in the lexicon...
"äänestys" is in the lexicon...
"äänioikeus" is in the lexicon...
"öykkärein" is in the lexicon...
"öykkäri" is in the lexicon...
"öykkärimpi" is in the lexicon...
"öykkäröi" is in the lexicon...
"öykkäröidä" is in the lexicon...
```

For more functionality you should use `hfst-ospell` directly.

### omorfi-generate.sh

Generating word-forms can be done using `omorfi-generate.sh`:

```console
$ omorfi-generate.sh

[WORD_ID=kissa][UPOS=NOUN][NUM=SG][CASE=INE]
[WORD_ID=kissa][UPOS=NOUN][NUM=SG][CASE=INE]	kissassa	0,000000
```

The input for generator is simply the output of the raw analyser.

Generation has not been used so much because I have no use cases.

There's some convenience scripts (not installed) in the `src/bash`, here's a
classical example by Fred Karlsson of generating all forms of a noun *kauppa* (a
shop) in Finnish.  [He lists 2,253
forms](https://www.ling.helsinki.fi/~fkarlsso/genkau2.html), our current version
is [here containing 6,602 forms of word *kauppa*](genkau3.html).  And here's the
execution:

```
echo kauppa > kauppa.wordlist
bash src/bash/generate-wordlist.sh kauppa.wordlist kauppa.wordforms
hfst-lookup src/generated/omorfi.describe.hfst -q < kauppa.wordforms |\
	sed -e 's/\[WORD_ID=kauppa\]\[UPOS=//' |\
	tr '][' '  ' | tr -s '\n' | sed -e 's/[0-9, ]*$//' |\
	fgrep -v DRV | fgrep -v COMPOUND | fgrep -v WORD_ID=kaupata
```

The third step is to regenerate the analyses and select only forms that we feel
are part of inflection and not derivation or compounding.

### omorfi-factorise.bash

*NB:* _This format is not actively developed any more as moses is getting kind
of obsolete in favor of neural machine translation platforms._

It is possible to produce a so-called factored output for use in conjunction
with [https://statmt.org/moses/] to create morphologically informed statistical
machine translation. Use omorfi-factorise.bash for this:

```
$ bash src/bash/omorfi-factorise.bash test/test.text
Juankosken|Juankoski|PROPN|Number=Sing.Case=Gen|Juankosken↲
kaupunki|kaupunki|NOUN|Number=Sing.Case=Nom|kaupunki↲
liittyy|liittyä|VERB|Voice=Act.↲
VerbForm=Fin.Mood=Ind.Tense=Pres.Number=Sing.Person=0|liitty.y↲
Kuopion|Kuopio|PROPN|Number=Sing.Case=Gen|Kuopion↲
kaupunkiin|kaupunki|NOUN|Number=Sing.Case=Ill|kaupunki.in↲
vuoden|vuoden|ADV||vuode.n↲
2017|2017|NUM|NumType=Card|2017↲
alussa|alku|NOUN|Number=Sing.Case=Ine|alus.sa↲
.|.|PUNCT||.↲

```

## Python scripts and pipeline building

The following scripts are included:

1. src/python/omorfi-download.py
1. src/python/omorfi-conllu.py
1. src/python/omorfi-factorise.py
1. src/python/omorfi-freq-evals.py
1. src/python/omorfi-ftb3.py
1. src/python/omorfi-ner.py
1. src/python/omorfi-segment.py
1. src/python/omorfi-sigmorphons.py
1. src/python/omorfi-tokenise.py
1. src/python/omorfi-unimorph.py
1. src/python/omorfi-vislcg.py

The python versions of the scripts are for more advanced usage. Their
invocations  all follow approximately the same format as the bash scripts',
however, the input is always given with `-i INFILE` switch, the output is always
specified with the `-o OUTFILE` switch, and you must provide the language model
with the `-a MODELFILE` switch.  For the small model, use `omorfi.analyse.hfst`
and for the larger model `omorfi.describe.hfst`.

With python scripts, you need to always build the whole pipeline, including
tokenisation and selecting correct formats. E.g.:

```
omorfi-tokenise.py -a src/generated/omorfi.describe.hfst \
  -i test/test.text -O conllu |\
	omorfi-conllu.py -a src/generated/omorfi.describe.hfst
```

### omorfi-tokenise.py

Most python pipelines must start from tokenisation:

```
omorfi-tokenise.py -a src/generated/omorfi.describe.hfst \
  -i test/test.text -O conllu
```

The format to use is dependent on the task usually, e.g. conllu for dependency
analysis and ftb3 for legacy data.

E.g. for CONLL-U and so Universal dependencies, you can use `omorfi-tokenise.py
-O conllu`:

```
$ omorfi-tokenise.py -a /usr/local/share/omorfi/omorfi.describe.hfst \
  -i test/test.text -O conllu
# new doc id= test/test.text
# sent_id = 1
# text = Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa.
1	Juankosken	_	_	_	_	_	_	_	_
2	kaupunki	_	_	_	_	_	_	_	_
3	liittyy	_	_	_	_	_	_	_	_
4	Kuopion	_	_	_	_	_	_	_	_
5	kaupunkiin	_	_	_	_	_	_	_	_
6	vuoden	_	_	_	_	_	_	_	_
7	2017	_	_	_	_	_	_	_	_
8	alussa	_	_	_	_	_	_	_	_
9	.	_	_	_	_	_	_	_	_

# sent_id = 2
# text = Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti↲
# maanantaina.
1	Kuopion	_	_	_	_	_	_	_	_
2	kaupunginvaltuusto	_	_	_	_	_	_	_	_
3	hyväksyi	_	_	_	_	_	_	_	_
4	liitoksen	_	_	_	_	_	_	_	_
5	yksimielisesti	_	_	_	_	_	_	_	_
6	maanantaina	_	_	_	_	_	_	_	_
7	.	_	_	_	_	_	_	_	_

# sent_id = 3
# text = Juankosken kaupunginvaltuusto hyväksyi liitoksen viime viikolla.
1	Juankosken	_	_	_	_	_	_	_	_
2	kaupunginvaltuusto	_	_	_	_	_	_	_	_
3	hyväksyi	_	_	_	_	_	_	_	_
4	liitoksen	_	_	_	_	_	_	_	_
5	viime	_	_	_	_	_	_	_	_
6	viikolla	_	_	_	_	_	_	_	_
7	.	_	_	_	_	_	_	_	_

...
```

# Programming interfaces / bindings

→ See also: [API
design](https://flammie.github.io/omorfi/API-Design.html), [generated API
docs](https://flammie.github.io/omorfi/api/html/)

The bash and python scripts provided are suitable for specific tasks they were
written for, for any other uses, there are programming language bindings
available as well as the language models themselves, which you can use and
manipulate with suitable tools.

One main design choice I have in the APIs is that I want to provide a simple API
first, that basically works like:

1. find language model file
1. open and load language model
1. analyse wordform
1. iterate analyses

anything beyond that is hidden on more complex data structures and functions,
but the basic ~5 lines of code should work in any programming language like that
for the most common use case.

## Python

Python interface is in package `omorfi`, the base interface contains `load`
function and `find_omorfi` convenience function; the loaded object should always
have an analyse method that returns iterable analyses with more information:

```
$ python
Python 3.5.7 (default, Nov 25 2019, 07:48:48)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import omorfi
>>> analyser = omorfi.load("/usr/local/share/omorfi/omorfi.describe.hfst")
>>> analyses = analyser.analyse("alusta")
>>> for analysis in analyses:
...     print(analysis.get_lemmas(), analysis.get_upos(),
              analysis.printable_ud_feats())
...
['alku'] NOUN Case=Ela|Number=Sing
['alunen'] NOUN Case=Par|Number=Sing
['alus'] NOUN Case=Par|Number=Sing
['alusta'] NOUN Case=Nom|Number=Sing
['alusta'] ADV _
['alusta'] ADV _
['alustaa'] VERB Mood=Imp|Number=Sing|Person=2|VerbForm=Fin|Voice=Act
['alustaa'] VERB Connegative=Yes|Mood=Ind|Tense=Pres|VerbForm=Fin
>>>
```

Any other part of the omorfi API is subject to change...

## Java

Java class `com.github.flammie.omorfi.Omorfi` has an example implementation with
a simple input loop.

```
$ java com.github.flammie.omorfi.Omorfi
```

The basic interface is based on the class methods `loadAnalyser` and `analyse`,
which returns an iterable collection of analyses (Strings at the moment).

```java

import com.github.flammie.omorfi.Omorfi;

...

Omorfi omorfi = new Omorfi();
omorfi.loadAnalyser("/usr/share/omorfi/omorfi.describe.hfstol");
Collection<String> analyses = omorfi.analyse("talossa");
for (String analysis : analyses) {
    System.out.println(analysis);
}
```

## C++

The header `omorfi.hh` and the library `libomorfi` has basic interface for
loading and running omorfi language models. There is an example command-line
tool with input loop in `omorfi-lookup.cc`:

```
$ ./omorfi-lookup /usr/share/omorfi/omorfi.describe.hfst
```

The basic interface is based on `omorfi::Omorfi` class and methods
`loadAnalyser` and `analyse` which returns a data structure containing analyses
that can be iterated with foreach:

```c++
#include "omorfi.hh"
...
omorfi::omorfi Omorfi;
omorfi.loadAnalyser("/usr/share/omorfi/omorfi.describe.hfst");
auto& analyse = omorfi.analyse("talossa");
for (auto& analysis : analyses) {
  std::cout << analysis << std::endl;
}
```

## Other programming language bindings

I would be happy to have more programming language bindings, most are dependent
on what HFST has been ported to since we depend on it for our language models.

## Raw automata

Most of language models are finite-state automata binaries for
[HFST](//hfst.github.io).  The installed files are in `$prefix/share/omorfi` (my
installation is in linux default: `/usr/local`)

```
$ ls -1 /usr/local/share/omorfi/
master.tsv
omorfi.accept.hfst
omorfi.analyse.hfst
omorfi.cg3bin
omorfi.describe.hfst
omorfi-ftb3.analyse.hfst
omorfi-ftb3.generate.hfst
omorfi.generate.hfst
omorfi-giella.analyse.hfst
omorfi-giella.generate.hfst
omorfi.hyphenate-rules.hfst
omorfi.labelsegment.hfst
omorfi.lemmatise.hfst
omorfi-omor.analyse.hfst
omorfi-omor.generate.hfst
omorfi-omor_recased.analyse.hfst
omorfi_recased.analyse.hfst
omorfi_recased.describe.hfst
omorfi.segment.hfst
omorfi.tokenise.hfst
speller-omorfi.zhfst
```

The naming is probably not gonna be same forever, but should be pretty
similar and comprehensible in future versions too.

### HFST tools

You can directly access specific automata using finite-state tools from the HFST
project (details can be found on their individual man pages and
[HFST github site](//hfst.github.io):

```
hfst-lookup /usr/local/share/omorfi/omorfi.segment.hfst
> talossani
talossani	talo{DB}s{MB}sa{MB}ni	0,000000
talossani	talo{MB}ssa{MB}ni	0,000000

> on
on	on	0,000000

> hirveä
hirveä	hirve{MB}ä	0,000000
hirveä	hirveä	0,000000

> kissakoira-apina
kissakoira-apina	kissa{hyph?}koira{hyph?}apina	0,000000
```

When using `hfst-lookup` with large unclean material, it may get stuck at odd
looking long strings, consider using `-t` switch to set timeout for individual
analyses; omorfi bash and python APIs set this to 15 seconds.

