# Installing omorfi

The NLP analysers / language models are based on finite-state automata
technology and require some special tools to be installed before compilation and
use.

## Downloading

Choose one:

1. [Download a release tarball from
 github](https://github.com/flammie/omorfi/releases)
    wget https://github.com/flammie/omorfi/releases/download/20200511/omorfi-20200511.tar.xz
    tar Jxvf omorfi-2020511.tar.xz
1. or [clone
the bleeding edge version with git](https://github.com/flammie/omorfi/)
    git clone git@github.com:flammie/omorfi

## Dependencies

Required for compilation and use:

* **hfst-3.15** or greater,
* **python-3.5** or greater,
* **libhfst-python**,
* **C++** compiler (gcc or clang)
* **libtool**
* **autoconf-2.64**
* **automake-1.12**
* **pkg-config** (or pkgconf)

Optionally:

* VISL CG 3
* hfst-ospell
* java

Choose only one of the methods of installing dependencies!

### Option 1) Installing dependencies on Debian / Ubuntu / Redhat or compatible

It is recommended to follow the [Installing grammar
libraries](https://wiki.apertium.org/wiki/Installation_of_grammar_libraries)
instructions provided by apertium project. In summary:

```
wget http://apertium.projectjj.com/apt/install-nightly.sh -O - | sudo bash
sudo apt-get install hfst python3-hfst libhfst-dev cg3
```

But also check the apertium wiki for updates e.g. if the package names may
change.

### Option 2a) Installing everything with pip or conda (python only)

Omorfi has preliminary python packaging on pip, it can be used to install
some of the relevant dependencies and run parts of omorfi without installing
extra software. This installation lacks tools like spell-checking and
correction or morphological disambiguation, which require non-python
dependencies not found in pip repositories.

```
pip install omorfi
```

### Option 2b) Installing with anaconda (python only)

Omorfi has preliminary python pacakging on anaconda, it can be used to install
some of the relevant dependencies and run parts of omorfi without installing
extra software. This installation lacks tools like spell-checking and correction
or morphological disambiguation, which require non-python dependencies not found
in anaconda repositories.

![Anaconda](https://anaconda.org/flammie/omorfi/badges/installer/conda.svg)

### Option 3) Installing dependencies on other systems

Follow the instructions by [HFST](https://hfst.github.io) and [VISL CG
3](https://visl.sdu.dk/cg3.html) projects.

## Installing omorfi

Choose only one of the methods of installing omorfi language models!

### Option 1) Using stable omorfi without full compilation

It is possible to download pre-compiled omorfi models and use them without going
through the compilation process. If you have downloaded and installed all the
dependencies, you can run the configuration script:

```
./configure
```

To check that all necessary tools are installed and usable, it also sets up some
details of the convenience scripts. Then:

```
omorfi-download.bash
```

found in `src/bash` folder will fetch the language models.

Note that if you downloaded pip version, you can only use:

```
omorfi-download.py
```

instead of the bash version.

If the downloading worked you can proceed to [usage examples](usage.html). Be
aware that some of the examples may not work depending on which depdendencies
you installed and version downloaded.

### Option 2) Compiling omorfi

Installation uses standard autotools system (see the contents of
[INSTALL](https://github.com/flammie/omorfi/blob/develop/INSTALL) from GNU
project if you are not familiar):

```
./configure && make && make install
```

The compiling may take minutes to hours, depending on the hardware and settings
used. You should be prepared with at least 4 gigs of RAM, however, it is
possible to compile a limited vocabulary system with less. This is a limitation
of the HFST system used to compile the language models, and it is only present
at compile time, the final models use perhaps up to hundreds of megabytes in
memory.

If you did not install HFST from package manager, you may need to adjust
ocnfigurations:

```
./configure --with-hfst=${HFSTPATH}
```

Autotools system supports installation to e.g. home directory:

```
./configure --prefix=${HOME}
```

With git version you must create the necessary autotools files in the host
system once, after initial checkout:

```
./autogen.sh
```

There are a number of options that you can pass to `configure` script. The
default configuration leaves lots of features out to speed up the process,
for a full listing:

```
./configure --help
```

Some of the features that build more automata double the time required to
compile and the space used by the automata (approximately). Some features are
to enable or disable the API bindings for Java or other languages. The
`configure` script displays the current setup in the end:

```
* Analysers: yes
    * OMOR yes (flags: --omor-props   --omor-sem)
    * FTB3.1 no
    * apertium no
    * giella: no
    * labeled segmenter: no
* Limits:
    * tiny lexicons:
    * big tests:
* Applications
    * Voikko speller: yes
    * segmenter: no
    * lemmatiser: no
    * hyphenators: no
* Clusters
    * run tests on PBS cluster: false → mailto: no
    * run tests on SLURM cluster: false → mailto: no
```

If you have ran `configure`, `make` and `make install`, you can carry on to
[usage examples](usage.html).
