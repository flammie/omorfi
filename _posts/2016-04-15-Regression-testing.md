---
layout: page
title: "Regression testing"
category: design
date: 2016-04-15 16:41:24
---


# Omorfi testing

A large and old project like omorfi needs a lot of testing and consistency
checking to be useful for all end users of a morphological database. This
document describes the testing done.

## Automatic testing

Will be detailed later. In typical setup, a simple `make check` will invoke
the test suite.

## Manually testing for regressions

For each release, we must check the changes manually as well as having
automatic checkers and continuous integration do their job. For many linguistic
tasks as well as statistical modeling of language a certain kind of stability
of the analyses is of utmost importance so every change in coverage and tagging
must be verified by a real human.

### Preparations

Assuming you have repositories in current directory and omorfi master cloned in
and configured omorfi:

``` bash
cd omorfi/
make
cd test
bash get-covered.bash
make check
cd ../..
wget omorfi-20150904.tar.xz
tar Jxvf ~/Downloads/omorfi-20150904.tar.xz 
cd omorfi-20150904/
./configure
make
cd test/
for f in /home/tpirinen/Koodit/omorfi/test/*.uniq.freqs ; do
    ln -s $f . -v ;
done
for f in /home/tpirinen/Koodit/omorfi/test/*.tokens ; do
    ln -s $f . -v ;
done
for f in /home/tpirinen/Koodit/omorfi/test/*.text ; do
    ln -s $f . -v ;
 done
for f in /home/tpirinen/Koodit/omorfi/test/*.conllu ;
    do ln -s $f . -v ;
done
cd ..
cp ../omorfi/test/*.py test/
make check
```

### Python-based checks

``` bash
cd omorfi
cd test/
python3 regress-coveragelogs.py -c $(pwd) \
    -r ../../omorfi-20150904/test/ --log regresslog
less regresslog
```

### Bash-based checks

The python script is not very good with some things, it doesn't recognise sort
order of non-latin very well. We also use unix tool comm to glance at the
regressions and developments like so:

``` bash
sort europarl-v7.fi-en.fi.coveragelog > europarl-v7.fi-en.fi.coveragelog.sorted
sort ../../omorfi-20150904/test/europarl-v7.fi-en.fi.coveragelog >\
   europarl-v7.fi-en.fi.coveragelog.20150904.sorted
# regressions
comm -23 europarl-v7.fi-en.fi.coveragelog.sorted \
    europarl-v7.fi-en.fi.coveragelog.20150904.sorted | less
# developments and additions
comm -13 europarl-v7.fi-en.fi.coveragelog.sorted \
    europarl-v7.fi-en.fi.coveragelog.20150904.sorted | less
# stable misses
comm -12 europarl-v7.fi-en.fi.coveragelog.sorted \
    europarl-v7.fi-en.fi.coveragelog.20150904.sorted | less
```

This is somewhat packaged to a parallel script called: 
`regress-coveragelogs.bash`.

