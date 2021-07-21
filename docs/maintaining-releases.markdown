# Developer's guide to omorfi

Some useful snippets for maintaining omorfi.

## Pypi packaging

## Anaconda packaging

Based on 
<https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html>

```
$ docker run -i -t continuumio/miniconda3 /bin/bash
# conda install conda-build
# conda skeleton pypi omorfi
# conda config --add channels apertium
# conda-build omorfi
# conda install --use-local omorfi
# conda convert --platform all /opt/conda/conda-bld/linux-64/omorfi-0.0.2-py38_0.tar.bz2 
# conda install anaconda-client
# anaconda login
# anaconda upload /opt/conda/conda-bld/linux-64/omorfi-0.0.2-py38_0.tar.bz2 
# for d in linux-32 linux-aarch64 linux-armv6l linux-armv7l linux-ppc64 \
      linux-ppc64le linux-s390x osx-64 osx-arm64 win-32 win-64 ; do \
    anaconda upload $d/omorfi-0.0.2-py38_0.tar.bz2 ; \
done
```

