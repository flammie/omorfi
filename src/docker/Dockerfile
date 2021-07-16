# Minimal dockerfile to run omorfi

FROM ubuntu:latest
MAINTAINER Flammie A Pirinen <flammie@iki.fi>

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential automake autoconf git wget lsb-release libtool zip pkg-config &&\
    wget http://apertium.projectjj.com/apt/install-nightly.sh -O - | bash && \
    DEBIAN_FRONTEND=noninteractive  apt-get install python3-hfst libhfst-dev cg3 -y && \
    git clone https://github.com/flammie/omorfi && \
    cd omorfi && \ 
    ./autogen.sh && \
    ./configure && \
    make

