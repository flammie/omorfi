---
layout: page
title: Omor stuff–Internal codes
---
# omor stuff: some internal short-hand codes in omorfi databases

_This is an automatically generated documentation based on omorfilexical database._

Stuff are internal things, but they appear in database a lot, so you will want to know what they are if you are gonna modify database of affixes.

The stuff is typically used by the file format and/or analysis generators to either define analysis tags or decide whether or not to include the affected string into language model. The default renditions for a handful of omorfi tag formats are provided (only ones that have trivially mapped formatting are included.

<table id="stufftable" class="display">
<thead>
<tr>
<th>Stuff</th>
</tr>
</thead>
<tbody>
{% for page in site.pages %}
{% if page.stuff %}
<tr><td><a href="stuffs/{{page.stuff}}.html">{{page.stuff}}</a></td></tr>
{% endif %}
{% endfor %}
</tbody>
</table>


| Stuff | Doc | Omorfi | Apertium | FTB 3.1 | Giella |
|:-----:|:---:|:------:|:--------:|:-------:|:------:|
| ` NOUN ` | Noun, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/NOUN.html | ` [UPOS=NOUN]` | ` %<n%>` | ` % N` | ` +N`  |
| ` PROPN ` | Proper noun, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/PROPN.html | ` [UPOS=PROPN]` | ` %<np%>` | ` ` | ` +Prop`  |
| ` ADJ ` | Adjective, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/ADJ.html | ` [UPOS=ADJ]` | ` %<adj%>` | ` % A` | ` `  |
| ` VERB ` | Verb, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/VERB.html | ` [UPOS=VERB]` | ` %<vblex%>` | ` % V` | ` +V`  |
| ` AUX ` | Auxiliary verb, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/AUX.html | ` [UPOS=AUX]` | ` %<vaux%>` | ` ` | ` `  |
| ` ADV ` | Adverb, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/ADV.html | ` [UPOS=ADV]` | ` %<adv%>` | ` % Adv` | ` `  |
| ` INTJ ` | Interjection, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/INTJ.html | ` [UPOS=INTJ]` | ` %<ij%>` | ` % Interj` | ` `  |
| ` PRON ` | Pronoun, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/PRON.html | ` [UPOS=PRON]` | ` %<prn%>` | ` % Pron` | ` `  |
| ` NUM ` | Numeral, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/NUM.html | ` [UPOS=NUM]` | ` %<num%>` | ` % Num` | ` +Num`  |
| ` ADP ` | Adposition, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/ADP.html | ` [UPOS=ADP]` | ` %<post%>` | ` % Adp% Po` | ` `  |
| ` CCONJ ` | Coordinating conjunction, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/CCONJ.html | ` [UPOS=CCONJ]` | ` %<cnjcoo%>` | ` ` | ` `  |
| ` SCONJ ` | Adverbial conjunction, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/SCONJ.html | ` [UPOS=SCONJ]` | ` %<cnjsub%>` | ` % CS` | ` `  |
| ` DET ` | Determiner, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/DET.html | ` [UPOS=DET]` | ` %<det%>` | ` ` | ` `  |
| ` PUNCT ` | Punctuation, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/PUNCT.html | ` [UPOS=PUNCT]` | ` %<punct%>` | ` ` | ` `  |
| ` SYM ` | Symbol, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/SYM.html | ` [UPOS=SYM]` | ` %<sym%>` | ` ` | ` `  |
| ` X ` | Unclassifiable lexeme, lexical feature, based on UPOS, refer to http://universaldependencies.org/u/pos/X.html | ` [UPOS=X]` | ` %<x%>` | ` ` | ` `  |
| ` PREPOSITION ` | Preposition, lexical feature based on UD-Finnish AdpType, an adposition that is before its complent, refer to http://universaldependencies.org/fi/feat/AdpType.html | ` [ADPTYPE=PREP]` | ` ` | ` % Adp% Pr` | ` +Adp+Pr`  |
| ` POSTPOSITION ` | Postposition, lexical feature based on UD-Finnish AdpType, an adposition that is after its complement | ` [ADPTYPE=POST]` | ` ` | ` ` | ` `  |
| ` COMPARATIVE ` | Comparative conjunction, lexical feature based on the Finnish grammar, mainly for the lexeme 'kuin', refer to http://kaino.kotus.fi/visk/sisallys.php?p=819 | ` [UPOS=SCONJ][CONJ=COMPARATIVE]` | ` %<cnjsub%>` | ` ` | ` +CS`  |
| ` ABBREVIATION ` | Abbreviation, shortening, non-inflecting, may end in full stop | ` [ABBR=ABBREVIATION]` | ` %<abbr%>` | ` % Abbr` | ` +ABBR`  |
| ` ACRONYM ` | Acronym, shortening that inflects with colon | ` [ABBR=ACRONYM]` | ` %<acr%>` | ` % N% Abbr` | ` +ACR`  |
| ` CARDINAL ` | Cardinal, lexical feature based on UD NumType, refer to http://universaldependencies.org/u/feat/NumType.html | ` [NUMTYPE=CARD]` | ` %<card%>` | ` ` | ` `  |
| ` ORDINAL ` | Ordinal, lexical feature based on UD NumType, refer to http://universaldependencies.org/u/feat/NumType.html | ` [NUMTYPE=ORD]` | ` %<ord%>` | ` % Ord` | ` +Ord`  |
| ` DEMONSTRATIVE ` | Demonstrative, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html | ` [PRONTYPE=DEM]` | ` %<dem%>` | ` % Dem` | ` +Dem`  |
| ` QUANTOR ` | Quantifier, lexical feature for non-inflecting adjective types, not used elsewhere(?) | ` [SUBCAT=QUANTIFIER]` | ` %<qu%>` | ` % Qnt` | ` +Qnt`  |
| ` PERSONAL ` | Personal, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html | ` [PRONTYPE=PRS]` | ` %<pers%>` | ` % Pers` | ` +Pers`  |
| ` INDEFINITE ` | Indefinite (pronoun), lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html | ` [PRONTYPE=IND]` | ` %<ind%>` | ` % Indef` | ` +Indef`  |
| ` INTERROGATIVE ` | Interrogative, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html | ` [PRONTYPE=INT]` | ` %<itg%>` | ` % Interr` | ` +Interr`  |
| ` REFLEXIVE ` | Reflexive (pronoun), lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html | ` [SUBCAT=REFLEXIVE]` | ` %<reflex%>` | ` % Refl` | ` +Refl`  |
| ` RELATIVE ` | Relative, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html | ` [PRONTYPE=REL]` | ` %<rel%>` | ` % Rel` | ` +Rel`  |
| ` RECIPROCAL ` | Reciprocal, lexical feature based on UD PronType, refer to http://universaldependencies.org/u/feat/PronType.html | ` [PRONTYPE=REC]` | ` %<rec%>` | ` ` | ` `  |
| ` DASH ` | Dash, lexical feature of SYM, apertium compatibility | ` [SUBCAT=DASH]` | ` ` | ` % Dash` | ` +Dash`  |
| ` SPACE ` | Space, lexical feature of SYM, needed for compatibility with many external systems that do not support space-as-a-token concept | ` [SUBCAT=SPACE]` | ` ` | ` ` | ` `  |
| ` DECIMAL ` | Decimal digits, lexical feature of NUMs written in digits | ` [SUBCAT=DECIMAL]` | ` ` | ` ` | ` `  |
| ` CLAUSE-BOUNDARY ` | Clause final, lexical feature of clause bounding tokens | ` [BOUNDARY=CLAUSE]` | ` ` | ` ` | ` `  |
| ` SENTENCE-BOUNDARY ` | Sentence final, lexical feature of sentece bounding tokens | ` [BOUNDARY=SENTENCE]` | ` ` | ` ` | ` `  |
| ` INITIAL-QUOTE ` | Left quotation mark, lexical feature of SYM, for apertium compatibility | ` [SUBCAT=QUOTATION][POSITION=INITIAL]` | ` ` | ` % Quote` | ` +Quote`  |
| ` FINAL-QUOTE ` | Right quotation mark, lexical feature of SYM, for apertium compatibility | ` [SUBCAT=QUOTATION][POSITION=FINAL]` | ` ` | ` % Quote` | ` +Quote`  |
| ` INITIAL-BRACKET ` | Left bracket, lexical feature of SYM, for apertium compatibility | ` [SUBCAT=BRACKET][POSITION=INITIAL]` | ` ` | ` ` | ` `  |
| ` FINAL-BRACKET ` | Right bracket, lexical feature of SYM, for apertium compatibility | ` [SUBCAT=BRACKET][POSITION=FINAL]` | ` ` | ` ` | ` `  |
| ` DIGIT ` | Digits, lexical feature of NUMs written in digits | ` ` | ` ` | ` % Digit` | ` +Digit`  |
| ` ROMAN ` | Roman numerals, lexical feature of NUMs written in roman numerals | ` [SUBCAT=ROMAN]` | ` ` | ` % Roman` | ` +Roman`  |
| ` PL1 ` | First plural, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=PL1]` | ` %<p1%>` | ` % Pl1` | ` +Pl1`  |
| ` PL2 ` | Secod plural, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=PL2]` | ` %<p2%>` | ` % Pl2` | ` +Pl2`  |
| ` PL3 ` | Third plural, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=PL3]` | ` %<p3%>` | ` % Pl3` | ` +Pl3`  |
| ` SG1 ` | First singular, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=SG1]` | ` %<p1%>` | ` % Sg1` | ` +Sg1`  |
| ` SG2 ` | Second singular, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=SG2]` | ` %<p2%>` | ` % Sg2` | ` +Sg2`  |
| ` SG3 ` | Third singular, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=SG3]` | ` %<p3%>` | ` % Sg3` | ` +Sg3`  |
| ` PE4 ` | Passive / fourth persion, lexicalised version for inflectional feature of verbs, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=PE4]` | ` ` | ` % Pe4` | ` +Pe4`  |
| ` COMP ` | Comparative, lexicalised version for inflectional feature of adjectives, refer to http://universaldependencies.org/u/feat/Degree.html | ` [CMP=CMP]` | ` ` | ` % Comp` | ` +Comp`  |
| ` SUPERL ` | Superlative, lexicalised version for inflectional feature of adjectives, refer to http://universaldependencies.org/u/feat/Degree.html | ` [CMP=SUP]` | ` %<sup%>` | ` % Superl` | ` +Superl`  |
| ` UNSPECIFIED ` | Unclassified particle, lexical feature for undecided particles | ` ` | ` %<part%>` | ` % Adv` | ` +Pcle`  |
| ` LEMMA-START ` | Left marker for lemma | ` [WORD_ID=` | ` ` | ` ` | ` `  |
| ` Bc ` | Compound boundary for generated (derivational-inflectional) compounds | ` [BOUNDARY=COMPOUND]` | ` %<cmp%>+` | ` #` | ` #`  |
| ` .sent ` | Sentence marker, legacy support? | ` [BOUNDARY=SENTENCE]` | ` ` | ` ` | ` `  |
| ` B- ` | Marker for co-ordinated compound hyphen | ` [COMPOUND_FORM=OMIT]` | ` %<cmp-split%>` | ` % TrunCo` | ` +Trunc`  |
| ` B→ ` | Marker for left co-ordinated compound hyphen | ` [POSITION=SUFFIX]` | ` %<compound-R%>` | ` TrunCo% ` | ` TruncSuffix+`  |
| ` B← ` | Marker for right co-ordinated compound hyphen | ` [POSITION=PREFIX]` | ` %<compound-only-L%>` | ` % TrunCo` | ` +TruncPrefix`  |
| ` Cma ` | Agent participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html | ` [PCP=AGENT]` | ` %<agent%>` | ` % AgPrc` | ` +AgPrc`  |
| ` Cmaisilla ` | Fifth infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html | ` ERRORMACRO` | ` ` | ` % Adv` | ` +Der/maisilla`  |
| ` Cnut ` | Nut participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html | ` [PCP=NUT]` | ` %<pp%>` | ` % PrfPrc` | ` +PrfPrc`  |
| ` Cva ` | Va participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html | ` [PCP=VA]` | ` %<pprs%>` | ` % PrsPrc` | ` +PrsPrc`  |
| ` Cmaton ` | Negation participle, inflectional feature, refer to http://universaldependencies.org/fi/feat/PartForm.html | ` [PCP=NEG]` | ` %<pneg%>` | ` % NegPrc` | ` +NegPrc`  |
| ` Cpos ` | Positive comparison, inflectional feature, refer to http://universaldependencies.org/u/feat/Degree.html | ` [CMP=POS]` | ` %<pos%>` | ` % Pos` | ` +Pos`  |
| ` Ccmp ` | Comparative comparison, inflectional feature, refer to http://universaldependencies.org/u/feat/Degree.html | ` [CMP=CMP]` | ` %<com%>` | ` % Comp` | ` +Comp`  |
| ` Csup ` | Superlative comparison, inflectional featurehttp://universaldependencies.org/u/feat/Degree.html, refer to http://universaldependencies.org/u/feat/Degree.html | ` [CMP=SUP]` | ` %<sup%>` | ` % Superl` | ` +Superl`  |
| ` Dmaisilla ` | Deverbal -mAisillA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=MAISILLA]` | ` +maisilla%<adv%>` | ` % Inf5` | ` +Der/maisilla`  |
| ` Dminen ` | Deverbal -minen, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=MINEN]` | ` +minen%<n%>` | ` % N` | ` +N`  |
| ` Dnut ` | Deverbal -nUt, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=NUT]` | ` +nut%<adj%>` | ` % PrfPrc% Act` | ` +PrfPrc+Act`  |
| ` Dtu ` | Deverbal -tU, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=TU]` | ` +tu%<adj%>` | ` % PrfPrc% Pass` | ` +PrfPrc+Pass`  |
| ` Dva ` | Deverbal -vA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=VA]` | ` +va%<adj%>` | ` % PrsPrc% Act` | ` +PrsPrc+Act`  |
| ` Dtava ` | Deverbal -tAvA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=TAVA]` | ` +tava%<adj%>` | ` % PrsPrc% Pass` | ` +PrsPrc+Pass`  |
| ` Dmaton ` | Deverbal mAtOn, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=MATON]` | ` +maton%<adj%>` | ` % NegPrc` | ` +NegPrc`  |
| ` Duus ` | Derivation -UUs, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=UUS]` | ` +uus%<adj%>` | ` ` | ` +Der/uus`  |
| ` Dttaa ` | Derivation -ttAA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=TTAA]` | ` +ttaa%<vblex%>` | ` ` | ` +Der/ttaa`  |
| ` Dtattaa ` | Derivation -tAttAA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=TATTAA]` | ` +tattaa%<vblex%>` | ` ` | ` +Der/tattaa`  |
| ` Dtatuttaa ` | Derivation -tAtUttAA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=TATUTTAA]` | ` +tatuttaa%<vblex%>` | ` ` | ` +Der/tatuttaa`  |
| ` Dma ` | Derivation -mA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=MA]` | ` +ma%<n%>` | ` % AgPrc` | ` +AgPrc`  |
| ` Dinen ` | Derivation -inen, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=NEN]` | ` +inen%<n%>` | ` ` | ` +Der/inint`  |
| ` Dja ` | Derivation -jA, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=JA]` | ` +ja%<n%>` | ` ` | ` +Der/ja`  |
| ` Dmpi ` | Derivation -mpi, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=MPI]` | ` ` | ` ` | ` +Comp`  |
| ` Din ` | Derivation -in, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=IN]` | ` +in%<n%>` | ` ` | ` +Superl`  |
| ` Ds ` | Derivaiton -s, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=S]` | ` +s%<n%>` | ` ` | ` +Cmp`  |
| ` Du ` | Derivation -u, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=U]` | ` +u%<n%>` | ` ` | ` +Der/u`  |
| ` Dsti ` | Derivation -sti, derivational feature, refer to http://universaldependencies.org/fi/feat/Derivation.html | ` [DRV=STI]` | ` +sti%<adv%>` | ` ` | ` +Der/sti`  |
| ` FTB3man ` | Manner adverbial derivation (analysis for legacy support) | ` ` | ` ` | ` % Man` | ` +Man`  |
| ` Ia ` | A infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/InfForm.html | ` [INF=A]` | ` %<infa%>` | ` % Inf1` | ` +Inf1`  |
| ` Ie ` | E infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/InfForm.html | ` [INF=E]` | ` %<infe%>` | ` % Inf2` | ` +Inf2`  |
| ` Ima ` | mA infinitive, inflectional feature, refer to http://universaldependencies.org/fi/feat/InfForm.html | ` [INF=MA]` | ` %<infma%>` | ` % Inf3` | ` +Inf3`  |
| ` Iminen ` | Fourth infinitive, inflectional feature | ` [INF=MINEN]` | ` %<infminen%>` | ` % N` | ` +N`  |
| ` Ncon ` | Conneg verb form (in negative constructions), inflectional feature, refer to http://universaldependencies.org/fi/feat/Connegative.html  | ` [NEG=CON]` | ` %<conneg%>` | ` % ConNeg` | ` +ConNeg`  |
| ` Nneg ` | Negation verb, lexical feature of the verbs that complent the conneg form verbs | ` [SUBCAT=NEG]` | ` %<neg%>` | ` % Neg` | ` +Neg`  |
| ` Npl ` | Plural, inflectional feature, refer to http://universaldependencies.org/u/feat/Number.html | ` [NUM=PL]` | ` %<pl%>` | ` % Pl` | ` +Pl`  |
| ` Nsg ` | Singular, inflectional feature, refer to http://universaldependencies.org/u/feat/Number.html | ` [NUM=SG]` | ` %<sg%>` | ` % Sg` | ` +Sg`  |
| ` N?? ` | Number to be determined, inflectional feature | ` ` | ` %<sp%>` | ` % Sg` | ` +Sg`  |
| ` Osg1 ` | First person singular possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html | ` [POSS=SG1]` | ` %<pxsg1%>` | ` % PxSg1` | ` +PxSg1`  |
| ` Osg2 ` | Second person singular possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html | ` [POSS=SG2]` | ` %<pxsg2%>` | ` % PxSg2` | ` +PxSg2`  |
| ` Osg3 ` | Third person singular possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html | ` ERRORMACRO` | ` ` | ` ` | ` `  |
| ` O3 ` | Third person ambiguous possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html | ` [POSS=3]` | ` %<pxsp3%>` | ` % Px3` | ` +Px3`  |
| ` Opl1 ` | First person plural possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html | ` [POSS=PL1]` | ` %<pxpl1%>` | ` % PxPl1` | ` +PxPl1`  |
| ` Opl2 ` | Second person plural possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html | ` [POSS=PL2]` | ` %<pxpl2%>` | ` % PxPl2` | ` +PxPl2`  |
| ` Opl3 ` | Third person plural possessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Person-psor.html and http://universaldependencies.org/u/feat/Number-psor.html | ` ERRORMACRO` | ` ` | ` ` | ` `  |
| ` Ppl1 ` | First person plural actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=PL1]` | ` %<p1%>%<pl%>` | ` % Pl1` | ` +Pl1`  |
| ` Ppl2 ` | Second person plural actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=PL2]` | ` %<p2%>%<pl%>` | ` % Pl2` | ` +Pl2`  |
| ` Ppl3 ` | Third person plural actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=PL3]` | ` %<p3%>%<pl%>` | ` % Pl3` | ` +Pl3`  |
| ` Psg1 ` | First person singular actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=SG1]` | ` %<p1%>%<sg%>` | ` % Sg1` | ` +Sg1`  |
| ` Psg2 ` | Second person singular actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=SG2]` | ` %<p2%>%<sg%>` | ` % Sg2` | ` +Sg2`  |
| ` Psg3 ` | Third person singular actor, inflectional feature, refer to http://universaldependencies.org/u/feat/Person.html and http://universaldependencies.org/u/feat/Number.html | ` [PERS=SG3]` | ` %<p3%>%<sg%>` | ` % Sg3` | ` +Sg3`  |
| ` Ppe4 ` | Passive" , inflectional feature | ` [PERS=PE4]` | ` %<impers%>` | ` % Pe4` | ` +Pe4`  |
| ` Qka ` | Focus clitic particle -kA, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html | ` [CLIT=KA]` | ` +ka%<enc%>` | ` % Foc%_kA` | ` +Foc/ka`  |
| ` Qs ` | Focus clitic particle -s, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html | ` [CLIT=S]` | ` +s%<enc%>` | ` % Foc%_s` | ` +Foc/s`  |
| ` Qpa ` | Focus clitic particle -pA, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html | ` [CLIT=PA]` | ` +pa%<enc%>` | ` % Foc%_pA` | ` +Foc/pa`  |
| ` Qko ` | Focus clitic particle -kO (question), inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html | ` [CLIT=KO]` | ` +ko%<qst%>` | ` % Foc%_kO` | ` +Foc/ko`  |
| ` Qkin ` | Focus clitic particle -kin, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html | ` [CLIT=KIN]` | ` +kin%<enc%>` | ` % Foc%_kin` | ` +Foc/kin`  |
| ` Qkaan ` | Focus clitic particle -kAAn, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html | ` [CLIT=KAAN]` | ` +kaan%<enc%>` | ` % Foc%_kAAn` | ` +Foc/kaan`  |
| ` Qhan ` | Focus clitic particle -hAn, inflectional feature. refer to http://universaldependencies.org/fi/feat/Clitic.html | ` [CLIT=HAN]` | ` +han%<enc%>` | ` % Foc%_hAn` | ` +Foc/han`  |
| ` Tcond ` | Conditional, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html | ` [MOOD=COND]` | ` %<cond%>` | ` % Cond` | ` +Cond`  |
| ` Timp ` | Impertative, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html | ` [MOOD=IMPV]` | ` %<imp%>` | ` % Impv` | ` +Impv`  |
| ` Tpast ` | Indicative past, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html | ` [MOOD=INDV][TENSE=PAST]` | ` %<past%>` | ` % Pst` | ` +Pst`  |
| ` Tpot ` | Potential, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html | ` [MOOD=POTN]` | ` %<pot%>` | ` % Pot` | ` +Pot`  |
| ` Tpres ` | Indicative Present, inflectional feature, refer to http://universaldependencies.org/u/feat/Mood.html | ` [MOOD=INDV][TENSE=PRESENT]` | ` %<pri%>` | ` % Prs` | ` +Prs`  |
| ` Topt ` | Optative, inflectional feature, archaic | ` [MOOD=OPT]` | ` ` | ` % Opt` | ` +Opt`  |
| ` Uarch ` | Archaic form | ` [STYLE=ARCHAIC]` | ` %<use_archaic%>` | ` ` | ` +Use/Arch`  |
| ` Udial ` | Dialectal (generic) form | ` [STYLE=DIALECTAL]` | ` %<use_nonstd%>` | ` ` | ` +Dial/Finland`  |
| ` Urare ` | Rare form | ` [STYLE=RARE]` | ` ` | ` ` | ` +Use/Marg`  |
| ` Unonstd ` | Non-standard form | ` [STYLE=NONSTANDARD]` | ` %<use_nonstd%>` | ` ` | ` +Err/Orth`  |
| ` Vact ` | Active mood, inflectional feature, refer to http://universaldependencies.org/u/feat/Voice.html | ` [VOICE=ACT]` | ` %<actv%>` | ` % Act` | ` +Act`  |
| ` Vpss ` | Passive, inflectional feature, refer to http://universaldependencies.org/u/feat/Voice.html | ` [VOICE=PSS]` | ` %<pasv%>` | ` % Pass` | ` +Pass`  |
| ` Xabe ` | Abessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ABE]` | ` %<abe%>` | ` % Abe` | ` +Abe`  |
| ` Xabl ` | Ablative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ABL]` | ` %<abl%>` | ` % Abl` | ` +Abl`  |
| ` Xade ` | Adessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ADE]` | ` %<ade%>` | ` % Ade` | ` +Ade`  |
| ` Xall ` | Allative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ALL]` | ` %<all%>` | ` % All` | ` +All`  |
| ` Xcom ` | Comitative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=COM]` | ` %<com%>` | ` % Com` | ` +Com`  |
| ` Xela ` | Elative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ELA]` | ` %<ela%>` | ` % Ela` | ` +Ela`  |
| ` Xess ` | Essive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ESS]` | ` %<ess%>` | ` % Ess` | ` +Ess`  |
| ` Xgen ` | Genitive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=GEN]` | ` %<gen%>` | ` % Gen` | ` +Gen`  |
| ` Xill ` | Illative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ILL]` | ` %<ill%>` | ` % Ill` | ` +Ill`  |
| ` Xine ` | Inessive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=INE]` | ` %<ine%>` | ` % Ine` | ` +Ine`  |
| ` Xins ` | Instructive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=INS]` | ` %<ins%>` | ` % Ins` | ` +Ins`  |
| ` Xnom ` | Nominative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=NOM]` | ` %<nom%>` | ` % Nom` | ` +Nom`  |
| ` Xpar ` | Partitive, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=PAR]` | ` %<par%>` | ` % Par` | ` +Par`  |
| ` Xtra ` | Transtlative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=TRA]` | ` %<tra%>` | ` % Tra` | ` +Tra`  |
| ` Xlat ` | Lative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=LAT]` | ` %<lat%>` | ` % Lat` | ` +Lat`  |
| ` Xacc ` | Accusative, inflectional feature, refer to http://universaldependencies.org/u/feat/Case.html | ` [CASE=ACC]` | ` %<acc%>` | ` % Acc` | ` +Acc`  |
| ` X??? ` | Case to be determined, inflectional feature | ` ` | ` ` | ` % Nom` | ` +Nom`  |
<!-- vim: set ft=markdown:-->
