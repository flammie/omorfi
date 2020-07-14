# Installing omorfi

The NLP analysers / language models are based on finite-state automata
technology and require some special tools to be installed before use.


## Dependencies

Required for compilation and use:

* **hfst-3.15** or greater,
* **python-3.5** or greater,
* **libhfst-python**,
* **C++** compiler and **libtool**
* GNU **autoconf-2.64**, **automake-1.12**; compatible **pkg-config**
  implementation

Optionally:

* VISL CG 3
* hfst-ospell
* java

### Installing dependencies on Debian / Ubuntu or compatible

It is recommended to follow [instructions by Apertium
project](http://wiki.apertium.org/wiki/Install_Apertium_core_using_packaging).

### Installing dependencies on other systems

Follow the instructions by [HFST](https://hfst.github.io) and [VISL CG
3](https://visl.sdu.dk/cg3.html) projects.

## Compiling omorfi

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


