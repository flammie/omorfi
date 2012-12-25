#!/usr/bin/env python3

from sys import stderr

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
    s = s.replace("0", "%0")
    s = s.replace("!", "%!")
    s = s.replace("__PERCENT__", "%%")
    return s

