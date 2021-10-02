# Omorfi usage

Omorfi can be used with convenience command-line scripts, manually, using
programming language bindings / APIs, etc. This page gives you few basic
examples to get going. We assume here you have done [full
installation](install.html), if you did a *python only* installation you can
only use python examples.

## Bash-based tools

The bash-based command line tools are easiest to use, as they combine multiple
operations into pipeline, select language models automatically and so forth.The
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

```
$
```

When following the instructions, please do not copy/paste the dollar sign, it is
not a part of the command, but a command-line prompt indicator!

The example texts used here are part of omorfi distribution:

```
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

**NB:** The examples below use the extended dictionary, `-X`, for more
information of this, see the [Notes about lexicon sizes](Smaller-lexicons.html).

The output in examples is re-wrapped to fit browser windows and editors, some of
the lines in the real world output will be very long. I use the ↲ symbol to
indicate such wraps.

### Download models

If you haven't built omorfi manually with `./configure && make && make install`,
it is possible to get some of the models for analysis from the internet (the
long URLs redacted from output, note this was on pre-release version so your
output should be slightly different):

```
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

### Analyse and disambiguate

This is probably what most users want.

```
$ omorfi-disambiguate-text.sh -X test/test.text
Lines: 10 Tokens: 110 Ratio: 11.0 tokens/line
CPU time: 0.034928154000000045 Real time: 0.03501545637845993
Tokens per timeunit: 3141.469835808494 Lines per timeunit: 285.5881668916813
"<Juankosken>"
	"Juankoski" UPOS=PROPN Case=Gen Number=Sing <PropnType=Geo> <CMP=1> <W=0>
"<kaupunki>"
	"kaupunki" UPOS=NOUN Case=Nom Number=Sing <CMP=1> <W=0>
"<liittyy>"
	"liittyä" UPOS=VERB Number=Sing Person=3 Voice=Act VerbForm=Fin Tense=Pres↲
              Mood=Ind <CMP=1> <W=0>
"<Kuopion>"
	"Kuopio" UPOS=PROPN Case=Gen Number=Sing <PropnType=Geo> <CMP=1> <W=0>
"<kaupunkiin>"
	"kaupunki" UPOS=NOUN Case=Ill Number=Sing <CMP=1> <W=0>
"<vuoden>"
	"vuoden" UPOS=ADV <CMP=1> <W=0>
	"vuosi" UPOS=NOUN Case=Gen Number=Sing <CMP=1> <W=0>
"<2017>"
	"2017" UPOS=NUM NumType=Card <NumType=Digit> <CMP=1> <W=0>
	"2017" UPOS=NUM Case=Nom Number=Sing NumType=Card <NumType=Digit> ↲
           <CMP=1> <W=0>
"<alussa>"
	"alku" UPOS=NOUN Case=Ine Number=Sing <CMP=1> <W=0>
	"alussa" UPOS=ADV <CMP=1> <W=0>
	"alussa" UPOS=ADP AdpType=Post <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>

"<Kuopion>"
	"Kuopio" UPOS=PROPN Case=Gen Number=Sing <PropnType=Geo> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Case=Nom Number=Sing <CMP=1> <W=0>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Number=Sing Person=3 Voice=Act VerbForm=Fin ↲
               Tense=Past Mood=Ind <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Case=Gen Number=Sing <CMP=1> <W=0>
"<yksimielisesti>"
	"yksimielisesti" UPOS=ADV <Lexicalised=Sti> <CMP=1> <W=0>
"<maanantaina>"
	"maanantaina" UPOS=ADV <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>

"<Juankosken>"
	"Juankoski" UPOS=PROPN Case=Gen Number=Sing <PropnType=Geo> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Case=Nom Number=Sing <CMP=1> <W=0>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Number=Sing Person=3 Voice=Act VerbForm=Fin ↲
               Tense=Past Mood=Ind <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Case=Gen Number=Sing <CMP=1> <W=0>
"<viime>"
	"viime" UPOS=ADV <CMP=1> <W=0>
	"viime" UPOS=ADJ Case=Nom Number=Sing Degree=Pos <CMP=1> <W=0>
"<viikolla>"
	"viikko" UPOS=NOUN Case=Ade Number=Sing <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>
...
# Tokens: 110
# Unknown: 3 2.727272727272727 %
# CPU time: 0.15221513399999997
# Real time: 0.20484047383069992
# Tokens per timeunit: 537.003249127976

```

Compare this to the [Analyses without disambiguation](#Analyses without
disambiguation (VISL-CG3 format)) below to determine which one is more suitable
for your research.

For advanced usage options there is `omorfi-vislcg.py` python script.

#### Analysis without disambiguation (VISL-CG3 format)

It is possible to view the full ambiguous analyses in this format as well, i.e.
before the CG rules try to remove most unlikely things. To do so, use
omorfi-vislcg3.bash script:

```
$ omorfi-vislcg.bash -X test/test.text
...
"<Juankosken>"
	"Juankoski" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
	"juan#koski" UPOS=NOUN Number=Sing Case=Gen <CMP=2> <W=10000>
"<kaupunki>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<liittyy>"
	"liittyä" UPOS=VERB Mood=Ind Number=Sing Tense=Pres Person=0 Voice=Act ↲
              VerbForm=Fin <CMP=1> <W=0>
	"liittyä" UPOS=VERB Mood=Ind Number=Sing Tense=Pres Person=3 Voice=Act ↲
              VerbForm=Fin <CMP=1> <W=0>
"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunkiin>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Ill <CMP=1> <W=0>
"<vuoden>"
	"vuoden" UPOS=ADV <CMP=1> <W=0>
	"vuosi" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<2017>"
	"2017" UPOS=NUM NumType=Card <NumType=Digit> <CMP=1> <W=0>
	"2017" UPOS=NUM Number=Sing NumType=Card Case=Nom <NumType=Digit> ↲
           <CMP=1> <W=0>
"<alussa>"
	"alku" UPOS=NOUN Number=Sing Case=Ine <CMP=1> <W=0>
	"alunen" UPOS=NOUN Style=Arch Number=Sing Case=Ess <CMP=1> <W=0>
	"alussa" UPOS=ADP AdpType=Post <CMP=1> <W=0>
	"alussa" UPOS=ADV <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>


"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
	"kuopia" UPOS=VERB Style=Arch Number=Sing Person=1 Voice=Act ↲
             VerbForm=Fin <Mood=Opt> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
	"kaupunki#valtuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=2> <W=10000>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Mood=Ind Number=Sing Tense=Past Person=0 ↲
               Voice=Act VerbForm=Fin <CMP=1> <W=0>
	"hyväksyä" UPOS=VERB Mood=Ind Number=Sing Tense=Past Person=3 ↲
               Voice=Act VerbForm=Fin <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<yksimielisesti>"
	"yksi#-mielinen" UPOS=ADJ Degree=Pos Derivation=Sti <AffixType=Suffix> ↲
                     <CMP=2> <W=15000>
	"yksi#-mielisesti" UPOS=ADV <Lexicalised=Sti> <AffixType=Suffix> ↲
                       <CMP=2> <W=10000>
	"yksimielinen" UPOS=ADJ Degree=Pos Derivation=Sti <CMP=1> <W=5000>
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
	"kaupunki#valtuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=2> <W=10000>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Mood=Ind Number=Sing Tense=Past Person=0 ↲
               Voice=Act VerbForm=Fin <CMP=1> <W=0>
	"hyväksyä" UPOS=VERB Mood=Ind Number=Sing Tense=Past Person=3 ↲
               Voice=Act VerbForm=Fin <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<viime>"
	"viime" UPOS=ADV <CMP=1> <W=0>
	"viime" UPOS=ADJ Degree=Pos Number=Sing Case=Nom <CMP=1> <W=0>
"<viikolla>"
	"viikko" UPOS=NOUN Number=Sing Case=Ade <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>
...
```

### Xerox / Finite-State Morphology style analysis

Traditional Finite-State Morphology produces all possible hypotheses of each
input token in tabular format. This format uses so-called raw omorfi style
analysis strings. This can be created with `omorfi-analyse-text.sh`:

```
$ omorfi-analyse-text.sh -X test/test.text
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

If your text is already split into word-forms (one word-form per line), it can
be analysed faster with `omorfi-analyse-tokenised.sh` tool:

```
$ omorfi-analyse-tokenised.sh -X test/wordforms.list
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
6285	6285	0	10866
Coverage	Ambiguity
1,000000	1,728878
```


### Analysis into CONLL-U / Universal Dependencies format

[Universal Dependencies](http://universaldependencies.org) are the up-and-coming
standard for all your morpho-syntactic needs! Omorfi is currently scheduled to
follow up on Universal dependencies relaeas schedules and analysis and design
principles. Omorfi can fill in the LEMMA, UPOS, and UFEAT morphological feature
field, also the MISC field is used for omorfi data that is not covered by
CONLL-U.

Use `omorfi-conllu.bash` for basic parsing:

```
$ omorfi-conllu.bash -X test/test.text
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

### FTB3.1 analysis

Omorfi can output FTB3.1-compatible format with `omorfi-ftb3.bash`:

```
$ omorfi-ftb3.bash -X test/test.text
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

### Coverage analysis

It is possible to get naïve coverage estimates with `omorfi-freq-evals.bash`:

```
$ omorfi-freq-evals.bash -X test/test.text
reading from <stdin>
1	OOV	Shinzo
1	OOV	Narendra
CPU time: 0.112268327 real time: 0.13999610301107168
Lines	Covered	OOV
110	108	2
100.0	98.18181818181819	1.8181818181818181
Types	Covered	OOV
87	85	2
100.0	97.70114942528735	2.2988505747126435
needs to have 99 % coverage to pass regress test
 please examine <stdout> for regressions
```

The python script `omorfi-freq-evals.py` has further options including
Precision/Recall analysis over string matches.

### Raw text tokenisation

Most tools will handle tokenisation internally, if you want to see the
intermediate steps for example, you can invoke `omorfi-tokenise.bash` directly:

```
$ omorfi-tokenise.bash -X test/test.text
Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa .
Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina .
Juankosken kaupunginvaltuusto hyväksyi liitoksen viime viikolla .

```

For more output formats and options, the python script `omorfi-tokenise.py` is
available.

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



### Morphological segmentation

Omorfi can be used to segment word-forms into sub-word units with
`omorfi-segment.bash`:

```
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

### Spell-Checking and correction

Spelling correction may be done if hfst-ospell is installed using
`omorfi-spell.sh`:

```
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

The omorfi.zhfst that is built in omorfi could be a drop-in replacement for
voikko and giellatekno, but theirs is curated for specific purpose of
spell-checking whereas omorfi is large-coverage dictionary so ymmv, I (Flammie)
like my spell-checker to recognise and suggest obscure and obscene terms but
pit's not for everyone.

### Morphological generation

Generating word-forms can be done using `omorfi-generate.sh`:

```
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

### Moses factored format

*NB:* _This format is not actively developed any more as moses is getting kind
of obsolete in favor of neural machine translation platforms._

It is possible to produce a so-called factored output for use in conjunction
with [https://statmt.org/moses/] to create morphologically informed statistical
machine translation. Use omorfi-factorise.bash for this:

```
$ bash src/bash/omorfi-factorise.bash -X test/test.text
Juankosken|Juankoski|PROPN|Number.Case|Juankosken↲
kaupunki|kaupunki|NOUN|Number.Case|kaupunki↲
liittyy|liittyä|VERB|Number.Person.Tense.Voice.Mood.VerbForm|liitty.y↲
Kuopion|Kuopio|PROPN|Number.Case|Kuopion↲
kaupunkiin|kaupunki|NOUN|Number.Case|kaupunki.in↲
vuoden|vuoden|ADV||vuode.n↲
2017|2017|NUM|NumType|2017↲
alussa|alku|NOUN|Number.Case|alus.sa↲
.|.|PUNCT||.↲

Kuopion|Kuopio|PROPN|Number.Case|Kuopion↲
kaupunginvaltuusto|kaupunginvaltuusto|NOUN|Number.Case|kaupungin.valtuusto↲
hyväksyi|hyväksyä|VERB|Number.Person.Tense.Voice.Mood.VerbForm|hyväksy.i↲
liitoksen|liitos|NOUN|Number.Case|liitokse.n↲
yksimielisesti|yksimielisesti|ADV||yksi.mielisesti↲
maanantaina|maanantai|NOUN|Number.Case|maanantai.na↲
.|.|PUNCT||.↲

Juankosken|Juankoski|PROPN|Number.Case|Juankosken↲
kaupunginvaltuusto|kaupunginvaltuusto|NOUN|Number.Case|kaupungin.valtuusto↲
hyväksyi|hyväksyä|VERB|Number.Person.Tense.Voice.Mood.VerbForm|hyväksy.i↲
liitoksen|liitos|NOUN|Number.Case|liitokse.n↲
viime|viime|ADV||viime↲
viikolla|viikko|NOUN|Number.Case|viiko.lla↲
.|.|PUNCT||.↲

```

## Python scripts and pipeline building

The python versions of the scripts are for more advanced usage. Their
invocations  all follow approximately the same format as the bash scripts',
however, the input is always given with `-i INFILE` switch, the output is always
specified with the `-o OUTFILE` switch, and you must provide the language model
with the `-a MODELFILE` switch.  For the small model, use `omorfi.analyse.hfst`
and for the larger model `omorfi.describe.hfst`.  You must also always build
your whole pipeline, including tokenisation and selecting correct formats. E.g.:

```
omorfi-tokenise.py -a src/generated/omorfi.describe.hfst \
  -i test/test.text -O conllu |\
	omorfi-conllu.py -a src/generated/omorfi.describe.hfst
reading from <stdin>
Lines: 10 Tokens: 110 Ratio: 11.0 tokens/line
CPU time: 0.006683539000000002 Real time: 0.006686871871352196
Tokens per timeunit: 16450.14322335986 Lines per timeunit: 1495.4675657599873
# new doc id= test/test.text
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
Tense=Past|VerbForm=Fin|Voice=Act   _	_	_	Weight=0.0
4	liitoksen	liitos	NOUN	N	Case=Gen|Number=Sing	_	_	_↲
	Weight=0.0
5	yksimielisesti	yksimielisesti	ADV	Adv	_	_	_	_	Weight=0.0
6	maanantaina	maanantai	NOUN	N	Case=Ess|Number=Plur	_	_	_↲
	Weight=0.0
7	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0
...
```

The following scripts are included:

1. src/python/omorfi-conllu.py
1. src/python/omorfi-download.py
1. src/python/omorfi-factorise.py
1. src/python/omorfi-freq-evals.py
1. src/python/omorfi-ftb3.py
1. src/python/omorfi-segment.py
1. src/python/omorfi-sigmorphons.py
1. src/python/omorfi-tokenise.py
1. src/python/omorfi-unimorph.py
1. src/python/omorfi-vislcg.py
1. src/python/omorfi-wikitable.py

# Programming interfaces / bindings

→ See also: [API
design](https://flammie.github.io/omorfi/API-Design.html), [generated API
docs](https://flammie.github.io/omorfi/api/html/)

The bash and python scripts provided are suitable for specific tasks they were
written for, for any other uses, there are programming language bindings
available as well as the language models themselves, which you can use and
manipulate with suitable tools.

## Python

Python interface:

```
$ python
Python 3.5.7 (default, Nov 25 2019, 07:48:48)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from omorfi.omorfi import Omorfi
>>> omorfi = Omorfi()
>>> omorfi.load_analyser("/usr/local/share/omorfi/omorfi.describe.hfst")
>>> omorfi.analyse("koira")
[<omorfi.analysis.Analysis object at 0x7fe9ce361c18>]
>>> analyses = omorfi.analyse("alusta")
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

## Java

Java class `com.github.flammie.omorfi.Omorfi` has an example implementation with
a simple input loop.

```
$ java com.github.flammie.omorfi.Omorfi
```
I am not a big fan of Java but acknowledge that some times there are no easy way
to avoid it (Android, Servlets, legacy code base), so this may be more useful
than native interfacing or other hacks.

## C++

The header `omorfi.hh` and the library `libomorfi` has basic interface for
loading and running omorfi language models. There is an example command-line
tool with input loop in `omorfi-lookup.cc`.

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
omorfi.tokenise.pmatchfst
omorfi.tokenise.pmatchfst.debug1
omorfi.tokenise.pmatchfst.debug2
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

