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
        if 'BOUNDARY=' in feat.group(0) or 'WORD_ID=' in feat.group(0):
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
        if key in ["ALLO", "SEM", "STYLE"]:
            # semantics, non-core morph in brackets
            vislcgs += ["<" + key + "_" + value + ">"]
        elif key in ["CASE", "NUM", "PERSON", "UPOS"]:
            # core morph show only value as is (omor style though)
            vislcgs += [value]
        else:
            print("Unhandled", key, "=", value, "in", token,
                    "for vislcg")
            exit(1)
    if "recase" in token and token['recase'] != "ORIGINAL":
        vislcgs += ["<*" + token['recase'] + ">"]
    if "weight" in token:
        vislcgs += ["<W=" + int(token['weight'] * 1000) + ">"]
    if "lemmaweight" in token:
        vislcgs += ["<L=" + int(token['weight'] * 1000) + ">"]
    if "guess" in token:
        vislcgs += ["<Heur?>", "<Guesser_" + token['guess'] + ">"]
    return vislcgs


def get_segments(token, options):
    segments = [token['segments']]
    # this code is ugly
    segments = segments.replace('{hyph?}', '')
    resegs = []
    for segment in segments:
        if options.split_morphs:
            resegs += segments.split('{MB}')
        else:
            resegs += [segment]
    segments = resegs
    resegs = []
    for segment in segments:
        if options.split_words:
            resegs += segments.split('{WB}')
        else:
            resegs += [segments]
    segments = resegs
    resegs = []
    for segment in segments:
        if options.split_new_words:
            resegs += segments.split('{wB}')
        else:
            resegs += [segments]
    segments = resegs
    resegs = []
    for segment in segments:
        if options.split_derivs:
            resegs += segments.split('{DB}')
        else:
            resegs += [segments]
    segments = resegs
    resegs = []
    for segment in segments:
        if options.split_nonwords:
            resegs += segments.split('{XB}')
        else:
            resegs += [segments]
    return resegs

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

