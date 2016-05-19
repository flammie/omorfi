---
layout: page
title: "Coverages"
category: stats
date: 2016-02-08 18:23:58
---


# Introduction #

This page contains semi-automatically run test results for omorfi. The results
have been achieved by running free corpora, such as Wikipedia, project
gutenberg ebooks, jrc-acquis, FinnTreeBank 3.1 and Turku Dependency Treebank.
The results are given for the _stable versions_ at the given date. The
tokenisation is not stable so some of the mistakes are often artifacts of
different tokenisation approaches, e.g., http may be a part of a URL.

* [2013-03-19](#2013-03-19)
* [2013-04-17](#2013-04-17)
* [2014-10-14](#2014-10-14)
* [2015-03-26](#2015-03-19-coverages)
* [2015-09-04](#2015-09-04-coverages)

These are in ascending order of time, since I just `>>` them to the end of this
file. For sheet view, see [omorfi progress sheet in google
 docs](https://docs.google.com/spreadsheets/d/1eTpUhCz0SzpRl3VYjuzI7etFB2N2bPrzyTV43ebYf6k/edit?usp=sharing)

# 2013-03-19 #

## fi-gutenberg ##

### Coverage ###

98.3300

## fiwiki ##

### Coverage ###

98.3500

# 2013-04-17 #

## fi-jrc-acquis ##

### Coverage ###

99.2900

## fi-gutenberg ##

### Coverage ###

98.3400

## fiwiki ##

### Coverage ###

98.3700

# 2013-08-29 #

(some regressions in tokenising...)

## fi-jrc-acquis ##

### Coverage ###

99.2900

## fi-gutenberg ##

### Coverage ###

98.2200

## fiwiki ##

### Coverage ###

98.2300

# 2014-10-14 #

## europarl-v7.fi-en.fi ##

### Coverage ###

Tokens: 37616193, misses: 420283
Token Coverage:98.8900 %
Unique tokens: 778361, misses: 105794
Type Coverage:86.4100 %

## fiwiki-latest-pages-articles ##

### Coverage ###

Tokens: 58057894, misses: 4849989
Token Coverage:91.6500 %
Unique tokens: 3228687, misses: 1267413
Type Coverage:60.7500 %

## ftb3.1 ##

### Coverage ###

Tokens: 25723770, misses: 897802
Token Coverage:96.5100 %
Unique tokens: 777899, misses: 216446
Type Coverage:72.1800 %

## gutenberg-fi ##

### Coverage ###

Tokens: 38654089, misses: 1410648
Token Coverage:96.3600 %
Unique tokens: 1467305, misses: 408654
Type Coverage:72.1500 %

## jrc-fi ##

### Coverage ###

Tokens: 47687901, misses: 3102494
Token Coverage:93.5000 %
Unique tokens: 1339272, misses: 543636
Type Coverage:59.4100 %

# 2015-03-26 coverages

## europarl-v7.fi-en.fi

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 338810 |  99.1000 % | 37616194 |
| Types   | 32593 | 95.8200 % | 778361 |

## fiwiki-latest-pages-articles

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 3926532 |  93.4700 % | 60129188 |
| Types   | 404763 | 87.7300 % | 3297519 |

## ftb3.1

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 2440935 |  96.8100 % | 76369439 |
| Types   | 205124 | 87.5600 % | 1648417 |

## gutenberg-fi

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 1288462 |  97.1600 % | 45368099 |
| Types   | 147351 | 90.9300 % | 1623042 |


## jrc-fi

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 2752471 |  94.2300 % | 47687902 |
| Types   | 229089 | 82.9000 % | 1339269 |

# 2015-09-04 coverages

## europarl-v7.fi-en.fi

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 336523 |  99.1100 % | 37616194 |
| Types   | 32438 | 95.8400 % | 778361 |

## fiwiki-latest-pages-articles

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 4180477 |  93.2600 % | 61976241 |
| Types   | 418540 | 87.6000 % | 3373292 |

## ftb3.1

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 2437369 |  96.8100 % | 76369439 |
| Types   | 204934 | 87.5700 % | 1648418 |

## gutenberg-fi

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 1435755 |  97.2300 % | 51666227 |
| Types   | 161772 | 90.8500 % | 1766877 |

## jrc-fi

| Feature | Missed | Coverage | All |
|:--------|-------:|---------:|----:|
| Tokens  | 2750893 |  94.2400 % | 47687902 |
| Types   | 229007 | 82.9100 % | 1339270 |

## 2016-05-19 coverages

### europarl-v7.fi-en.fi

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 37157275 |  99.2300 % | 37449133 |
| Types   | 684025 | 96.0700 % | 712019 |

### fi_ftb-ud-all

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 159257 |  99.4600 % | 160127 |
| Types   | 46465 | 99.3800 % | 46756 |

### fi-ud-all

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 179030 |  98.9000 % | 181022 |
| Types   | 52466 | 98.8100 % | 53103 |

### fiwiki-latest-pages-articles

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 93725546 |  92.3100 % | 101539475 |
| Types   | 3648070 | 83.2200 % | 4383679 |

### ftb3.1

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 74179981 |  97.1400 % | 76369439 |
| Types   | 1454752 | 88.2600 % | 1648418 |

### gutenberg-fi

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 58037774 |  97.2300 % | 59692254 |
| Types   | 1721477 | 89.9700 % | 1913489 |

### jrc-fi

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 43280036 |  95.0000 % | 45562643 |
| Types   | 1059219 | 83.7100 % | 1265450 |

### OpenSubtitles2016.fi

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 205563130 |  97.8900 % | 210005702 |
| Types   | 2037092 | 84.3900 % | 2414131 |

### tatoeba-fi

| Feature | Coverage # | Coverage % | All |
|:--------|-------:|---------:|----:|
| Tokens  | 442300 |  99.7700 % | 443346 |
| Types   | 49657 | 99.4200 % | 49947 |

