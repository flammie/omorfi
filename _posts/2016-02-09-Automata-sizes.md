---
layout: page
title: "Automata sizes"
category: stats
date: 2016-02-08 18:23:58
---


# Automata sizes

While automata sizes are dependent on the underlying enginery, some changes in
dictionary structures and implementations can greatly affect the sizes and thus
efficiency of the stuff. This page shows automated test results of that for
omorfi releases.


# Automated size tests

These are in ascending order of time, since I just `>>` them to the end of this
file. For sheet view, see [omorfi progress sheet in google
 docs](https://docs.google.com/spreadsheets/d/1eTpUhCz0SzpRl3VYjuzI7etFB2N2bPrzyTV43ebYf6k/edit?usp=sharing)

## 2014-04-01 (manual tests)

### ../src/dictionary.default.hfst sizes

| *Feature* | *Value* |
|:----------|--------:|
| file size | 52M |
| states |  652713 |
| arcs |  2893005 |
| average arcs per state |  4.432277 |
| average input epsilons per state |  0.417595 |
| average input ambiguity |  1.095717 |
| average output ambiguity |  1.095717 |

### ../src/generation.ftb3.hfst sizes

| *Feature* | *Value* |
|:----------|--------:|
| file size | 69M |
| states |  652713 |
| arcs |  2893005 |
| average arcs per state |  4.432277 |
| average input epsilons per state |  0.326942 |
| average input ambiguity |  2.024982 |
| average output ambiguity |  1.095717 |

### ../src/lemmatize.default.hfst sizes

| *Feature* | *Value* |
|:----------|--------:|
| file size | 52M |
| states |  652713 |
| arcs |  2893005 |
| average arcs per state |  4.432277 |
| average input epsilons per state |  0.417595 |
| average input ambiguity |  1.095717 |
| average output ambiguity |  2.024982 |

### ../src/morphology.ftb3.hfst sizes

| *Feature* | *Value* |
|:----------|--------:|
| file size | 88M |
| states |  652713 |
| arcs |  2893005 |
| average arcs per state |  4.432277 |
| average input epsilons per state |  0.417595 |
| average input ambiguity |  1.095717 |
| average output ambiguity |  2.024982 |

## 2015-03-26 sizes

### ../src/generated/omorfi-omor.analyse.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 27M |
| states |  442094 |
| arcs |  955017 |
| average arcs per state |  2.160213 |
| average input epsilons per state |  0.336906 |
| average input ambiguity |  1.125475 |
| average output ambiguity |  1.087680 |

### ../src/generated/omorfi-omor.generate.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 36M |
| states |  442192 |
| arcs |  937498 |
| average arcs per state |  2.120115 |
| average input epsilons per state |  0.072903 |
| average input ambiguity |  1.069566 |
| average output ambiguity |  1.128215 |

### ../src/generated/omorfi-omor.lexc.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 20M |
| states |  441660 |
| arcs |  929726 |
| average arcs per state |  2.105072 |
| average input epsilons per state |  0.065209 |
| average input ambiguity |  1.064512 |
| average output ambiguity |  1.121208 |

### ../src/generated/omorfi-ftb3.analyse.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 50M |
| states |  431164 |
| arcs |  1692833 |
| average arcs per state |  3.926193 |
| average input epsilons per state |  0.541446 |
| average input ambiguity |  1.201040 |
| average output ambiguity |  1.342586 |

### ../src/generated/omorfi-ftb3.generate.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 36M |
| states |  452122 |
| arcs |  1005093 |
| average arcs per state |  2.223057 |
| average input epsilons per state |  0.046505 |
| average input ambiguity |  1.087878 |
| average output ambiguity |  1.100758 |

### ../src/generated/omorfi-ftb3.lexc.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 20M |
| states |  451709 |
| arcs |  935372 |
| average arcs per state |  2.070740 |
| average input epsilons per state |  0.038926 |
| average input ambiguity |  1.016209 |
| average output ambiguity |  1.060113 |

### ../src/generated/omorfi.accept.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 31M |
| states |  431164 |
| arcs |  1692833 |
| average arcs per state |  3.926193 |
| average input epsilons per state |  0.541446 |
| average input ambiguity |  1.201040 |
| average output ambiguity |  1.201040 |

### ../src/generated/omorfi.lemmatise.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 50M |
| states |  431164 |
| arcs |  1692833 |
| average arcs per state |  3.926193 |
| average input epsilons per state |  0.541446 |
| average input ambiguity |  1.201040 |
| average output ambiguity |  1.372894 |

### ../src/generated/omorfi.segment.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 28M |
| states |  394347 |
| arcs |  911855 |
| average arcs per state |  2.312316 |
| average input epsilons per state |  0.215173 |
| average input ambiguity |  1.011387 |
| average output ambiguity |  1.027478 |

### ../src/generated/omorfi.tokenise.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 21K |
| states |  18 |
| arcs |  1078 |
| average arcs per state |  59.888889 |
| average input epsilons per state |  0.888889 |
| average input ambiguity |  1.000000 |
| average output ambiguity |  1.001859 |


## 2015-09-04 sizes

### ../src/generated/omorfi-omor.analyse.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 22M |
| states |  442471 |
| arcs |  953519 |
| average arcs per state |  2.154986 |
| average input epsilons per state |  0.337575 |
| average input ambiguity |  1.125778 |
| average output ambiguity |  1.085401 |

### ../src/generated/omorfi-omor.generate.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 22M |
| states |  442552 |
| arcs |  936005 |
| average arcs per state |  2.115017 |
| average input epsilons per state |  0.068790 |
| average input ambiguity |  1.067308 |
| average output ambiguity |  1.128531 |

### ../src/generated/omorfi-omor.lexc.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 20M |
| states |  442028 |
| arcs |  930242 |
| average arcs per state |  2.104487 |
| average input epsilons per state |  0.064976 |
| average input ambiguity |  1.064522 |
| average output ambiguity |  1.121211 |

### ../src/generated/omorfi-ftb3.analyse.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 35M |
| states |  431151 |
| arcs |  1635723 |
| average arcs per state |  3.793852 |
| average input epsilons per state |  0.541439 |
| average input ambiguity |  1.192366 |
| average output ambiguity |  1.297094 |

### ../src/generated/omorfi-ftb3.generate.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 23M |
| states |  452112 |
| arcs |  972277 |
| average arcs per state |  2.150522 |
| average input epsilons per state |  0.042733 |
| average input ambiguity |  1.052337 |
| average output ambiguity |  1.085213 |

### ../src/generated/omorfi-ftb3.lexc.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 20M |
| states |  451705 |
| arcs |  935438 |
| average arcs per state |  2.070905 |
| average input epsilons per state |  0.038946 |
| average input ambiguity |  1.016213 |
| average output ambiguity |  1.060144 |

### ../src/generated/omorfi.accept.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 185M |
| states |  535827 |
| arcs |  8682596 |
| average arcs per state |  16.204103 |
| average input epsilons per state |  0.000000 |
| average input ambiguity |  1.103236 |
| average output ambiguity |  1.103236 |

### ../src/generated/omorfi.lemmatise.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 35M |
| states |  431151 |
| arcs |  1635723 |
| average arcs per state |  3.793852 |
| average input epsilons per state |  0.541439 |
| average input ambiguity |  1.192366 |
| average output ambiguity |  1.326331 |

### ../src/generated/omorfi.segment.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 22M |
| states |  394463 |
| arcs |  910218 |
| average arcs per state |  2.307486 |
| average input epsilons per state |  0.215300 |
| average input ambiguity |  1.011443 |
| average output ambiguity |  1.025282 |

### ../src/generated/omorfi.tokenise.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 22K |
| states |  18 |
| arcs |  1078 |
| average arcs per state |  59.888889 |
| average input epsilons per state |  0.888889 |
| average input ambiguity |  1.000000 |
| average output ambiguity |  1.001859 |


## 2016-05-19 sizes

### ../src/generated/omorfi-omor.analyse.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 22M |
| states |  457883 |
| arcs |  974299 |
| average arcs per state |  2.127834 |
| average input epsilons per state |  0.340871 |
| average input ambiguity |  1.125085 |
| average output ambiguity |  1.083649 |

### ../src/generated/omorfi-omor.generate.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 22M |
| states |  457715 |
| arcs |  955684 |
| average arcs per state |  2.087946 |
| average input epsilons per state |  0.068798 |
| average input ambiguity |  1.065164 |
| average output ambiguity |  1.127683 |

### ../src/generated/omorfi-omor.lexc.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 20M |
| states |  457467 |
| arcs |  951728 |
| average arcs per state |  2.080430 |
| average input epsilons per state |  0.065095 |
| average input ambiguity |  1.062566 |
| average output ambiguity |  1.120789 |

### ../src/generated/omorfi-ftb3.analyse.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 54M |
| states |  797956 |
| arcs |  2410789 |
| average arcs per state |  3.021205 |
| average input epsilons per state |  0.357513 |
| average input ambiguity |  1.124715 |
| average output ambiguity |  1.328092 |

### ../src/generated/omorfi-ftb3.generate.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 23M |
| states |  452342 |
| arcs |  974929 |
| average arcs per state |  2.155292 |
| average input epsilons per state |  0.044327 |
| average input ambiguity |  1.052407 |
| average output ambiguity |  1.086378 |

### ../src/generated/omorfi-ftb3.lexc.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 20M |
| states |  452148 |
| arcs |  940321 |
| average arcs per state |  2.079675 |
| average input epsilons per state |  0.040558 |
| average input ambiguity |  1.016653 |
| average output ambiguity |  1.062322 |

### ../src/generated/omorfi.accept.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 44M |
| states |  459328 |
| arcs |  1900510 |
| average arcs per state |  4.137588 |
| average input epsilons per state |  0.057913 |
| average input ambiguity |  1.022871 |
| average output ambiguity |  1.014195 |

### ../src/generated/omorfi.lemmatise.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size |  |

### ../src/generated/omorfi.segment.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size |  |

### ../src/generated/omorfi.tokenise.hfst 

| *Feature* | *Value* |
|:----------|--------:|
| file size | 22K |
| states |  18 |
| arcs |  1078 |
| average arcs per state |  59.888889 |
| average input epsilons per state |  0.888889 |
| average input ambiguity |  1.000000 |
| average output ambiguity |  1.001859 |

