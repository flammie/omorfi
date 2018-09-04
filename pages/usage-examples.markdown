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

### Analyse and disambiguate

This is probably what most users want. 

```
$ omorfi-disambiguate-text.sh -X test/test.text 
"<Juankosken>"
	"Juankoski" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>
"<kaupunki>"
	"kaupunki" NOUN SG NOM <W=0> <CMP=1>
"<liittyy>"
	"liittyä" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>
"<Kuopion>"
	"Kuopio" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>
"<kaupunkiin>"
	"kaupunki" NOUN SG ILL <W=0> <CMP=1>
"<vuoden>"
	"vuoden" ADV <W=0> <CMP=1>
	"vuosi" NOUN SG GEN <W=0> <CMP=1>
"<2017>"
	"2017" NUM <SUBCAT_DIGIT> CARD <W=0> <CMP=1>
	"2017" NUM <SUBCAT_DIGIT> CARD SG NOM <W=0> <CMP=1>
"<alussa>"
	"alku" NOUN SG INE <W=0> <CMP=1>
	"alussa" ADV <W=0> <CMP=1>
	"alussa" ADP <W=0> <CMP=1>
"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kuopion>"
	"Kuopio" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" NOUN SG NOM <W=0> <CMP=1>
"<hyväksyi>"
	"hyväksyä" VERB ACT INDV PAST SG3 <W=0> <CMP=1>
"<liitoksen>"
	"liitos" NOUN SG GEN <W=0> <CMP=1>
"<yksimielisesti>"
	"yksimielisesti" ADV <LEX_STI> <W=0> <CMP=1>
"<maanantaina>"
	"maanantaina" ADV <W=0> <CMP=1>
"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Juankosken>"
	"Juankoski" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>
"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" NOUN SG NOM <W=0> <CMP=1>
"<hyväksyi>"
	"hyväksyä" VERB ACT INDV PAST SG3 <W=0> <CMP=1>
"<liitoksen>"
	"liitos" NOUN SG GEN <W=0> <CMP=1>
"<viime>"
	"viime" ADV <W=0> <CMP=1>
	"viime" ADJ POS SG NOM <W=0> <CMP=1>
"<viikolla>"
	"viikko" NOUN SG ADE <W=0> <CMP=1>
"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kuntaliitoksen>"
	"kuntaliitos" NOUN SG GEN <*LOWERCASED> <W=0> <CMP=1>
"<selvittämisessä>"
	"selvittäminen" NOUN SG INE <W=0> <CMP=1>
"<oli>"
	"olla" AUX ACT INDV PAST SG3 <W=0> <CMP=1>
	"olla" VERB ACT INDV PAST SG3 <W=0> <CMP=1>
"<mukana>"
	"mukana" ADP POST <W=0> <CMP=1>
	"mukana" ADV PREP <W=0> <CMP=1>
"<myös>"
	"myös" ADV <W=0> <CMP=1>
"<Tuusniemen>"
	"Tuusniemi" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>
"<kunta>"
	"kunta" NOUN SG NOM <W=0> <CMP=1>
"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>
"<mutta>"
	"mutta" ADP <W=0> <CMP=1>
	"mutta" CCONJ <W=0> <CMP=1>
"<sen>"
	"se" PRON DEM SG GEN <W=0> <CMP=1>
	"se" DET SG GEN <W=0> <CMP=1>
"<valtuusto>"
	"valtuusto" NOUN SG NOM <W=0> <CMP=1>
"<päätti>"
	"päättää" VERB ACT INDV PAST SG3 <W=0> <CMP=1>
"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>
"<että>"
	"että" SCONJ <W=0> <CMP=1>
"<Tuusniemi>"
	"Tuusniemi" PROPN <PROPER_GEO> SG NOM <W=0> <CMP=1>
"<jatkaa>"
	"jatkaa" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>
	"jatkaa" VERB ACT INFA SG <W=0> <CMP=1>
"<itsenäisenä>"
	"itsenäinen" ADJ POS SG ESS <W=0> <CMP=1>
"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>
```

Compare this to [raw ambiguous analysis of the same data](#VISL_CG_3_format) to see which one suits you better:

### VISL CG 3 format

It is possible to create VISL CG 3 format analyses without performing disambiguation using the `omorfi-vislcg.bash`:

```
$ omorfi-vislcg.bash -X test/test.text 
"<Juankosken>"
	"juan#koski" NOUN SG GEN <W=0> <CMP=2>
	"Juankoski" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>

"<kaupunki>"
	"kaupunki" NOUN SG NOM <W=0> <CMP=1>

"<liittyy>"
	"liittyä" VERB ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"liittyä" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>

"<Kuopion>"
	"Kuopio" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>

"<kaupunkiin>"
	"kaupunki" NOUN SG ILL <W=0> <CMP=1>

"<vuoden>"
	"vuoden" ADV <W=0> <CMP=1>
	"vuosi" NOUN SG GEN <W=0> <CMP=1>

"<2017>"
	"2017" NUM <SUBCAT_DIGIT> CARD <W=0> <CMP=1>
	"2017" NUM <SUBCAT_DIGIT> CARD SG NOM <W=0> <CMP=1>

"<alussa>"
	"alku" NOUN SG INE <W=0> <CMP=1>
	"alunen" NOUN SG ESS <STYLE_ARCHAIC> <W=0> <CMP=1>
	"alussa" ADP <W=0> <CMP=1>
	"alussa" ADV <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kuopion>"
	"kuopia" VERB ACT OPT SG1 <STYLE_ARCHAIC> <W=0> <CMP=1>
	"Kuopio" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>

"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" NOUN SG NOM <W=0> <CMP=1>
	"kaupunki#valtuusto" NOUN SG NOM <W=0> <CMP=2>

"<hyväksyi>"
	"hyväksyä" VERB ACT INDV PAST SG0 <W=0> <CMP=1>
	"hyväksyä" VERB ACT INDV PAST SG3 <W=0> <CMP=1>

"<liitoksen>"
	"liitos" NOUN SG GEN <W=0> <CMP=1>

"<yksimielisesti>"
	"yksi#-mielinen" ADJ <SUBCAT_SUFFIX> POS POS <DRV_STI> <W=0> <CMP=2>
	"yksi#-mielisesti" ADV <SUBCAT_SUFFIX> <LEX_STI> <W=0> <CMP=2>
	"yksimielinen" ADJ POS POS <DRV_STI> <W=0> <CMP=1>
	"yksimielisesti" ADV <LEX_STI> <W=0> <CMP=1>

"<maanantaina>"
	"maanantai" NOUN PL ESS <W=0> <CMP=1>
	"maanantai" NOUN SG ESS <W=0> <CMP=1>
	"maanantaina" ADV <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Juankosken>"
	"juan#koski" NOUN SG GEN <W=0> <CMP=2>
	"Juankoski" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>

"<kaupunginvaltuusto>"
	"kaupunginvaltuusto" NOUN SG NOM <W=0> <CMP=1>
	"kaupunki#valtuusto" NOUN SG NOM <W=0> <CMP=2>

"<hyväksyi>"
	"hyväksyä" VERB ACT INDV PAST SG0 <W=0> <CMP=1>
	"hyväksyä" VERB ACT INDV PAST SG3 <W=0> <CMP=1>

"<liitoksen>"
	"liitos" NOUN SG GEN <W=0> <CMP=1>

"<viime>"
	"viime" ADV <W=0> <CMP=1>
	"viime" ADJ POS SG NOM <W=0> <CMP=1>

"<viikolla>"
	"viikko" NOUN SG ADE <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kuntaliitoksen>"
	"kunta#liitos" NOUN SG GEN <*LOWERCASED> <W=0> <CMP=2>
	"kuntaliitos" NOUN SG GEN <*LOWERCASED> <W=0> <CMP=1>

"<selvittämisessä>"
	"selvittäminen" NOUN SG INE <W=0> <CMP=1>
	"selvittää" VERB <DRV_MINEN> SG INE <W=0> <CMP=1>

"<oli>"
	"olla" AUX ACT INDV PAST SG3 <W=0> <CMP=1>
	"olla" VERB ACT INDV PAST SG3 <W=0> <CMP=1>

"<mukana>"
	"mukana" ADP POST <W=0> <CMP=1>
	"mukana" ADV PREP <W=0> <CMP=1>

"<myös>"
	"myödä" VERB <STYLE_DIALECTAL> ACT IMPV SG2 CLITS <W=0> <CMP=1>
	"myös" ADV <W=0> <CMP=1>
	"myös" ADV <W=0> <CMP=1>

"<Tuusniemen>"
	"Tuusniemi" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>

"<kunta>"
	"kunta" NOUN SG NOM <W=0> <CMP=1>

"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>
	"," SYM <W=0> <CMP=1>

"<mutta>"
	"mutta" ADP <W=0> <CMP=1>
	"mutta" CCONJ <W=0> <CMP=1>
	"mä" PRON PRS SG1 <STYLE_DIALECTAL> SG ABE <W=0> <CMP=1>

"<sen>"
	"se" PRON DEM SG GEN <W=0> <CMP=1>
	"se" DET SG GEN <W=0> <CMP=1>
	"sen" ADV <W=0> <CMP=1>

"<valtuusto>"
	"valtuusto" NOUN SG NOM <W=0> <CMP=1>

"<päätti>"
	"päättää" VERB ACT INDV PAST SG0 <W=0> <CMP=1>
	"päättää" VERB ACT INDV PAST SG3 <W=0> <CMP=1>

"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>
	"," SYM <W=0> <CMP=1>

"<että>"
	"että" SCONJ <W=0> <CMP=1>
	"että" INTJ <W=0> <CMP=1>
	"että" CCONJ <W=0> <CMP=1>

"<Tuusniemi>"
	"Tuusniemi" PROPN <PROPER_GEO> SG NOM <W=0> <CMP=1>

"<jatkaa>"
	"jatkaa" VERB ACT INFA PL <W=0> <CMP=1>
	"jatkaa" VERB ACT INFA SG <W=0> <CMP=1>
	"jatkaa" VERB ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"jatkaa" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>

"<itsenäisenä>"
	"itsenäinen" ADJ POS SG ESS <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kuopio>"
	"Kuopio" PROPN <PROPER_GEO> SG NOM <W=0> <CMP=1>

"<ja>"
	"ja" CCONJ <W=0> <CMP=1>
	"ja" ADV <W=0> <CMP=1>

"<Juankoski>"
	"Juankoski" PROPN <PROPER_GEO> SG NOM <W=0> <CMP=1>

"<päättävät>"
	"päättävä" ADJ POS PL NOM <W=0> <CMP=1>
	"päättää" VERB ACT INDV PRESENT PL3 <W=0> <CMP=1>
	"päättää" VERB ACT PCPVA PL <W=0> <CMP=1>
	"päättää" VERB <DRV_VA> POS PL NOM <W=0> <CMP=1>

"<seuraavien>"
	"seuraava" ADJ POS PL GEN <W=0> <CMP=1>
	"seurata" VERB <DRV_VA> POS PL GEN <W=0> <CMP=1>

"<kuntavaalien>"
	"kunta#vaali" NOUN PL GEN <W=0> <CMP=2>
	"kuntavaali" NOUN PL GEN <W=0> <CMP=1>

"<toteuttamisesta>"
	"toteuttaa" VERB <DRV_MINEN> SG ELA <W=0> <CMP=1>
	"toteuttaminen" NOUN SG ELA <W=0> <CMP=1>

"<erikseen>"
	"erikseen" ADV <W=0> <CMP=1>
	"erikseen" ADV <W=0> <CMP=1>
	"erä" NOUN <**TOOSHORTFORCOMPOUND> PL TRA POSS3 <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kunnallisvaalit>"
	"kunnallinen#vaali" NOUN PL NOM <*LOWERCASED> <W=0> <CMP=2>

"<järjestetään>"
	"järjestää" VERB PSS INDV PRESENT PE4 <W=0> <CMP=1>

"<seuraavan>"
	"seuraava" ADJ POS SG GEN <W=0> <CMP=1>
	"seurata" VERB <DRV_VA> POS SG GEN <W=0> <CMP=1>

"<kerran>"
	"kerran" ADV MULT <W=0> <CMP=1>
	"kerran" ADV <W=0> <CMP=1>
	"kerta" NOUN SG GEN <W=0> <CMP=1>

"<vuonna>"
	"vuonna" ADV <W=0> <CMP=1>
	"vuonna" ADV <W=0> <CMP=1>
	"vuosi" NOUN SG ESS <STYLE_RARE> <W=0> <CMP=1>

"<2016.>"
	"2016." ADJ <SUBCAT_DIGIT> ORD SG NOM <W=0> <CMP=1>

"<Juankosken>"
	"juan#koski" NOUN SG GEN <W=0> <CMP=2>
	"Juankoski" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>

"<liittymisen>"
	"liittyminen" NOUN SG GEN <W=0> <CMP=1>
	"liittyä" VERB <DRV_MINEN> SG GEN <W=0> <CMP=1>

"<jälkeen>"
	"jälkeen" ADP POST <W=0> <CMP=1>
	"jälkeen" ADV PREP <W=0> <CMP=1>
	"jälki" NOUN SG ILL <W=0> <CMP=1>

"<Kuopion>"
	"Kuopio" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>

"<väkiluku>"
	"väki#luku" NOUN SG NOM <W=0> <CMP=2>
	"väkiluku" NOUN SG NOM <W=0> <CMP=1>

"<on>"
	"olla" AUX ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"olla" AUX ACT INDV PRESENT SG3 <W=0> <CMP=1>
	"olla" VERB ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"olla" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>

"<noin>"
	"noin" ADV <W=0> <CMP=1>
	"noin" ADV <W=0> <CMP=1>
	"noki" NOUN PL INS <W=0> <CMP=1>
	"nuo" PRON DEM PL INS <W=0> <CMP=1>

"<111>"
	"111" NUM <SUBCAT_DIGIT> CARD <W=0> <CMP=1>
	"111" NUM <SUBCAT_DIGIT> CARD SG NOM <W=0> <CMP=1>

"<000>"
	"000" NUM <SUBCAT_DIGIT> CARD SG NOM <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Intian>"
	"Intia" PROPN <PROPER_GEO> <SEM_COUNTRY> SG GEN <W=0> <CMP=1>

"<ja>"
	"ja" CCONJ <W=0> <CMP=1>
	"ja" ADV <W=0> <CMP=1>

"<Japanin>"
	"Japan" PROPN <PROPER_MISC> SG GEN <W=0> <CMP=1>
	"Japani" PROPN <PROPER_GEO> <SEM_COUNTRY> SG GEN <W=0> <CMP=1>

"<pääministerit>"
	"pää#ministeri" NOUN <SEM_TITLE> PL NOM <W=0> <CMP=2>
	"pää#ministeri" NOUN <SEM_TITLE> PL NOM <W=0> <CMP=2>
	"pääministeri" NOUN <SEM_TITLE> PL NOM <W=0> <CMP=1>

"<tapaavat>"
	"tavata" VERB ACT INDV PRESENT PL3 <W=0> <CMP=1>
	"tavata" VERB ACT PCPVA PL <W=0> <CMP=1>
	"tavata" VERB <DRV_VA> POS PL NOM <W=0> <CMP=1>

"<Tokiossa>"
	"Tokio" PROPN <PROPER_GEO> SG INE <W=0> <CMP=1>

"<Intian>"
	"Intia" PROPN <PROPER_GEO> <SEM_COUNTRY> SG GEN <W=0> <CMP=1>

"<uusi>"
	"uusi" ADJ POS SG NOM <W=0> <CMP=1>
	"uusia" VERB ACT IMPV SG2 <W=0> <CMP=1>
	"uusia" VERB ACT INDV PAST SG3 <W=0> <CMP=1>
	"uusia" VERB ACT INDV PRESENT CONNEG <W=0> <CMP=1>

"<pääministeri>"
	"pää#ministeri" NOUN <SEM_TITLE> SG NOM <W=0> <CMP=2>
	"pää#ministeri" NOUN <SEM_TITLE> SG NOM <W=0> <CMP=2>
	"pääministeri" NOUN <SEM_TITLE> SG NOM <W=0> <CMP=1>

"<Narendra>"
	"Narendra" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<Modi>"
	"modi" NOUN SG NOM <*LOWERCASED> <W=0> <CMP=1>

"<tapaa>"
	"tapa" NOUN SG PAR <W=0> <CMP=1>
	"tavata" VERB ACT IMPV SG2 <W=0> <CMP=1>
	"tavata" VERB ACT INDV PRESENT CONNEG <W=0> <CMP=1>
	"tavata" VERB ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"tavata" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>

"<japanilaisen>"
	"japani#lainen" ADJ POS SG GEN <W=0> <CMP=2>
	"japanilainen" ADJ <SEM_COUNTRY> POS SG GEN <W=0> <CMP=1>
	"japanilainen" NOUN <SEM_INHABITANT> SG GEN <W=0> <CMP=1>
	"japanilainen" NOUN <SEM_COUNTRY> SG GEN <W=0> <CMP=1>
	"japanilainen" NOUN <SEM_INHABITANT> SG GEN <W=0> <CMP=1>

"<kollegansa>"
	"kollega" NOUN PL NOM POSS3 <W=0> <CMP=1>
	"kollega" NOUN SG GEN POSS3 <W=0> <CMP=1>
	"kollega" NOUN SG NOM POSS3 <W=0> <CMP=1>

"<Shinzo>"
	"Shinzo" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<Aben>"
	"Aben" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<Tokiossa>"
	"Tokio" PROPN <PROPER_GEO> SG INE <W=0> <CMP=1>

"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>
	"," SYM <W=0> <CMP=1>

"<keskustellakseen>"
	"keskustella" VERB ACT INFA TRA POSS3 <W=0> <CMP=1>

"<talous->"
	"talous" NOUN SG NOM <POSITION_PREFIX> <W=0> <CMP=1>

"<ja>"
	"ja" CCONJ <W=0> <CMP=1>
	"ja" ADV <W=0> <CMP=1>

"<turvallisuussuhteista>"
	"turvallisuus#-suhteinen" ADJ <SUBCAT_SUFFIX> POS SG PAR <W=0> <CMP=2>
	"turvallisuus#suhde" NOUN PL ELA <W=0> <CMP=2>

"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>
	"," SYM <W=0> <CMP=1>

"<ensimmäisellä>"
	"ensimmäinen" NOUN SG ADE <W=0> <CMP=1>
	"ensimmäinen" NUM ORD SG ADE <W=0> <CMP=1>
	"ensimmäinen" ADJ POS SG ADE <W=0> <CMP=1>

"<merkittävällä>"
	"merkittävä" ADJ POS SG ADE <W=0> <CMP=1>
	"merkittää" VERB <DRV_VA> POS SG ADE <W=0> <CMP=1>
	"merkitä" VERB <DRV_TAVA> POS SG ADE <W=0> <CMP=1>

"<ulkomaanvierailullaan>"
	"ulko#maa#vierailu" NOUN SG ADE POSS3 <W=0> <CMP=3>
	"ulkomaa#vierailu" NOUN SG ADE POSS3 <W=0> <CMP=2>

"<toukokuun>"
	"touko#kuu" NOUN <**TOOSHORTFORCOMPOUND> SG GEN <W=0> <CMP=2>
	"toukokuu" NOUN SG GEN <W=0> <CMP=1>

"<vaalivoiton>"
	"vaali#voitto" NOUN SG GEN <W=0> <CMP=2>
	"vaalivoitto" NOUN SG GEN <W=0> <CMP=1>

"<jälkeen>"
	"jälkeen" ADP POST <W=0> <CMP=1>
	"jälkeen" ADV PREP <W=0> <CMP=1>
	"jälki" NOUN SG ILL <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Modin>"
	"modi" NOUN SG GEN <*LOWERCASED> <W=0> <CMP=1>

"<viisipäiväisen>"
	"viisi#-päiväinen" ADJ <SUBCAT_SUFFIX> POS SG GEN <W=0> <CMP=2>
	"viisipäiväinen" ADJ POS SG GEN <W=0> <CMP=1>

"<Japaniin>"
	"japani" NOUN <SEM_LANGUAGE> SG ILL <W=0> <CMP=1>
	"Japan" PROPN <PROPER_MISC> SG ILL <W=0> <CMP=1>
	"Japani" PROPN <PROPER_GEO> <SEM_COUNTRY> SG ILL <W=0> <CMP=1>

"<suuntautuvan>"
	"suu#tau#tupa" NOUN SG GEN <W=0> <CMP=3>
	"suu#tau#tuva" NOUN <SEM_LANGUAGE> SG GEN <W=0> <CMP=3>
	"suuntautua" VERB <DRV_VA> POS SG GEN <W=0> <CMP=1>

"<vierailun>"
	"vierailu" NOUN SG GEN <W=0> <CMP=1>

"<tarkoituksena>"
	"tarkoitus" NOUN SG ESS <W=0> <CMP=1>

"<on>"
	"olla" AUX ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"olla" AUX ACT INDV PRESENT SG3 <W=0> <CMP=1>
	"olla" VERB ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"olla" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>

"<vahvistaa>"
	"vahvistaa" VERB ACT INFA PL <W=0> <CMP=1>
	"vahvistaa" VERB ACT INFA SG <W=0> <CMP=1>
	"vahvistaa" VERB ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"vahvistaa" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>

"<taloussuhteita>"
	"talous#suhde" NOUN PL PAR <W=0> <CMP=2>
	"taloussuhde" NOUN PL PAR <W=0> <CMP=1>

"<maailman>"
	"maa#ilma" NOUN SG GEN <W=0> <CMP=2>
	"maailma" NOUN SG GEN <W=0> <CMP=1>
	"maailma" NOUN SG GEN <W=0> <CMP=1>

"<kolmanneksi>"
	"kolmas" NUM ORD SG TRA <W=0> <CMP=1>
	"kolmas" ADJ POS SG TRA <W=0> <CMP=1>

"<suurimpaan>"
	"suuri" ADJ <DRV_IN²> SUP SG ILL <W=0> <CMP=1>

"<talouteen>"
	"talo#ute" NOUN <**TOOSHORTFORCOMPOUND> SG ILL <W=0> <CMP=2>
	"talous" NOUN SG ILL <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>
```

Compare this to the [results of disambiguation](#analyse and disambiguate) to determine which format suits you better.

For further options there is `omorfi-vislcg.py` python script.

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
alussa	[WORD_ID=alussa][UPOS=ADP]
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
```

If your text is already split into word-forms (one word-form per line), it can
be analysed faster with `omorfi-analyse-tokenised.sh` tool:

```
$ omorfi-analyse-tokenised.sh test/wordforms.list | head
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
$ omorfi-factorise.bash test/test.text 
Juankosken|Juankosken|UNK|UNKNOWN|0 kaupunki|kaupunki|NOUN|NOUN.SG.NOM|0 liittyy|liittyä|VERB|VERB.ACT.INDV.PRESENT.SG0|0 Kuopion|kuopia|VERB|VERB.ACT.OPT.SG1.ARCHAIC.LOWERCASED|0 kaupunkiin|kaupunki|NOUN|NOUN.SG.ILL|0 vuoden|vuosi|NOUN|NOUN.SG.GEN|0 2017|2017|NUM|NUM.DIGIT.CARD|0 alussa|alku|NOUN|NOUN.SG.INE|0 .|.|PUNCT|PUNCT.SENTENCE|0 
Kuopion|kuopia|VERB|VERB.ACT.OPT.SG1.ARCHAIC.LOWERCASED|0 kaupunginvaltuusto|kaupunginvaltuusto|NOUN|NOUN.SG.NOM|o hyväksyi|hyväksyä|VERB|VERB.ACT.INDV.PAST.SG0|0 liitoksen|liitos|NOUN|NOUN.SG.GEN|0 yksimielisesti|yksi+-mielinen|ADJ|ADJ.SUFFIX.POS.POS.STI|i maanantaina|maanantai|NOUN|NOUN.PL.ESS|0 .|.|PUNCT|PUNCT.SENTENCE|0 
Juankosken|Juankosken|UNK|UNKNOWN|0 kaupunginvaltuusto|kaupunginvaltuusto|NOUN|NOUN.SG.NOM|o hyväksyi|hyväksyä|VERB|VERB.ACT.INDV.PAST.SG0|0 liitoksen|liitos|NOUN|NOUN.SG.GEN|0 viime|viime|ADV|ADV|0 viikolla|viikko|NOUN|NOUN.SG.ADE|0 .|.|PUNCT|PUNCT.SENTENCE|0 
Kuntaliitoksen|kunta+liitos|NOUN|NOUN.SG.GEN.LOWERCASED|0 selvittämisessä|selvittää|VERB|VERB.MINEN.SG.INE|.ssä oli|olla|AUX|AUX.ACT.INDV.PAST.SG3|0 mukana|mukana|ADP|ADP.POST|0 myös|myödä|VERB|VERB.DIALECTAL.ACT.IMPV.SG2.S|0 Tuusniemen|Tuusniemen|UNK|UNKNOWN|0 kunta|kunta|NOUN|NOUN.SG.NOM|0 ,|,|PUNCT|PUNCT.CLAUSE.COMMA|0 mutta|mutta_2|CCONJ|CCONJ|0 sen|se|PRON|PRON.DEM.SG.GEN|0 valtuusto|valtuusto|NOUN|NOUN.SG.NOM|0 päätti|päättää|VERB|VERB.ACT.INDV.PAST.SG0|0 ,|,|PUNCT|PUNCT.CLAUSE.COMMA|0 että|että|SCONJ|SCONJ|0 Tuusniemi|Tuusniemi|UNK|UNKNOWN|0 jatkaa|jatkaa|VERB|VERB.ACT.A.PL.LAT|0 itsenäisenä|itsenäinen|ADJ|ADJ.POS.SG.ESS|0 .|.|PUNCT|PUNCT.SENTENCE|0 
Kuopio|Kuopio|UNK|UNKNOWN|0 ja|ja|CCONJ|CCONJ|0 Juankoski|Juankoski|UNK|UNKNOWN|0 päättävät|päättävä|ADJ|ADJ.POS.PL.NOM|0 seuraavien|seuraava|ADJ|ADJ.POS.PL.GEN|0 kuntavaalien|kunta+vaali|NOUN|NOUN.PL.GEN|.i.en toteuttamisesta|toteuttaa|VERB|VERB.MINEN.SG.ELA|.sta erikseen|erikseen|ADV|ADV|0 .|.|PUNCT|PUNCT.SENTENCE|0 
Kunnallisvaalit|kunnallinen+vaali|NOUN|NOUN.PL.NOM.LOWERCASED|0 järjestetään|järjestää|VERB|VERB.PSS.INDV.PRESENT.PE4|0 seuraavan|seuraava|ADJ|ADJ.POS.SG.GEN|0 kerran|kerran|ADV|ADV.MULT|0 vuonna|vuonna|ADV|ADV|0 2016.|2016.|ADJ|ADJ.DIGIT.ORD.SG.NOM|0 
Juankosken|Juankosken|UNK|UNKNOWN|0 liittymisen|liittyä|VERB|VERB.MINEN.SG.GEN|.n jälkeen|jälki|NOUN|NOUN.SG.ILL|0 Kuopion|kuopia|VERB|VERB.ACT.OPT.SG1.ARCHAIC.LOWERCASED|0 väkiluku|väki+luku|NOUN|NOUN.SG.NOM|u on|olla|AUX|AUX.ACT.INDV.PRESENT.SG0|0 noin|noin|ADV|ADV|0 111|111|NUM|NUM.DIGIT.CARD|0 000|000|NUM|NUM.DIGIT.CARD.SG.NOM|0 .|.|PUNCT|PUNCT.SENTENCE|0 
Intian|Intian|UNK|UNKNOWN|0 ja|ja|CCONJ|CCONJ|0 Japanin|japani|NOUN|NOUN.LANGUAGE.SG.GEN.LOWERCASED|0 pääministerit|pää+ministeri|NOUN|NOUN.TITLE.PL.NOM|.t tapaavat|tavata_2|VERB|VERB.ACT.INDV.PRESENT.PL3|.t Tokiossa|Tokiossa|UNK|UNKNOWN|0 
Intian|Intian|UNK|UNKNOWN|0 uusi|uusi|ADJ|ADJ.POS.SG.NOM|0 pääministeri|pää+ministeri|NOUN|NOUN.TITLE.SG.NOM|i Narendra|Narendra|UNK|UNKNOWN|0 Modi|Modi|UNK|UNKNOWN|0 tapaa|tapa|NOUN|NOUN.SG.PAR|0 japanilaisen|japani+lainen|ADJ|ADJ.POS.SG.GEN|0 kollegansa|kollega|NOUN|NOUN.PL.NOM.3|0 Shinzo|Shinzo|UNK|UNKNOWN|0 Aben|Aben|UNK|UNKNOWN|0 Tokiossa|Tokiossa|UNK|UNKNOWN|0 ,|,|PUNCT|PUNCT.CLAUSE.COMMA|0 keskustellakseen|keskustella|VERB|VERB.ACT.A.TRA.3|0 talous-|talous|NOUN|NOUN.SG.NOM.PREFIX|0 ja|ja|CCONJ|CCONJ|0 turvallisuussuhteista|turvallisuus+-suhteinen|ADJ|ADJ.SUFFIX.POS.SG.PAR|.ta ,|,|PUNCT|PUNCT.CLAUSE.COMMA|0 ensimmäisellä|ensimmäinen|NOUN|NOUN.SG.ADE|0 merkittävällä|merkittävä|ADJ|ADJ.POS.SG.ADE|0 ulkomaanvierailullaan|ulko+maa+vierailu|NOUN|NOUN.SG.ADE.3|.n{hyph?}vierailu.lla.an toukokuun|touko+kuu|NOUN|NOUN.TOOSHORTFORCOMPOUND.SG.GEN|.n vaalivoiton|vaali+voitto|NOUN|NOUN.SG.GEN|.n jälkeen|jälki|NOUN|NOUN.SG.ILL|0 .|.|PUNCT|PUNCT.SENTENCE|0 
Modin|Modin|UNK|UNKNOWN|0 viisipäiväisen|viisi+-päiväinen|ADJ|ADJ.SUFFIX.POS.SG.GEN|0 Japaniin|japani|NOUN|NOUN.LANGUAGE.SG.ILL.LOWERCASED|0 suuntautuvan|suu+tau+tupa|NOUN|NOUN.SG.GEN|.n vierailun|vierailu|NOUN|NOUN.SG.GEN|0 tarkoituksena|tarkoitus|NOUN|NOUN.SG.ESS|0 on|olla|AUX|AUX.ACT.INDV.PRESENT.SG0|0 vahvistaa|vahvistaa|VERB|VERB.ACT.A.PL.LAT|0 taloussuhteita|talous+suhde|NOUN|NOUN.PL.PAR|.i.ta maailman|maa+ilma|NOUN|NOUN.SG.GEN|0 kolmanneksi|kolmas|NUM|NUM.ORD.SG.TRA|0 suurimpaan|suuri|ADJ|ADJ.IN².SUP.SG.ILL|{STUB}mpa.an talouteen|talous|NOUN|NOUN.SG.ILL|0 .|.|PUNCT|PUNCT.SENTENCE|0 
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
1	Juankosken	Juankoski	PROPN	N	Case=Gen|Number=Sing	_	_	_	_
2	kaupunki	kaupunki	NOUN	N	Case=Nom|Number=Sing	_	_	_	_
3	liittyy	liittyä	VERB	V	Mood=Ind|Number=Sing|Tense=Pres|VerbForm=Fin|Voice=Act	_	_	_	_
4	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	__	_
5	kaupunkiin	kaupunki	NOUN	N	Case=Ill|Number=Sing	_	_	_	_
6	vuoden	vuoden	ADV	Adv	_	_	_	_	_
7	2017	2017	NUM	Num	NumType=Card	_	_	__
8	alussa	alku	NOUN	N	Case=Ine|Number=Sing	_	__	_
9	.	.	PUNCT	Punct	_	_	_	_	_

# sent_id = 2
# text = Kuopion kaupunginvaltuusto hyväksyi liitoksen yksimielisesti maanantaina.
1	Kuopion	Kuopio	PROPN	N	Case=Gen|Number=Sing	_	__	_
2	kaupunginvaltuusto	kaupunginvaltuusto	NOUN	N	Case=Nom|Number=Sing	_	_	_	_
3	hyväksyi	hyväksyä	VERB	V	Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act	_	_	_	_
4	liitoksen	liitos	NOUN	N	Case=Gen|Number=Sing	_	_	_	_
5	yksimielisesti	yksi#-mielinen	ADJ	A	Degree=Pos|Derivation=Sti	_	_	_	_
6	maanantaina	maanantai	NOUN	N	Case=Ess|Number=Plur	_	_	_	_
7	.	.	PUNCT	Punct	_	_	_	_	_
```

For more options there is a python script `omorfi-conllu.py`.

### FTB3.1 analysis

Omorfi can output FTB3.1-compatible format with `omorfi-ftb3.bash`:

```
$ omorfi-ftb3.bash -X test/test.text 
reading from <stdin>
<s><loc file="<stdin>" line="1" />
1	Juankosken	Juankoski	N	N	N Prop Sg Gen	_	_	_	_
2	kaupunki	kaupunki	N	N	N Sg Nom	__	_	_
3	liittyy	liittyä	V	V	V Act Prs Sg3	_	_	__
4	Kuopion	Kuopio	N	N	N Prop Sg Gen	_	_	__
5	kaupunkiin	kaupunki	N	N	N Sg Ill	__	_	_
6	vuoden	vuoden	Adv	Adv	Adv	_	_	_	_
7	2017	2017	Num	Num	Num Digit	_	_	__
8	alussa	alku	N	N	N Sg Ine	_	_	__
9	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="2" />
1	Kuopion	Kuopio	N	N	N Prop Sg Gen	_	_	__
2	kaupunginvaltuusto	kaupunginvaltuusto	N	N	N Sg Nom	_	_	_	_
3	hyväksyi	hyväksyä	V	V	V Act Past Sg3	_	_	_	_
4	liitoksen	liitos	N	N	N Sg Gen	_	__	_
5	yksimielisesti	yksi#-mielinen	A	A	A Pos Pos	__	_	_
6	maanantaina	maanantai	N	N	N Pl Ess	__	_	_
7	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="3" />
1	Juankosken	Juankoski	N	N	N Prop Sg Gen	_	_	_	_
2	kaupunginvaltuusto	kaupunginvaltuusto	N	N	N Sg Nom	_	_	_	_
3	hyväksyi	hyväksyä	V	V	V Act Past Sg3	_	_	_	_
4	liitoksen	liitos	N	N	N Sg Gen	_	__	_
5	viime	viime	Adv	Adv	Adv	_	_	_	_
6	viikolla	viikko	N	N	N Sg Ade	_	__	_
7	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="4" />
1	Kuntaliitoksen	kunta#liitos	N	N	N Sg Gen	__	_	_
2	selvittämisessä	selvittäminen	N	N	N Sg Ine	__	_	_
3	oli	olla	V	V	V Act Past Sg3	_	_	__
4	mukana	mukana	Adp	Adp	Adp Po	_	_	_	_
5	myös	myödä	V	V	V Act Imp Sg2 S	_	_	__
6	Tuusniemen	Tuusniemi	N	N	N Prop Sg Gen	_	_	_	_
7	kunta	kunta	N	N	N Sg Nom	_	_	__
8	,	,	Punct	Punct	Punct	_	_	_	_
9	mutta	mutta	Adp	Adp	Adp	_	_	_	_
10	sen	se	Pron	Pron	Pron Dem Sg Gen	_	_	__
11	valtuusto	valtuusto	N	N	N Sg Nom	__	_	_
12	päätti	päättää	V	V	V Act Past Sg3	_	_	__
13	,	,	Punct	Punct	Punct	_	_	_	_
14	että	että	CS	CS	CS	_	_	_	_
15	Tuusniemi	Tuusniemi	N	N	N Prop Sg Nom	_	_	_	_
16	jatkaa	jatkaa	V	V	V Inf1 Lat	_	_	__
17	itsenäisenä	itsenäinen	A	A	A Pos Sg Ess	_	_	_	_
18	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="5" />
1	Kuopio	Kuopio	N	N	N Prop Sg Nom	_	_	__
2	ja	ja	CC	CC	CC	_	_	_	_
3	Juankoski	Juankoski	N	N	N Prop Sg Nom	_	_	_	_
4	päättävät	päättävä	A	A	A Pos Pl Nom	_	_	_	_
5	seuraavien	seuraava	A	A	A Pos Pl Gen	_	_	_	_
6	kuntavaalien	kunta#vaali	N	N	N Pl Gen	__	_	_
7	toteuttamisesta	toteuttaa	N	N	N Sg Ela	__	_	_
8	erikseen	erikseen	Adv	Adv	Adv	_	__	_
9	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="6" />
1	Kunnallisvaalit	kunnallinen#vaali	N	N	N Pl Nom	_	_	_	_
2	järjestetään	järjestää	V	V	V Pass Prs Pe4	_	_	_	_
3	seuraavan	seuraava	A	A	A Pos Sg Gen	_	_	_	_
4	kerran	kerran	Adv	Adv	Adv Mult	_	_	__
5	vuonna	vuonna	Adv	Adv	Adv	_	_	_	_
6	2016.	2016.	A	A	A Digit Sg Nom	_	_	__
</s>
<s><loc file="<stdin>" line="7" />
1	Juankosken	Juankoski	N	N	N Prop Sg Gen	_	_	_	_
2	liittymisen	liittyminen	N	N	N Sg Gen	__	_	_
3	jälkeen	jälkeen	Adp	Adp	Adp Po	_	_	_	_
4	Kuopion	Kuopio	N	N	N Prop Sg Gen	_	_	__
5	väkiluku	väki#luku	N	N	N Sg Nom	__	_	_
6	on	olla	V	V	V Act Prs Sg3	_	_	__
7	noin	noin	Adv	Adv	Adv	_	_	_	_
8	111	111	Num	Num	Num Digit	_	_	__
9	000	000	Num	Num	Num Digit Sg Nom	_	__	_
10	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="8" />
1	Intian	Intia	N	N	N Prop Sg Gen	_	_	__
2	ja	ja	CC	CC	CC	_	_	_	_
3	Japanin	Japan	N	N	N Prop Sg Gen	_	_	__
4	pääministerit	pää#ministeri	N	N	N Pl Nom	__	_	_
5	tapaavat	tavata	V	V	V Act Prs Pl3	_	__	_
6	Tokiossa	Tokio	N	N	N Prop Sg Ine	_	__	_
</s>
<s><loc file="<stdin>" line="9" />
1	Intian	Intia	N	N	N Prop Sg Gen	_	_	__
2	uusi	uusi	A	A	A Pos Sg Nom	_	_	__
3	pääministeri	pää#ministeri	N	N	N Sg Nom	__	_	_
4	Narendra	Narendra	N	N	N Prop Sg Nom	_	_	_	_
5	Modi	modi	N	N	N Sg Nom	_	_	__
6	tapaa	tapa	N	N	N Sg Par	_	_	__
7	japanilaisen	japani#lainen	A	A	A Pos Sg Gen	_	_	_	_
8	kollegansa	kollega	N	N	N Pl Nom PxSp3	_	__	_
9	Shinzo	Shinzo	N	N	N Prop Sg Nom	_	_	__
10	Aben	Aben	N	N	N Prop Sg Nom	_	_	__
11	Tokiossa	Tokio	N	N	N Prop Sg Ine	_	__	_
12	,	,	Punct	Punct	Punct	_	_	_	_
13	keskustellakseen	keskustella	V	V	V Inf1 Tra PxSp3	_	_	_	_
14	talous-	talous	N	N	N Sg Nom	_	_	__
15	ja	ja	CC	CC	CC	_	_	_	_
16	turvallisuussuhteista	turvallisuus#-suhteinen	A	A	A Pos Sg Par	_	_	_	_
17	,	,	Punct	Punct	Punct	_	_	_	_
18	ensimmäisellä	ensimmäinen	N	N	N Sg Ade	__	_	_
19	merkittävällä	merkittävä	A	A	A Pos Sg Ade	_	_	_	_
20	ulkomaanvierailullaan	ulko#maa#vierailu	N	N	N Sg Ade PxSp3	_	_	_	_
21	toukokuun	touko#kuu	N	N	N Sg Gen	__	_	_
22	vaalivoiton	vaali#voitto	N	N	N Sg Gen	__	_	_
23	jälkeen	jälkeen	Adp	Adp	Adp Po	_	_	_	_
24	.	.	Punct	Punct	Punct	_	_	_	_
</s>
<s><loc file="<stdin>" line="10" />
1	Modin	modi	N	N	N Sg Gen	_	_	__
2	viisipäiväisen	viisi#-päiväinen	A	A	A Pos Sg Gen	_	_	_	_
3	Japaniin	Japan	N	N	N Prop Sg Ill	_	__	_
4	suuntautuvan	suu#tau#tupa	N	N	N Sg Gen	__	_	_
5	vierailun	vierailu	N	N	N Sg Gen	__	_	_
6	tarkoituksena	tarkoitus	N	N	N Sg Ess	__	_	_
7	on	olla	V	V	V Act Prs Sg3	_	_	__
8	vahvistaa	vahvistaa	V	V	V Inf1 Lat__	_	_
9	taloussuhteita	talous#suhde	N	N	N Pl Par	__	_	_
10	maailman	maa#ilma	N	N	N Sg Gen	__	_	_
11	kolmanneksi	kolmas	Num	Num	Num Ord Sg Tra	_	__	_
12	suurimpaan	suuri	A	A	A Sup Sg Ill	_	__	_
13	talouteen	talo#ute	N	N	N Sg Ill	__	_	_
14	.	.	Punct	Punct	Punct	_	_	_	_
</s>
```

### Coverage analysis

It is possible to get naïve coverage estimates with `omorfi-freq-evals.bash`:

```
$ omorfi-freq-evals.bash -X test/test.text 
reading from <stdin>
OOV	Shinzo
OOV	Narendra
OOV	Aben
CPU time: 0.05708267499999997 real time: 0.05948968802113086
Lines	Covered	OOV
110	107	3
100.0	97.27272727272728	2.727272727272727
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

For CONLL-U and so Universal dependencies, you'd use `-O conllu`:

```
$ omorfi-tokenise.py -a /usr/local/share/omorfi/omorfi.describe.hfst -i test/test.text -O conllu | head
# new doc id= test/test.text
# sent_id = 1
# text = Juankosken kaupunki liittyy Kuopion kaupunkiin vuoden 2017 alussa.
1	Juankosken	_	_	_	_	_	_	__
2	kaupunki	_	_	_	_	_	_	__
3	liittyy	_	_	_	_	_	_	_	_
4	Kuopion	_	_	_	_	_	_	_	_
5	kaupunkiin	_	_	_	_	_	_	__
6	vuoden	_	_	_	_	_	_	_	_
7	2017	_	_	_	_	_	_	_	_
```



### Morphological segmentation

Omorfi can be used to segment word-forms into sub-word units with `omorfi-segment.bash`:

```
$ omorfi-segment.sh test/test.text 
Juankosken kaupunki liitty→ ←y Kuopion kaupunki→ ←in vuode→ ←n 2017 alus→ ←sa . 
Kuopion kaupungin→ ←valtuusto hyväksy→ ←i liitokse→ ←n yksi→ ←mielisesti maanantai→ ←na . 
Juankosken kaupungin→ ←valtuusto hyväksy→ ←i liitokse→ ←n viime viiko→ ←lla . 
Kuntaliitoksen selvittämise→ ←ssä ol→ ←i mukana myös Tuusniemen kunta , mutta sen valtuusto päätt→ ←i , että Tuusniemi jatka→ ←a itsenäise→ ←nä . 
Kuopio ja Juankoski päättävä→ ←t seuraav→ ←i→ ←en kuntavaal→ ←i→ ←en toteuttamise→ ←sta erikseen . 
Kunnallisvaalit järjeste→ ←tään seuraava→ ←n kerran vuonna 2016 . 
Juankosken liittymise→ ←n jälke→ ←en Kuopion väki→ ←luku on noin 111 000 . 
Intian ja Japanin pää→ ←ministeri→ ←t tapaava→ ←t Tokiossa 
Intian uusi pää→ ←ministeri Narendra Modi tapaa japanilaise→ ←n kollega→ ←nsa Shinzo Aben Tokiossa , keskustell→ ←a→ ←kse→ ←en talous- ja turvallisuussuhteis→ ←ta , ensimmäise→ ←llä merkittävä→ ←llä ulko→ ←maa→ ←nvierailu→ ←lla→ ←an touko→ ←kuu→ ←n vaali→ ←voito→ ←n jälke→ ←en . 
Modin viisipäiväise→ ←n Japaniin suuntautuva→ ←n vierailu→ ←n tarkoitukse→ ←na on vahvista→ ←a talous→ ←suhte→ ←i→ ←ta maailma→ ←n kolmanne→ ←ksi suuri{STUB}mpa→ ←an taloute→ ←en . 
```

For further options there is a `omorfi-segment.py` python script.

**Preliminary** support for labeled segmentation is also available but not
guaranteed to work.

### Spell-Checking and correction

Spelling correction may be done if hfst-ospell is installed using `omorfi-spell.sh`:

```
$ omorfi-spell.sh test/wordforms.list | head
"." is in the lexicon...
"1" is in the lexicon...
"10" is in the lexicon...
"1 000" is in the lexicon...
"1000–2000" is in the lexicon...
"11" is in the lexicon...
"12" is in the lexicon...
"13" is in the lexicon...
"13 600" is in the lexicon...
"14" is in the lexicon...
```

### Morphological generation

Generating word-forms can be done using `omorfi-generate.sh`:

```
$ omorfi-generate.sh 

[WORD_ID=kissa][UPOS=NOUN][NUM=SG][CASE=INE]
[WORD_ID=kissa][UPOS=NOUN][NUM=SG][CASE=INE]	kissassa	0,0
```

The input for generator is simply the output of the raw analyser.

Generation has not been used so much because I have no use cases. There's some convenience scripts not installed in the `src/bash`, here's a classical example by Fred Karlsson of generating all forms of a noun *kauppa* (a shop) in Finnish. [He lists 2,253 forms](https://www.ling.helsinki.fi/~fkarlsso/genkau2.html), our current version is [here containing 35,983 forms of word *kauppa*](genkau3.html). And here's the execution:

```
echo kauppa > kauppa.wordlist
bash src/bash/generate-wordlist.sh kauppa.wordlist kauppa.wordforms
hfst-lookup src/generated/omorfi.describe.hfst -q < kauppa.wordforms | sed -e 's/\[WORD_ID=kauppa\]\[UPOS=//' | tr '][' '  ' | tr -s '\n' | sed -e 's/[0-9, ]*$//'
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
[{'surf': 'koira', 'analsurf': 'koira', 'anal': '[WORD_ID=koira][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.000000]', 'weight': 0.0}, {'surf': 'koira', 'recase': 'Titlecased', 'analsurf': 'Koira', 'anal': '[WORD_ID=Koira][UPOS=PROPN][BLACKLIST=PROPN-BLOCKING][PROPER=GEO][NUM=SG][CASE=NOM][CASECHANGE=TITLECASED][WEIGHT=28021984.000000]', 'weight': 28021984.0}, {'surf': 'koira', 'analsurf': 'Koira', 'recase': 'Titlecased', 'anal': '[WORD_ID=Koira][UPOS=PROPN][BLACKLIST=PROPN-BLOCKING][PROPER=GEO][NUM=SG][CASE=NOM][WEIGHT=0.000000][CASECHANGE=TITLECASED]', 'weight': 0.0}]
>>> analyses = omorfi.analyse("alusta")
>>> for analysis in analyses:
...     print(analysis['surf'], analysis['anal'], sep=' -> ')
... 
alusta -> [WORD_ID=alku][UPOS=NOUN][NUM=SG][CASE=ELA][WEIGHT=0.000000]
alusta -> [WORD_ID=alunen][UPOS=NOUN][NUM=SG][CASE=PAR][WEIGHT=0.000000]
alusta -> [WORD_ID=alus][UPOS=NOUN][NUM=SG][CASE=PAR][WEIGHT=0.000000]
alusta -> [WORD_ID=alusta][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.000000]
alusta -> [WORD_ID=alusta_2][UPOS=ADV][WEIGHT=0.000000]
alusta -> [WORD_ID=alusta_3][UPOS=ADV][WEIGHT=0.000000]
alusta -> [WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=IMPV][PERS=SG2][WEIGHT=0.000000]
alusta -> [WORD_ID=alustaa][UPOS=VERB][VOICE=ACT][MOOD=INDV][TENSE=PRESENT][NEG=CON][WEIGHT=0.000000]
alusta -> [WORD_ID=Alku][UPOS=PROPN][BLACKLIST=PROPN-BLOCKING][PROPER=FIRST][NUM=SG][CASE=ELA][CASECHANGE=TITLECASED][WEIGHT=28021984.000000]
alusta -> [WORD_ID=Alku_2][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=ELA][CASECHANGE=TITLECASED][WEIGHT=28021984.000000]
alusta -> [WORD_ID=Alku_3][UPOS=PROPN][PROPER=LAST][NUM=SG][CASE=ELA][CASECHANGE=TITLECASED][WEIGHT=28021984.000000]
alusta -> [WORD_ID=Alus][UPOS=PROPN][BLACKLIST=PROPN-BLOCKING][PROPER=LAST][NUM=SG][CASE=PAR][CASECHANGE=TITLECASED][WEIGHT=28021984.000000]
alusta -> [WORD_ID=Alku][UPOS=PROPN][BLACKLIST=PROPN-BLOCKING][PROPER=FIRST][NUM=SG][CASE=ELA][WEIGHT=0.000000][CASECHANGE=TITLECASED]
alusta -> [WORD_ID=Alku_2][UPOS=PROPN][PROPER=GEO][NUM=SG][CASE=ELA][WEIGHT=0.000000][CASECHANGE=TITLECASED]
alusta -> [WORD_ID=Alku_3][UPOS=PROPN][PROPER=LAST][NUM=SG][CASE=ELA][WEIGHT=0.000000][CASECHANGE=TITLECASED]
alusta -> [WORD_ID=Alus][UPOS=PROPN][BLACKLIST=PROPN-BLOCKING][PROPER=LAST][NUM=SG][CASE=PAR][WEIGHT=0.000000][CASECHANGE=TITLECASED]
>>> 
```

## Java

Java class:

```
Reading all in system locations
Loading /usr/local/share/omorfi/
omorfi-giella.generate.hfst
omorfi.describe.hfst
omorfi.describe.hfst = describe : omorfi
omorfi-omor_recased.analyse.hfst
omorfi.generate.hfst
omorfi-omor.generate.hfst
omorfi_recased.describe.hfst
omorfi.analyse.hfst
omorfi.analyse.hfst = analyse : omorfi
omorfi-omor.analyse.hfst
omorfi.accept.hfst
omorfi_recased.analyse.hfst
omorfi.labelsegment.hfst
omorfi.labelsegment.hfst: Unrecognised type labelsegment
omorfi.lemmatise.hfst
omorfi-giella.analyse.hfst
omorfi.tokenise.hfst
/usr/local/share/omorfi/omorfi.tokenise.hfst:net.sf.hfst.FormatException
omorfi.segment.hfst
omorfi-ftb3.analyse.hfst
omorfi-ftb3.generate.hfst
omorfi.hyphenate-rules.hfst
omorfi.hyphenate-rules.hfst: Unrecognised type hyphenate-rules
Loading /usr/share/omorfi/
Loading /home/flammie/.omorfi/
Loading ./
Loading generated/
Loading src/generated/
Loading ../src/generated/
Read all.
> talo
Analysing talo
[WORD_ID=talo][UPOS=NOUN][NUM=SG][CASE=NOM][WEIGHT=0.0]
```
I am not a big fan of Java but acknowledge that some times there are no easy way to avoid it (Android, Servlets, legacy code base), so this may be more useful than native interfacing or other hacks.

## Raw automata

The installed files are in `$prefix/share/omorfi` (my installation is in linux
default: `/usr/local`)

```
$ ls /usr/local/share/omorfi/
master.tsv                   omorfi.lemmatise.hfst
omorfi.accept.hfst           omorfi-omor.analyse.hfst
omorfi.analyse.hfst          omorfi-omor.generate.hfst
omorfi.cg3bin                omorfi-omor_recased.analyse.hfst
omorfi.describe.hfst         omorfi_recased.analyse.hfst
omorfi-ftb3.analyse.hfst     omorfi_recased.describe.hfst
omorfi-ftb3.generate.hfst    omorfi.segment.hfst
omorfi.generate.hfst         omorfi.tokenise.hfst
omorfi-giella.analyse.hfst   omorfi.tokenise.pmatchfst
omorfi-giella.generate.hfst  omorfi.tokenise.pmatchfst.debug1
omorfi.hyphenate-rules.hfst  omorfi.tokenise.pmatchfst.debug2
omorfi.labelsegment.hfst     speller-omorfi.zhfst
```

The naming is probably not gonna be same forever, but should be pretty transparent.

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
