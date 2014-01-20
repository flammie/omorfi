#!/usr/bin/env python3
def init_wordmap():
    wordmap = {"lemma": None, "new_paras": None, "pos": None, "kotus_tn": None,
               "kotus_av": None, "plurale_tantum": None,
               "possessive": None, "clitics": None,
               "is_proper": None, "proper_noun_class": None, "style": None,
               "stub": None, "gradestem": None, "twolstem": None, 
               "grade_dir": None, "harmony": None, "is_suffix": None,
               "is_prefix": None, "stem_vowel": None, "stem_diphthong": None,
               "sem": None, "particle": None, "pronunciation": None,
               "boundaries": None, "bracketstub": None, "origin": None}
    return wordmap

def get_wordmap_fieldnames():
    return ["lemma", "new_paras", "pos", "kotus_tn", "kotus_av",
            "plurale_tantum", "possessive", "clitics", "is_proper",
            "proper_noun_class", "style", "stub", "gradestem", "twolstem",
            "grade_dir", "harmony", "is_suffix", "is_prefix", "stem_vowel",
            "stem_diphthong", "subcat", "sem", "particle", "pronunciation", 
            "boundaries", "bracketstub", "origin"]
