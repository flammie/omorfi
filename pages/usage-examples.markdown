---
layout: page
Title: Omorfi usage examples
---

# Omorfi usage

The following examples have been run in the omorfi source dir after succesful
installation. The command lines look like this:

```
$
```

When testing the instructions, please do not copy/paste the dollar sign, it is
not a part of the command, but a command-line prompt indicator!

## Command-line

### Raw text tokenisation

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

Different kinds of morphological analysis use cases: traditional linguistics
with Xerox-style analysis, followed by constraitn grammars, or Universal
dependency pre-parses, or factorised analysis for statistical machine
ranslations.

#### Xerox / Finite-State Morphology format

The Xerox finite-State Morphology uses simple tab-separated analysis per line
format with tokens separated by empty lines, this is the output format of the
`omorfi-analyse-text` tool.

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

1 000	[WORD_ID=1 000][UPOS=NUM][NUMTYPE=CARD]	0,000000
1 000	[WORD_ID=1 000][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM]	0,000000
```

#### VISL CG 3 format


A full pipeline for VISL CG 3 disambiguation is implemented as a convenience
script that works like text analysis script:

```
$ omorfi-disambiguate-text.sh test/newstest2016-enfi-ref.fi.text | tail -n 40
"<kokoukseen>"
	"kokouksi" NOUN SG ILL
	"kokouksi_2" NOUN SG ILL
	"kokous" NOUN SG ILL
"<osallistui>"
	"osallistua" VERB ACT INDV PAST SG3
"<myös>"
	"myödä" VERB <DIALECTAL> ACT IMPV SG2 S
"<pääministeri>"
	"pääministeri" NOUN SG NOM
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
	"johtaja" NOUN PL NOM
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

CG style input format can be generated using python based analyser script
`omorfi-vislcg.py` (this is the ambiguous morphological analysis, just formatted
for omorfi's CG ruleset):

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
	"julkaista" VERB TU POS SG INE
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

Some of the fields are produced by different automata, where automaton is
missing, placeholder values can appear, such as UNK or 0.


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
# text = Luonto-Liitto ehdottaa Metsähallitukselle täydentämään suojelupäätöstä muuallekin Suomessa, kuten Kainuuseen.
# sent_id =  wn074.11
1	Luonto-Liitto	Luonto-Liitto	PROPN	N	Case=Nom|Number=Sing	_	_	_	_
2	ehdottaa	ehdottaa	VERB	V	InfForm=1|Number=Sing|VerbForm=Inf|Voice=Act	_	_	__
3	Metsähallitukselle	Metsähallitus	PROPN	N	Case=All|Number=Sing	_	_	_	_
4	täydentämään	täydentää	VERB	V	Case=Ill|InfForm=3|Number=Sing|VerbForm=Inf|Voice=Act	_	__	_
5	suojelupäätöstä	suojelu#päätös	NOUN	N	Case=Par|Number=Sing	_	_	_	_
6	muuallekin	muualle	ADV	Adv	Clitic=Kin	_	_	_	_
7	Suomessa	Suomi	PROPN	N	Case=Ine|Number=Sing	_	_	_	_
8	,	,	PUNCT	Punct	_	_	_	_	_
9	kuten	kuten	ADV	Adv	_	_	_	_	_
10	Kainuuseen	Kainuu	PROPN	N	Case=Ill|Number=Sing	_	_	_	_
11	.	.	PUNCT	Punct	_	_	_	_	_

# text = Hakkuut vanhoissa metsissä saavat aina aikaan konfliktin.
# sent_id =  wn074.12
1	Hakkuut	Hakkuu	PROPN	N	Case=Nom|Number=Plur	_	_	_	_
2	vanhoissa	vanha	ADJ	A	Case=Ine|Degree=Pos|Number=Plur	_	_	_	_
3	metsissä	metsä	NOUN	N	Case=Ine|Number=Plur	_	_	_	_
4	saavat	saada	VERB	V	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act	_	_	__
5	aina	aina	ADP	Adp	_	_	_	_	_
6	aikaan	aika	NOUN	N	Case=Ill|Number=Sing	_	_	_	_
7	konfliktin	konflikti	NOUN	N	Case=Gen|Number=Sing	_	_	_	_
8	.	.	PUNCT	Punct	_	_	_	_	_
```

This can be combined with tokenisation to analyse raw corpora:

```
$ omorfi-tokenise.py -O conllu -i test/newstest2016-enfi-ref.fi.text | omorfi-conllu.py | tail -n 40
# sentence-text: Kokoukseen osallistui myös pääministeri Li Keqiang, sekä vanhemmat johtajat Liu Yunshan ja Zhang Gaoli, kerrottiin kokouksen jälkeen julkaistussa lausunnossa.
1	kokoukseen	koko#uksi	NOUN	N	Case=Ill|Number=Sing	_	_	_	_
2	osallistui	osallistua	VERB	V	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin|Voice=Act	_	_	_	_
3	myös	myödä	VERB	V	Clitic=S|Mood=Imp|Number=Sing|Person=2|Style=Coll|VerbForm=Fin|Voice=Act	__	_	_
4	pääministeri	pää#ministeri	NOUN	N	Case=Nom|Number=Sing	_	_	_	_
5	Li	Li	NUM	Num	_	_	_	_	_
6	Keqiang		PROPN	N	Case=Nom|Number=Sing	_	_	_	GUESS=HEUR
7	,	,	PUNCT	Punct	_	_	_	_	_
8	sekä	sekä	CCONJ	C	_	_	_	_	_
9	vanhemmat	vanha	ADJ	A	Case=Nom|Degree=Cmp|Number=Plur	_	_	_	_
10	johtajat	johtaa	VERB	V	Case=Nom|Derivation=Ja|Number=Plur	_	_	_	_
11	Liu	Liu	PROPN	N	Case=Nom|Number=Sing	_	_	_	_
12	Yunshan		PROPN	N	Case=Nom|Number=Sing	_	_	_	GUESS=HEUR
13	ja	ja	CCONJ	C	_	_	_	_	_
14	Zhang	Zhang	PROPN	N	Case=Nom|Number=Sing	_	_	_	_
15	Gaoli		PROPN	N	Case=Nom|Number=Sing	_	_	_	GUESS=HEUR
16	,	,	PUNCT	Punct	_	_	_	_	_
17	kerrottiin	kertoa	VERB	V	Mood=Ind|Tense=Past|VerbForm=Fin|Voice=Pass	_	_	_	_
18	kokouksen	koko#uksi	NOUN	N	Case=Gen|Number=Sing	_	_	_	_
19	jälkeen	jälkeen	ADP	Adp	AdpType=Post	_	_	_	_
20	julkaistussa	julkaista	VERB	V	Case=Ine|Degree=Pos|Number=Sing	_	_	_	_
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
lisäksi ulko→ ←maalais→ ←ten pysyv→ ←i→ ←en asukas→ ←lup→ ←i→ ←en , ” Green cardien , ” haku→ ←prosessi→ ←a helpote→ ←taan optimoima→ ←lla vaatimuks→ ←i→ ←a ja keventämä→ ←llä haku→ ←prosessi→ ←a .
kokoukse→ ←ssa keskustel→ ←tiin myös lakimies→ ←ten ammattinharjoittamisoikeuksien takaamise→ ←sta sekä ammatti→ ←tuomare→ ←i→ ←den ja - syyttäj→ ←i→ ←en tukemise→ ←sta .
kokoukse→ ←en osallistu→ ←i myös pää→ ←ministeri Li Keqiang , sekä vanhemma→ ←t johtaja→ ←t Liu Yunshan ja Zhang Gaoli , kerrot→ ←tiin kokoukse→ ←n jälkeen julkaistu→ ←ssa lausunno→ ←ssa .
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

→ See also: [API
design](https://flammie.github.io/omorfi/pages/API-Design.html), [generated API
docs](https://flammie.github.io/omorfi/doc/html/) ):

For serious business, the convenience shell-scripts are not usually sufficient.
We offer bindings to several popular programming languages as well as low-level
access to the automata either via command-line or the external programming
libraries from the toolkit generating the automata.

## Python

Python interface:

```
$ python3
Python 3.4.0 (default, Mar 18 2014, 16:02:57)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from omorfi.omorfi import Omorfi
>>> omorfi = Omorfi()
>>> omorfi.load_from_dir()
>>> omorfi.analyse("koira")
(('[WORD_ID=koira][UPOS=NOUN][NUM=SG][CASE=NOM]', 0.0),
('[WORD_ID=Koira][UPOS=PROPN][NUM=SG][CASE=NOM]', 0.0))
>>> for analysis in analyses:
...     print(analysis[0])
...
[WORD_ID=alku][UPOS=NOUN][NUM=SG][CASE=ELA]
[WORD_ID=alunen][UPOS=NOUN][NUM=SG][CASE=PAR]
[WORD_ID=alus][UPOS=NOUN][NUM=SG][CASE=PAR]
[WORD_ID=alusta][UPOS=NOUN][NUM=SG][CASE=NOM]
[WORD_ID=alusta_2][UPOS=ADV]
[WORD_ID=alusta_3][UPOS=ADV]
[WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=IMPV][PERS=SG2]
[WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON]
[WORD_ID=Alku][UPOS=PROPN]ERRORMACROPROPN-BLOCKING][NUM=SG][CASE=ELA]
[WORD_ID=Alku_2][UPOS=PROPN][NUM=SG][CASE=ELA]
[WORD_ID=Alku_3][UPOS=PROPN][NUM=SG][CASE=ELA]
[WORD_ID=Alus][UPOS=PROPN]ERRORMACROPROPN-BLOCKING][NUM=SG][CASE=PAR]
>>>
>>>
```

## Java

Java class (more details on java API pages):

```
$ CLASSPATH=$HOME/github/hfst/hfst-optimized-lookup/hfst-optimized-lookup-java/hfst-ol.jar:. java com.github.flammie.omorfi.Omorfi
...
Read all.
> talo
Analysing talo
{omorfi-omor_recased=net.sf.hfst.WeightedTransducer@63947c6b, omorfi-giella=net.sf.hfst.WeightedTransducer@2b193f2d, omorfi-ftb3=net.sf.hfst.WeightedTransducer@355da254, omorfi-omor=net.sf.hfst.WeightedTransducer@4dc63996}
Analysing talo with omorfi-omor
[WORD_ID=talo][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.0]
[WORD_ID=talo][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.0][CASECHANGE=LOWERCASED]
```

Especially loading all automata from system paths requires more memory than
java typically gives you, so use `-Xmx` switch.

### Raw automata

The installed files are in `$prefix/share/omorfi` (my installation is in linux
default: `/usr/local`)

```
$ ls /usr/local/share/omorfi/
master.tsv           omorfi.describe.hfst      omorfi_recased.analyse.hfst   speller-omorfi.zhfst
omorfi.accept.hfst   omorfi.generate.hfst      omorfi_recased.describe.hfst
omorfi.analyse.hfst  omorfi.labelsegment.hfst  omorfi.segment.hfst
omorfi.cg3bin        omorfi.lemmatise.hfst     omorfi.tokenise.pmatchfst
```

The naming is probably not gonna be same forever.

## HFST tools

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
