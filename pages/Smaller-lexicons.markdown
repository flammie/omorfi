---
title: Smaller lexicon
layout: default
---

# Notes about the smaller lexicon version of omorfi

From 2017 onwards omorfi has included support for optional smaller, higher
quality word list lexicon. This version contains only the words found in the
*Nykysuomen sanalista* and a handful of high frequency tokens verified by omorfi
team. This version is also suitable for limited memory and processing power
devices, e.g. I (flammie) use it on my Asus eee mini laptop when travelling and
developing; the compilation of large lexicon requires over 2 Gigabytes of RAM.

**This version is also suitable for users who oppose the inclusion of Kadai
languages (such as "tai"), south american fishes (such as "tule) or Dravidian
languages (such as "kui" or "kuvi) as plausible lexemes.**

If you use the smaller lexicon in your scientific work, you must state that
clearly in any publications.

## Example

This is an exerpt of the `newstest 2016` WMT test corpus analysed with the
smaller lexicon:

```
"<Juankosken>"
	"Juankosken" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<kaupunki>"
	"kaupunki" NOUN SG NOM <W=0> <CMP=1>

"<liittyy>"
	"liittyä" VERB ACT INDV PRESENT SG0 <W=0> <CMP=1>
	"liittyä" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>

"<Kuopion>"
	"kuopia" VERB ACT OPT SG1 <STYLE_ARCHAIC> <*LOWERCASED> <W=0> <CMP=1>

"<kaupunkiin>"
	"kaupunki" NOUN SG ILL <W=0> <CMP=1>

"<vuoden>"
	"vuosi" NOUN SG GEN <W=0> <CMP=1>

"<2017>"
	"2017" NUM <SUBCAT_DIGIT> CARD <W=0> <CMP=1>
	"2017" NUM <SUBCAT_DIGIT> CARD SG NOM <W=0> <CMP=1>

"<alussa>"
	"alku" NOUN SG INE <W=0> <CMP=1>
	"alunen" NOUN SG ESS <STYLE_ARCHAIC> <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kuopion>"
	"kuopia" VERB ACT OPT SG1 <STYLE_ARCHAIC> <*LOWERCASED> <W=0> <CMP=1>

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

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Juankosken>"
	"Juankosken" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

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

"<viikolla>"
	"viikko" NOUN SG ADE <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kuntaliitoksen>"
	"kunta#liitos" NOUN SG GEN <*LOWERCASED> <W=0> <CMP=2>
	"kuntaliitos" NOUN SG GEN <*LOWERCASED> <W=0> <CMP=1>

"<selvittämisessä>"
	"selvittää" VERB <DRV_MINEN> SG INE <W=0> <CMP=1>

"<oli>"
	"olla" AUX ACT INDV PAST SG3 <W=0> <CMP=1>
	"olla" VERB ACT INDV PAST SG3 <W=0> <CMP=1>

"<mukana>"
	"mukana" ADP POST <W=0> <CMP=1>

"<myös>"
	"myödä" VERB <STYLE_DIALECTAL> ACT IMPV SG2 CLITS <W=0> <CMP=1>
	"myös" ADV <W=0> <CMP=1>
	"myös" ADV <W=0> <CMP=1>

"<Tuusniemen>"
	"Tuusniemen" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<kunta>"
	"kunta" NOUN SG NOM <W=0> <CMP=1>

"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>

"<mutta>"
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

"<että>"
	"että" SCONJ <W=0> <CMP=1>

"<Tuusniemi>"
	"Tuusniemi" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

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
	"Kuopio" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<ja>"
	"ja" CCONJ <W=0> <CMP=1>

"<Juankoski>"
	"Juankoski" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

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

"<toteuttamisesta>"
	"toteuttaa" VERB <DRV_MINEN> SG ELA <W=0> <CMP=1>

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
	"Juankosken" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<liittymisen>"
	"liittyä" VERB <DRV_MINEN> SG GEN <W=0> <CMP=1>

"<jälkeen>"
	"jälki" NOUN SG ILL <W=0> <CMP=1>

"<Kuopion>"
	"kuopia" VERB ACT OPT SG1 <STYLE_ARCHAIC> <*LOWERCASED> <W=0> <CMP=1>

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
	"Intian" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<ja>"
	"ja" CCONJ <W=0> <CMP=1>

"<Japanin>"
	"japani" NOUN <SEM_LANGUAGE> SG GEN <*LOWERCASED> <W=0> <CMP=1>

"<pääministerit>"
	"pää#ministeri" NOUN <SEM_TITLE> PL NOM <W=0> <CMP=2>
	"pää#ministeri" NOUN <SEM_TITLE> PL NOM <W=0> <CMP=2>
	"pääministeri" NOUN <SEM_TITLE> PL NOM <W=0> <CMP=1>

"<tapaavat>"
	"tavata" VERB ACT INDV PRESENT PL3 <W=0> <CMP=1>
	"tavata" VERB ACT PCPVA PL <W=0> <CMP=1>
	"tavata" VERB <DRV_VA> POS PL NOM <W=0> <CMP=1>

"<Tokiossa>"
	"Tokiossa" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<Intian>"
	"Intian" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

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
	"Modi" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

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
	"Tokiossa" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>

"<keskustellakseen>"
	"keskustella" VERB ACT INFA TRA POSS3 <W=0> <CMP=1>

"<talous->"
	"talous" NOUN SG NOM <POSITION_PREFIX> <W=0> <CMP=1>

"<ja>"
	"ja" CCONJ <W=0> <CMP=1>

"<turvallisuussuhteista>"
	"turvallisuus#-suhteinen" ADJ <SUBCAT_SUFFIX> POS SG PAR <W=0> <CMP=2>
	"turvallisuus#suhde" NOUN PL ELA <W=0> <CMP=2>

"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>

"<ensimmäisellä>"
	"ensimmäinen" NOUN SG ADE <W=0> <CMP=1>
	"ensimmäinen" NUM ORD SG ADE <W=0> <CMP=1>

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
	"jälki" NOUN SG ILL <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Modin>"
	"Modin" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>

"<viisipäiväisen>"
	"viisi#-päiväinen" ADJ <SUBCAT_SUFFIX> POS SG GEN <W=0> <CMP=2>
	"viisipäiväinen" ADJ POS SG GEN <W=0> <CMP=1>

"<Japaniin>"
	"japani" NOUN <SEM_LANGUAGE> SG ILL <*LOWERCASED> <W=0> <CMP=1>

"<suuntautuvan>"
	"suu#tau#tupa" NOUN SG GEN <W=0> <CMP=3>
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

"<kolmanneksi>"
	"kolmas" NUM ORD SG TRA <W=0> <CMP=1>

"<suurimpaan>"
	"suuri" ADJ <DRV_IN²> SUP SG ILL <W=0> <CMP=1>

"<talouteen>"
	"talous" NOUN SG ILL <W=0> <CMP=1>

"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>
```

This is same corpus with full lexicon:

```
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

And this is the same corpus analysed with **full** lexicon and using
*disambiguation*:

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

"<Kuopio>"
	"Kuopio" PROPN <PROPER_GEO> SG NOM <W=0> <CMP=1>
"<ja>"
	"ja" CCONJ <W=0> <CMP=1>
"<Juankoski>"
	"Juankoski" PROPN <PROPER_GEO> SG NOM <W=0> <CMP=1>
"<päättävät>"
	"päättävä" ADJ POS PL NOM <W=0> <CMP=1>
	"päättää" VERB ACT INDV PRESENT PL3 <W=0> <CMP=1>
	"päättää" VERB ACT PCPVA PL <W=0> <CMP=1>
"<seuraavien>"
	"seuraava" ADJ POS PL GEN <W=0> <CMP=1>
"<kuntavaalien>"
	"kuntavaali" NOUN PL GEN <W=0> <CMP=1>
"<toteuttamisesta>"
	"toteuttaminen" NOUN SG ELA <W=0> <CMP=1>
"<erikseen>"
	"erikseen" ADV <W=0> <CMP=1>
"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Kunnallisvaalit>"
	"kunnallinen#vaali" NOUN PL NOM <*LOWERCASED> <W=0> <CMP=2>
"<järjestetään>"
	"järjestää" VERB PSS INDV PRESENT PE4 <W=0> <CMP=1>
"<seuraavan>"
	"seuraava" ADJ POS SG GEN <W=0> <CMP=1>
"<kerran>"
	"kerran" ADV MULT <W=0> <CMP=1>
	"kerran" ADV <W=0> <CMP=1>
	"kerta" NOUN SG GEN <W=0> <CMP=1>
"<vuonna>"
	"vuonna" ADV <W=0> <CMP=1>
	"vuosi" NOUN SG ESS <STYLE_RARE> <W=0> <CMP=1>
"<2016.>"
	"2016." ADJ <SUBCAT_DIGIT> ORD SG NOM <W=0> <CMP=1>
"<Juankosken>"
	"Juankoski" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>
"<liittymisen>"
	"liittyminen" NOUN SG GEN <W=0> <CMP=1>
"<jälkeen>"
	"jälkeen" ADP POST <W=0> <CMP=1>
"<Kuopion>"
	"Kuopio" PROPN <PROPER_GEO> SG GEN <W=0> <CMP=1>
"<väkiluku>"
	"väkiluku" NOUN SG NOM <W=0> <CMP=1>
"<on>"
	"olla" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>
	"olla" AUX ACT INDV PRESENT SG3 <W=0> <CMP=1>
"<noin>"
	"noin" ADV <W=0> <CMP=1>
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
"<Japanin>"
	"Japani" PROPN <PROPER_GEO> <SEM_COUNTRY> SG GEN <W=0> <CMP=1>
"<pääministerit>"
	"pääministeri" NOUN <SEM_TITLE> PL NOM <W=0> <CMP=1>
"<tapaavat>"
	"tavata" VERB ACT INDV PRESENT PL3 <W=0> <CMP=1>
"<Tokiossa>"
	"Tokio" PROPN <PROPER_GEO> SG INE <W=0> <CMP=1>
"<Intian>"
	"Intia" PROPN <PROPER_GEO> <SEM_COUNTRY> SG GEN <W=0> <CMP=1>
"<uusi>"
	"uusi" ADJ POS SG NOM <W=0> <CMP=1>
"<pääministeri>"
	"pääministeri" NOUN <SEM_TITLE> SG NOM <W=0> <CMP=1>
"<Narendra>"
	"Narendra" PROPN SG NOM <W=28021984000> <Heur?> <Guesser_PYTHON0ISUPPER> <CMP=1>
"<Modi>"
	"modi" NOUN SG NOM <*LOWERCASED> <W=0> <CMP=1>
"<tapaa>"
	"tapa" NOUN SG PAR <W=0> <CMP=1>
	"tavata" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>
"<japanilaisen>"
	"japanilainen" ADJ <SEM_COUNTRY> POS SG GEN <W=0> <CMP=1>
	"japanilainen" NOUN <SEM_INHABITANT> SG GEN <W=0> <CMP=1>
	"japanilainen" NOUN <SEM_COUNTRY> SG GEN <W=0> <CMP=1>
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
"<keskustellakseen>"
	"keskustella" VERB ACT INFA TRA POSS3 <W=0> <CMP=1>
"<talous->"
	"talous" NOUN SG NOM <POSITION_PREFIX> <W=0> <CMP=1>
"<ja>"
	"ja" CCONJ <W=0> <CMP=1>
"<turvallisuussuhteista>"
	"turvallisuus#-suhteinen" ADJ <SUBCAT_SUFFIX> POS SG PAR <W=0> <CMP=2>
	"turvallisuus#suhde" NOUN PL ELA <W=0> <CMP=2>
"<,>"
	"," PUNCT <CLB> <SUBCAT_COMMA> <W=0> <CMP=1>
"<ensimmäisellä>"
	"ensimmäinen" ADJ POS SG ADE <W=0> <CMP=1>
"<merkittävällä>"
	"merkittävä" ADJ POS SG ADE <W=0> <CMP=1>
"<ulkomaanvierailullaan>"
	"ulkomaa#vierailu" NOUN SG ADE POSS3 <W=0> <CMP=2>
"<toukokuun>"
	"toukokuu" NOUN SG GEN <W=0> <CMP=1>
"<vaalivoiton>"
	"vaalivoitto" NOUN SG GEN <W=0> <CMP=1>
"<jälkeen>"
	"jälkeen" ADP POST <W=0> <CMP=1>
"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>

"<Modin>"
	"modi" NOUN SG GEN <*LOWERCASED> <W=0> <CMP=1>
"<viisipäiväisen>"
	"viisipäiväinen" ADJ POS SG GEN <W=0> <CMP=1>
"<Japaniin>"
	"japani" NOUN <SEM_LANGUAGE> SG ILL <W=0> <CMP=1>
	"Japani" PROPN <PROPER_GEO> <SEM_COUNTRY> SG ILL <W=0> <CMP=1>
"<suuntautuvan>"
	"suuntautua" VERB <DRV_VA> POS SG GEN <W=0> <CMP=1>
"<vierailun>"
	"vierailu" NOUN SG GEN <W=0> <CMP=1>
"<tarkoituksena>"
	"tarkoitus" NOUN SG ESS <W=0> <CMP=1>
"<on>"
	"olla" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>
	"olla" AUX ACT INDV PRESENT SG3 <W=0> <CMP=1>
"<vahvistaa>"
	"vahvistaa" VERB ACT INDV PRESENT SG3 <W=0> <CMP=1>
	"vahvistaa" VERB ACT INFA SG <W=0> <CMP=1>
"<taloussuhteita>"
	"taloussuhde" NOUN PL PAR <W=0> <CMP=1>
"<maailman>"
	"maailma" NOUN SG GEN <W=0> <CMP=1>
"<kolmanneksi>"
	"kolmas" ADJ POS SG TRA <W=0> <CMP=1>
"<suurimpaan>"
	"suuri" ADJ <DRV_IN²> SUP SG ILL <W=0> <CMP=1>
"<talouteen>"
	"talous" NOUN SG ILL <W=0> <CMP=1>
"<.>"
	"." PUNCT <SENT> <W=0> <CMP=1>
```

## Statistics

Compiling smaller lexicon version on 2017-08-31T17:46+02:00 took *2.666 minutes*
as opposed to full version's *8.7 minutes*. For more statistics, see the
[automatically generated statistics](../statistics.html) section of the site.
