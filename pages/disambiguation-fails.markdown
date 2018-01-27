---
title: Disamgiguation fails (funny)
layout: page
---

# Disambiguation fails

This is just a hand-written list of funny Finnish ambiguities we have found during manual annotation work.

## kuulumiset

From fi-ud-dev: *Oliko nyt muuten tarpeeksi höpötystä ja _kuulumisia_?:)* = was there btw enough gossipping and reminiscing?

```
"<kuulumisia>"
	"kuulumiset" NOUN PL PAR <W=0> <CMP=1> SELECT:83:least-compounds            ; reminicings
;	"kuulua" VERB <DRV_MINEN> PL PAR <W=0> <CMP=1> REMOVE:82:least-derivations  ; to hear
;	"kuu#luminen" ADJ POS PL PAR <W=0> <CMP=2> SELECT:83:least-compounds        ; snowy moon
```

Was there btw enough gossipping and snowy moons?

