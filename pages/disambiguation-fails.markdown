---
title: Disamgiguation fails (funny)
layout: page
---

# Disambiguation fails

This is just a hand-written list of funny Finnish ambiguities we have found during manual annotation work.

## kuulumiset

Ambiguity of:

1. kuuluminen, noun (typically plurale tantum but not exclusively): lit. hearings, e.g. gossip and small-talk
1. kuu+luminen, noun and adjective: moon, snowy

From fi-ud-dev: *Oliko nyt muuten tarpeeksi höpötystä ja _kuulumisia_?:)* =

1. was there btw enough gossipping and reminiscing?
1. Was there btw enough gossipping and snowy moons?

```
"<kuulumisia>"
	"kuulumiset" NOUN PL PAR <W=0> <CMP=1> SELECT:83:least-compounds            ; reminicings
;	"kuulua" VERB <DRV_MINEN> PL PAR <W=0> <CMP=1> REMOVE:82:least-derivations  ; to hear
;	"kuu#luminen" ADJ POS PL PAR <W=0> <CMP=2> SELECT:83:least-compounds        ; snowy moon
```



## hienosto

1. hienosto, noun: affluent, well-of (of areas etc.)
1. hien+osto, noun (singular genitive) + noun: sweat's buying
1. hie+nosto, noun (singular genitive) + noun: polished stuff's lift-up (hie is ~rare result derivation of hioa: to polish, sharpen)

Also from fi-ud-dev: *Komisario Palmu ratkoi murhia Helsingin idyllisissä hienostokaupunginosissa.* = 

1. (Officer Palmu solved murders) in idyllic nice parts of Helsinki (Komisario Palmu is a popular crime novel series)
1. ... in idyllic sweat shopping parts of Helsinki
1. ... in idyllic polished stuff lifting parts of Helsinki

```
	"hienosto#kaupunginosa" NOUN PL INE <W=0> <CMP=2> SELECT:83:least-compounds
;	"hie#nosto#kaupunginosa" NOUN PL INE <W=0> <CMP=3> SELECT:83:least-compounds
;	"hie#nosto#kaupunki#osa" NOUN PL INE <W=0> <CMP=4> SELECT:83:least-compounds
;	"hienosto#kaupunki#osa" NOUN PL INE <W=0> <CMP=3> SELECT:83:least-compounds
;	"hiki#osto#kaupunginosa" NOUN PL INE <W=0> <CMP=3> SELECT:83:least-compounds
;	"hiki#osto#kaupunki#osa" NOUN PL INE <W=0> <CMP=4> SELECT:83:least-compounds
```
