#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Support functions for handling tokens. Now in class form.
"""
import re

# debug :-(
from sys import stderr


class Token:
    """Token holds a slice of text with its analyses and features.

    Token is typically a word-form, such as "pojat" or "juopottelevat", but
    can also be a white-space sequence or placeholder for some out of text
    metadata, a tag, comment or i/o error.

    For a reference, see [spaCy tokens](https://spacy.io/api/token), it's
    not exactly the same thing and I don't agree with all there, but it's
    quite cool and well-documented.
    """

    def __init__(self, surf=None):
        """Create token with surface string optionally."""
        ## underlying raw omor analysis
        self.omor = None
        ## original surface form
        self.surf = surf
        ## surface used for analysis
        self.analsurf = None
        ## Lemma or word ID or baseform
        self.lemma = None
        ## whether the word starts the sentence
        self.firstinsent = False
        ## word index in context, e.g. UD column 1
        self.pos = 0
        ## whether analysis was guessed from OOV
        self.oov = False
        ## generic weight
        self.weight = None
        ## weight based on lexems
        self.lexicalweight = None
        ## whitespace
        self.whitespace = False
        ## nontoken
        self.nontoken = False
        ## misc (UD field)
        self.misc = None
        ## comment (esp. with non-token)
        self.comment = None
        ## use when tokenisation or parsing breaks
        self.error = None
        ## Case transformation performed between surf and analysis
        self.recased = False
        ## The actual analysed token if changed for analysis from surf
        self.analsurf = None
        ## Guesser used to produce analysis for oov
        self.guesser = None
        ## Underlying raw segment analysis
        self.segments = None
        self.segmentweight = None
        ## Underlying raw labelsegment analysis
        self.labelsegments = None
        self.lsweight = None
        ## If token is separated by space from left
        self.spacebefore = False
        ## If token is separated by space from right
        self.spaceafter = False
        ## hide reference conll-u here
        self._conllu = None

    def __getitem__(self, key):
        """Tokens are like dicts ever still."""
        if key == 'anal':
            return self.omor
        else:
            raise KeyError(key)

    def __str__(self):
        s = 'Token: {'
        if self.surf:
            s += ', surf: ' + self.surf
        if self.omor:
            s += ', omor: ' + self.omor
        if self.nontoken:
            s += ', nontoken: ' + self.nontoken
        if self.error:
            s += ', error: ' + self.error
        if self.comment:
            s += ', comment: ' + self.comment
        s += '}'
        return s

    @staticmethod
    def fromdict(token):
        """Create token from pre-2019 tokendict."""
        cons = Token(token['surf'])
        for k, v in token.items():
            if k == 'anal':
                cons.omor = v
        return cons

    @staticmethod
    def fromsurf(surf):
        """Creat token from surface string."""
        return Token(surf)

    @staticmethod
    def fromconllu(conllu):
        """Create token from conll-u line."""
        fields = conllu.split()
        if len(fields) != 10:
            print("conllu2token conllu fail", fields)
        upos = fields[3]
        wordid = fields[2]
        surf = fields[1]
        ufeats = fields[5]
        misc = fields[9]
        analysis = '[WORD_ID=%s][UPOS=%s]%s' % (wordid, upos,
                                                Token._ufeats2omor(ufeats))
        token = Token(surf)
        token.omor = analysis
        token.misc = misc
        token.surf = surf
        return token

    @staticmethod
    def fromvislcg(line):
        '''Create a token from VISL CG-3 line.

        VISL-CG 3 is not a line based format, so you only get a partial token.
        '''
        token = Token()
        line = line.rstrip()
        if not line or line == '':
            token.nontoken = True
            token.comment = ''
        elif line.startswith("#") or line.startswith("<"):
            token.nontoken = True
            token.comment = line.strip()
        elif line.startswith('"<') and line.endswith('>"'):
            token.surf = line[2:-2]
        elif line.startswith('\t"'):
            fields = line.strip().split()
            token.lemma = fields[1].strip('"')
        elif line.startswith(';\t"'):
            # gold?
            token.nontoken = True
            token.comment = line.strip()
        else:
            token.nontoken = True
            token.error = 'vislcg: ' + line.strip()
        return token

    @staticmethod
    def _ufeats2omor(ufeats):
        return '[' + ufeats.replace('|', '][') + ']'

    def error_in_omors(self, omor, blah):
        '''Convenience function to log error and die in format handlings.'''
        if blah:
            print(blah, file=stderr)
        print("Unrecongised", omor, "in", self, file=stderr)
        exit(1)

    def get_lemmas(self, hacks=None):
        '''Get lemma(s) from analysed token.'''
        if not self.omor:
            if self.surf:
                return [self.surf]
            else:
                return None
        re_lemma = re.compile(r"\[WORD_ID=([^]]*)\]")
        escanal = self.omor.replace('[WORD_ID=]]',
                                    '[WORD_ID=@RIGHTSQUAREBRACKET@]')
        lemmas = re_lemma.finditer(escanal)
        rv = []
        for lemma in lemmas:
            s = lemma.group(1)
            for i in range(32):
                hnsuf = '_' + str(i)
                if s.endswith(hnsuf):
                    s = s[:-len(hnsuf)]
            if s == '@RIGHTSQUAREBRACKET@':
                s = ']'
            rv += [s]
        # legacy pron hack
        if len(rv) == 1 and rv[0] in ['me', 'te', 'he', 'nämä', 'ne'] and\
                self.get_upos() == 'PRON' and hacks:
            if rv[0] == 'me':
                rv[0] = 'minä'
            elif rv[0] == 'te':
                rv[0] = 'sinä'
            elif rv[0] == 'he':
                rv[0] = 'hän'
            elif rv[0] == 'nämä':
                rv[0] = 'tämä'
            elif rv[0] == 'ne':
                rv[0] = 'se'
        return rv

    def get_last_feat(self, feat):
        '''Get last (effective) value for the given morphological feature.

        This function tries to determine the most likely morphosyntactic
        feature values from complex analyses, e.g. with compounds and
        derivations the most relevant ones for the whole token.
        '''
        if not self.omor:
            return None
        re_feat = re.compile(r"\[" + feat + r"=([^]]*)\]")
        feats = re_feat.finditer(self.omor)
        rv = ""
        for f in feats:
            rv = f.group(1)
        return rv

    def get_last_feats(self):
        '''Get last (effective) value for the given morphological feature.

        This function tries to determine the most likely morphosyntactic
        feature values from complex analyses, e.g. with compounds and
        derivations the most relevant ones for the whole token.
        '''
        if not self.omor:
            return None
        re_feats = re.compile(r"\[[A-Z_]*=[^]]*\]")
        rvs = list()
        feats = re_feats.finditer(self.omor)
        for feat in feats:
            if 'WORD_ID=' in feat.group(0):
                # feats reset on word boundary
                rvs = list()
            else:
                rvs.append(feat.group(0))
        return rvs

    def get_upos(self, deriv_munging=True):
        '''Get Universal Part-of-Speech.'''
        upos = self.get_last_feat("UPOS")
        if deriv_munging:
            drv = self.get_last_feat("DRV")
            if upos == 'VERB' and drv == 'MINEN':
                upos = 'NOUN'
        return upos

    def get_ftb_feats(self):
        '''Get FTB analyses from token data.'''
        feats = self.get_last_feats()
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
                elif value == 'ADV' and self.surf.endswith("sti"):
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
                    self.error_in_omors(key, "for ftb")
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
                    if self.surf == '—':
                        rvs += ['EmDash']
                    elif self.surf == '–':
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
                    self.error_in_omors('SUBCAT', 'FTB3')
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
                    self.error_in_omors('ADPTYPE', 'FTB3')
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
                self.error_in_omors(key, 'FTB3')
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

    def get_ud_feats(self, hacks=None):
        '''Get Universal Dependencies features from analysed token.'''
        feats = self.get_last_feats()
        if not feats:
            return None
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
                elif value in ['DECIMAL', 'ROMAN', 'DIGIT']:
                    # not annotated in UD feats:
                    # * decimal, roman NumType
                    continue
                elif value in ['PREFIX', 'SUFFIX']:
                    # not annotated in UD feats:
                    # * decimal, roman NumType
                    continue
                else:
                    self.error_in_omors('SUBCAT', 'UD')
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
                    self.error_in_omors('STYLE', 'UD')
            elif key in ['DRV', 'LEX']:
                if value in ['INEN', 'JA', 'LAINEN', 'LLINEN', 'MINEN', 'STI',
                             'TAR', 'TON', 'TTAA', 'TTAIN', 'U', 'VS']:
                    # values found in UD finnish Derivs
                    rvs['Derivation'] = value[0] + value[1:].lower()
                elif value in ['S', 'MAISILLA', 'VA', 'MATON', 'UUS', 'ADE',
                               'INE', 'ELA', 'ILL', 'NEN', 'MPI', 'IN', 'IN²',
                               'HKO', 'ISA', 'MAINEN', 'NUT', 'TU', 'VA',
                               'TAVA', 'MA', 'LOC', 'LA']:
                    # valuse not found in UD finnish Derivs
                    continue
                else:
                    self.error_in_omors(key, 'UD')
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
                self.error_in_omors(key, 'UD')
        return rvs

    def get_vislcg_feats(self):
        '''Get VISL-CG 3 features from analysed token.'''
        feats = self.get_last_feats()
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
                    self.error_in_omors('BOUNDARY', 'VISLCG')
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
                self.error_in_omors(key, 'VISLCG')
        if self.recased:
            vislcgs += ["<*" + self.recased + ">"]
        if self.weight:
            vislcgs += ["<W=" + str(int(self.weight * 1000)) + ">"]
        if self.lexicalweight:
            vislcgs += ["<L=" + str(int(self.lexicalweight * 1000)) + ">"]
        if self.guesser:
            vislcgs += ["<Heur?>", "<Guesser_" + self.guesser + ">"]
        # number of compound parts in compound is a good CG numeric feature!!
        lemmas = self.get_lemmas()
        vislcgs += ['<CMP=' + str(len(lemmas)) + '>']
        return vislcgs

    def get_segments(self, split_morphs=True, split_words=True,
                     split_new_words=True, split_derivs=False,
                     split_nonwords=False):
        '''Get specified segments from segmented analysis.'''
        segments = self.segments
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
        analysis = self.labelsegments
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
        if self.guesser:
            miscs += ["Guesser=" + self.guesser]
        if self.analsurf and self.analsurf != self.surf:
            miscs += ['AnalysisForm=' + self.analsurf]
        if self.recased:
            miscs += ['CaseChanged=' + self.recased]
        if self.spaceafter:
            miscs += ['SpaceAfter=' + self.spaceafter]
        if self.spacebefore:
            miscs += ['SpaceBefore=' + self.spacebefore]
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
        rvs = self.get_ud_feats(hacks)
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
        lemmas = self.get_lemmas(True)
        return '\t"' + '#'.join(lemmas) + '" ' + ' '.join(mrds)


def is_tokenlist_oov(l):
    '''Checks if all hypotheses are OOV guesses.'''
    if not l:
        return True
    elif len(l) == 1 and l[0].oov:
        return True
    elif l and not l[0].oov:
        return False
    else:
        return False


def printable_vislcg(l):
    '''Create VISL-CG 3 output from hypothesis list.'''
    vislcg = '"<' + l[0].surf + '>"\n'
    for anal in l:
        vislcg += anal.printable_vislcg()
    return vislcg


