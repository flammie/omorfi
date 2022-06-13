# Omorfi release policy (and citing)

Omorfi gets updated sporadically, depending on my spare time (and the amount of
contributions I get via github sponsors and patreon j/k ;-). Please cite omorfi
if you use it in an academic context, for details see [omorfi
publications](articles.html).

# Stable releases

Releases are considered stable when they fill following criteria:

1. No regressions in naive coverage over main corpora (c.f.
   [statistics](statistics.html)
1. No regressions in recall over corpora: UD, FTB-3, unimorph
1. Passes `make distcheck`
1. spell-checker installation works with voikko, enchant
1. pip installation works in virtual env.

IF you are interested in these criteria please see [making
releases](making-release.html), it's a check-list I wrote for myself on how
to check release-readiness.

If you have further requirements for stability, please submit an automated test
case that can be run using the command `make check` or `make distcheck` during
the release process. For examples, see `test/ftb-test.py`,
`test/europarl-coverage.sh`, etc. *Anything that is not covered by an automated
test case that is ran by `make check` may and will change between releases. If
you rely on a feature, annotation or other stuff, create your test case asap.*

# Releases tagged in git

Each stable release is tagged in git. The version numbers 2015–2020 are dates
in YYYYMMDD format. Versions after 2022 are tagged with [semantic
versioning](https://semver.org) strategy.

# Unstable / development versions

Development is carried on github's version control system, you can always find
the latest and greatest by cloning the git repo and building it from there.
Follow the instructions on the front page or google for git(hub) tutorial.
Read the ReadMe. Here's an example:

```
git clone https://github.com/flammie/omorfi.git
cd omorfi
less README.md
[follow instructions]
autoreconf -i && ./configure && make && make check
```

When citing a development version, try to include the versioning system info in
some footnote, e.g. a git hash.

# Releases before 2014 (GoogleCode, GNA, CVS at Uni. Helsinki...)

**This is for seriously outdated versions, for reproducibility.**

The release 20130829 available in the hidden Downloads section from before
**Google discontinued downloads** does no longer work out of the box with
current HFST. I (Flammie) got it installed using following procedure:

```
make clean
for f in src/morphology/roots/*.lexc; do sed -i -e 's/^\([^:]*[^%]\) \(.*:\)/\1% \2/' $f; done
for f in src/morphology/roots/*.lexc; do sed -i -e 's/^\([^:]*[^%]\) \(.*:\)/\1% \2/' $f; done
for f in src/morphology/roots/*.lexc; do sed -i -e 's/^\([^:]*[^%]\) \(.*:\)/\1% \2/' $f; done
make
```

The reason for this is that previous versions `hfst-lexc` may have been more
lenient towards unescaped white-space, all cases of ' ' in lexicons need to be
replaced with '% '.

The installed scripts refer to wrong automata. The easiest way to fix this is
to download patch from
[r04c4e27b551a](https://code.google.com/p/omorfi/source/detail?r=04c4e27b551a2bdef8cdc91e97b2c4b3a79f7d3b)
or going to git clone and creating patch using commands:

```
git clone https://code.google.com/p/omorfi/
cd omorfi
git format-patch -1 04c4e27b551a
cd ../omorfi-20130829/
mv ../omorfi/0001-Use-configured-format-to-refer-to-automaton.patch .
patch -p1 < 0001-Use-configured-format-to-refer-to-automaton.patch
./configure
make
(sudo) make install
```

Another possibility is to switch back to the outdated, omor style tagging. This
was also broken at that time with missing distribution files. This can be
worked around:

```
for f in src/morphology/hacks/*.lexc ; do cp -v $f ${f/-ftb3/} ; done
```

The resulting tagging will be off for hacks but it's usable.

For analysis and generation only, you may also download the automaton binary.
