# omor stuff: some internal short-hand codes in omorfi databases

_This is an automatically generated documentation based on omorfilexical database._

Stuff are internal things, but they appear in database a lot, so you will want to know what they are if you are gonna modify database of affixes.

The stuff is typically used by the file format and/or analysis generators to either define analysis tags or decide whether or not to include the affected string into language model. The default renditions for a handful of omorfi tag formats are provided (only ones that have trivially mapped formatting are included.


## Stuffs in tabular format

The symbols are default output variants without context-sensitive filtering.
This means that some symbols may be further modified in python code of the
outpyt formatter.



| Stuff | Doc | Omorfi | Apertium | FTB 3.1 | Giella |
|:-----:|:---:|:------:|:--------:|:-------:|:------:|
| [ABBREVIATION](stuffs/ABBREVIATION.html) | Abbreviation, shortening, non-inflecting, may end in full stop |  [ABBR=ABBREVIATION] |  %<abbr%> |  % Abbr |  +ABBR  |
| [ACRONYM](stuffs/ACRONYM.html) | Acronym, shortening that inflects with colon |  [ABBR=ACRONYM] |  %<acr%> |  % N% Abbr |  +ACR  |
| [ADJ](stuffs/ADJ.html) | Adjective, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/ADJ.html |  [UPOS=ADJ] |  %<adj%> |  % A |    |
| [ADP](stuffs/ADP.html) | Adposition, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/ADP.html |  [UPOS=ADP] |  %<post%> |  % Adp% Po |    |
| [ADV](stuffs/ADV.html) | Adverb, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/ADV.html |  [UPOS=ADV] |  %<adv%> |  % Adv |    |
| [AUX](stuffs/AUX.html) | Auxiliary verb, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/AUX.html |  [UPOS=AUX] |  %<vaux%> |   |    |
| [Bc](stuffs/Bc.html) | Compound boundary for generated (derivational-inflectional) compounds |  [BOUNDARY=COMPOUND] |  %<cmp%>+ |  # |  #  |
| [B-](stuffs/B-.html) | Marker for co-ordinated compound hyphen |  [COMPOUND_FORM=OMIT] |  %<cmp-split%> |  % TrunCo |  +Trunc  |
| [B→](stuffs/B→.html) | Marker for left co-ordinated compound hyphen |  [POSITION=SUFFIX] |  %<compound-R%> |  TrunCo%  |  TruncSuffix+  |
| [B←](stuffs/B←.html) | Marker for right co-ordinated compound hyphen |  [POSITION=PREFIX] |  %<compound-only-L%> |  % TrunCo |  +TruncPrefix  |
| [Bxxx](stuffs/Bxxx.html) | Compound missing hyphen unjoined |  [COMPOUND_FORM=MISSING-] |  %<compound-only-L%> |   |    |
| [CARDINAL](stuffs/CARDINAL.html) | Cardinal, lexical feature based on UD NumType, refer to http://universaldependencies.org/u/feat/NumType.html |  [NUMTYPE=CARD] |  %<card%> |   |    |
| [Ccmp](stuffs/Ccmp.html) | Comparative comparison, inflectional feature, refer to http://universaldependencies.org/u/feat/Degree.html |  [CMP=CMP] |  %<comp%> |  % Comp |  +Comp  |
| [CCONJ](stuffs/CCONJ.html) | Coordinating conjunction, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/CCONJ.html |  [UPOS=CCONJ] |  %<cnjcoo%> |   |    |
| [CLAUSE-BOUNDARY](stuffs/CLAUSE-BOUNDARY.html) | Clause final, lexical feature of clause bounding tokens |  [BOUNDARY=CLAUSE] |   |   |    |
| [Cma](stuffs/Cma.html) | Agent participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html |  [PCP=AGENT] |  %<agent%> |  % AgPrc |  +AgPrc  |
| [Cmaisilla](stuffs/Cmaisilla.html) | Fifth infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html |  ERRORMACRO |   |  % Adv |  +Der/maisilla  |
| [Cmaton](stuffs/Cmaton.html) | Negation participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html |  [PCP=NEG] |  %<pneg%> |  % NegPrc |  +NegPrc  |
| [Cnut](stuffs/Cnut.html) | Nut participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html |  [PCP=NUT] |  %<pp%> |  % PrfPrc |  +PrfPrc  |
| [COMPARATIVE](stuffs/COMPARATIVE.html) | Comparative conjunction, lexical feature based on the Finnish grammar, mainly for the lexeme 'kuin', refer to http://kaino.kotus.fi/visk/sisallys.php?p=819 |  [UPOS=SCONJ][CONJ=COMPARATIVE] |  %<cnjsub%> |   |  +CS  |
| [COMP](stuffs/COMP.html) | Comparative, lexicalised version for inflectional feature of adjectives, refer to http://universaldependencies.org/u/feat/Degree.html |  [CMP=CMP] |   |  % Comp |  +Comp  |
| [Cpos](stuffs/Cpos.html) | Positive comparison |  [CMP=POS] |  %<pst%> |  % Pos |  +Pos  |
| [Cpos](stuffs/Cpos.html) | Positive comparison, inflectional feature, refer to http://universaldependencies.org/u/feat/Degree.html |  [CMP=POS] |  %<pst%> |  % Pos |  +Pos  |
| [Csup](stuffs/Csup.html) | Superlative comparison |  [CMP=SUP] |  %<sup%> |  % Superl |  +Superl  |
| [Csup](stuffs/Csup.html) | Superlative comparison, inflectional featurehttp://universaldependencies.org/u/feat/Degree.html, refer to http://universaldependencies.org/u/feat/Degree.html |  [CMP=SUP] |  %<sup%> |  % Superl |  +Superl  |
| [Cva](stuffs/Cva.html) | Va participle |  [PCP=VA] |  %<pprs%> |  % PrsPrc |  +PrsPrc  |
| [Cva](stuffs/Cva.html) | Va participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html |  [PCP=VA] |  %<pprs%> |  % PrsPrc |  +PrsPrc  |
| [DASH](stuffs/DASH.html) | Dash, lexical feature of SYM, apertium compatibility |  [SUBCAT=DASH] |   |  % Dash |  +Dash  |
| [DECIMAL](stuffs/DECIMAL.html) | Decimal digits, lexical feature of NUMs written in digits |  [SUBCAT=DECIMAL] |   |   |    |
| [DEMONSTRATIVE](stuffs/DEMONSTRATIVE.html) | Demonstrative, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html |  [PRONTYPE=DEM] |  %<dem%> |  % Dem |  +Dem  |
| [DET](stuffs/DET.html) | Determiner, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/DET.html |  [UPOS=DET] |  %<det%> |   |    |
| [DIGIT](stuffs/DIGIT.html) | Digits, lexical feature of NUMs written in digits |  [SUBCAT=DIGIT] |   |  % Digit |  +Digit  |
| [Din](stuffs/Din.html) | Derivation -in, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=IN] |  +in%<n%> |   |  +Superl  |
| [Dinen](stuffs/Dinen.html) | Derivation -inen, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=INEN] |  +inen%<n%> |   |  +Der/inint  |
| [Dja](stuffs/Dja.html) | Derivation -jA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=JA] |  +ja%<n%> |   |  +Der/ja  |
| [Dma](stuffs/Dma.html) | Derivation -mA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=MA] |  +ma%<n%> |  % AgPrc |  +AgPrc  |
| [Dmaisilla](stuffs/Dmaisilla.html) | Deverbal -mAisillA |  [DRV=MAISILLA] |  +maisilla%<adv%> |  % Inf5 |  +Der/maisilla  |
| [Dmaisilla](stuffs/Dmaisilla.html) | Deverbal -mAisillA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=MAISILLA] |  +maisilla%<adv%> |  % Inf5 |  +Der/maisilla  |
| [Dmaton](stuffs/Dmaton.html) | Deverbal mAtOn, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=MATON] |  +maton%<adj%> |  % NegPrc |  +NegPrc  |
| [Dminen](stuffs/Dminen.html) | Deverbal -minen, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=MINEN] |  +minen%<n%> |  % N |  +N  |
| [Dmpi](stuffs/Dmpi.html) | Derivation -mpi, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=MPI] |   |   |  +Comp  |
| [Dnut](stuffs/Dnut.html) | Deverbal -nUt, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=NUT] |  +nut%<adj%> |  % PrfPrc% Act |  +PrfPrc+Act  |
| [Ds](stuffs/Ds.html) | Derivaiton -s, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=S] |  +s%<n%> |   |  +Cmp  |
| [Dsti](stuffs/Dsti.html) | Derivation -sti, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=STI] |  +sti%<adv%> |   |  +Der/sti  |
| [Dtattaa](stuffs/Dtattaa.html) | Derivation -tAttAA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=TATTAA] |  +tattaa%<vblex%> |   |  +Der/tattaa  |
| [Dtatuttaa](stuffs/Dtatuttaa.html) | Derivation -tAtUttAA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=TATUTTAA] |  +tatuttaa%<vblex%> |   |  +Der/tatuttaa  |
| [Dtava](stuffs/Dtava.html) | Deverbal -tAvA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=TAVA] |  +tava%<adj%> |  % PrsPrc% Pass |  +PrsPrc+Pass  |
| [Dttaa](stuffs/Dttaa.html) | Derivation -ttAA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=TTAA] |  +ttaa%<vblex%> |   |  +Der/ttaa  |
| [Dtu](stuffs/Dtu.html) | Deverbal -tU, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=TU] |  +tu%<adj%> |  % PrfPrc% Pass |  +PrfPrc+Pass  |
| [Du](stuffs/Du.html) | Derivation -u, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=U] |  +u%<n%> |   |  +Der/u  |
| [Duus](stuffs/Duus.html) | Derivation -UUs, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=UUS] |  +uus%<adj%> |   |  +Der/uus  |
| [Dva](stuffs/Dva.html) | Deverbal -vA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html |  [DRV=VA] |  +va%<adj%> |  % PrsPrc% Act |  +PrsPrc+Act  |
| [FINAL-BRACKET](stuffs/FINAL-BRACKET.html) | Right bracket, lexical feature of SYM, for apertium compatibility |  [SUBCAT=BRACKET][POSITION=FINAL] |   |   |    |
| [FINAL-QUOTE](stuffs/FINAL-QUOTE.html) | Right quotation mark, lexical feature of SYM, for apertium compatibility |  [SUBCAT=QUOTATION][POSITION=FINAL] |   |  % Quote |  +Quote  |
| [FTB3man](stuffs/FTB3man.html) | Manner adverbial (analysis for legacy support) |   |   |  % Man |  +Man  |
| [FTB3man](stuffs/FTB3man.html) | Manner adverbial derivation (analysis for legacy support) |   |   |  % Man |  +Man  |
| [Ia](stuffs/Ia.html) | A infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/InfForm.html |  [INF=A] |  %<infa%> |  % Inf1 |  +Inf1  |
| [Ie](stuffs/Ie.html) | E infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/InfForm.html |  [INF=E] |  %<infe%> |  % Inf2 |  +Inf2  |
| [Ima](stuffs/Ima.html) | mA infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/InfForm.html |  [INF=MA] |  %<infma%> |  % Inf3 |  +Inf3  |
| [Iminen](stuffs/Iminen.html) | Fourth infinitive, inflectional feature |  [INF=MINEN] |  %<infminen%> |  % N |  +N  |
| [INDEFINITE](stuffs/INDEFINITE.html) | Indefinite (pronoun), lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html |  [PRONTYPE=IND] |  %<ind%> |  % Indef |  +Indef  |
| [INITIAL-BRACKET](stuffs/INITIAL-BRACKET.html) | Left bracket, lexical feature of SYM, for apertium compatibility |  [SUBCAT=BRACKET][POSITION=INITIAL] |   |   |    |
| [INITIAL-QUOTE](stuffs/INITIAL-QUOTE.html) | Left quotation mark, lexical feature of SYM, for apertium compatibility |  [SUBCAT=QUOTATION][POSITION=INITIAL] |   |  % Quote |  +Quote  |
| [INTERROGATIVE](stuffs/INTERROGATIVE.html) | Interrogative, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html |  [PRONTYPE=INT] |  %<itg%> |  % Interr |  +Interr  |
| [INTJ](stuffs/INTJ.html) | Interjection, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/INTJ.html |  [UPOS=INTJ] |  %<ij%> |  % Interj |    |
| [LEMMA-START](stuffs/LEMMA-START.html) | Left marker for lemma |  [WORD_ID= |   |   |    |
| [Ncon](stuffs/Ncon.html) | Conneg verb form (in negative constructions), inflectional feature, refer to http://universaldependencies.org/fi/feat/Connegative.html  |  [NEG=CON] |  %<conneg%> |  % ConNeg |  +ConNeg  |
| [Nneg](stuffs/Nneg.html) | Negation verb, lexical feature of the verbs that complent the conneg form verbs |  [SUBCAT=NEG] |  %<neg%> |  % Neg |  +Neg  |
| [N??](stuffs/N__.html) | Number to be determined, inflectional feature |   |  %<sp%> |  % Sg |  +Sg  |
| [NOUN](stuffs/NOUN.html) | Noun, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/NOUN.html |  [UPOS=NOUN] |  %<n%> |  % N |  +N  |
| [Npl](stuffs/Npl.html) | Plural, inflectional feature, refer to http://universaldependencies.org/u/feat/Number.html |  [NUM=PL] |  %<pl%> |  % Pl |  +Pl  |
| [Nsg](stuffs/Nsg.html) | Singular, inflectional feature, refer to http://universaldependencies.org/u/feat/Number.html |  [NUM=SG] |  %<sg%> |  % Sg |  +Sg  |
| [NUM](stuffs/NUM.html) | Numeral, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/NUM.html |  [UPOS=NUM] |  %<num%> |  % Num |  +Num  |
| [O3](stuffs/O3.html) | Third person ambiguous possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html |  [POSS=3] |  %<px3sp%> |  % Px3 |  +Px3  |
| [Opl1](stuffs/Opl1.html) | First person plural possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html |  [POSS=PL1] |  %<px1pl%> |  % PxPl1 |  +PxPl1  |
| [Opl2](stuffs/Opl2.html) | Second person plural possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html |  [POSS=PL2] |  %<px2pl%> |  % PxPl2 |  +PxPl2  |
| [Opl3](stuffs/Opl3.html) | Third person plural possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html |  ERRORMACRO |   |   |    |
| [ORDINAL](stuffs/ORDINAL.html) | Ordinal, lexical feature based on UD NumType, refer to http://universaldependencies.org/u/feat/NumType.html |  [NUMTYPE=ORD] |  %<ord%> |  % Ord |  +Ord  |
| [Osg1](stuffs/Osg1.html) | First person singular possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html |  [POSS=SG1] |  %<px1sg%> |  % PxSg1 |  +PxSg1  |
| [Osg2](stuffs/Osg2.html) | Second person singular possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html |  [POSS=SG2] |  %<px2sg%> |  % PxSg2 |  +PxSg2  |
| [Osg3](stuffs/Osg3.html) | Third person singular possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html |  ERRORMACRO |   |   |    |
| [PE4](stuffs/PE4.html) | Passive / fourth persion, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=PE4] |   |  % Pe4 |  +Pe4  |
| [PERSONAL](stuffs/PERSONAL.html) | Personal, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html |  [PRONTYPE=PRS] |  %<pers%> |  % Pers |  +Pers  |
| [PL1](stuffs/PL1.html) | First plural, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=PL1] |  %<p1%> |  % Pl1 |  +Pl1  |
| [PL2](stuffs/PL2.html) | Secod plural, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=PL2] |  %<p2%> |  % Pl2 |  +Pl2  |
| [PL3](stuffs/PL3.html) | Third plural, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=PL3] |  %<p3%> |  % Pl3 |  +Pl3  |
| [POSTPOSITION](stuffs/POSTPOSITION.html) | Postposition, lexical feature based on UD-Finnish AdpType, an adposition that is after its complement |  [ADPTYPE=POST] |   |   |    |
| [Ppe4](stuffs/Ppe4.html) | Passive" , inflectional feature |  [PERS=PE4] |  %<impers%> |  % Pe4 |  +Pe4  |
| [Ppl1](stuffs/Ppl1.html) | First person plural actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=PL1] |  %<p1%>%<pl%> |  % Pl1 |  +Pl1  |
| [Ppl2](stuffs/Ppl2.html) | Second person plural actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=PL2] |  %<p2%>%<pl%> |  % Pl2 |  +Pl2  |
| [Ppl3](stuffs/Ppl3.html) | Third person plural actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=PL3] |  %<p3%>%<pl%> |  % Pl3 |  +Pl3  |
| [PREPOSITION](stuffs/PREPOSITION.html) | Preposition, lexical feature based on UD-Finnish AdpType, an adposition that is before its complent, refer to http://universaldependencies.org/fi/feat/AdpType.html |  [ADPTYPE=PREP] |   |  % Adp% Pr |  +Adp+Pr  |
| [PRON](stuffs/PRON.html) | Pronoun, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/PRON.html |  [UPOS=PRON] |  %<prn%> |  % Pron |    |
| [PROPN](stuffs/PROPN.html) | Proper noun, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/PROPN.html |  [UPOS=PROPN] |  %<np%> |   |  +Prop  |
| [Psg1](stuffs/Psg1.html) | First person singular actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=SG1] |  %<p1%>%<sg%> |  % Sg1 |  +Sg1  |
| [Psg2](stuffs/Psg2.html) | Second person singular actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=SG2] |  %<p2%>%<sg%> |  % Sg2 |  +Sg2  |
| [Psg3](stuffs/Psg3.html) | Third person singular actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=SG3] |  %<p3%>%<sg%> |  % Sg3 |  +Sg3  |
| [PUNCT](stuffs/PUNCT.html) | Punctuation, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/PUNCT.html |  [UPOS=PUNCT] |  %<punct%> |   |    |
| [Qhan](stuffs/Qhan.html) | Focus clitic particle -hAn, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html |  [CLIT=HAN] |  +han%<enc%> |  % Foc%_hAn |  +Foc/han  |
| [Qkaan](stuffs/Qkaan.html) | Focus clitic particle -kAAn, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html |  [CLIT=KAAN] |  +kaan%<enc%> |  % Foc%_kAAn |  +Foc/kaan  |
| [Qka](stuffs/Qka.html) | Focus clitic particle -kA, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html |  [CLIT=KA] |  +ka%<enc%> |  % Foc%_kA |  +Foc/ka  |
| [Qkin](stuffs/Qkin.html) | Focus clitic particle -kin, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html |  [CLIT=KIN] |  +kin%<enc%> |  % Foc%_kin |  +Foc/kin  |
| [Qko](stuffs/Qko.html) | Focus clitic particle -kO (question), inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html |  [CLIT=KO] |  +ko%<qst%> |  % Foc%_kO |  +Foc/ko  |
| [Qpa](stuffs/Qpa.html) | Focus clitic particle -pA, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html |  [CLIT=PA] |  +pa%<enc%> |  % Foc%_pA |  +Foc/pa  |
| [Qs](stuffs/Qs.html) | Focus clitic particle -s, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html |  [CLIT=S] |  +s%<enc%> |  % Foc%_s |  +Foc/s  |
| [QUANTOR](stuffs/QUANTOR.html) | Quantifier, lexical feature for non-inflecting adjective types, not used elsewhere(?) |  [SUBCAT=QUANTIFIER] |  %<qu%> |  % Qnt |  +Qnt  |
| [RECIPROCAL](stuffs/RECIPROCAL.html) | Reciprocal, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html |  [PRONTYPE=REC] |  %<rec%> |   |    |
| [REFLEXIVE](stuffs/REFLEXIVE.html) | Reflexive (pronoun), lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html |  [SUBCAT=REFLEXIVE] |  %<reflex%> |  % Refl |  +Refl  |
| [RELATIVE](stuffs/RELATIVE.html) | Relative, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html |  [PRONTYPE=REL] |  %<rel%> |  % Rel |  +Rel  |
| [ROMAN](stuffs/ROMAN.html) | Roman numerals, lexical feature of NUMs written in roman numerals |  [SUBCAT=ROMAN] |   |  % Roman |  +Roman  |
| [SCONJ](stuffs/SCONJ.html) | Adverbial conjunction, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/SCONJ.html |  [UPOS=SCONJ] |  %<cnjsub%> |  % CS |    |
| [SENTENCE-BOUNDARY](stuffs/SENTENCE-BOUNDARY.html) | Sentence final, lexical feature of sentece bounding tokens |  [BOUNDARY=SENTENCE] |   |   |    |
| [.sent](stuffs/.sent.html) | Sentence marker, legacy support? |  [BOUNDARY=SENTENCE] |   |   |    |
| [SG1](stuffs/SG1.html) | First singular, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=SG1] |  %<p1%> |  % Sg1 |  +Sg1  |
| [SG2](stuffs/SG2.html) | Second singular, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=SG2] |  %<p2%> |  % Sg2 |  +Sg2  |
| [SG3](stuffs/SG3.html) | Third singular, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html |  [PERS=SG3] |  %<p3%> |  % Sg3 |  +Sg3  |
| [SPACE](stuffs/SPACE.html) | Space, lexical feature of SYM, needed for compatibility with many external systems that do not support space-as-a-token concept |  [SUBCAT=SPACE] |   |   |    |
| [SUPERL](stuffs/SUPERL.html) | Superlative, lexicalised version for inflectional feature of adjectives, refer to http://universaldependencies.org/u/feat/Degree.html |  [CMP=SUP] |  %<sup%> |  % Superl |  +Superl  |
| [SYM](stuffs/SYM.html) | Symbol, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/SYM.html |  [UPOS=SYM] |  %<sym%> |   |    |
| [Tcond](stuffs/Tcond.html) | Conditional, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html |  [MOOD=COND] |  %<cni%> |  % Cond |  +Cond  |
| [Timp](stuffs/Timp.html) | Impertative, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html |  [MOOD=IMPV] |  %<imp%> |  % Impv |  +Impv  |
| [Topt](stuffs/Topt.html) | Optative, inflectional feature, archaic |  [MOOD=OPT] |   |  % Opt |  +Opt  |
| [Tpast](stuffs/Tpast.html) | Indicative past, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html |  [MOOD=INDV][TENSE=PAST] |  %<past%> |  % Pst |  +Pst  |
| [Tpot](stuffs/Tpot.html) | Potential, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html |  [MOOD=POTN] |  %<pot%> |  % Pot |  +Pot  |
| [Tpres](stuffs/Tpres.html) | Indicative Present, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html |  [MOOD=INDV][TENSE=PRESENT] |  %<pri%> |  % Prs |  +Prs  |
| [Uarch](stuffs/Uarch.html) | Archaic form |  [STYLE=ARCHAIC] |  %<use_archaic%> |   |  +Use/Arch  |
| [Udial](stuffs/Udial.html) | Dialectal (generic) form |  [STYLE=DIALECTAL] |  %<use_nonstd%> |   |  +Dial/Finland  |
| [Unonstd](stuffs/Unonstd.html) | Non-standard form |  [STYLE=NONSTANDARD] |  %<use_nonstd%> |   |  +Err/Orth  |
| [UNSPECIFIED](stuffs/UNSPECIFIED.html) | Unclassified particle, lexical feature for undecided particles |   |  %<part%> |  % Adv |  +Pcle  |
| [Urare](stuffs/Urare.html) | Rare form |  [STYLE=RARE] |   |   |  +Use/Marg  |
| [Vact](stuffs/Vact.html) | Active mood, inflectional feature, refer to http://universaldependencies.org/u/feat/Voice.html |  [VOICE=ACT] |  %<actv%> |  % Act |  +Act  |
| [VERB](stuffs/VERB.html) | Verb, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/VERB.html |  [UPOS=VERB] |  %<vblex%> |  % V |  +V  |
| [Vpss](stuffs/Vpss.html) | Passive, inflectional feature, refer to http://universaldependencies.org/u/feat/Voice.html |  [VOICE=PSS] |  %<pasv%> |  % Pass |  +Pass  |
| [Xabe](stuffs/Xabe.html) | Abessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ABE] |  %<abe%> |  % Abe |  +Abe  |
| [Xabl](stuffs/Xabl.html) | Ablative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ABL] |  %<abl%> |  % Abl |  +Abl  |
| [Xacc](stuffs/Xacc.html) | Accusative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ACC] |  %<acc%> |  % Acc |  +Acc  |
| [Xade](stuffs/Xade.html) | Adessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ADE] |  %<ade%> |  % Ade |  +Ade  |
| [Xall](stuffs/Xall.html) | Allative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ALL] |  %<all%> |  % All |  +All  |
| [X???](stuffs/X___.html) | Case to be determined, inflectional feature |   |   |  % Nom |  +Nom  |
| [Xcom](stuffs/Xcom.html) | Comitative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=COM] |  %<com%> |  % Com |  +Com  |
| [Xela](stuffs/Xela.html) | Elative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ELA] |  %<ela%> |  % Ela |  +Ela  |
| [Xess](stuffs/Xess.html) | Essive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ESS] |  %<ess%> |  % Ess |  +Ess  |
| [Xgen](stuffs/Xgen.html) | Genitive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=GEN] |  %<gen%> |  % Gen |  +Gen  |
| [Xill](stuffs/Xill.html) | Illative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=ILL] |  %<ill%> |  % Ill |  +Ill  |
| [Xine](stuffs/Xine.html) | Inessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=INE] |  %<ine%> |  % Ine |  +Ine  |
| [Xins](stuffs/Xins.html) | Instructive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=INS] |  %<ins%> |  % Ins |  +Ins  |
| [Xlat](stuffs/Xlat.html) | Lative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=LAT] |  %<lat%> |  % Lat |  +Lat  |
| [Xnom](stuffs/Xnom.html) | Nominative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=NOM] |  %<nom%> |  % Nom |  +Nom  |
| [Xpar](stuffs/Xpar.html) | Partitive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=PAR] |  %<par%> |  % Par |  +Par  |
| [Xtra](stuffs/Xtra.html) | Transtlative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html |  [CASE=TRA] |  %<tra%> |  % Tra |  +Tra  |
| [X](stuffs/X.html) | Unclassifiable lexeme, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/X.html |  [UPOS=X] |  %<x%> |   |    |

<!-- vim: set ft=markdown:-->
