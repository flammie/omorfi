---
layout: page
title: Omorfi troubleshooting
---
# Troubleshooting omorfi

Omorfi is not a bug-free software. These are the issues that have been reported
to us so far. Some of them may not apply to current versions of omorfi but they
are kept here for completeness.

## hfst-lexc: Unknown option

This may happen when compiling the system with make:

```
hfst-lexc --Werror -o generated/omorfi-ftb3.lexc.hfst generated/omorfi-ftb3.lexc
Try ``/usr/local/bin/hfst-lexc --help'' for more information.
/usr/local/bin/hfst-lexc: Unknown option
```

It means your hfst-lexc is too old. You need at least version 3.8 to handle
`--Werror` switch. You can workaround by removing `--Werror` from
`src/Makefile.am`, although this is not recommended, as the newer versions of
HFST have provided this option to ensure the data is not broken.

The same problem may re-appear with the --alignStrings option.

## ImportError (or other Python problems)

E.g. error message of form:

```
ImportError: No module named 'omorfi'
```

In order for python scripts to work you need to install them to same prefix as
python, or define PYTHONPATH, e.g.:

```
$ PYTHONPATH=/usr/local/lib/python3.4/site-packages/ omorfi-disambiguate-text.sh kalevala.txt
```

The scripts require *python3* as the system python, in case I forget to
set the whole shebang right. You can work around this by, e.g.,:

```
python3 $(which omorfi-analyse.py )
```

This should not affect release versions but keep in mind if you are using a
python2-based system and development versions.

## Missing FILENAME

When omorfi files are not where bash scripts are looking for them.

If you have moved your installation manually after make install, you may need to
modify paths in omorfi.bash or set environment variable OMORFI_PATH.

If the file missing is `omorfi.cg3bin`, it may mean that the vislcg3 was missing
at the time of the installation. Similarly may happen with omorfi-speller.zhfst,
it will only be created when hfst-ospell and it's dependencies and zip are all
available.

## Processing text gets stuck / takes long

Occasionally some tokens yield very complicated analyses and take a lot of
memory or time. This happens especially with long strings that can be analysed
as combinations of interjections like ahahaha...ha (in theory, each ah, aha, ha
and hah within the string are ambiguous wrt. compounding), while current
versions have blacklisted most such combinations some may still exist. When
using hfst tools directly this can be solved using `-t` option to set the
timeout. While these workarounds will slowly trickle to all parts of HFST and
omorfi, it is often a good idea to pre-process text to remove or normalise
offending strings as they will trip other NLP tools too.

Some operations of omorfi legitly take a lot of memory, and most tools are
suspectible to memory leaks. It may be often beneficial to `split` your data
and process it in smaller chunks.

## Make gets killed

Compiling omorfi takes some memory, of course it is over 10 megabytes of words
that need to be expanded and processed in a number of ways, it can momentarily
take up more than 2 or 4 gigabytes of memory. If you have that or less RAM,
depending on your setup it may either slow down the computer a lot, or just
cause compilation to fail. The error  message in that case will usually only
read something like:

```
make[2]: Verzeichnis „/home/tpirinen/github/flammie/omorfi/src“ wird betreten
/usr/bin/hfst-lexc  --alignStrings --Werror -o generated/omorfi.accept.lexc.hfst generated/omorfi.accept.lexc
/usr/bin/hfst-lexc: warning: Defaulting to OpenFst tropical type
...  Getötet
make[2]: *** [generated/omorfi.lexc.hfst] Killed
```

it all depends on versions of make and language settings, but in general most of
the time it will say at least "killed" and usually nothing more as an error message
near the end. Current versions of omorfi support compiling a limited-size version with
high-quality dictionaries only, using `./configure --enable-small-lexicons` option.
If this works but normal compilation doesn't, you may need to acquire more RAM or
tweak some memory-related settings.

## Configure hangs infinitely when testing for java on Mac OS X

I hear that the java test hangs on some Mac OS X versions of some java
implementations. It may be fixable by some interrupt, but you can also
work around by commenting the lines `AX_PROG_JAVA` and `AX_CHECK_CLASS` out in
the `configure.ac` and running `autogen.sh`. You may also want to change the
`AM_CONDITIONAL(CAN_JAVA, ...)` into `AM_CONDITIONAL(CAN_JAVA, false)` so the
java bindings won't be tried.

