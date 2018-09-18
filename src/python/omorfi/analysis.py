#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A container for analysis.

Contains single hypothesis of single aspect of things.
"""

import re
from sys import stderr

from .omor_formatter import OmorFormatter


class Analysis:
    """Contains a single analysis of a token.

    Analysis is a hypothesis of what token's some features may be:
    morphological analysis contains morphosyntactic readings and segmentation
    contains segment markers.
    """

    def __init__(self):
        """Create an empty analysis

        @param raw  analysis in string form
        @param weight  penalty weight for analysis
        """
        #: underlying raw omor analysis
        self.raw = None
        #: universal part of speech
        self.upos = None
        #: last effective universal feats (private feats allowed, but see misc)
        self.ufeats = dict()
        #: misc features
        self.misc = dict()
        #: type of analysis: omor, segmentation, lemmatisation etc.
        self.rawtype = None
        #: FSA or similar weight
        self.weight = float("inf")
        #: surface actually used for analysis (if different from parent token's
        #: surf)
        self.analsurf = None
        #: Recasers, spelling correctors and plain guessers
        self.manglers = list()
        #: lemmas
        self.lemmas = list()

    def __str__(self):
        s = '"omorfi.Analysis": {'
        if self.rawtype:
            s += '"rawtype": "' + self.rawtype + '", '
        if self.raw:
            s += '"raw": "' + self.raw + '", '
        s += '"weight": "' + str(self.weight) + '"'
        s += '}'
        return s

    def get_upos(self):
        return self.upos

    def get_lemmas(self):
        return self.lemmas

    def get_ufeats(self):
        return self.ufeats

    @staticmethod
    def fromstr(s: str):
        '''Constructs analysis from string'''
        a = Analysis()
        if '"omorfi.Analysis":' not in s:
            return None
        start = s.find('"omorfi.Analysis":') + len('"omorfi.Analysis":')
        start = s.find("{", start)
        end = s.rfind("}")
        fields = s[start:end].split(", ")
        for field in fields:
            k, v = field.split(":")
            if k.strip('"') == "rawtype":
                a.rawtype = v.strip('"')
            elif k.strip('"') == "raw":
                a.raw = v.strip('"')
            elif k.strip('"') == "weight":
                a.weight = float(v.strip('"'))
            else:
                print("Cannot parse", s, "as analysis", file=stderr)
                exit(1)
        return a

    @staticmethod
    def fromomor(s: str, weight=float("inf"), hacks=None):
        '''Constructs analysis form Omor style string.

        Typically used to create an analysis from libhfst string and weight
        after using omorfi HFST analyser on a surface string.

        Args:
            s       An omor-style analysis string, e.g.
                "[WORD_ID=äh][UPOS=INTJ]"
            weight  A penalty-weight of the analysis
            hacks   Used for mangling some values based on some standards and
                treebanks

        Returns:
            a token with omor analysis parsed into structured information
        '''
        a = Analysis()
        a.raw = s
        a.rawtype = "omor"
        a.weight = weight
        a.upos = OmorFormatter.get_upos(s)
        a.lemmas = OmorFormatter.get_lemmas(s)
        feats = OmorFormatter.get_last_feats(s)
        if not feats:
            a.feats = None
            return a
        a.feats = dict()
        for f in feats:
            key = f.split("=")[0].lstrip("[")
            value = f.split("=")[1].rstrip("]")
            if key == 'CASE':
                if value == 'LAT' and hacks != 'ftb':
                    # XXX: hack to retain compability
                    a.feats['Number'] = 'Sing'
                else:
                    a.feats['Case'] = value[0] + value[1:].lower()
            elif key == 'NUM':
                if value == 'SG':
                    a.feats['Number'] = 'Sing'
                elif value == 'PL':
                    a.feats['Number'] = 'Plur'
            elif key == 'TENSE':
                if 'PRESENT' in value:
                    a.feats['Tense'] = 'Pres'
                elif 'PAST' in value:
                    a.feats['Tense'] = 'Past'
            elif key == 'MOOD':
                a.feats['VerbForm'] = 'Fin'
                if value == 'INDV':
                    a.feats['Mood'] = 'Ind'
                elif value == 'COND':
                    a.feats['Mood'] = 'Cnd'
                elif value == 'IMPV':
                    a.feats['Mood'] = 'Imp'
                else:
                    a.feats['Mood'] = value[0] + value[1:].lower()
            elif key == 'VOICE':
                if value == 'PSS':
                    a.feats['Voice'] = 'Pass'
                elif value == 'ACT':
                    a.feats['Voice'] = 'Act'
            elif key == 'PERS':
                if 'SG' in value:
                    a.feats['Number'] = 'Sing'
                elif 'PL' in value:
                    a.feats['Number'] = 'Plur'
                if '1' in value:
                    a.feats['Person'] = '1'
                elif '2' in value:
                    a.feats['Person'] = '2'
                elif '3' in value:
                    a.feats['Person'] = '3'
            elif key == 'POSS':
                if 'SG' in value:
                    a.feats['Number[psor]'] = 'Sing'
                elif 'PL' in value:
                    a.feats['Number[psor]'] = 'Plur'
                if '1' in value:
                    a.feats['Person[psor]'] = '1'
                elif '2' in value:
                    a.feats['Person[psor]'] = '2'
                elif '3' in value:
                    a.feats['Person[psor]'] = '3'
            elif key == 'NEG':
                if value == 'CON':
                    a.feats['Connegative'] = 'Yes'
                    # XXX
                    a.feats.pop('Voice')
                elif value == 'NEG':
                    a.feats['Polarity'] = 'Neg'
                    a.feats['VerbForm'] = 'Fin'
            elif key == 'PCP':
                a.feats['VerbForm'] = 'Part'
                if value == 'VA':
                    a.feats['PartForm'] = 'Pres'
                elif value == 'NUT':
                    a.feats['PartForm'] = 'Past'
                elif value == 'MA':
                    a.feats['PartForm'] = 'Agent'
                elif value == 'MATON':
                    a.feats['PartForm'] = 'Neg'
            elif key == 'INF':
                a.feats['VerbForm'] = 'Inf'
                if value == 'A':
                    a.feats['InfForm'] = '1'
                elif value == 'E':
                    a.feats['InfForm'] = '2'
                    # XXX
                    a.feats['Number'] = 'Sing'
                elif value == 'MA':
                    a.feats['InfForm'] = '3'
                    # XXX
                    a.feats['Number'] = 'Sing'
                elif value == 'MINEN':
                    a.feats['InfForm'] = '4'
                elif value == 'MAISILLA':
                    a.feats['InfForm'] = '5'
            elif key == 'CMP':
                if value == 'SUP':
                    a.feats['Degree'] = 'Sup'
                elif value == 'CMP':
                    a.feats['Degree'] = 'Cmp'
                elif value == 'POS':
                    a.feats['Degree'] = 'Pos'
            elif key == 'SUBCAT':
                if value == 'NEG':
                    a.feats['Polarity'] = 'Neg'
                    a.feats['VerbForm'] = 'Fin'
                elif value == 'QUANTIFIER':
                    a.feats['PronType'] = 'Ind'
                elif value == 'REFLEXIVE':
                    a.feats['Reflexive'] = 'Yes'
                elif value in ['COMMA', 'DASH', 'QUOTATION', 'BRACKET']:
                    # not annotated in UD feats:
                    # * punctuation classes
                    continue
                elif value in ['DECIMAL', 'ROMAN', 'DIGIT']:
                    # not annotated in UD feats:
                    # * decimal, roman NumType
                    continue
                elif value in ['PREFIX', 'SUFFIX']:
                    # not annotated in UD feats:
                    # * decimal, roman NumType
                    continue
                else:
                    print(key, value, 'SUBCAT', 'UD')
                    exit(1)
            elif key == 'ABBR':
                # XXX?
                a.feats['Abbr'] = 'Yes'
            elif key == 'NUMTYPE':
                a.feats['NumType'] = value[0] + value[1:].lower()
            elif key == 'PRONTYPE':
                a.feats['PronType'] = value[0] + value[1:].lower()
            elif key == 'ADPTYPE':
                a.feats['AdpType'] = value[0] + value[1:].lower()
            elif key == 'CLIT':
                a.feats['Clitic'] = value[0] + value[1:].lower()
            elif key == 'FOREIGN':
                a.feats['Foreign'] = value[0] + value[1:].lower()
            elif key == 'STYLE':
                if value in ['DIALECTAL', 'COLLOQUIAL']:
                    a.feats['Style'] = 'Coll'
                elif value == 'NONSTANDARD':
                    # XXX: Non-standard spelling is kind of a typo?
                    # e.g. seitsämän -> seitsemän
                    a.feats['Typo'] = 'Yes'
                elif value == 'ARCHAIC':
                    a.feats['Style'] = 'Arch'
                elif value == 'RARE':
                    continue
                else:
                    print(key, value, 'STYLE', 'UD')
                    exit(1)
            elif key in ['DRV', 'LEX']:
                if value in ['INEN', 'JA', 'LAINEN', 'LLINEN', 'MINEN', 'STI',
                             'TAR', 'TON', 'TTAA', 'TTAIN', 'U', 'VS']:
                    # values found in UD finnish Derivs
                    a.feats['Derivation'] = value[0] + value[1:].lower()
                elif value in ['S', 'MAISILLA', 'VA', 'MATON', 'UUS', 'ADE',
                               'INE', 'ELA', 'ILL', 'NEN', 'MPI', 'IN', 'IN²',
                               'HKO', 'ISA', 'MAINEN', 'NUT', 'TU', 'VA',
                               'TAVA', 'MA', 'LOC', 'LA']:
                    # valuse not found in UD finnish Derivs
                    continue
                else:
                    print(key, value, 'UD')
                    exit(1)
            elif key == 'BLACKLIST':
                continue
            elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE', 'NEWPARA',
                         'GUESS', 'PROPER', 'POSITION', 'SEM', 'CONJ',
                         'BOUNDARY']:
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
                # * clause / sentence boundary tag ignored
                continue
            else:
                print(key, value, 'UD')
                exit(1)
        return a

    @staticmethod
    def fromvislcg(s):
        '''Constructs analysis from VISL-CG string.

        The string should match what the method printable_vislcg creates plus
        optional VISL CG 3 trace and such markings.
        '''
        fields = s.strip().split()
        lemma = fields[0]
        if not fields[0].startswith('"'):
            print("Cannot find lemma in VISL CG 3:", s, file=stderr)
            exit(1)
        if not fields[0].endswith('"'):
            lemmaend = False
            for posm1, field in enumerate(fields[1:]):
                lemma += field
                if field.endswith('"'):
                    lemmaend = posm1 + 1
                    break
            if not lemmaend:
                print("Cannot find lemma in VISL CG 3:", s, file=stderr)
                exit(1)
            fields = [lemma] + fields[lemmaend + 1:]
        lemma = fields[0].strip('"')
        vislcgs = []
        omorstr = '[WORD_ID=' + lemma + ']'
        weight = 0.0
        if len(fields) < 2:
            return omorstr
        upos = fields[1]
        if upos in ["NOUN", "ADJ", "VERB", "AUX", "ADP", "X", "CCONJ", "PRON",
                    "SCONJ", "DET", "PROPN", "PUNCT", "SYM", "ADV", "NUM",
                    "INTJ"]:
            omorstr += '[UPOS=' + upos + ']'
        else:
            print("Cannot find UPOS in VISL CG 3:", fields, file=stderr)
            exit(1)
        if len(fields) < 3:
            return omorstr
        vislcgs = fields[2:]
        for vislcg in vislcgs:
            if vislcg in ["PRESENT", "PAST"]:
                omorstr += '[TENSE=' + vislcg + ']'
            elif vislcg in ["SG", "PL"]:
                omorstr += '[NUM=' + vislcg + ']'
            elif vislcg in ["ABE", "ABL", "ACC", "ADE", "ALL", "COM", "ELA",
                            "ESS", "GEN", "ILL", "INE", "INS", "LAT", "NOM",
                            "PAR", "TRA"]:
                omorstr += "[CASE=" + vislcg + "]"
            elif vislcg in ["INDV", "IMPV", "COND", "POTN", "IND"]:
                omorstr += "[MOOD=" + vislcg + "]"
            elif vislcg in ["SG1", "SG2", "SG3", "PL1", "PL2", "PL3", "PE4"]:
                omorstr += "[PERS=" + vislcg + "]"
            elif vislcg in ["CMP", "POS", "SUP"]:
                omorstr += "[CMP=" + vislcg + "]"
            elif vislcg == "CONNEG":
                omorstr += "[NEG=CON]"
            elif vislcg in ["PRS", "DEM", "REL", "INT", "REC"]:
                omorstr += "[PRONTYPE=" + vislcg + "]"
            elif vislcg in ["HAN", "KO", "PA", "S", "KA", "KIN", "KAAN"]:
                omorstr += "[CLIT=" + vislcg + "]"
            elif vislcg in ["PREP", "POST"]:
                omorstr += "[ADPTYPE=" + vislcg + "]"
            elif vislcg in ["CARD", "ORD", "FRAC", "MULT"]:
                omorstr += "[NUMTYPE=" + vislcg + "]"
            elif vislcg in ["ACT", "PSS"]:
                omorstr += "[VOICE=" + vislcg + "]"
            elif vislcg in ["SCONJ", "COMPARATIVE", "ADP", "SGNOM"]:
                # XXX: hacks that shouldn't be
                pass
            elif vislcg.startswith("POSS"):
                omorstr += "[POSS=" + vislcg[4:] + "]"
            elif vislcg.startswith("CLIT"):
                omorstr += "[CLIT=" + vislcg[4:] + "]"
            elif vislcg.startswith("PCP"):
                omorstr += "[PCP=" + vislcg[3:] + "]"
            elif vislcg.startswith("INF"):
                omorstr += "[INF=" + vislcg[3:] + "]"
            elif vislcg.startswith("<W=") and vislcg.endswith(">"):
                weight = float(vislcg[3:-1])
            elif vislcg.startswith("<") and vislcg.endswith(">"):
                # secondaries are safe to skip
                pass
            else:
                print("Cannot parse", vislcg, "as vislcg", file=stderr)
                exit(1)
        anal = Analysis(omorstr, weight, "omor")
        return anal

    def get_ftb_feats(self):
        '''Get FTB analyses from token data.'''
        feats = self.ufeats
        rvs = list()
        rvs += [self.get_xpos_ftb()]
        if not feats:
            return rvs
        for f in feats:
            key = f.split("=")[0].lstrip("[")
            value = f.split("=")[1].rstrip("]")
            if key == 'UPOS':
                if value == 'PROPN':
                    rvs += ['Prop']
                elif value == 'ADV' and self.get_lemmas()[-1].endswith("sti"):
                    # This is FTB oddity
                    rvs += ['Pos', 'Man']
                else:
                    continue
            elif key == 'NUM':
                if value == 'SG':
                    rvs += ['Sg']
                elif value == 'PL':
                    rvs += ['Pl']
            elif key == 'TENSE':
                if 'PRESENT' in value:
                    rvs += ['Prs']
                elif 'PAST' in value:
                    rvs += ['Past']
            elif key == 'MOOD':
                if value == 'INDV':
                    continue
                elif value == 'COND':
                    rvs += ['Cond']
                elif value == 'IMPV':
                    rvs += ['Imp']
                else:
                    rvs += [value[0] + value[1:].lower()]
            elif key == 'VOICE':
                if value == 'PSS':
                    rvs += ['Pass']
                elif value == 'ACT':
                    rvs += ['Act']
            elif key == 'PERS':
                if value == 'SG0':
                    rvs += ['Sg3']
                elif value == 'SG1':
                    rvs += ['Sg1']
                elif value == 'SG2':
                    rvs += ['Sg2']
                elif value == 'SG3':
                    rvs += ['Sg3']
                elif value == 'PL1':
                    rvs += ['Pl1']
                elif value == 'PL2':
                    rvs += ['Pl2']
                elif value == 'PL3':
                    rvs += ['Pl3']
                elif value == 'PE4':
                    rvs += ['Pe4']
                else:
                    print(key, "for ftb", file=stderr)
                    exit(1)
            elif key == 'POSS':
                if value == 'SG1':
                    rvs += ['PxSg1']
                elif value == 'SG2':
                    rvs += ['PxSg2']
                elif value == '3':
                    rvs += ['PxSp3']
                elif value == 'PL1':
                    rvs += ['PxPl1']
                elif value == 'PL2':
                    rvs += ['PxPl2']
                elif value == 'PL3':
                    rvs += ['PxPl3']
            elif key == 'NEG':
                if value == 'CON':
                    rvs += ['ConNeg']
                elif value == 'NEG':
                    rvs += ['Neg']
            elif key == 'INF':
                if value == 'A':
                    rvs += ['Inf1']
                elif value == 'E':
                    rvs += ['Inf2']
                elif value == 'MA':
                    rvs += ['Inf3']
                elif value == 'MINEN':
                    rvs += ['Inf4']
                elif value == 'MAISILLA':
                    rvs += ['Inf5']
            elif key == 'CASE':
                rvs += [value[0].upper() + value[1:].lower()]
            elif key == 'CMP':
                if value == 'SUP':
                    rvs += ['Sup']
                elif value == 'CMP':
                    rvs += ['Cmp']
                elif value == 'POS':
                    rvs += ['Pos']
            elif key == 'SUBCAT':
                if value == 'NEG':
                    rvs += ['Neg']
                elif value == 'QUOTATION':
                    rvs += ['Quote']
                elif value == 'QUANTIFIER':
                    rvs += ['Qnt']
                elif value == 'REFLEXIVE':
                    rvs += ['Refl']
                elif value == 'DIGIT':
                    rvs += ['Digit']
                elif value == 'DASH':
                    if self.get_lemmas()[-1] == '—':
                        rvs += ['EmDash']
                    elif self.get_lemmas()[-1] == '–':
                        rvs += ['EnDash']
                    else:
                        rvs += ['Dash']
                elif value in ['COMMA', 'BRACKET',
                               'ARROW', 'DECIMAL', 'PREFIX', 'SUFFIX']:
                    # not annotated in UD feats:
                    # * punctuation classes
                    continue
                elif value == 'ROMAN':
                    # not annotated in UD feats:
                    # * decimal, roman NumType
                    continue
                else:
                    print(key, value, 'SUBCAT', 'FTB3')
                    exit(1)
            elif key == 'NUMTYPE':
                if 'Digit' not in rvs:
                    rvs += [value[0] + value[1:].lower()]
            elif key == 'PRONTYPE':
                if value == 'PRS':
                    rvs += ['Pers']
                else:
                    rvs += [value[0] + value[1:].lower()]
            elif key == 'ADPTYPE':
                if value == 'POST':
                    rvs += ['Po']
                elif value == 'PREP':
                    rvs += ['Pr']
                else:
                    print(key, value, 'ADPTYPE', 'FTB3')
                    exit(1)
            elif key == 'CLIT':
                rvs += [value[0] + value[1:].lower()]
            elif key == 'ABBR':
                rvs += ['Abbr']
            elif key == 'DRV':
                if value in ['NUT', 'VA']:
                    rvs += ['Act']
                elif value in ['TU', 'TAVA']:
                    rvs += ['Pass']
                else:
                    continue
            elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE', 'NEWPARA',
                         'GUESS', 'PROPER', 'SEM', 'CONJ', 'BOUNDARY',
                         'PCP', 'DRV', 'LEX', 'BLACKLIST', 'STYLE', 'ABBR',
                         'POSITION', "FOREIGN"]:
                continue
            else:
                print(key, value, 'FTB3')
                exit(1)
        # post hacks
        if 'Neg' in rvs and 'Act' in rvs:
            revs = []
            for r in rvs:
                if r != 'Act':
                    revs += [r]
            rvs = revs
        elif 'Abbr' in rvs:
            revs = []
            for r in rvs:
                if r not in ['N', 'Prop']:
                    revs += [r]
            rvs = revs
        elif 'Inf1' in rvs:
            revs = []
            for r in rvs:
                if r not in ['Act', 'Pl', 'Sg']:
                    revs += [r]
            rvs = revs
        elif 'Pers' in rvs:
            revs = []
            for r in rvs:
                if r not in ['Pl1', 'Sg1', 'Pl2', 'Sg2', 'Pl3', 'Sg3']:
                    revs += [r]
            rvs = revs
        return rvs

    def get_vislcg_feats(self):
        '''Get VISL-CG 3 features from analysed token.'''
        feats = self.ufeats
        vislcgs = list()
        for feat in feats:
            key = feat.split("=")[0].strip("[")
            value = feat.split("=")[1].strip("]")
            if key == "SUBCAT" and value == "NEG":
                vislcgs += ["NEG"]
            elif key in ["CLIT", "INF", "PCP", "POSS"]:
                # ...except when only value is too short
                vislcgs += [key + value]
            elif key == "NEG" and value == "CON":
                vislcgs += ["CONNEG"]
            elif key in ["WEIGHT", "GUESS", "CASECHANGE"]:
                # Weights, recasing ... are handled via token features
                pass
            elif key == "BOUNDARY":
                if value == "CLAUSE":
                    vislcgs += ["<CLB>"]
                elif value == "SENTENCE":
                    vislcgs += ["<SENT>"]
                else:
                    print(key, value, 'BOUNDARY', 'VISLCG')
                    exit(1)
            elif key in ["ALLO", "SEM", "STYLE", "LEX", "DRV", "SUBCAT",
                         "POSITION", "ABBR", "FOREIGN", "PROPER"]:
                # semantics, non-core morph in brackets
                vislcgs += ["<" + key + "_" + value + ">"]
            elif key in ["CASE", "NUM", "PERS", "UPOS", "VOICE", "MOOD",
                         "TENSE", "NUMTYPE", "ADPTYPE", "CLIT", "PRONTYPE",
                         "CMP", "CONJ"]:
                # core morph show only value as is (omor style though)
                if value == 'LAT':
                    pass
                else:
                    vislcgs += [value]
            elif key == "BLACKLIST":
                vislcgs += ["<**" + value + ">"]
            else:
                print(key, value, 'VISLCG')
                exit(1)
        if self.weight:
            if self.weight != float('inf'):
                vislcgs += ["<W=" + str(int(self.weight) * 1000) + ">"]
        if self.manglers:
            for mangler in self.manglers:
                if "CASED" in mangler.upper():
                    vislcgs += ["<*" + mangler + ">"]
                elif "GUESS" in mangler.upper():
                    vislcgs += ["<Heur?>", "<?" + mangler + ">"]
        # number of compound parts in compound is a good CG numeric feature!!
        lemmas = self.get_lemmas()
        vislcgs += ['<CMP=' + str(len(lemmas)) + '>']
        return vislcgs

    def get_segments(self, split_morphs=True, split_words=True,
                     split_new_words=True, split_derivs=False,
                     split_nonwords=False):
        '''Get specified segments from segmented analysis.'''
        if self.rawtype != 'segments':
            return None
        segments = self.raw
        # this code is ugly
        segments = [segments.replace('{hyph?}', '').replace("{STUB}", "")]
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

    def get_moses_factor_segments(self):
        '''Create moses factors from analyses.'''
        if self.rawtype != 'labelsegments':
            return None
        analysis = self.raw
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
            r"\|AUX\.PASV\.PCPNUT([tdrsnl]?[uy])", r"\1|AUX.PASV.PCPNUT",
            moses)
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
            r"(t[aä])\|NOUN e (ssa|ssä)\|PASV.INFE.", r"\1|PASV e|INFE \2|",
            moses)
        # varot|VERB ta|NOUN e n|PASV.INFE.INS
        moses = re.sub(
            r"(t[aä])\|NOUN e n\|PASV.INFE.", r"\1|PASV e|INFE n|", moses)
        # tä|NOUN isi in|PASV.COND.PE4
        moses = re.sub(
            r"t([aä])\|NOUN isi in\|PASV.COND.PE4",
            r"t\1|PASV isi|COND in|PE4", moses)
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

    def get_ud_misc(self):
        '''Get random collection of analyses for token.

        Primarily used for UD MISC field but can be used for any extra data.
        '''
        miscs = []
        if self.manglers:
            miscs += ["Guesser=" + '|'.join(self.manglers)]
        if self.analsurf:
            miscs += ['AnalysisForm=' + self.analsurf]
        return miscs

    def printable_ud_misc(self):
        '''Formats UD misc like in UD data.'''
        miscs = self.get_ud_misc()
        if not miscs:
            return '_'
        return '|'.join(miscs)

    def printable_ud_feats(self, hacks=None):
        '''Formats UD feats from token data exactly as in fi-tdt data.

        When the correct analysis is in question the result should be equal
        to the UFEAT field of the connl-u data downloadable from UD web site,
        in string format.
        '''
        rvs = self.ufeats
        if not rvs:
            return '_'
        rv = ''
        for k in sorted(rvs, key=str.lower):
            rv += k + '=' + rvs[k] + '|'
        return rv.rstrip('|')

    def printable_ftb_feats(self):
        '''Formats FTB feats from token data like in FTB-2014 data.'''
        rvs = self.get_ftb_feats()
        return ' '.join(rvs)

    def get_xpos_ftb(self):
        '''Gets FTB-compatible part-of-speech from analysis.'''
        upos = self.get_upos()
        if upos in ['NOUN', 'PROPN']:
            return 'N'
        elif upos == 'ADJ':
            return 'A'
        elif upos in ['VERB', 'AUX']:
            pcp = self.get_last_feat('DRV')
            if pcp:
                if pcp in ['NUT', 'TU']:
                    return 'PrfPrc'
                elif pcp == 'MA':
                    return 'AgPrc'
                elif pcp in ['VA', 'TAVA']:
                    return 'PrsPrc'
                elif pcp == 'NEG':
                    return 'NegPrc'
                else:
                    return 'V'
            return 'V'
        elif upos == 'CCONJ':
            return 'CC'
        elif upos == 'SCONJ':
            return 'CS'
        elif upos == 'ADP':
            return 'Adp'
        elif upos == 'ADV':
            return 'Adv'
        elif upos == 'PRON':
            return 'Pron'
        elif upos in ['PUNCT', 'SYM']:
            return 'Punct'
        elif upos == 'INTJ':
            return 'Interj'
        elif upos == 'NUM':
            return 'Num'
        elif upos == 'DET':
            return 'Pron'
        elif upos == 'X':
            return 'Forgn'
        else:
            return 'Unkwn'
        return upos

    def get_xpos_tdt(self):
        '''Get TDT-compatible part-of-speech from analysed token.'''
        upos = self.get_upos()
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

    def printable_vislcg(self):
        '''Create VISL-CG 3 output from the token.'''
        mrds = self.get_vislcg_feats()
        lemmas = self.get_lemmas()
        return '\t"' + '#'.join(lemmas) + '" ' + ' '.join(mrds)

    def is_oov(self):
        '''Figures out if this analysis was guessed for an OOV.'''
        if self.manglers:
            for mangler in self.manglers:
                if 'GUESS' in mangler.upper():
                    return True
        return False
