#!/usr/bin/env python3

from sys import stderr

# common symbols for all

version_id_easter_egg='OMORFI_VERSION_≥_14_©_GNU_GPL_V3'
word_boundary="{WB}"
weak_boundary="{XB}"
deriv_boundary="{DB}"
morph_boundary="{MB}"
stub_boundary="{STUB}"
optional_hyphen="{hyph?}"
# It's not fully symmetric so two sets
fin_lowercase = "abcdefghijklmnopqrsštuvwxyzžåäö" + \
    "áàâãāăąçćĉċčđðďéèêëēĕęėěƒĝğġģȟħíìîïĩīĭįıĳĵķĸĺļľŀłñńņňŉŋ" + \
    "óòôōŏŕŗřśŝşſţťŧßþúùûüũūŭůųŵýŷÿűźżʒæøœőə"
fin_uppercase = "ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽÅÄÖ" \
    "ÁÀÂÃĀĂĄÇĆĈĊČÐĎÉÈÊËĒĔĘĖĚĜĞĠĢȞĦÍÌÎÏĨĪĬĮİĲĴĶĹĻĽĿŁÑŃŅŇŊ" + \
    "ÓÒÔŌŎŔŖŘŚŜŞŢŤŦÞÚÙÛÜŨŪŬŮŲŴÝŶŰŹŻƷÆØŒŐƏ"
fin_lower_vowels = "aeiouyåäö" + \
    "áàâãāăąéèêëēĕęėěíìîïĩīĭįıóòôōŏúùûüũūŭůųýŷÿűæøœőə"
fin_upper_vowels = "AEIOUYÅÄÖ" \
    "ÁÀÂÃĀĂĄÉÈÊËĒĔĘĖĚÍÌÎÏĨĪĬĮİÓÒÔŌŎÚÙÛÜŨŪŬŮŲÝŶŰÆØŒŐƏ"
fin_vowels = fin_lower_vowels + fin_upper_vowels
fin_lower_consonants = "bcdfghjklmnpqrsštvwxzž" + \
    "çćĉċčđðďƒĝğġģȟħĵķĸĺļľŀłñńņňŉŋŕŗřśŝşſţťŧßþŵźżʒ"
fin_upper_consonants = "BCDFGHJKLMNPQRSŠTVWXZŽ" \
    "ÇĆĈĊČÐĎĜĞĠĢȞĦĴĶĹĻĽĿŁÑŃŅŇŊŔŖŘŚŜŞŢŤŦÞŴŹŻƷ"
fin_consonants = fin_lower_consonants + fin_upper_consonants
# the words containing symbols are likely weird / props etc.
fin_symbols = "1234567890§!\"#¤%&/()=?½@£$‚{[]}<>*"
# known variants and old orthographies 1:1
# (a conservative listing for sure)
fin_orth_pairs = [("’", "'"), ("’", "´"), ("’", "′"), ("-", "‐"), ("-", "‑"), ("-", "‑")]

def fail_formatting_missing_for(stuff, format, moar=None):
    print("\033[93mMissing tag!\033[0m Trying to format:", stuff, "for tagset:",
            format, file=stderr)
    if moar:
        print("\033[92mExplanation\033[0m:", moar, file=stderr)

def fail_guess_because(wordmap, matches, failures, moar=None):
    print("\033[93mUnguessable!\033[0m Following has been seen:", matches,
            "\nfollowing was tested and failed:", failures,
            "\nwhen trying: (", 
            wordmap['lemma'], wordmap['pos'], 
            wordmap['kotus_tn'], wordmap['kotus_av'],
            wordmap['harmony'], ")", file=stderr)
    if moar:
        print("\033[92mExplanation\033[0m:", moar, file=stderr)
    # This can be used to automate classifying plurales etc.
    #if wordmap['lemma'].endswith('t'):
    #if wordmap['is_proper']:
    #    print(wordmap['lemma'], wordmap['kotus_tn'], wordmap['kotus_av'])

def require_suffix(wordmap, suffix):
    if not wordmap['lemma'].endswith(suffix):
        fail_guess_because(wordmap, [], [suffix])

def remove_suffix(s, suffix):
    if s.endswith(suffix):
        return s[:s.rfind(suffix)]
    else:
        return s

def remove_suffixes_or_die(s, suffixes):
    for suffix in suffixes:
        nu =  remove_suffix(s, suffix)
        if nu != s:
            return nu
    print("\033[91mUnstubbable!\033[0m Trying to rstrip ", ", ".join(suffixes),
        "from", s)
    return None

def replace_suffix(s, suffix, repl):
    if s.endswith(suffix):
        return s[:s.rfind(suffix)] + repl + s[s.rfind(suffix):]
    else:
        return s

def replace_suffixes_or_die(s, suffixes, repl):
    for suffix in suffixes:
        nu = replace_suffix(s, suffix, repl)
        if nu != s:
            return nu
    print("\033[91mSuffix fail!\033[0m Trying to rstrip ", ", ".join(suffixes),
        "from", s)
    return s

def mangle_suffixes_or_die(wordmap, suffixes):
    wordmap['bracketstub'] = replace_suffixes_or_die(wordmap['stub'], suffixes,
            '<Del>→')
    wordmap['stub'] = remove_suffixes_or_die(wordmap['stub'], suffixes)
    if wordmap['stub'] == None:
        print("Word has been misclassified or suffix stripping is insufficient."
                "Fix the database or stripping rules to continue.",
                "Relevant word entry:\n", wordmap, file=stderr)
        exit(1)
    return wordmap

# misc functions
def replace_rightmost(s, needle, repl):
    '''Replace one occurrence of rightmost match.'''
    return replace_rightmosts(s, [needle], [repl])

def replace_rightmosts(s, needles, repls):
    '''Perform replacement on the rightmost matching substring from the list.
    '''
    rm = -1
    rmi = -1
    for i in range(len(needles)):
        pos = s.rfind(needles[i])
        if pos > rm:
            rm = pos
            rmi = i
    if rm != -1:
        s = s[:rm] + repls[rmi] + s[rm+len(needles[rmi]):]
    else:
        print("Suspicious replacement attempts!", file=stderr)
        print("tried to ", needles, " => ", repls, " in ", s, file=stderr)
    return s

def lexc_escape(s):
    '''Escape symbols that have special meaning in lexc.'''
    s = s.replace("%", "__PERCENT__")
    s = s.replace(" ", "% ")
    s = s.replace("<", "%<")
    s = s.replace(">", "%>")
    s = s.replace("0", "%0")
    s = s.replace("!", "%!")
    s = s.replace(":", "%:")
    s = s.replace('"', '%"')
    s = s.replace(";", "%;")
    s = s.replace("__PERCENT__", "%%")
    return s

def twolc_escape(s):
    '''Escape symbols that have special meaning in twolc.'''
    s = s.replace("%", "__PERCENT__")
    for c in ' <>0!:";%_^{}-[]/?+|&':
        s = s.replace(c, "%" + c)
    s = s.replace("__PERCENT__", "%%")
    return s

