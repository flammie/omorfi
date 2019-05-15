---
layout: default
Title: Omorfi usage examples
---

# Omorfi usage

Omorfi can be used with convenience command-line scripts, manually, using programming language bindings / APIs, etc.

## Command-line

Command-line is the easiest to start with.

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
Kuntaliitoksen selvittämisessä oli mukana myös Tuusniemen kunta, mutta sen valtuusto päätti, että Tuusniemi jatkaa itsenäisenä.
Kuopio ja Juankoski päättävät seuraavien kuntavaalien toteuttamisesta erikseen.
Kunnallisvaalit järjestetään seuraavan kerran vuonna 2016.
Juankosken liittymisen jälkeen Kuopion väkiluku on noin 111 000.
Intian ja Japanin pääministerit tapaavat Tokiossa
Intian uusi pääministeri Narendra Modi tapaa japanilaisen kollegansa Shinzo Aben Tokiossa, keskustellakseen talous- ja turvallisuussuhteista, ensimmäisellä merkittävällä ulkomaanvierailullaan toukokuun vaalivoiton jälkeen.
Modin viisipäiväisen Japaniin suuntautuvan vierailun tarkoituksena on vahvistaa taloussuhteita maailman kolmanneksi suurimpaan talouteen.
```

This newspaper text originates from [Shared task of 1st International Conference on Machine Translation](http://statmt.org/wmt16 )

**NB:** The examples below use the extended dictionary, `-X`, for more information of this, see the [Notes about lexicon sizes](Smaller-lexicons.html).

### Download models

If you haven't built omorfi manually with `./configure && make && make install`, it is possible to get some of the models for analysis from the internet (the long URLs redacted from output, note this was on pre-release version so your output should be slightly different):

```
$ omorfi-download.bash
--2018-11-16 12:57:07--  https://github.com/flammie/omorfi/releases/download/20181111-alpha/omorfi-hfst-models-20181111_alpha.tar.xz
Auflösen des Hostnamens github.com… 192.30.253.113, 192.30.253.112
Verbindungsaufbau zu github.com|192.30.253.113|:443 … verbunden.
HTTP-Anforderung gesendet, auf Antwort wird gewartet … 302 Found
Platz: https://github-production-release-asset-[...] [folgend]
--2018-11-16 12:57:08--  https://github-production-release-asset-[...]
Auflösen des Hostnamens github-production-release-asset-… 52.216.226.192
Verbindungsaufbau zu github-production-release-asset-...|52.216.226.192|:443 … verbunden.
HTTP-Anforderung gesendet, auf Antwort wird gewartet … 200 OK
Länge: 13756036 (13M) [application/octet-stream]
Wird in »omorfi-hfst-models-20181111_alpha.tar.xz.1« gespeichert.

omorfi-hfst-models-20181111_a 100%[==============================================>]  13,12M  4,86MB/s    in 2,7s    

2018-11-16 12:57:11 (4,86 MB/s) - »omorfi-hfst-models-20181111_alpha.tar.xz« gespeichert [13756036/13756036]

omorfi.accept.hfst
omorfi.analyse.hfst
omorfi.describe.hfst
omorfi.generate.hfst
omorfi.labelsegment.hfst
omorfi.segment.hfst

```

The binaries are unpacked in current directory and are from the previous release. If you work within the omorfi git directory, you may want to download the binaries in `src/generated/`.

### Analyse and disambiguate

This is probably what most users want. 

```
$ omorfi-disambiguate-text.sh -X test/test.text 
"<Juankosken>"
	"Juankoski" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunki>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<liittyy>"
	"liittyä" UPOS=VERB Number=Sing Tense=Pres Person=3 Mood=Ind VerbForm=Fin Voice=Act <CMP=1> <W=0>
"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunkiin>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Ill <CMP=1> <W=0>
"<vuoden>"
	"vuoden" UPOS=ADV <CMP=1> <W=0>
	"vuosi" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<2017>"
	"2017" UPOS=NUM NumType=Card <NumType=Digit> <CMP=1> <W=0>
	"2017" UPOS=NUM Number=Sing NumType=Card Case=Nom <NumType=Digit> <CMP=1> <W=0>
"<alussa>"
	"alku" UPOS=NOUN Number=Sing Case=Ine <CMP=1> <W=0>
	"alussa" UPOS=ADV <CMP=1> <W=0>
	"alussa" UPOS=ADP AdpType=Post <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>

"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Number=Sing Tense=Past Person=3 Mood=Ind VerbForm=Fin Voice=Act <CMP=1> <W=0>
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
	"hyväksyä" UPOS=VERB Number=Sing Tense=Past Person=3 Mood=Ind VerbForm=Fin Voice=Act <CMP=1> <W=0>
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
# Tokens: 110 
# Unknown: 4 3.6363636363636362 %
# CPU time: 0.017872999 
# Real time: 0.025131045375019312
# Tokens per timeunit: 4377.056280728452
```

Compare this to the [Analyses without disambiguation](#Analyses without disambiguation (VISL-CG3 format)) below to determine which one is more suitable for your research.

For advanced usage options there is `omorfi-vislcg.py` python script.

#### Analysis without disambiguation (VISL-CG3 format)

It is possible to view the full ambiguous analyses in this format as well, i.e. before the CG rules try to remove most unlikely things. To do so, use omorfi-vislcg3.bash script:

```
$ ▓▒omorfi-vislcg.bash -X test/test.text 
Lines: 10 Tokens: 110 Ratio: 11.0 tokens/line
CPU time: 0.0069146009999999924 Real time: 0.006927895825356245
Tokens per timeunit: 15877.836903580113 Lines per timeunit: 1443.439718507283
"<Juankosken>"
	"Juankoski" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
	"juan#koski" UPOS=NOUN Number=Sing Case=Gen <CMP=2> <W=10000>
"<kaupunki>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
"<liittyy>"
	"liittyä" UPOS=VERB Number=Sing Mood=Ind Voice=Act Person=0 Tense=Pres VerbForm=Fin <CMP=1> <W=0>
	"liittyä" UPOS=VERB Number=Sing Mood=Ind Voice=Act Person=3 Tense=Pres VerbForm=Fin <CMP=1> <W=0>
"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
"<kaupunkiin>"
	"kaupunki" UPOS=NOUN Number=Sing Case=Ill <CMP=1> <W=0>
"<vuoden>"
	"vuoden" UPOS=ADV <CMP=1> <W=0>
	"vuosi" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<2017>"
	"2017" UPOS=NUM NumType=Card <NumType=Digit> <CMP=1> <W=0>
	"2017" UPOS=NUM Number=Sing Case=Nom NumType=Card <NumType=Digit> <CMP=1> <W=0>
"<alussa>"
	"alku" UPOS=NOUN Number=Sing Case=Ine <CMP=1> <W=0>
	"alunen" UPOS=NOUN Style=Arch Number=Sing Case=Ess <CMP=1> <W=0>
	"alussa" UPOS=ADP AdpType=Post <CMP=1> <W=0>
	"alussa" UPOS=ADV <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>


"<Kuopion>"
	"Kuopio" UPOS=PROPN Number=Sing Case=Gen <PropnType=Geo> <CMP=1> <W=0>
	"kuopia" UPOS=VERB Style=Arch Number=Sing Voice=Act Person=1 VerbForm=Fin <Mood=Opt> <CMP=1> <W=0>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=1> <W=0>
	"kaupunki#valtuusto" UPOS=NOUN Number=Sing Case=Nom <CMP=2> <W=10000>
"<hyväksyi>"
	"hyväksyä" UPOS=VERB Number=Sing Mood=Ind Voice=Act Person=0 Tense=Past VerbForm=Fin <CMP=1> <W=0>
	"hyväksyä" UPOS=VERB Number=Sing Mood=Ind Voice=Act Person=3 Tense=Past VerbForm=Fin <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<yksimielisesti>"
	"yksi#-mielinen" UPOS=ADJ Derivation=Sti Degree=Pos <AffixType=Suffix> <CMP=2> <W=15000>
	"yksi#-mielisesti" UPOS=ADV <Lexicalised=Sti> <AffixType=Suffix> <CMP=2> <W=10000>
	"yksimielinen" UPOS=ADJ Derivation=Sti Degree=Pos <CMP=1> <W=5000>
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
	"hyväksyä" UPOS=VERB Number=Sing Mood=Ind Voice=Act Person=0 Tense=Past VerbForm=Fin <CMP=1> <W=0>
	"hyväksyä" UPOS=VERB Number=Sing Mood=Ind Voice=Act Person=3 Tense=Past VerbForm=Fin <CMP=1> <W=0>
"<liitoksen>"
	"liitos" UPOS=NOUN Number=Sing Case=Gen <CMP=1> <W=0>
"<viime>"
	"viime" UPOS=ADV <CMP=1> <W=0>
	"viime" UPOS=ADJ Number=Sing Case=Nom Degree=Pos <CMP=1> <W=0>
"<viikolla>"
	"viikko" UPOS=NOUN Number=Sing Case=Ade <CMP=1> <W=0>
"<.>"
	"." UPOS=PUNCT <CMP=1> <W=0>

```



### Xerox / Finite-State Morphology style analysis

Traditional Finite-State Morphology produces all possible hypotheses of each input token in tabular format.
This can be created with `omorfi-analyse-text.sh`:

```
$ omorfi-analyse-text.sh -X test/test.text 
Juankosken	[WORD_ID=Juankoski][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Juankosken	[WORD_ID=juan][UPOS=NOUN][SEM=CURRENCY][NUM=SG][CASE=NOM][BOUNDARY=COMPOUND][WORD_ID=koski][UPOS=NOUN][NUM=SG][CASE=GEN]

kaupunki	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=NOM]

liittyy	[WORD_ID=liittyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG0]
liittyy	[WORD_ID=liittyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT][PERS=SG3]

Kuopion	[WORD_ID=Kuopio][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Kuopion	[WORD_ID=kuopia][UPOS=VERB][VOICE=ACT][MOOD=OPT][PERS=SG1][STYLE=ARCHAIC]

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
Kuopion	[WORD_ID=kuopia][UPOS=VERB][VOICE=ACT][MOOD=OPT][PERS=SG1][STYLE=ARCHAIC]

kaupunginvaltuusto	[WORD_ID=kaupunginvaltuusto][UPOS=NOUN][NUM=SG][CASE=NOM]
kaupunginvaltuusto	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=GEN][BOUNDARY=COMPOUND][WORD_ID=valtuusto][UPOS=NOUN][NUM=SG][CASE=NOM]

hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG0]
hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG3]

liitoksen	[WORD_ID=liitos][UPOS=NOUN][NUM=SG][CASE=GEN]

yksimielisesti	[WORD_ID=yksi][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM][BOUNDARY=COMPOUND][WORD_ID=-mielinen][UPOS=ADJ][SUBCAT=SUFFIX][CMP=POS][CMP=POS][DRV=STI]
yksimielisesti	[WORD_ID=yksi][UPOS=NUM][NUMTYPE=CARD][NUM=SG][CASE=NOM][BOUNDARY=COMPOUND][WORD_ID=-mielisesti][UPOS=ADV][SUBCAT=SUFFIX][LEX=STI]
yksimielisesti	[WORD_ID=yksimielinen][UPOS=ADJ][CMP=POS][CMP=POS][DRV=STI]
yksimielisesti	[WORD_ID=yksimielisesti][UPOS=ADV][LEX=STI]

maanantaina	[WORD_ID=maanantai][UPOS=NOUN][NUM=PL][CASE=ESS]
maanantaina	[WORD_ID=maanantai][UPOS=NOUN][NUM=SG][CASE=ESS]
maanantaina	[WORD_ID=maanantaina][UPOS=ADV]

.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]

Juankosken	[WORD_ID=Juankoski][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=GEN]
Juankosken	[WORD_ID=juan][UPOS=NOUN][SEM=CURRENCY][NUM=SG][CASE=NOM][BOUNDARY=COMPOUND][WORD_ID=koski][UPOS=NOUN][NUM=SG][CASE=GEN]

kaupunginvaltuusto	[WORD_ID=kaupunginvaltuusto][UPOS=NOUN][NUM=SG][CASE=NOM]
kaupunginvaltuusto	[WORD_ID=kaupunki][UPOS=NOUN][NUM=SG][CASE=GEN][BOUNDARY=COMPOUND][WORD_ID=valtuusto][UPOS=NOUN][NUM=SG][CASE=NOM]

hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG0]
hyväksyi	[WORD_ID=hyväksyä][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PAST][PERS=SG3]

liitoksen	[WORD_ID=liitos][UPOS=NOUN][NUM=SG][CASE=GEN]

viime	[WORD_ID=viime][UPOS=ADV]
viime	[WORD_ID=viime_2][UPOS=ADJ][CMP=POS][NUM=SG][CASE=NOM]

viikolla	[WORD_ID=viikko][UPOS=NOUN][NUM=SG][CASE=ADE]

.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]
```

If your text is already split into word-forms (one word-form per line), it can
be analysed faster with `omorfi-analyse-tokenised.sh` tool:

```
$ omorfi-analyse-tokenised.sh -X test/wordforms.list | head
.	[WORD_ID=.][UPOS=PUNCT][BOUNDARY=SENTENCE]	0,000000

1	[WORD_ID=1][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD]	0,000000
1	[WORD_ID=1][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD][NUM=SG][CASE=NOM]	0,000000

10	[WORD_ID=10][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD]	0,000000
10	[WORD_ID=10][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD][NUM=SG][CASE=NOM]	0,000000

1 000	[WORD_ID=1 000][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD]	0,000000
1 000	[WORD_ID=1 000][UPOS=NUM][SUBCAT=DIGIT][NUMTYPE=CARD][NUM=SG][CASE=NOM]	0,000000

```


#### Moses factored format

It is possible to produce a so-called factored output for use in conjunction with https://statmt.org/moses/ to create morphologically informed statistical machine translation.

```
$ Juankosken|Juankoski|PROPN|Case.Number|Juan.koske.n kaupunki|kaupunki|NOUN|Case.Number|kaupunki liittyy|liittyä|VERB|Mood.Tense.Person.VerbForm.Voice.Number|liitty.y Kuopion|Kuopio|PROPN|Case.Number|Kuopio.n kaupunkiin|kaupunki|NOUN|Case.Number|kaupunki.in vuoden|vuoden|ADV||vuoden 2017|2017|NUM|NumType|2017 alussa|alku|NOUN|Case.Number|alussa .|.|PUNCT||. 
Kuopion|Kuopio|PROPN|Case.Number|Kuopio.n kaupunginvaltuusto|kaupunginvaltuusto|NOUN|Case.Number|kaupungin.valtuusto hyväksyi|hyväksyä|VERB|Mood.Tense.Person.VerbForm.Voice.Number|hyväksy.i liitoksen|liitos|NOUN|Case.Number|liitokse.n yksimielisesti|yksimielisesti|ADV||yksimielisesti maanantaina|maanantai|NOUN|Case.Number|maanantaina .|.|PUNCT||. 
Juankosken|Juankoski|PROPN|Case.Number|Juan.koske.n kaupunginvaltuusto|kaupunginvaltuusto|NOUN|Case.Number|kaupungin.valtuusto hyväksyi|hyväksyä|VERB|Mood.Tense.Person.VerbForm.Voice.Number|hyväksy.i liitoksen|liitos|NOUN|Case.Number|liitokse.n viime|viime|ADV||viime viikolla|viikko|NOUN|Case.Number|viiko.lla .|.|PUNCT||. 
Kuntaliitoksen|kuntaliitos|NOUN|Case.Number|Kuntaliitoksen selvittämisessä|selvittäminen|NOUN|Case.Number|selvittämise.ssä oli|olla|AUX|Mood.Tense.Person.VerbForm.Voice.Number|ol.i mukana|mukana|ADP|AdpType|mukana myös|myödä|VERB|Clitic.Mood.Person.Style.Voice.VerbForm.Number|myös Tuusniemen|Tuusniemi|PROPN|Case.Number|Tuus.nieme.n kunta|kunta|NOUN|Case.Number|kunta ,|,|PUNCT||, mutta|mutta|CCONJ||mutta sen|se|PRON|Case.PronType.Number|sen valtuusto|valtuusto|NOUN|Case.Number|valtuusto päätti|päättää|VERB|Mood.Tense.Person.VerbForm.Voice.Number|päätt.i ,|,|PUNCT||, että|että|SCONJ||että Tuusniemi|Tuusniemi|PROPN|Case.Number|Tuus.niemi jatkaa|jatkaa|VERB|InfForm.VerbForm.Voice.Number|jatka.a itsenäisenä|itsenäinen|ADJ|Number.Case.Degree|itsenäise.nä .|.|PUNCT||. 
Kuopio|Kuopio|PROPN|Case.Number|Kuopio ja|ja|CCONJ||ja Juankoski|Juankoski|PROPN|Case.Number|Juan.koski päättävät|päättävä|ADJ|Number.Case.Degree|päättävä.t seuraavien|seuraava|ADJ|Number.Case.Degree|seuraav.i.en kuntavaalien|kuntavaali|NOUN|Case.Number|kuntavaal.i.en toteuttamisesta|toteuttaminen|NOUN|Case.Number|toteuttamise.sta erikseen|erikseen|ADV||erikseen .|.|PUNCT||. 
Kunnallisvaalit|kunnallinen+vaali|NOUN|Case.Number|Kunnallisvaalit järjestetään|järjestää|VERB|Mood.VerbForm.Tense.Voice|järjeste.tään seuraavan|seuraava|ADJ|Number.Case.Degree|seuraava.n kerran|kerran|ADV|NumType|kerran vuonna|vuonna|ADV||vuonna 2016.|2016.|ADJ|Case.NumType.Number|2016. 
Juankosken|Juankoski|PROPN|Case.Number|Juan.koske.n liittymisen|liittyminen|NOUN|Case.Number|liittymise.n jälkeen|jälkeen|ADP|AdpType|jälkeen Kuopion|Kuopio|PROPN|Case.Number|Kuopio.n väkiluku|väkiluku|NOUN|Case.Number|väki.luku on|olla|AUX|Mood.Tense.Person.VerbForm.Voice.Number|on noin|noin|ADV||noin 111|111|NUM|NumType|111 000|000|NUM|Case.NumType.Number|000 .|.|PUNCT||. 
Intian|Intia|PROPN|Case.Number|Intia.n ja|ja|CCONJ||ja Japanin|Japan|PROPN|Case.Number|Japani.n pääministerit|pääministeri|NOUN|Case.Number|pää.ministeri.t tapaavat|tavata|VERB|Mood.Tense.Person.VerbForm.Voice.Number|tapaava.t Tokiossa|Tokio|PROPN|Case.Number|Tokio.ssa 
Intian|Intia|PROPN|Case.Number|Intia.n uusi|uusi|ADJ|Number.Case.Degree|uusi pääministeri|pääministeri|NOUN|Case.Number|pää.ministeri Narendra|Narendra|X||Narendra Modi|Modi|X||Modi tapaa|tapa|NOUN|Case.Number|tapaa japanilaisen|japanilainen|ADJ|Number.Case.Degree|japanilaise.n kollegansa|kollega|NOUN|Person[psor].Case.Number|kollega.nsa Shinzo|Shinzo|X||Shinzo Aben|Aben|X||Aben Tokiossa|Tokio|PROPN|Case.Number|Tokio.ssa ,|,|PUNCT||, keskustellakseen|keskustella|VERB|InfForm.VerbForm.Voice.Person[psor].Case|keskustell.a.kse.en talous-|talous|NOUN|Case.Number|talous- ja|ja|CCONJ||ja turvallisuussuhteista|turvallisuus+-suhteinen|ADJ|Number.Case.Degree|turvallisuussuhteis.ta ,|,|PUNCT||, ensimmäisellä|ensimmäinen|NOUN|Case.Number|ensimmäise.llä merkittävällä|merkittävä|ADJ|Number.Case.Degree|merkittävä.llä ulkomaanvierailullaan|ulkomaa+vierailu|NOUN|Person[psor].Case.Number|ulko.maa.nvierailu.lla.an toukokuun|toukokuu|NOUN|Case.Number|touko.kuu.n vaalivoiton|vaalivoitto|NOUN|Case.Number|vaali.voito.n jälkeen|jälkeen|ADP|AdpType|jälkeen .|.|PUNCT||. 
Modin|modi|NOUN|Case.Number|Modin viisipäiväisen|viisipäiväinen|ADJ|Number.Case.Degree|viisipäiväise.n Japaniin|Japan|PROPN|Case.Number|Japani.in suuntautuvan|suuntautua|VERB|PartForm.Case.Degree.VerbForm.Voice.Number|suuntautuva.n vierailun|vierailu|NOUN|Case.Number|vierailu.n tarkoituksena|tarkoitus|NOUN|Case.Number|tarkoitukse.na on|olla|AUX|Mood.Tense.Person.VerbForm.Voice.Number|on vahvistaa|vahvistaa|VERB|InfForm.VerbForm.Voice.Number|vahvista.a taloussuhteita|taloussuhde|NOUN|Case.Number|talous.suhte.i.ta maailman|maailma|NOUN|Case.Number|maailma.n kolmanneksi|kolmas|NUM|Case.NumType.Number|kolmanne.ksi suurimpaan|suuri|ADJ|Number.Case.Degree|suurimpa.an talouteen|talous|NOUN|Case.Number|taloute.en .|.|PUNCT||. 
```

### Analysis into CONLL-U / Universal Dependencies format

[Universal Dependencies](http://universaldependencies.org) are the up-and-coming
standard for all your morpho-syntactic needs! Omorfi is currently scheduled to
follow up on Universal dependencies relaeas schedules and analysis and design
principles. Omorfi can fill in the LEMMA, UPOS, and UFEAT morphological feature field,
also the MISC field is used for omorfi data that is not covered by CONLL-U.

Use `omorfi-conllu.bash` for basic parsing:

```
$ omorfi-conllu.bash -X test/test.text 
reading from <stdin>
# new doc id= <stdin>
# sent_id = 1
# text = Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa.
1	Juankosken	Juankoski	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
2	kaupunki	kaupunki	NOUN	N	Case=Nom|Number=Sing	_	_	_	Weight=0.0
3	liittyy	liittyä	VERB	V	Mood=Ind|Number=Sing|Person=0|Tense=Pres|VerbForm=Fin|Voice=Act	_	_	_Weight=0.0
4	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
5	kaupunkiin	kaupunki	NOUN	N	Case=Ill|Number=Sing	_	_	_	Weight=0.0
6	vuoden	vuoden	ADV	Adv	_	_	_	_	Weight=0.0
7	2017	2017	NUM	Num	NumType=Card	_	_	_	Weight=0.0
8	alussa	alku	NOUN	N	Case=Ine|Number=Sing	_	_	_	Weight=0.0
9	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0

# sent_id = 2
# text = Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina.
1	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
2	kaupunginvaltuusto	kaupunginvaltuusto	NOUN	N	Case=Nom|Number=Sing	_	_	_	Weight=0.0
3	hyväksyi	hyväksyä	VERB	V	Mood=Ind|Number=Sing|Person=0|Tense=Past|VerbForm=Fin|Voice=Act	_	_	_	Weight=0.0
4	liitoksen	liitos	NOUN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
5	yksimielisesti	yksimielisesti	ADV	Adv	_	_	_	_	Weight=0.0
6	maanantaina	maanantai	NOUN	N	Case=Ess|Number=Plur	_	_	_	Weight=0.0
7	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0

# sent_id = 3
# text = Juankosken kaupunginvaltuusto hyväksyi liitoksen viime viikolla.
1	Juankosken	Juankoski	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
2	kaupunginvaltuusto	kaupunginvaltuusto	NOUN	N	Case=Nom|Number=Sing	_	_	_	Weight=0.0
3	hyväksyi	hyväksyä	VERB	V	Mood=Ind|Number=Sing|Person=0|Tense=Past|VerbForm=Fin|Voice=Act	_	_	_	Weight=0.0
4	liitoksen	liitos	NOUN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
5	viime	viime	ADV	Adv	_	_	_	_	Weight=0.0
6	viikolla	viikko	NOUN	N	Case=Ade|Number=Sing	_	_	_	Weight=0.0
7	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0

```

For more options there is a python script `omorfi-conllu.py`.

### FTB3.1 analysis

Omorfi can output FTB3.1-compatible format with `omorfi-ftb3.bash`:

```
$ omorfi-ftb3.bash -X test/test.text 
reading from <stdin>
<s><loc file="<stdin>" line="1" />
1	Juankosken	Juankoski	N	N	N Prop Gen Sg Prop	_	_	_	_
2	kaupunki	kaupunki	N	N	N Nom Sg	_	_	_	_
3	liittyy	liittyä	V	V	V Prs Act Sg3	_	_	_	_
4	Kuopion	Kuopio	N	N	N Prop Gen Sg Prop	_	_	_	_
5	kaupunkiin	kaupunki	N	N	N Ill Sg	_	_	_	_
6	vuoden	vuoden	Adv	Adv	Adv	_	_	_	_
7	2017	2017	Num	Num	Num Digit	_	_	_	_
8	alussa	alku	N	N	N Ine Sg	_	_	_	_
9	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="2" />
1	Kuopion	Kuopio	N	N	N Prop Gen Sg Prop	_	_	_	_
2	kaupunginvaltuusto	kaupunginvaltuusto	N	N	N Nom Sg	_	_	_	_
3	hyväksyi	hyväksyä	V	V	V Prt Act Sg3	_	_	_	_
4	liitoksen	liitos	N	N	N Gen Sg	_	_	_	_
5	yksimielisesti	yksimielisesti	Adv	Adv	Adv Pos Man	_	_	_	_
6	maanantaina	maanantai	N	N	N Ess Pl	_	_	_	_
7	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="3" />
1	Juankosken	Juankoski	N	N	N Prop Gen Sg Prop	_	_	_	_
2	kaupunginvaltuusto	kaupunginvaltuusto	N	N	N Nom Sg	_	_	_	_
3	hyväksyi	hyväksyä	V	V	V Prt Act Sg3	_	_	_	_
4	liitoksen	liitos	N	N	N Gen Sg	_	_	_	_
5	viime	viime	Adv	Adv	Adv	_	_	_	_
6	viikolla	viikko	N	N	N Ade Sg	_	_	_	_
7	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="4" />
1	Kuntaliitoksen	kuntaliitos	N	N	N Gen Sg	_	_	_	_
2	selvittämisessä	selvittäminen	N	N	N Ine Sg	_	_	_	_
3	oli	olla	V	V	V Prt Act Sg3	_	_	_	_
4	mukana	mukana	Adp	Adp	Adp Po	_	_	_	_
5	myös	myödä	V	V	V Foc_S Act Imp Sg2	_	_	_	_
6	Tuusniemen	Tuusniemi	N	N	N Prop Gen Sg Prop	_	_	_	_
7	kunta	kunta	N	N	N Nom Sg	_	_	_	_
8	,	,	Punct	Punct	Punct	_	_	_	_
9	mutta	mutta	CC	CC	CC	_	_	_	_
10	sen	se	Pron	Pron	Pron Gen Dem Sg	_	_	_	_
11	valtuusto	valtuusto	N	N	N Nom Sg	_	_	_	_
12	päätti	päättää	V	V	V Prt Act Sg3	_	_	_	_
13	,	,	Punct	Punct	Punct	_	_	_	_
14	että	että	CS	CS	CS	_	_	_	_
15	Tuusniemi	Tuusniemi	N	N	N Prop Nom Sg Prop	_	_	_	_
16	jatkaa	jatkaa	V	V	V Inf1 Lat	_	_	_	_
17	itsenäisenä	itsenäinen	A	A	A Pos Ess Sg	_	_	_	_
18	.	.	Punct	Punct	Punct	_	_	_	_
</s>
```

### Coverage analysis

It is possible to get naïve coverage estimates with `omorfi-freq-evals.bash`:

```
$ omorfi-freq-evals.bash -X test/test.text 
reading from <stdin>
1	OOV	Shinzo
1	OOV	Narendra
1	OOV	Aben
CPU time: 0.013742949000000004 real time: 0.042139661964029074
Lines	Covered	OOV
110	107	3
100.0	97.27272727272728	2.727272727272727
Types	Covered	OOV
87	84	3
100.0	96.55172413793103	3.4482758620689653
needs to have 99 % coverage to pass regress test
 please examine <stdout> for regressions
```

The python script `omorfi-freq-evals.py` has further options including Precision/Recall analysis over string matches.

### Raw text tokenisation

Most tools will handle tokenisation internally, if you want to see the intermediate steps for example, you can invoke `omorfi-tokenise.bash` directly:

```
$ omorfi-tokenise.bash -X test/test.text 
Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa .
Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina .
Juankosken kaupunginvaltuusto hyväksyi liitoksen viime viikolla .
Kuntaliitoksen selvittämisessä oli mukana myös Tuusniemen kunta , mutta sen valtuusto päätti , että Tuusniemi jatkaa itsenäisenä .
Kuopio ja Juankoski päättävät seuraavien kuntavaalien toteuttamisesta erikseen .
Kunnallisvaalit järjestetään seuraavan kerran vuonna 2016.
Juankosken liittymisen jälkeen Kuopion väkiluku on noin 111 000 .
Intian ja Japanin pääministerit tapaavat Tokiossa
Intian uusi pääministeri Narendra Modi tapaa japanilaisen kollegansa Shinzo Aben Tokiossa , keskustellakseen talous- ja turvallisuussuhteista , ensimmäisellä merkittävällä ulkomaanvierailullaan toukokuun vaalivoiton jälkeen .
Modin viisipäiväisen Japaniin suuntautuvan vierailun tarkoituksena on vahvistaa taloussuhteita maailman kolmanneksi suurimpaan talouteen .
```

For more output formats and options, the python script `omorfi-tokenise.py` is available.

E.g. for CONLL-U and so Universal dependencies, you can use `omorfi-tokenise.py -O conllu`:

```
$ omorfi-tokenise.py -a /usr/local/share/omorfi/omorfi.describe.hfst -i test/test.text -O conllu
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
# text = Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina.
1	Kuopion	_	_	_	_	_	_	_	_
2	kaupunginvaltuusto	_	_	_	_	_	_	_	_
3	hyväksyi	_	_	_	_	_	_	_	_
4	liitoksen	_	_	_	_	_	_	_	_
5	yksimielisesti	_	_	_	_	_	_	_	_
6	maanantaina	_	_	_	_	_	_	_	_
7	.	_	_	_	_	_	_	_	_
...
```



### Morphological segmentation

Omorfi can be used to segment word-forms into sub-word units with `omorfi-segment.bash`:

```
$ omorfi-segment.sh test/test.text 
Juan→ ←koske→ ←n kaupunki liitty→ ←y Kuopio→ ←n kaupunki→ ←in vuoden 2017 alussa. 
Kuopio→ ←n kaupungin→ ←valtuusto hyväksy→ ←i liitokse→ ←n yksimielisesti maanantaina. 
Juan→ ←koske→ ←n kaupungin→ ←valtuusto hyväksy→ ←i liitokse→ ←n viime viikolla. 
Kuntaliitoksen selvittämise→ ←ssä ol→ ←i mukana myös Tuus→ ←nieme→ ←n kunta, mutta sen valtuusto päätti, että Tuus→ ←niemi jatka→ ←a itsenäisenä. 
Kuopio ja Juan→ ←koski päättävä→ ←t seuraav→ ←i→ ←en kuntavaal→ ←i→ ←en toteuttamise→ ←sta erikseen. 
Kunnallisvaalit järjeste→ ←tään seuraava→ ←n kerran vuonna 2016. 
Juan→ ←koske→ ←n liittymise→ ←n jälkeen Kuopio→ ←n väki→ ←luku on noin 111 000. 
Intia→ ←n ja Japani→ ←n pää→ ←ministeri→ ←t tapaava→ ←t Tokio→ ←ssa 
Intia→ ←n uusi pää→ ←ministeri Narendra Modi tapaa japanilaise→ ←n kollega→ ←nsa Shinzo Aben Tokiossa, keskustell→ ←a→ ←kse→ ←en talous- ja turvallisuussuhteista, ensimmäise→ ←llä merkittävä→ ←llä ulko→ ←maa→ ←nvierailu→ ←lla→ ←an touko→ ←kuu→ ←n vaali→ ←voito→ ←n jälkeen. 
Modin viisipäiväise→ ←n Japani→ ←in suuntautuva→ ←n vierailu→ ←n tarkoitukse→ ←na on vahvista→ ←a talous→ ←suhte→ ←i→ ←ta maailma→ ←n kolmanne→ ←ksi suurimpa→ ←an talouteen. 
```

For further options there is a `omorfi-segment.py` python script.

**Preliminary** support for labeled segmentation is also available but not
guaranteed to work.

### Spell-Checking and correction

Spelling correction may be done if hfst-ospell is installed using `omorfi-spell.sh`:

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

The omorfi.zhfst that is built in omorfi could be a drop-in replacement for voikko and giellatekno, but theirs is curated for specific purpose of spell-checking whereas omorfi is large-coverage dictionary so ymmv, I (Flammie) like my spell-checker to recognise and suggest obscure and obscene terms but it's not for everyone.

### Morphological generation

Generating word-forms can be done using `omorfi-generate.sh`:

```
$ omorfi-generate.sh 

[WORD_ID=kissa][UPOS=NOUN][NUM=SG][CASE=INE]
[WORD_ID=kissa][UPOS=NOUN][NUM=SG][CASE=INE]	kissassa	0,0
```

The input for generator is simply the output of the raw analyser.

Generation has not been used so much because I have no use cases. There's some convenience scripts not installed in the `src/bash`, here's a classical example by Fred Karlsson of generating all forms of a noun *kauppa* (a shop) in Finnish. [He lists 2,253 forms](https://www.ling.helsinki.fi/~fkarlsso/genkau2.html), our current version is [here containing 6,602 forms of word *kauppa*](genkau3.html). And here's the execution:

```
echo kauppa > kauppa.wordlist
bash src/bash/generate-wordlist.sh kauppa.wordlist kauppa.wordforms
hfst-lookup src/generated/omorfi.describe.hfst -q < kauppa.wordforms |\
	sed -e 's/\[WORD_ID=kauppa\]\[UPOS=//' |\
	tr '][' '  ' | tr -s '\n' | sed -e 's/[0-9, ]*$//' |\
	fgrep -v DRV | fgrep -v COMPOUND | fgrep -v WORD_ID=kaupata
```

## Python scripts and pipeline building

The python versions of the scripts are for more advanced usage. They all follow approximately the same format, however, the input is always given with `-i INFILE` switch, the output is always specified with the `-o OUTFILE` switch, and you must provide the language model automatically with the `-a MODELFILE` switch. You must also always build your whole pipeline, including tokenisation and selecting correct formats. E.g.:

```
omorfi-tokenise.py -a src/generated/omorfi.describe.hfst -i test/test.text -O conllu |\
	omorfi-conllu.py -a src/generated/omorfi.describe.hfst 
reading from <stdin>
Lines: 10 Tokens: 110 Ratio: 11.0 tokens/line
CPU time: 0.006683539000000002 Real time: 0.006686871871352196
Tokens per timeunit: 16450.14322335986 Lines per timeunit: 1495.4675657599873
# new doc id= test/test.text
# sent_id = 1
# text = Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa.
1	Juankosken	Juankoski	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
2	kaupunki	kaupunki	NOUN	N	Case=Nom|Number=Sing	_	_	_	Weight=0.0
3	liittyy	liittyä	VERB	V	Mood=Ind|Number=Sing|Person=0|Tense=Pres|VerbForm=Fin|Voice=Act	_	_	_Weight=0.0
4	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
5	kaupunkiin	kaupunki	NOUN	N	Case=Ill|Number=Sing	_	_	_	Weight=0.0
6	vuoden	vuoden	ADV	Adv	_	_	_	_	Weight=0.0
7	2017	2017	NUM	Num	NumType=Card	_	_	_	Weight=0.0
8	alussa	alku	NOUN	N	Case=Ine|Number=Sing	_	_	_	Weight=0.0
9	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0

# sent_id = 2
# text = Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina.
1	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
2	kaupunginvaltuusto	kaupunginvaltuusto	NOUN	N	Case=Nom|Number=Sing	_	_	_	Weight=0.0
3	hyväksyi	hyväksyä	VERB	V	Mood=Ind|Number=Sing|Person=0|Tense=Past|VerbForm=Fin|Voice=Act	_	_	_	Weight=0.0
4	liitoksen	liitos	NOUN	N	Case=Gen|Number=Sing	_	_	_	Weight=0.0
5	yksimielisesti	yksimielisesti	ADV	Adv	_	_	_	_	Weight=0.0
6	maanantaina	maanantai	NOUN	N	Case=Ess|Number=Plur	_	_	_	Weight=0.0
7	.	.	PUNCT	Punct	_	_	_	_	Weight=0.0
...
```

# Programming interfaces / bindings

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
Python 3.6.3 (default, Jan 16 2018, 06:46:41) 
[GCC 6.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from omorfi.omorfi import Omorfi
>>> omorfi = Omorfi()
>>> omorfi.load_analyser("/usr/local/share/omorfi/omorfi.describe.hfst")
>>> omorfi.analyse("koira")
[<omorfi.analysis.Analysis object at 0x7fe9ce361c18>]
>>> analyses = omorfi.analyse("alusta")
>>> for analysis in analyses:
...     print(analysis.get_lemmas(), analysis.get_upos(), analysis.printable_ud_feats())
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

Java class:

```
$ java com.github.flammie.omorfi.Omorfi ../generated/omorfi.describe.hfst 
Reading analyser at ../generated/omorfi.describe.hfst
Read all.
> kissa
Analysing kissa
[WORD_ID=kissa][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.0]
> alusta
Analysing alusta
[WORD_ID=alku][UPOS=NOUN][NUM=SG][CASE=ELA][WEIGHT=0.0]
[WORD_ID=alunen][UPOS=NOUN][NUM=SG][CASE=PAR][WEIGHT=0.0]
[WORD_ID=alus][UPOS=NOUN][NUM=SG][CASE=PAR][WEIGHT=0.0]
[WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=IMPV][PERS=SG2][WEIGHT=0.0]
[WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON][WEIGHT=0.0]
[WORD_ID=alusta][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.0]
[WORD_ID=alusta_2][UPOS=ADV][WEIGHT=0.0]
[WORD_ID=alusta_3][UPOS=ADV][WEIGHT=0.0]

```
I am not a big fan of Java but acknowledge that some times there are no easy way to avoid it (Android, Servlets, legacy code base), so this may be more useful than native interfacing or other hacks.

## Raw automata

Most of language models are finite-state automata binaries for [HFST](//hfst.github.io).
The installed files are in `$prefix/share/omorfi` (my installation is in linux
default: `/usr/local`)

```
ls /usr/local/share/omorfi/
master.tsv           omorfi.describe.hfst         omorfi.lemmatise.hfst         omorfi.tokenise.pmatchfst
omorfi.accept.hfst   omorfi.generate.hfst         omorfi_recased.analyse.hfst   speller-omorfi.zhfst
omorfi.analyse.hfst  omorfi.hyphenate-rules.hfst  omorfi_recased.describe.hfst
omorfi.cg3bin        omorfi.labelsegment.hfst     omorfi.segment.hfst
```

The naming is probably not gonna be same forever, but should be pretty transparent.

### HFST tools

You can directly access specific automata using finite-state tools from the HFST
project (details can be found on their individual man pages and
[HFST wiki](https://kitwiki.csc.fi/):

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
analyses; omorfi bash API sets this to 15 seconds.
