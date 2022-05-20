#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A container for analysis.

Contains single hypothesis of single aspect of things.
"""

import re
from sys import stderr

from .formats.omor_formatter import OmorFormatter


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
        #: UD dep, target and name
        self.udepname = None
        self.udeppos = None
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
        if self.raw:
            s += '"rawtype": "' + self.rawtype + '", '
            s += '"raw": "' + self.raw + '", '
        if self.upos:
            s += '"upos": "' + self.upos + '", '
        if self.ufeats:
            s += '"ufeats": "' + str(self.ufeats) + '", '
        if self.misc:
            s += '"misc": "' + str(self.misc) + '", '
        s += '"weight": "' + str(self.weight) + '"'
        if self.udepname:
            s += '"udep": "' + self.udepname + '"'
            s += '"udephead": "' + str(self.udeppos) + '"'
        s += '}'
        return s

    def get_upos(self):
        '''Finds UPOS from analyses.

        Returns:
            upos in a string
        '''
        return self.upos

    def get_lemmas(self):
        '''Finds lemmas from analyses.

        Returns:
            list of strings.
        '''
        return self.lemmas

    def get_ufeats(self):
        '''Finds UD Feats from analyses.

        Returns:
            dict of key value pairs of UD Feat column.
        '''
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
        a.weight += (len(a.lemmas) - 1) * 10
        a.weight += s.count('DRV') * 5
        feats = OmorFormatter.get_last_feats(s)
        if not feats:
            a.ufeats = None
            return a
        a.ufeats = dict()
        for f in feats:
            key = f.split("=")[0].lstrip("[")
            value = f.split("=")[1].rstrip("]")
            if key == 'CASE':
                if value == 'LAT' and hacks != 'ftb':
                    # XXX: hack to retain compability
                    a.ufeats['Number'] = 'Sing'
                else:
                    a.ufeats['Case'] = value[0] + value[1:].lower()
            elif key == 'NUM':
                if value == 'SG':
                    a.ufeats['Number'] = 'Sing'
                elif value == 'PL':
                    a.ufeats['Number'] = 'Plur'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'TENSE':
                if 'PRESENT' in value:
                    a.ufeats['Tense'] = 'Pres'
                elif 'PAST' in value:
                    a.ufeats['Tense'] = 'Past'
            elif key == 'MOOD':
                a.ufeats['VerbForm'] = 'Fin'
                if value == 'INDV':
                    a.ufeats['Mood'] = 'Ind'
                elif value == 'COND':
                    a.ufeats['Mood'] = 'Cnd'
                elif value == 'IMPV':
                    a.ufeats['Mood'] = 'Imp'
                elif value == 'POTN':
                    a.ufeats['Mood'] = 'Pot'
                elif value == 'OPT':
                    a.misc['Mood'] = 'Opt'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'VOICE':
                if value == 'PSS':
                    a.ufeats['Voice'] = 'Pass'
                elif value == 'ACT':
                    a.ufeats['Voice'] = 'Act'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'PERS':
                if 'SG' in value:
                    a.ufeats['Number'] = 'Sing'
                elif 'PL' in value:
                    a.ufeats['Number'] = 'Plur'
                elif 'PE' in value:
                    pass
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
                if '1' in value:
                    a.ufeats['Person'] = '1'
                elif '2' in value:
                    a.ufeats['Person'] = '2'
                elif '3' in value:
                    a.ufeats['Person'] = '3'
                elif '0' in value:
                    a.ufeats['Person'] = '0'
                elif '4' in value:
                    a.misc['Person'] = '4'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'POSS':
                if 'SG' in value:
                    a.ufeats['Number[psor]'] = 'Sing'
                elif 'PL' in value:
                    a.ufeats['Number[psor]'] = 'Plur'
                elif value == '3':
                    pass
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
                if '1' in value:
                    a.ufeats['Person[psor]'] = '1'
                elif '2' in value:
                    a.ufeats['Person[psor]'] = '2'
                elif '3' in value:
                    a.ufeats['Person[psor]'] = '3'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'NEG':
                if value == 'CON':
                    a.ufeats['Connegative'] = 'Yes'
                    # XXX
                    a.ufeats.pop('Voice')
                elif value == 'NEG':
                    a.ufeats['Polarity'] = 'Neg'
                    a.ufeats['VerbForm'] = 'Fin'
            elif key == 'PCP':
                a.ufeats['VerbForm'] = 'Part'
                if value == 'VA':
                    a.ufeats['PartForm'] = 'Pres'
                elif value == 'NUT':
                    a.ufeats['PartForm'] = 'Past'
                elif value in ["MA", "AGENT"]:
                    a.ufeats['PartForm'] = 'Agt'
                elif value in ["MATON", "NEG"]:
                    a.ufeats['PartForm'] = 'Neg'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'INF':
                a.ufeats['VerbForm'] = 'Inf'
                if value == 'A':
                    a.ufeats['InfForm'] = '1'
                elif value == 'E':
                    a.ufeats['InfForm'] = '2'
                    # XXX
                    a.ufeats['Number'] = 'Sing'
                elif value == 'MA':
                    a.ufeats['InfForm'] = '3'
                    # XXX
                    a.ufeats['Number'] = 'Sing'
                elif value == 'MINEN':
                    a.ufeats['Derivation'] = 'Minen'
                elif value == 'MAISILLA':
                    a.ufeats['InfForm'] = '5'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'CMP':
                if value == 'SUP':
                    a.ufeats['Degree'] = 'Sup'
                elif value == 'CMP':
                    a.ufeats['Degree'] = 'Cmp'
                elif value == 'POS':
                    a.ufeats['Degree'] = 'Pos'
                else:
                    print(key, value, 'omor', file=stderr)
                    exit(1)
            elif key == 'SUBCAT':
                if value == 'NEG':
                    a.ufeats['Polarity'] = 'Neg'
                    a.ufeats['VerbForm'] = 'Fin'
                elif value == 'QUANTIFIER':
                    a.ufeats['PronType'] = 'Ind'
                elif value == 'REFLEXIVE':
                    a.ufeats['Reflex'] = 'Yes'
                elif value in ['COMMA', 'DASH', 'QUOTATION', 'BRACKET',
                               'ARROW']:
                    # not annotated in UD feats:
                    # * punctuation classes
                    a.misc['PunctType'] = value[0] + value[1:].lower()
                elif value in ['DECIMAL', 'ROMAN', 'DIGIT']:
                    # not annotated in UD feats:
                    # * decimal, roman NumType
                    a.misc['NumType'] = value[0] + value[1:].lower()
                elif value in ['PREFIX', 'SUFFIX']:
                    # not annotated in UD feats:
                    # * Hanging prefix/suffix?
                    a.misc['AffixType'] = value[0] + value[1:].lower()
                else:
                    print(key, value, 'SUBCAT', 'UD')
                    exit(1)
            elif key == 'ABBR':
                # XXX?
                a.ufeats['Abbr'] = 'Yes'
            elif key == 'NUMTYPE':
                a.ufeats['NumType'] = value[0] + value[1:].lower()
            elif key == 'PRONTYPE':
                a.ufeats['PronType'] = value[0] + value[1:].lower()
            elif key == 'ADPTYPE':
                a.ufeats['AdpType'] = value[0] + value[1:].lower()
            elif key == 'CLIT':
                a.ufeats['Clitic'] = value[0] + value[1:].lower()
            elif key == 'FOREIGN':
                a.ufeats['Foreign'] = 'Yes'
            elif key == 'STYLE':
                if value in ['DIALECTAL', 'COLLOQUIAL']:
                    a.ufeats['Style'] = 'Coll'
                elif value == 'NONSTANDARD':
                    # XXX: Non-standard spelling is kind of a typo?
                    # e.g. seitsämän -> seitsemän
                    a.ufeats['Typo'] = 'Yes'
                elif value == 'ARCHAIC':
                    a.ufeats['Style'] = 'Arch'
                elif value == 'RARE':
                    continue
                else:
                    print(key, value, 'STYLE', 'UD')
                    exit(1)
            elif key == 'DRV':
                if value in ['INEN', 'JA', 'LAINEN', 'LLINEN', 'MINEN', 'STI',
                             'TAR', 'TON', 'TTAA', 'TTAIN', 'U', 'VS']:
                    # values found in UD finnish Derivs
                    a.ufeats['Derivation'] = value[0] + value[1:].lower()
                elif value in ['S', 'MAISILLA', 'VA', 'MATON', 'UUS', 'ADE',
                               'INE', 'ELA', 'ILL', 'NEN', 'MPI', 'IN', 'IN²',
                               'HKO', 'ISA', 'MAINEN', 'NUT', 'TU', 'VA',
                               'TAVA', 'MA', 'LOC', 'LA', 'TUTTAA']:
                    # valuse not found in UD finnish Derivs
                    a.misc['Derivation'] = value[0] + value[1:].lower()
                else:
                    print(key, value, 'DRV', 'UD')
                    exit(1)
            elif key == 'LEX':
                a.misc['Lexicalised'] = value[0] + value[1:].lower()
            elif key == 'BLACKLIST':
                a.misc['Blacklisted'] = value
            elif key == 'PROPER':
                a.misc['PropnType'] = value[0] + value[1:].lower()
            elif key == 'POSITION':
                a.misc['Position'] = value[0] + value[1:].lower()
            elif key == 'SEM':
                a.misc['SemType'] = value[0] + value[1:].lower()
            elif key == 'COMPOUND_FORM':
                a.misc['GoesWith'] = value[0] + value[1:].lower()
            elif key == 'HOMONYM':
                a.misc['HomonymIndex'] = value
            elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE', 'NEWPARA',
                         'GUESS', 'CONJ', 'BOUNDARY']:
                # Not feats in UD:
                # * UPOS is another field
                # * Allomorphy is ignored
                # * Weight = no pties
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
                print(key, value, 'omor')
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
        anal = Analysis.fromomor(omorstr)
        anal.weight = weight
        return anal

    def get_ftb_feats(self):
        '''Get ftb analyses from token data.'''
        feats = self.ufeats
        rvs = list()
        rvs += [self.get_xpos_ftb()]
        if self.upos == 'PROPN':
            rvs += ['Prop']
        elif self.upos == 'ADV' and self.get_lemmas()[-1].endswith("sti"):
            # This is FTB oddity
            rvs += ['Pos', 'Man']
        for key, value in feats.items():
            if key == 'Number':
                if value == 'Sing':
                    rvs += ['Sg']
                elif value == 'Plur':
                    rvs += ['Pl']
            elif key == 'Tense':
                if value == 'Pres':
                    rvs += ['Prs']
                elif value == 'Past':
                    rvs += ['Prt']
            elif key == 'Mood':
                if value == 'Ind':
                    continue
                elif value == 'Cnd':
                    rvs += ['Cond']
                elif value == 'Impv':
                    rvs += ['Imp']
                else:
                    rvs += [value]
            elif key == 'Voice':
                rvs += [value]
            elif key == 'Person':
                if value == '0':
                    rvs += ['__3']
                elif value == '1':
                    rvs += ['__1']
                elif value == '2':
                    rvs += ['__2']
                elif value == '3':
                    rvs += ['__3']
                elif value == '4':
                    rvs += ['Pe4']
                else:
                    print(key, value, "for ftb", file=stderr)
                    exit(1)
            elif key == 'Number[psor]':
                if value == 'Sing':
                    rvs += ['PxSg_']
                elif value == 'Plur':
                    rvs += ['PxPl_']
                else:
                    print(key, value, "for ftb", file=stderr)
                    exit(1)
            elif key == 'Person[psor]':
                if value == '1':
                    rvs += ['Px__1']
                elif value == '2':
                    rvs += ['Px__2']
                elif value == '3':
                    rvs += ['PxSp3']
                else:
                    print(key, value, "for ftb", file=stderr)
                    exit(1)
            elif key == 'Polarity':
                if value == 'Neg':
                    rvs += ['Neg']
                else:
                    print(key, value, "ftb", file=stderr)
                    exit(1)
            elif key == 'Connegative':
                if value == 'Yes':
                    rvs += ['Act', 'ConNeg']
                else:
                    print(key, value, "ftb", file=stderr)
                    exit(1)
            elif key == 'InfForm':
                if value == '1':
                    rvs += ['Inf1', 'Lat']
                elif value == '2':
                    rvs += ['Inf2']
                elif value == '3':
                    rvs += ['Inf3']
                elif value == 'MINEN':
                    rvs += ['Inf4']
                elif value == 'MAISILLA':
                    rvs += ['Inf5']
            elif key == 'PartForm':
                # FTB participle is POS
                pass
            elif key == 'Case':
                rvs += [value]
            elif key == 'Degree':
                rvs += [value]
            elif key == 'SUBCAT':
                if value == 'NEG':
                    rvs += ['Neg']
                elif value == 'QUOTATION':
                    rvs += ['Quote']
                elif value == 'QUANTIFIER':
                    rvs += ['Qnt']
                elif value == 'DIGIT':
                    rvs += ['Digit']
                elif value in ['COMMA', 'BRACKET',
                               'ARROW', 'DECIMAL', 'PREFIX', 'SUFFIX']:
                    # not annotated in FTN feats:
                    # * punctuation classes
                    continue
                elif value == 'ROMAN':
                    # not annotated in FTN feats:
                    # * decimal, roman NumType
                    continue
                else:
                    print(key, value, 'SUBCAT', 'FTB3')
                    exit(1)
            elif key == 'NumType':
                if value == 'Ord':
                    rvs += [value]
                else:
                    pass
            elif key == 'PronType':
                if value == 'Prs':
                    rvs += ['Pers']
                elif value == 'Ind':
                    rvs += ['Qnt']
                elif value == 'Int':
                    rvs += ['Interr']
                else:
                    rvs += [value]
            elif key == 'AdpType':
                if value == 'Post':
                    rvs += ['Po']
                elif value == 'Prep':
                    rvs += ['Pr']
                elif value == 'Any':
                    pass
                else:
                    print(key, value, 'ADPTYPE', 'FTB3')
                    exit(1)
            elif key == 'Clitic':
                if value == 'Ka':
                    rvs += ['Foc_kA']
                else:
                    rvs += ['Foc_' + value]
            elif key == 'Abbr':
                rvs += ['Abbr']
            elif key == 'Derivation':
                if value in ['NUT', 'VA']:
                    rvs += ['Act']
                elif value in ['TU', 'TAVA']:
                    rvs += ['Pass']
                else:
                    continue
            elif key == 'Reflex':
                rvs += ['Refl']
            elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE', 'NEWPARA',
                         'GUESS', 'PROPER', 'SEM', 'CONJ', 'BOUNDARY',
                         'PCP', 'DRV', 'LEX', 'BLACKLIST', 'Style',
                         'POSITION', "Foreign", 'VerbForm',
                         'Typo']:
                continue
            else:
                print(key, value, 'FTB3')
                exit(1)
        for key, value in self.misc.items():
            if key == 'NumType':
                rvs += [value]
            elif key == 'Person' and value == '4':
                rvs += ['Pe4']
            elif key == 'PunctType':
                if value == "Quotation":
                    rvs += ["Quote"]
                elif value == "Dash":
                    if self.get_lemmas()[-1] == '—':
                        rvs += ['EmDash']
                    elif self.get_lemmas()[-1] == '–':
                        rvs += ['EnDash']
                    else:
                        rvs += ['Dash']
                elif value in ["Comma", "Bracket", "Arrow"]:
                    pass
                else:
                    print(key, value, 'FTB3', file=stderr)
                    exit(1)
            elif key == 'PropnType':
                rvs += ["Prop"]
            elif key in ['AffixType', "GoesWith", "Position"]:
                # XXX
                pass
            elif key == 'SemType':
                pass
            elif key == "Derivation":
                if value in ["Tava", "Tu"]:
                    rvs += ["Pass"]
                elif value in ["Va", "Nut"]:
                    rvs += ["Act"]
                else:
                    pass
            elif key == "Mood":
                if value == 'Opt':
                    rvs += ["Opt"]
            elif key in ["Lexicalised", "Blacklisted", "HomonymIndex"]:
                continue
            else:
                print(key, value, 'FTB3miscelse', file=stderr)
                exit(1)
        # post hacks
        if self.lemmas == ['ei'] and 'Foc_kA' in rvs:
            revs = []
            for r in rvs:
                if r != 'V':
                    revs += [r]
                else:
                    revs += ['CC']
            rvs = revs
        if 'Punct' in rvs and 'Sg' in rvs and 'Nom' in rvs:
            revs = []
            for r in rvs:
                if r not in ['Sg', 'Nom']:
                    revs += [r]
            rvs = revs
        if '__1' in rvs or '__2' in rvs or '__3' in rvs:
            revs = []
            for r in rvs:
                if r not in ['__1', '__2', '__3', 'Sg', 'Pl']:
                    revs += [r]
            if 'Sg' in rvs and '__1' in rvs:
                revs += ['Sg1']
            elif 'Sg' in rvs and '__2' in rvs:
                revs += ['Sg2']
            elif 'Sg' in rvs and '__3' in rvs:
                revs += ['Sg3']
            elif 'Pl' in rvs and '__1' in rvs:
                revs += ['Pl1']
            elif 'Pl' in rvs and '__2' in rvs:
                revs += ['Pl2']
            elif 'Pl' in rvs and '__3' in rvs:
                revs += ['Pl3']
            else:
                print("__X without Sg or Pl", file=stderr)
            rvs = revs
        if 'Px__1' in rvs or 'Px__2' in rvs or 'Px__3' in rvs:
            revs = []
            for r in rvs:
                if r not in ['Px__1', 'Px__2', 'Px__3', 'PxSg_', 'PxPl_']:
                    revs += [r]
            if 'PxSg_' in rvs and 'Px__1' in rvs:
                revs += ['PxSg1']
            elif 'PxSg_' in rvs and 'Px__2' in rvs:
                revs += ['PxSg2']
            elif 'PxSg_' in rvs and 'Px__3' in rvs:
                revs += ['PxSg3']
            elif 'PxPl_' in rvs and 'Px__1' in rvs:
                revs += ['PxPl1']
            elif 'PxPl_' in rvs and 'Px__2' in rvs:
                revs += ['PxPl2']
            elif 'PxPl_' in rvs and 'Px__3' in rvs:
                revs += ['PxPl3']
            elif 'Px__3' in rvs:
                revs += ['Px3']
            else:
                print("__X without Sg or Pl", file=stderr)
            rvs = revs
        if 'Neg' in rvs and 'Act' in rvs:
            revs = []
            for r in rvs:
                if r != 'Act':
                    revs += [r]
            rvs = revs
        if 'Abbr' in rvs:
            revs = []
            for r in rvs:
                if r not in ['N', 'Prop']:
                    revs += [r]
            rvs = revs
        if 'Inf1' in rvs:
            revs = []
            for r in rvs:
                if r not in ['Act', 'Pl', 'Sg']:
                    revs += [r]
            rvs = revs
        if 'Pers' in rvs:
            revs = []
            for r in rvs:
                if r not in ['Pl1', 'Sg1', 'Pl2', 'Sg2', 'Pl3', 'Sg3']:
                    revs += [r]
                elif r in ['Pl1', 'Pl2', 'Pl3']:
                    revs += ['Pl']
                elif r in ['Sg1', 'Sg2', 'Sg3']:
                    revs += ['Sg']
                else:
                    print("Logical error", r, rvs)
                    exit(2)
            rvs = revs
        if 'Card' in rvs and 'Digit' in rvs:
            revs = []
            for r in rvs:
                if r != 'Card':
                    revs += [r]
            rvs = revs
        return rvs

    def get_unimorph_feats(self):
        '''Get Unimorph analyses from token data.'''
        rvs = list()
        if self.upos == 'NOUN' or self.upos == 'PROPN':
            rvs += ['N']
        elif self.upos == 'VERB':
            if 'PartForm' in self.ufeats:
                rvs += ['V.PTCP']
            else:
                rvs += ['V']
        elif self.upos == 'ADJ':
            rvs += ['ADJ']
        for key, value in self.ufeats.items():
            if key == 'Number':
                if value == 'Sing':
                    rvs += ['SG']
                elif value == 'Plur':
                    rvs += ['PL']
            elif key == 'Tense':
                if value == 'Pres':
                    rvs += ['PRS']
                elif value == 'Past':
                    rvs += ['PST']
            elif key == 'Mood':
                if value == 'Ind':
                    rvs += ['POS', 'IND']
                elif value == 'Cnd':
                    rvs += ['PRS', 'POS', 'COND']
                elif value == 'Imp':
                    rvs += ['PRS', 'POS', 'IMP']
                elif value == 'Pot':
                    rvs += ['PRS', 'POS', 'POT']
                else:
                    rvs += [value.upper()]
            elif key == 'Voice':
                rvs += [value.upper()]
            elif key == 'Person':
                if value == '0':
                    rvs += ['3']
                elif value == '1':
                    rvs += ['1']
                elif value == '2':
                    rvs += ['2']
                elif value == '3':
                    rvs += ['3']
                elif value == '4':
                    pass
                else:
                    print(key, value, "for unimorph", file=stderr)
                    exit(1)
            elif key == 'Number[psor]':
                if value == 'Sing':
                    rvs += ['PSS_S']
                elif value == 'Plur':
                    rvs += ['PSS_P']
                else:
                    print(key, value, "for unimorph", file=stderr)
                    exit(1)
            elif key == 'Person[psor]':
                if value == '1':
                    rvs += ['PSS1']
                elif value == '2':
                    rvs += ['PSS2']
                elif value == '3':
                    rvs += ['PSS3']
                else:
                    print(key, value, "for unimorph", file=stderr)
                    exit(1)
            elif key == 'Polarity':
                rvs += ['???']
            elif key == 'Connegative':
                rvs += ['NEG']
            elif key == 'InfForm':
                if value == '1':
                    rvs += ['NFIN']
                elif value == '2':
                    rvs += ['???']
                elif value == '3':
                    rvs += ['???']
                elif value == 'MINEN':
                    rvs += ['???']
                elif value == 'MAISILLA':
                    rvs += ['???']
            elif key == 'PartForm':
                if value == 'Pres':
                    rvs += ['PRS']
                elif value == 'Past':
                    rvs += ['PST']
                elif value == '3':
                    rvs += ['???']
            elif key == 'Case':
                if value == 'Nom':
                    rvs += ['NOM']
                elif value == 'Ill':
                    rvs += ['IN+ALL']
                elif value == 'Tra':
                    rvs += ['TRANS']
                elif value == 'Ade':
                    rvs += ['AT+ESS']
                elif value == 'All':
                    rvs += ['AT+ALL']
                elif value == 'Abl':
                    rvs += ['AT+ABL']
                elif value == 'Ess':
                    rvs += ['FRML']
                elif value == 'Com':
                    rvs += ['COM', 'PL']
                elif value == 'Ins':
                    rvs += ['INS']
                elif value == 'Ine':
                    rvs += ['IN+ESS']
                elif value == 'Ela':
                    rvs += ['IN+ABL']
                elif value == 'Abe':
                    rvs += ['PRIV']
                elif value == 'Par':
                    rvs += ['PRT']
                elif value == 'Gen':
                    rvs += ['GEN']
                elif value == 'Acc':
                    rvs += ['ACC']
                else:
                    rvs += ['???']
            elif key == 'Degree':
                # yeah. unimorph has same analysis for comparative and positive
                pass
            elif key == 'SUBCAT':
                rvs += ['???']
            elif key == 'NumType':
                rvs += ['???']
            elif key == 'PronType':
                rvs += ['???']
            elif key == 'AdpType':
                rvs += ['???']
            elif key == 'Clitic':
                rvs += ['???']
            elif key == 'Abbr':
                rvs += ['???']
            elif key == 'Derivation':
                rvs += ['???']
            elif key == 'Reflex':
                rvs += ['???']
            elif key in ['UPOS', 'ALLO', 'WEIGHT', 'CASECHANGE', 'NEWPARA',
                         'GUESS', 'PROPER', 'SEM', 'CONJ', 'BOUNDARY',
                         'PCP', 'DRV', 'LEX', 'BLACKLIST', 'Style',
                         'POSITION', "Foreign", 'VerbForm',
                         'Typo']:
                continue
            else:
                print(key, value, 'unimorph')
                exit(1)
        # unimorph is very limited so we delete a lot of tags...
        if 'V.PTCP' in rvs and 'ACT' in rvs and 'PRS' in rvs:
            rvs = ['V.PTCP', 'ACT', 'PRS']
        elif 'V.PTCP' in rvs and 'ACT' in rvs and 'PST' in rvs:
            rvs = ['V.PTCP', 'ACT', 'PST']
        elif 'V.PTCP' in rvs and 'PASS' in rvs and 'PRS' in rvs:
            rvs = ['V.PTCP', 'PASS', 'PRS']
        elif 'V.PTCP' in rvs and 'PASS' in rvs and 'PST' in rvs:
            rvs = ['V.PTCP', 'PASS', 'PST']
        elif 'NFIN' in rvs:
            rvs = ['V', 'NFIN']
        # hack combinations
        if 'COM' in rvs and 'PSS3' in rvs:
            # ???
            rvs.remove('PSS3')
        # merge possessive readings and hac
        if 'PSS_S' in rvs:
            if 'PSS1' in rvs:
                rvs.append('PSS1S')
                rvs.remove('PSS1')
            elif 'PSS2' in rvs:
                rvs.append('PSS2S')
                rvs.remove('PSS2')
            elif 'PSS3' in rvs:
                rvs.append('PSS3S')
                rvs.remove('PSS3')
            rvs.remove('PSS_S')
        elif 'PSS_P' in rvs:
            if 'PSS1' in rvs:
                rvs.append('PSS1P')
                rvs.remove('PSS1')
            elif 'PSS2' in rvs:
                rvs.append('PSS2P')
                rvs.remove('PSS2')
            elif 'PSS3' in rvs:
                rvs.append('PSS3P')
                rvs.remove('PSS3')
            rvs.remove('PSS_P')
        # re-order as use
        revs = []
        for r in rvs:
            if r not in ['SG', 'PL']:
                revs.append(r)
        for r in rvs:
            if r in ['SG', 'PL']:
                revs.append(r)
        return revs

    def get_vislcg_feats(self):
        '''Get VISL-CG 3 features from analysed token.'''
        vislcgs = list()
        vislcgs += ['UPOS=' + self.upos]
        for key, value in self.ufeats.items():
            vislcgs += [key + '=' + value]
        for key, value in self.misc.items():
            vislcgs += ['<' + key + '=' + value + '>']
        # number of compound parts in compound is a good CG numeric feature!!
        lemmas = self.get_lemmas()
        vislcgs += ['<CMP=' + str(len(lemmas)) + '>']
        if self.weight != float('inf'):
            vislcgs += ['<W=' + str(int(self.weight * 1000)) + '>']
        else:
            vislcgs += ['<W=999999999999999999999999>']
        for mangler in self.manglers:
            vislcgs += ['<*' + mangler + '>']
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
            miscs += ['|'.join(self.manglers)]
        if self.analsurf:
            miscs += ['AnalysisForm=' + self.analsurf]
        miscs += ['Weight=' + str(self.weight)]
        return miscs

    def printable_ud_misc(self):
        '''Formats UD misc like in UD data.'''
        miscs = self.get_ud_misc()
        if not miscs:
            return '_'
        return '|'.join(miscs)

    def printable_udepname(self):
        '''Format udep as string for CONLL-U.

        Returns:
            string of udep nam
        '''
        if self.udepname:
            return self.udepname
        else:
            return '_'

    def printable_udephead(self):
        '''Format udep head position for CONLL-U.

        Returns:
            string of non-ngative integer or _'''
        if self.udepname and self.udepname == 'root' and self.udeppos == 0:
            return '0'
        if self.udeppos:
            return str(self.udeppos)
        else:
            return '_'

    def printable_ud_feats(self, hacks=None):
        '''Formats UD feats from token data exactly as in fi-tdt data.

        When the correct analysis is in question the result should be equal
        to the UFEAT field of the connl-u data downloadable from UD web site,
        in string format.

        Returns:
            string of |-separated key=value pairs in correct order or _
        '''
        rvs = self.ufeats
        if not rvs:
            return '_'
        rv = ''
        for k in sorted(rvs, key=str.lower):
            rv += k + '=' + rvs[k] + '|'
        return rv.rstrip('|')

    def printable_unimorph(self):
        '''Formats FTB feats from token data like in FTB-2014 data.'''
        rvs = self.get_unimorph_feats()
        return ';'.join(rvs)

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
            # this is inverse that I intended but oh well...
            if 'PartForm' in self.ufeats:
                if self.ufeats['PartForm'] == 'Past':
                    return 'PrfPrc'
                elif self.ufeats['PartForm'] == 'Agt':
                    return 'AgPrc'
                elif self.ufeats['PartForm'] == 'Pres':
                    return 'PrsPrc'
                elif self.ufeats['PartForm'] == 'Neg':
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
        if self.weight == float("inf"):
            return True
        return False
