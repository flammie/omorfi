#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Support functions for handling tokens. Now in class form.
"""
# debug :-(
from sys import stderr

from .analysis import Analysis


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
        ## all gathered analyses so far as Analysis objects
        self.analyses = []
        ## all constructed morph segmentations
        self.segmentations = []
        ## all constructed morph labelsegmentations
        self.labelsegmentations = []
        ## all constructed lemmatisations
        self.lemmatisations = []
        ## original surface form
        self.surf = surf
        ## word index in context, e.g. UD column 1
        self.pos = 0
        ## nontoken
        self.nontoken = False
        ## comment (esp. with non-token)
        self.comment = None
        ## use when tokenisation or parsing breaks
        self.error = None
        ## If token is separated by space from left
        self.spacebefore = False
        ## If token is separated by space from right
        self.spaceafter = False
        ## Gold reference can be stored in token for few apps
        self.gold = None

    def __getitem__(self, key):
        """Tokens can still be accessed like dicts for compatibility.

        Some keys like surf and pos are obvious and direct while some old keys
        like omor for analysis is mapped to 1-random analysis string if there
        are any.
        """
        if key == 'anal':
            # return first omor analysis for b/w comp & ease of use
            for analysis in self.analyses:

                if analysis.name == 'omor':
                    return analysis.raw
            return None
        elif key == 'surf':
            return self.surf
        elif key == 'pos':
            return self.pos
        else:
            raise KeyError(key)

    def __str__(self):
        s = '"omorfi.Token": {'
        if self.surf:
            s += '"surf": "' + self.surf + '"'
        if self.nontoken:
            s += '"nontoken": "' + self.nontoken + '"'
        if self.pos:
            s += ',\n "pos": "' + str(self.pos) + '"'
        if self.analyses:
            s += ',\n "omorfi.Analyses": ['
            comma = ""
            for anal in self.analyses:
                s += comma + "\n" + str(anal)
                comma = ","
            s += '\n]'
        if self.error:
            s += ',\n "error": "' + self.error + '"'
        if self.comment:
            s += ',\n "comment": "' + self.comment + '"'
        s += '}'
        return s

    @staticmethod
    def fromstr(s: str):
        """Creates token from string.

        Strings should be made with print(token).
        """
        lines = s.split("\n")
        token = Token()
        in_anals = False
        for line in lines:
            if '"omorfi.Token"' in line:
                # first
                continue
            elif line.strip() == '}':
                # last
                continue
            elif in_anals:
                if line.strip() == ']':
                    in_anals = False
                else:
                    anal = Analysis.fromstr(line)
                    token.analyses.append(anal)
            else:
                k, v = line.split(":")
                if k == '"surf"':
                    token.surf = v.strip().strip('"')
                elif k == '"nontoken"':
                    token.nontoken = v.strip().strip('"')
                elif k == '"pos"':
                    token.pos = int(v.strip().strip('"'))
                elif k == '"error"':
                    token.error = v.strip().strip('"')
                elif k == '"comment"':
                    token.comment = v.strip().strip('"')
                elif k == '"omorfi.Analyses"':
                    in_anals = True
                else:
                    print("Error parsing token", line, file=stderr)
                    exit(1)
        return token

    @staticmethod
    def fromdict(token: dict):
        """Create token from pre-2019 tokendict."""
        cons = Token(token['surf'])
        for k, v in token.items():
            if k == 'anal':
                anal = Analysis(v, 0.0)
                cons.analyses.append(anal)
        return cons

    @staticmethod
    def fromsurf(surf: str):
        """Creat token from surface string."""
        return Token(surf)

    @staticmethod
    def fromconllu(conllu: str):
        """Create token from conll-u line."""
        fields = conllu.split()
        if len(fields) != 10:
            print("conllu2token conllu fail", fields)
        upos = fields[3]
        wordid = fields[2]
        surf = fields[1]
        ufeats = fields[5]
        misc = fields[9]
        omor = Analysis('[WORD_ID=' + wordid + ']' + '[UPOS=' + upos + ']' +
                        Token._ufeats2omor(ufeats), 0.0, "omor")
        omor.misc = misc
        token = Token(surf)
        token.analyses.append(omor)
        # we can now store the original here
        orig = Analysis(conllu, 0.0, "conllu")
        token.analyses.append(orig)
        token.surf = surf
        return token

    @staticmethod
    def fromvislcg(s: str):
        '''Create a token from VISL CG-3 text block.

        The content should at most contain one surface form with a set of
        analyses.
        '''
        token = Token()
        lines = s.split('\n')
        for line in lines:
            line = line.rstrip()
            if not line or line == '':
                token.nontoken = 'separator'
            elif line.startswith("#") or line.startswith("<"):
                token.nontoken = 'comment'
                token.comment = line.strip()
            elif line.startswith('"<') and line.endswith('>"'):
                token.surf = line[2:-2]
            elif line.startswith('\t"'):
                anal = Analysis(line.strip(), 0.0, "vislcg")
                token.analyses.append(anal)
            elif line.startswith(';\t"'):
                # gold?
                anal = Analysis(line[1:].strip(), float("inf"), "vislcg")
                token.analyses.append()
            else:
                token.nontoken = "error"
                token.error = 'vislcg: ' + line.strip()
        return token

    @staticmethod
    def _ufeats2omor(ufeats):
        return '[' + ufeats.replace('|', '][') + ']'

    def is_oov(self):
        '''Checks if all hypotheses are OOV guesses.'''
        for analysis in self.analyses:
            if not analysis.is_oov():
                return False
        return True

    def printable_vislcg(self):
        '''Create VISL-CG 3 output based on token and its analyses.'''
        if self.error:
            return "<ERROR>" + self.error + "</ERROR>"
        elif self.nontoken:
            if self.nontoken == 'comment':
                return self.comment
            elif self.nontoken == 'separator':
                return '\n'
            elif self.nontoken == 'eof':
                return ""
            else:
                return "<ERROR>" + self.nontoken + "</ERROR>"
        elif self.surf:
            vislcg = '"<' + self.surf + '>"\n'
            newline = ""
            for anal in self.analyses:
                vislcg += newline + anal.printable_vislcg()
                newline = "\n"
            return vislcg
        else:
            return "<ERROR>" + self + "</ERROR>"

    def _select_anal(self, which):
        anal = None
        if which == "1random":
            if self.analyses:
                anal = self.analyses[0]
        elif which == "1best":
            minw = float("inf")
            for a in self.analyses:
                if a.weight < minw:
                    anal = a
                    minw = a.weight
        elif self.analyses[which]:
            anal = self.analyses[which]
        else:
            print("Unknown which", which)
            exit(1)
        return anal

    def printable_conllu(self, hacks=None, which="1best"):
        '''Create CONLL-U output based on token and selected analysis.'''
        if self.nontoken:
            if self.nontoken == 'error':
                return "# ERROR:" + self.error
            elif self.nontoken == 'comment':
                if self.comment.startswith('#'):
                    return self.comment
                else:
                    return '# ' + self.comment
            elif self.nontoken == 'separator':
                # not returning \n since the it's already printed on a line
                return ''
            else:
                # ignore other nontokens??
                return ''
        lemma = self.surf
        upos = 'X'
        third = '_'
        ud_feats = '_'
        ud_misc = '_'
        anal = self._select_anal(which)
        if anal:
            upos = anal.get_upos()
            if hacks and hacks == 'ftb':
                third = anal.get_xpos_ftb()
            else:
                third = anal.get_xpos_tdt()
            lemmas = anal.get_lemmas()
            if lemmas:
                lemma = '#'.join(lemmas)
            ud_feats = anal.printable_ud_feats()
            ud_misc = anal.printable_ud_misc()
            depname = anal.printable_udepname()
            dephead = anal.printable_udephead()
        else:
            upos = 'X'
            lemma = self.surf
            third = upos
            ud_feats = '_'
            dephead = '0'
            depname = 'dep'
            ud_misc = '_'
        return "\t".join([str(self.pos), self.surf, lemma, upos, third,
                          ud_feats, dephead, depname, "_", ud_misc])

    def printable_ftb3(self, which="1best"):
        '''Create FTB-3 output based on token and selected analysis.'''
        if self.nontoken:
            if self.nontoken == 'error':
                return "# ERROR:" + self.error
            elif self.nontoken == 'comment':
                if self.comment.startswith('#'):
                    return self.comment
                else:
                    return '# ' + self.comment
            elif self.nontoken == 'separator':
                # not returning \n since the it's already printed on a line
                return ''
            else:
                # ignore other nontokens??
                return ''
        lemma = self.surf
        pos = '_'
        feats = '_'
        anal = self._select_anal(which)
        if anal:
            pos = anal.get_xpos_ftb()
            lemmas = anal.get_lemmas()
            if lemmas:
                lemma = '#'.join(lemmas)
            feats = anal.printable_ftb_feats()
        return '\t'.join([str(self.pos), self.surf, lemma, pos, pos, feats,
                          '_', '_', '_', '_'])

    def _get_nbest(self, n: int, anals: list):
        nbest = []
        worst = -1.0
        if n == 0:
            n = 65535
        for anal in anals:
            if len(nbest) < n:
                nbest.append(anal)
                # when filling the queue find biggest
                if anal.weight > worst:
                    worst = anal.weight
            elif anal.weight < worst:
                # replace worst
                for i, a in enumerate(nbest):
                    if a.weight == worst:
                        nbest[i] = anal
                worst = -1.0
                for a in nbest:
                    if a.weight > worst:
                        worst = a.weight
        return nbest

    def get_nbest(self, n: int):
        """Get n most likely analyses.

        Args:
            n: number of analyses, use 0 to get all

        Returns:
            At most n analyses of given type or empty list if there aren't any.
        """
        return self._get_nbest(n, self.analyses)

    def get_best(self):
        """Get most likely analysis.

        Returns:
            most probably analysis of given type, or None if analyses have not
            been made for the type.
        """
        nbest1 = self.get_nbest(1)
        if nbest1:
            return nbest1[0]
        else:
            return None

    def get_best_segments(self):
        """Get most likely segmentation.

        Returns:
            list of strings each one being a morph or other sub-word segment.
        """
        nbest1 = self._get_nbest(1, self.segmentations)
        if nbest1:
            return nbest1[0]
        else:
            return None
