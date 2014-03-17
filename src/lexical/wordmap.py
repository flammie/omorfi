#!/usr/bin/env python3
def init_wordmap():
    wordmap = {"pos": None, "lemma": None, "new_paras": list(), "kotus_tn": None,
               "kotus_av": None, "plurale_tantum": None,
               "possessive": None, "clitics": None,
               "is_proper": None, "proper_noun_class": list(), "style": None,
               "stub": None, "gradestem": None, "twolstem": None, 
               "grade_dir": None, "harmony": None, "is_suffix": None,
               "is_prefix": None, "stem_vowel": None, "stem_diphthong": None,
               "subcat": list(), "sem": list(), "particle": list(), "pronunciation": None,
               "boundaries": None, "bracketstub": None, "origin": None,
               "extra_i": False, "extra_e": False, "real_pos": None}
    return wordmap

def get_wordmap_fieldnames():
    return ["pos", "lemma", "new_paras", "kotus_tn", "kotus_av",
            "plurale_tantum", "possessive", "clitics", "is_proper",
            "proper_noun_class", "style", "stub", "gradestem", "twolstem",
            "grade_dir", "harmony", "is_suffix", "is_prefix", "stem_vowel",
            "stem_diphthong", "subcat", "sem", "particle", "pronunciation", 
            "boundaries", "bracketstub", "origin", "extra_i", "extra_e", "real_pos"]

# Split a wordmap into a list of wordmaps each having a different item of original
# <field> list in their respective <field>, or only '' if <field> list was empty.
def split_wordmap_by_field(wordmap, field):
    if not wordmap[field]:
        wordmap[field] = ['']
    wordmaps = []
    for value in wordmap[field]:
        wm_copy = dict(wordmap)
        wm_copy[field] = value
        wordmaps.append(wm_copy)
    return wordmaps
