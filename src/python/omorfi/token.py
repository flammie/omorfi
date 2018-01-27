#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Support functions for handling tokens. Tokens are currently dicts.
"""
import re

def require_token(token):
    if not isinstance(token, dict):
        raise TypeError("token expected, got:", token)

def require_omor(token):
    if not 'anal' in token:
        raise TypeError("this functionality requires token with omor analyses")

def get_lemmas(token):
    require_omor(token)
    re_lemma = re.compile("\[WORD_ID=([^]]*)\]")
    lemmas = re_lemma.finditer(token['anal'])
    rv = []
    for lemma in lemmas:
        s = lemma.group(1)
        for i in range(32):
            hnsuf = '_' + str(i)
            if s.endswith(hnsuf):
                s = s[:-len(hnsuf)]
        rv += [s]
    return rv


def get_last_feat(feat, token):
    require_omor(token)
    re_feat = re.compile("\[" + feat + "=([^]]*)\]")
    feats = re_feat.finditer(token['anal'])
    rv = ""
    for feat in feats:
        rv = feat.group(1)
    return rv


def get_last_feats(token):
    require_omor(token)
    re_feats = re.compile("\[[A-Z_]*=[^]]*\]")
    rvs = list()
    feats = re_feats.finditer(token['anal'])
    for feat in feats:
        if 'WORD_ID=' in feat.group(0):
            # feats reset on word boundary
            rvs = list()
        else:
            rvs.append(feat.group(0))
    return rvs

def get_upos(token, deriv_munging=True):
    upos = get_last_feat("UPOS", token)
    if deriv_munging:
        drv = get_last_feat("DRV", token)
        if upos == 'VERB' and drv == 'MINEN':
            upos = 'NOUN'
    return upos

def get_ud_feats(token, hacks=None):
    feats = get_last_feats(token)
    rvs = dict()
    for f in feats:
        key = f.split("=")[0].lstrip("[")
        value = f.split("=")[1].rstrip("]")
        if key == 'CASE':
            if value == 'LAT' and hacks != 'ftb':
                # XXX: hack to retain compability
                rvs['Number'] = 'Sing'
            else:
                rvs['Case'] = value[0] + value[1:].lower()
        elif key == 'NUM':
            if value == 'SG':
                rvs['Number'] = 'Sing'
            elif value == 'PL':
                rvs['Number'] = 'Plur'
        elif key == 'TENSE':
            if 'PRESENT' in value:
                rvs['Tense'] = 'Pres'
            elif 'PAST' in value:
                rvs['Tense'] = 'Past'
        elif key == 'MOOD':
            rvs['VerbForm'] = 'Fin'
            if value == 'INDV':
                rvs['Mood'] = 'Ind'
            elif value == 'COND':
                rvs['Mood'] = 'Cnd'
            elif value == 'IMPV':
                rvs['Mood'] = 'Imp'
            else:
                rvs['Mood'] = value[0] + value[1:].lower()
        elif key == 'VOICE':
            if value == 'PSS':
                rvs['Voice'] = 'Pass'
            elif value == 'ACT':
                rvs['Voice'] = 'Act'
        elif key == 'PERS':
            if 'SG' in value:
                rvs['Number'] = 'Sing'
            elif 'PL' in value:
                rvs['Number'] = 'Plur'
            if '1' in value:
                rvs['Person'] = '1'
            elif '2' in value:
                rvs['Person'] = '2'
            elif '3' in value:
                rvs['Person'] = '3'
        elif key == 'POSS':
            if 'SG' in value:
                rvs['Number[psor]'] = 'Sing'
            elif 'PL' in value:
                rvs['Number[psor]'] = 'Plur'
            if '1' in value:
                rvs['Person[psor]'] = '1'
            elif '2' in value:
                rvs['Person[psor]'] = '2'
            elif '3' in value:
                rvs['Person[psor]'] = '3'
        elif key == 'NEG':
            if value == 'CON':
                rvs['Connegative'] = 'Yes'
                # XXX
                rvs.pop('Voice')
            elif value == 'NEG':
                rvs['Polarity'] = 'Neg'
                rvs['VerbForm'] = 'Fin'
        elif key == 'PCP':
            rvs['VerbForm'] = 'Part'
            if value == 'VA':
                rvs['PartForm'] = 'Pres'
            elif value == 'NUT':
                rvs['PartForm'] = 'Past'
            elif value == 'MA':
                rvs['PartForm'] = 'Agent'
            elif value == 'MATON':
                rvs['PartForm'] = 'Neg'
        elif key == 'INF':
            rvs['VerbForm'] = 'Inf'
            if value == 'A':
                rvs['InfForm'] = '1'
            elif value == 'E':
                rvs['InfForm'] = '2'
                # XXX
                rvs['Number'] = 'Sing'
            elif value == 'MA':
                rvs['InfForm'] = '3'
                # XXX
                rvs['Number'] = 'Sing'
            elif value == 'MINEN':
                rvs['InfForm'] = '4'
            elif value == 'MAISILLA':
                rvs['InfForm'] = '5'
        elif key == 'CMP':
            if value == 'SUP':
                rvs['Degree'] = 'Sup'
            elif value == 'CMP':
                rvs['Degree'] = 'Cmp'
            elif value == 'POS':
                rvs['Degree'] = 'Pos'
        elif key == 'SUBCAT':
            if value == 'NEG':
                rvs['Polarity'] = 'Neg'
                rvs['VerbForm'] = 'Fin'
            elif value == 'QUANTIFIER':
                rvs['PronType'] = 'Ind'
            elif value == 'REFLEXIVE':
                rvs['Reflexive'] = 'Yes'
            elif value in ['COMMA', 'DASH', 'QUOTATION', 'BRACKET']:
                # not annotated in UD feats:
                # * punctuation classes
                continue
            elif value in ['DECIMAL', 'ROMAN']:
                # not annotated in UD feats:
                # * decimal, roman NumType
                continue
            else:
                print("Unhandled subcat: ", value)
                print("in", analtoken)
                exit(1)
        elif key == 'ABBR':
            # XXX?
            rvs['Abbr'] = 'Yes'
        elif key == 'NUMTYPE':
            rvs['NumType'] = value[0] + value[1:].lower()
        elif key == 'PRONTYPE':
            rvs['PronType'] = value[0] + value[1:].lower()
        elif key == 'ADPTYPE':
            rvs['AdpType'] = value[0] + value[1:].lower()
        elif key == 'CLIT':
            rvs['Clitic'] = value[0] + value[1:].lower()
        elif key == 'FOREIGN':
            rvs['Foreign'] = value[0] + value[1:].lower()
        elif key == 'STYLE':
            if value in ['DIALECTAL', 'COLLOQUIAL']:
                rvs['Style'] = 'Coll'
            elif value == 'NONSTANDARD':
                # XXX: Non-standard spelling is kind of a typo?
                # e.g. seitsämän -> seitsemän
                rvs['Typo'] = 'Yes'
            elif value == 'ARCHAIC':
                rvs['Style'] = 'Arch'
            elif value == 'RARE':
                continue
            else:
                print("Unknown style", value)
                print("in", analtoken)
                exit(1)
        elif key in ['DRV', 'LEX']:
            if value in ['INEN', 'JA', 'LAINEN', 'LLINEN', 'MINEN', 'STI',
                         'TAR', 'TON', 'TTAA', 'TTAIN', 'U', 'VS']:
                # values found in UD finnish Derivs
                rvs['Derivation'] = value[0] + value[1:].lower()
            elif value in ['S', 'MAISILLA', 'VA', 'MATON', 'UUS',
                           'ADE', 'INE', 'ELA', 'ILL', 'NEN', 'MPI', 'IN',
                           'HKO', 'ISA', 'MAINEN', 'NUT', 'TU', 'VA', 'TAVA',
                           'MA', 'LOC', 'LA']:
                # valuse not found in UD finnish Derivs
                continue
            else:
                print("Unknown non-inflectional affix", key, '=', value)
                print("in", analtoken)
                exit(1)
        elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE', 'NEWPARA',
                     'GUESS', 'PROPER', 'POSITION', 'SEM', 'CONJ']:
            # Not feats in UD:
            # * UPOS is another field
            # * Allomorphy is ignored
            # * Weight = no probabilities
            # * No feats for recasing
            # * FIXME: lexicalised inflection usually not a feat
            # * Guessering not a feat
            # * Proper noun classification not a feat
            # * punct sidedness is not a feat
            # * XXX: sem has not been used as a feat?
            # * special CONJ comparative is not used in UD
            continue
        else:
            print("Unhandled", key, '=', value)
            print("in", token)
            exit(1)
    return rvs

def get_vislcg_feats(token):
    feats = get_last_feats(token)
    vislcgs = list()
    for feat in feats:
        key = feat.split("=")[0].strip("[")
        value = feat.split("=")[1].strip("]")
        if key in ["ALLO", "SEM", "STYLE", "LEX", "DRV", "SUBCAT",
                "POSITION", "ABBR", "FOREIGN"]:
            # semantics, non-core morph in brackets
            vislcgs += ["<" + key + "_" + value + ">"]
        elif key in ["CASE", "NUM", "PERS", "UPOS", "VOICE", "MOOD",
                "TENSE", "NUMTYPE", "ADPTYPE", "CLIT", "PRONTYPE", "CMP",
                "CONJ"]:
            # core morph show only value as is (omor style though)
            vislcgs += [value]
        elif key in ["CLIT", "INF", "PCP", "POSS"]:
            # ...except when only value is too short
            vislcgs += [key + value]
        elif key == "NEG" and value == "CON":
            vislcgs += ["CONNEG"]
        elif key in ["WEIGHT", "GUESS"]:
            # Weights is handled via token features
            pass
        elif key == "BOUNDARY":
            if value == "CLAUSE":
                vislcgs += ["<CLB>"]
            elif value == "SENTENCE":
                vislcgs += ["<SENT>"]
            else:
                print("Unhandled boundary = ", value, "in", token)
                exit(1)
        else:
            print("Unhandled", key, "=", value, "in", token,
                    "for vislcg")
            exit(1)
    if "recase" in token and token['recase'] != "ORIGINALCASE":
        vislcgs += ["<*" + token['recase'] + ">"]
    if "weight" in token:
        vislcgs += ["<W=" + str(int(float(token['weight']) * 1000)) + ">"]
    if "lemmaweight" in token:
        vislcgs += ["<L=" + str(int(float(token['weight']) * 1000)) + ">"]
    if "guess" in token:
        vislcgs += ["<Heur?>", "<Guesser_" + token['guess'] + ">"]
    return vislcgs


def get_segments(token, split_morphs=True, split_words=True,
        split_new_words=True, split_derivs=False, split_nonwords=False):
    segments = token['segments']
    # this code is ugly
    segments = [segments.replace('{hyph?}', '')]
    resegs = []
    for segment in segments:
        if split_morphs:
            resegs += segment.split('{MB}')
        else:
            resegs += [segment.replace('{MB}', '')]
    segments = resegs
    resegs = []
    for segment in segments:
        if split_words:
            resegs += segment.split('{WB}')
        else:
            resegs += [segment.replace('{WB}', '')]
    segments = resegs
    resegs = []
    for segment in segments:
        if split_new_words:
            resegs += segment.split('{wB}')
        else:
            resegs += [segment.replace('{wB}', '')]
    segments = resegs
    resegs = []
    for segment in segments:
        if split_derivs:
            resegs += segment.split('{DB}')
        else:
            resegs += [segment.replace('{DB}', '')]
    segments = resegs
    resegs = []
    for segment in segments:
        if split_nonwords:
            resegs += segment.split('{XB}')
        else:
            resegs += [segment.replace('{XB}', '')]
    return resegs

def get_moses_factor_segments(token):
    analysis = token['labelsegments']
    splat = re.split("[]{}[]", analysis)
    skiptag = None
    nextsep = '|'
    moses = ''
    allow_uppers = True
    for split in splat:
        if split == '':
            continue
        elif split in ['STUB', 'hyph?', 'XB']:
            allow_uppers = True
            continue
        elif split in ['SG', 'NOM', 'POS', 'ACTV', 'PRES']:
            # we actually skip 0 morphs...?
            allow_uppers = True
            continue
        elif split in ['DB', 'MB', 'WB', 'wB']:
            allow_uppers = True
            if skiptag:
                moses += nextsep + skiptag
                skiptag = None
            moses += ' '
            nextsep = '|'
        elif split in ['NOUN', 'VERB', 'ADJ', 'COMP', 'PROPN',
                       'SUPER', 'AUX', 'NUM', 'PRON', 'DET']:
            allow_uppers = True
            skiptag = split
        elif split in ['ADV', 'ADP', 'X', 'PUNCT', 'CCONJ',
                       'SCONJ', 'CCONJ|VERB', 'INTJ', 'SYM']:
            allow_uppers = True
            moses += nextsep + split
        elif split in ['PL', 'INS', 'INE', 'ELA',
                       'ILL', 'ADE', 'ABL', 'ALL', 'ACTV', 'PASV',
                       'IMPV', 'POTN', 'COND', 'SG1', 'SG2', 'SG3', 'PL1',
                       'PL2', 'PL3', 'PAST', 'INFA', 'PAR',
                       'POSSP3', 'POSSG1', 'POSSG2', 'POSPL1', 'POSPL2',
                       'GEN', 'PCPVA', 'INFE', 'PCPMA', 'PCPNUT', 'INFMA',
                       'PE4', 'ABE', 'ESS', 'CONNEG', 'ORD', 'TRA', 'COM',
                       'INFMAISILLA', 'PCPMATON',
                       'HAN', 'KO', 'PA', 'S', 'KAAN', 'KA', 'KIN',
                       'ACC']:
            allow_uppers = True
            if skiptag:
                moses += nextsep + skiptag
                skiptag = None
                nextsep = '.'
            moses += nextsep + split
            nextsep = '.'
        elif split == 'TRUNC':
            allow_uppers = True
            # FIXME
            continue
        elif split.isupper():
            if not allow_uppers and not splat[0].startswith(split):
                print("unhandlend upper string?", split, splat)
                exit(1)
            else:
                moses += split
            allow_uppers = False
        else:
            allow_uppers = False
            moses += split
    if skiptag:
        moses += nextsep + skiptag
    # tweaks and hacks
    if " i " in moses or " j " in moses:
        moses = re.sub(r" ([ij]) ([a-zä]*)\|PL.", r" \1|PL \2|", moses)
    # i ne|COM
    moses = re.sub(r"i ne\|COM", "i|PL ne|COM", moses)
    # |ABEko.KO
    moses = re.sub(r"\|([A-Z][A-Z][A-Z]?)ko\.KO", r"|\1 ko|KO", moses)
    moses = re.sub(r" ([a-zåäö]+) ", r" \1|NOUN ", moses)
    moses = re.sub(r"^([a-zåäö]+) ", r"\1|NOUN ", moses)
    moses = re.sub(r"([snrl])\|PCPNUTut", r"\1ut|PCPNUT", moses)
    moses = re.sub(r"([snrl])\|PCPNUTee", r"\1ee|PCPNUT", moses)
    moses = re.sub(
        r"([snrl])\|AUX\.PCPNUTee", r"\1ee|AUX.PASV.PCPNUT", moses)
    moses = re.sub(r"([snrl])\|PCPNUTe", r"\1e|PCPNUT", moses)
    moses = re.sub(
        r"([snrl])\|AUX\.PCPNUTe", r"\1e|AUX.PASV.PCPNUT", moses)
    # teh|VERB |PCPNUTdy llä|ADE
    moses = re.sub(r"\|PCPNUT([tdrsnl]?[uy])", r"\1|PCPNUT", moses)
    moses = re.sub(
        r"\|AUX\.PASV\.PCPNUT([tdrsnl]?[uy])", r"\1|AUX.PASV.PCPNUT", moses)
    moses = re.sub(r"m\|PCPMA([a-zaä]+)", r"m\1|PCPMA", moses)
    moses = re.sub(r"v\|PCPVA([a-zaä]+)", r"v\1|PCPVA", moses)
    moses = re.sub(r"v\|VERB\.PCPVA([aä])", r"v\1|VERB.PCPVA", moses)
    moses = re.sub(r"v\|AUX.PCPVA([aä])", r"v\1|AUX.PCPVA", moses)
    # |PCPMATONön
    moses = re.sub(r"\|PCPMATON([a-zåäö]+)", r"\1|PCPMATON", moses)
    # puhu|VERB ma|NOUN an|INFMA.ILL
    moses = re.sub(r"(m[aä])\|NOUN ([aä]n)\|INFMA.ILL",
                   r"\1|INFMA \2|ILL", moses)
    # esitet|VERB tä|NOUN mä n|PASV.INFMA.INS
    # esitet|VERB tä|NOUN mä n|PASV.INFMA.INS
    moses = re.sub(r"(t[aä])\|NOUN (m[aä]) n\|PASV\.INFMA\.INS",
                   r"\1|PASV \2|INFMA n|INS", moses)
    # annet|VERB ta|NOUN va t|PASV.PCPVA.PL
    moses = re.sub(r"(t[aä])\|NOUN (v[aä]) t\|PASV\.PCPVA\.PL",
                   r"\1|PASV \2|PCPVA t|PL", moses)
    # todistet|VERB ta|NOUN va sti|PASV.PCPVA
    moses = re.sub(r"(t[aä])\|NOUN (v[aä]) sti\|PASV\.PCPVA",
                   r"\1|PASV \2|PCPVA sti|STI", moses)
    moses = re.sub(
        r"([ei])\|NOUN (n|ssa|ssä)\|INFE.", r"\1|INFE \2|", moses)
    # herättäv|VERB.PCPVAä sti
    moses = re.sub(
        r"v\|VERB.PCPVA([aä]) sti", r"v\1|VERB.PCPVA sti|STI", moses)
    # tarkastel|VERB ta|NOUN e ssa|PASV.INFE.INE
    moses = re.sub(
        r"(t[aä])\|NOUN e (ssa|ssä)\|PASV.INFE.", r"\1|PASV e|INFE \2|", moses)
    # varot|VERB ta|NOUN e n|PASV.INFE.INS
    moses = re.sub(
        r"(t[aä])\|NOUN e n\|PASV.INFE.", r"\1|PASV e|INFE n|", moses)
    # tä|NOUN isi in|PASV.COND.PE4
    moses = re.sub(
        r"t([aä])\|NOUN isi in\|PASV.COND.PE4", r"t\1|PASV isi|COND in|PE4", moses)
    # moniselitteise|ADJ sti
    moses = re.sub(r"ADJ sti$", "ADJ sti|STI", moses)
    # hillitse|VERB vä|PCPVA sti
    moses = re.sub(r"PCPVA sti$", "PCPVA sti|STI", moses)
    # säästä|VERB väi|PCPVAs i|PL lle|ALL
    moses = re.sub(r"\|PCPVAs", r"s|PCPVA", moses)
    # valveutu|VERB nee|PCPNUT sti
    moses = re.sub(r"PCPNUT sti$", "PCPNUT sti|STI", moses)
    # ehdotta|VERB ma|PCPMA sti
    moses = re.sub(r"PCPMA sti$", "PCPMA sti|STI", moses)
    # yhdenmukaista|VERB minen
    moses = re.sub(r"\|VERB minen$", "|VERB minen|NOUN", moses)
    # mi|NOUN s
    moses = re.sub(r"mi\|NOUN s", "mis|NOUN", moses)
    # kunnalli|ADJ s-
    moses = re.sub(r"\|(ADJ|NOUN|PROPN) s-", r"s-|\1", moses)
    # tarvin|AUX ne|NOUN |POTN.CONNEG
    moses = re.sub(r"ne\|NOUN \|POTN.CONNEG", r"ne|POTN.CONNEG", moses)
    # kiittel|VERB y
    # rauhoittel|VERB u-
    moses = re.sub(r"VERB ([uy])$", r"VERB \1|NOUN", moses)
    moses = re.sub(r"VERB ([uy]-)$", r"VERB \1|NOUN", moses)
    # clusterfuckup:
    # soveltamis|NOUN|mis|NOUN|NOUN päivä määrä|NOUN n|GEN
    # siirtämis|NOUNs|NOUN tä|PAR
    moses = re.sub(r"mis\|NOUN\|mis\|NOUN\|NOUN ([a-zåäö]+)",
                   r"mis|NOUN \1|NOUN", moses)
    moses = re.sub(r"mis\|NOUNs\|NOUN", r"mis|NOUN", moses)
    # toimi|NOUN alo|NOUN i|NOUN ttain
    moses = re.sub(r"NOUN ttain$", "NOUN ttain|DERTTAIN", moses)
    # |X|NUM
    moses = re.sub(r"\|X\|NUM", r"X|NUM", moses)
    moses = re.sub(r"\|X-\|NUM", r"X-|NUM", moses)
    # e|CONJ|VERBmme
    moses = re.sub(r"CCONJ\|VERB", r"CCONJVERB ", moses)
    # elin|NOUN tarvike ala|NOUN
    # kehitys|NOUN yhteis|NOUN työ mis|NOUNnisteri|NOUN nä|ESS
    # ulko|NOUN maalai|NOUN s|NOUN viha mielis|ADJ tä|PAR
    # epä|NOUN tasa-arvo asia|NOUN
    moses = re.sub(
        r"([a-zéšäöå-]+)\|NOUN ([a-zšéäöå-]+) ([a-zšéäöå]+)\|NOUN",
        r"\1|NOUN \2|NOUN \3|NOUN", moses)
    moses = re.sub(
        r"([a-zéšäöå-]+)\|NOUN ([a-zšéäöå-]+) ([a-zšéäöå]+)\|ADJ",
        r"\1|NOUN \2|NOUN \3|ADJ", moses)
    # šakki lauda|NOUN
    # pöytä|NOUN rosé viine|NOUN i|PL stä|ELA
    # linja-auto liikentee|NOUN n|GEN
    moses = re.sub(r"^([A-Za-z*ÉéÄŠÖÅšäöå-]+) ([a-zäöå-]+)\|NOUN",
                   r"\1|NOUN \2|NOUN", moses)
    moses = re.sub(r"^([A-Za-z*ÉéÄŠÖÅšäöå-]+) ([a-zäöå-]+)\|PROPN",
                   r"\1|PROPN \2|PROPN", moses)
    moses = re.sub(r"^\|([A-Za-z*ÉéÄŠÖÅšäöå-]+).PROPN",
                   r"\1|PROPN", moses)
    #  R|NOUN ja|ADV |S.NOUN
    # |S-.NOUN kirjaime|NOUN lla|ADE
    moses = re.sub(r"\|S.NOUN", r"S|NOUN", moses)
    moses = re.sub(r"\|S-.NOUN", r"S-|NOUN", moses)
    # |PA.NOUN
    moses = re.sub(r"\|PA.NOUN", r"PA|NOUN", moses)
    # (|PUNCT |PL.NOUN )|PUNCT
    moses = re.sub(r"^\|PL.NOUN", r"PL|NOUN", moses)
    # |NOUN |NOUN Aerospacen|UNK
    moses = re.sub(r"^\|NOUN", r"", moses)
    moses = re.sub(r" \|NOUN", r"", moses)
    moses = re.sub(r"\|NOUN\|NOUN", r"|NOUN", moses)
    # |NOUNsa|INE
    moses = re.sub(r"\|NOUN([st][aä])\|", r"|NOUN \1|", moses)
    # Slovenia... n|GEN- haara
    moses = re.sub(r"n\|([A-Z.]+)-+", r"n|\1", moses)
    # ADP
    moses = re.sub(r"\|ADP([in])", r"\1|ADP", moses)
    moses = re.sub(r"\|SG3pi", r"pi|SG3", moses)
    #
    moses = re.sub(r"([uy])\|PCPNUTt", r"\1t|PCPNUT", moses)
    # |NOUNäiliö|NOUN
    moses = re.sub(r"\|NOUN([a-zäåö]+)\|NOUN", r"\1|NOUN", moses)
    # || special case :-/
    moses = re.sub(r"\|\|SYM", "@pipe;|SYM", moses)
    # finally
##    segleft = ''
##    segright = ''
##    if seglen == 0:
##        segleft = ''
##        segright = ''
##    elif seglen == 1:
##        segleft = options.segment_marker
##        segright = options.segment_marker
##    elif seglen % 2 == 0:
##        segleft = options.segment_marker[:int(seglen / 2)]
##        segright = options.segment_marker[int(seglen / 2):]
##    else:
##        segleft = options.segment_marker[:int((seglen - 1) / 2)]
##        segright = options.segment_marker[int((seglen - 1) / 2):]
##    moses = re.sub(r"\|", segleft + "|", moses)
##    moses = re.sub(r" ", " " + segright, moses)
##    last = moses.rfind(segleft + "|")
##    moses = moses[:last + len(segleft) - 1] + moses[last + len(segleft):]
    return moses.split()

def format_misc_ud(token):
    guess = get_last_feat("GUESS", token)
    miscs = []
    if guess and not guess == "":
        miscs += ["Guesser=" + guess]
    if 'analsurf' in token and token['analsurf'] != token['surf']:
        miscs += ['AnalysisForm=' + token['analsurf']]
    if 'recase' in token and token['recase'] != 'ORIGINAL':
        miscs += ['CaseChanged=' + token['recase']]
    if 'SpaceAfter' in token:
        miscs += ['SpaceAfter=' + token['SpaceAfter']]
    if 'SpaceBefore' in token:
        miscs += ['SpaceBefore=' + token['SpaceBefore']]
    if len(miscs) > 0:
        return '|'.join(miscs)
    else:
        return '_'



def format_feats_ud(token, hacks=None):
    rvs = get_ud_feats(token, hacks)
    rv = ''
    for k in sorted(rvs, key=str.lower):
        rv += k + '=' + rvs[k] + '|'
    if len(rvs) != 0:
        return rv.rstrip('|')
    else:
        return '_'


def format_xpos_ftb(token):
    upos = get_upos(token)
    return upos


def format_xpos_tdt(token):
    upos = get_upos(token)
    if upos in ['NOUN', 'PROPN']:
        return 'N'
    elif upos == 'ADJ':
        return 'A'
    elif upos in ['VERB', 'AUX']:
        return 'V'
    elif upos in ['CCONJ', 'SCONJ']:
        return 'C'
    elif upos == 'ADP':
        return 'Adp'
    elif upos == 'ADV':
        return 'Adv'
    elif upos == 'PRON':
        return 'Pron'
    elif upos == 'PUNCT':
        return 'Punct'
    elif upos == 'SYM':
        return 'Symb'
    elif upos == 'INTJ':
        return 'Interj'
    elif upos == 'NUM':
        return 'Num'
    else:
        return 'X'

