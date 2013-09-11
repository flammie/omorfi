#!/usr/bin/env python3

from sys import stderr

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
    return s

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
    return wordmap

# misc functions
def replace_rightmost(s, needle, repl):
    '''Replace one occurrence of rightmost match.'''
    return replace_rightmosts(s, [needle], [repl])

def replace_rightmosts(s, needles, repls):
    '''Perform replacements of rightmost matching substrings.
    Performs match on first matching rightmost substring in the list.
    '''
    unfound = True
    for i in range(len(needles)):
        rm = s.rfind(needles[i])
        if rm != -1:
            s = s[:rm] + repls[i] + s[rm+len(needles[i]):]
            unfound = False
            break
    if unfound:
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
    s = s.replace("__PERCENT__", "%%")
    return s

