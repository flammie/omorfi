# Making releases a developers' documentation

Most stuff is quite predictable command line stuff if you know your autotools:

```console
$ $EDITOR configure.ac NEWS # fix at least vesrion numbers and fill in
$ make distcheck
$ ./configure --enable-big-tests
$ make clean
$ make
$ make check
$ make dist
$ cd docs
$ make update
$ doxygen
$ git add and commit all stuff
$ ./configure -/-enable-labeled-segments --enable-segmenter --enable-hyphenator
$ make omorfi-models-#<tabtab>
$ git push
```

Now you'll have to go to github and clicky on releases that is hidden in the
right hand panel at the moment. And there's a green button to draft new
release, create a new release tag that matches letter v plus version number.
Copypaste `NEWS` to release notes maybe add few words.

Go through all examples in [Usage examples](usage.html) from a fresh install.

## Python stuff

Many NLP researchers prefer python only environments so we support limitedly
pip and conda. Which need to be updated separately.

```console
$ cd src/python
$ $EDITOR pyproject.toml setup.cfg setup.py  # bump versions
$ python -m build
$ python -m twine upload dist/*
```

You'll need omorfi's pypi write token in `~/.pypirc`, if that is not in place
you can go to pypi.org and generate a new one and delete old ones or look
for the backup.

Conda is of course so badly made that it is uninstallable with linux package
managers or if you have non-empty `PYTHONPATH`, perhaps only bearable way to
use conda enough to make a package is to use docker:

```console
$ docker pull continuumio/miniconda3
$ docker run -i -t continuumio/miniconda3 /bin/bash
$ conda install conda-build
$ conda skeleton pypi omorfi -o omorfi-conda
  # also c/p omorfi/meta.yaml to omorfi github src/python/meta.yamö
  # especially at least version and checksums
$ conda-build omorfi
$ conda convert -f --platform all FILENAME # fill in package filename here
$ conda install anaconda-client
$ anaconda login
$ anaconda upload omorfi-conda/linux-32/omorfi-0.9.9-py39_0.tar.bz2
$ anaconda upload omorfi-conda/.../
```

You need to `anaconda upload` some twenty packages for all OSes.


