#!/bin/bash

if [ $# -lt 1 ] ; then
  echo "Usage: $0 TSV_FILE [...]"
  echo 
  echo "Add lexeme data from TSV file(s) to Omorfi lexicon and attribute files."
  echo "TSV data must be in same format as in the target files, i.e. first two fields"
  echo "define the base form and inflection class, and optional further fields"
  echo "define attributes in the form ATTRIBUTE=VALUE."
  echo
  exit 1
fi

BASEDIR=$(dirname $0)
LEXFILE="${BASEDIR}/lexemes/lexemes.tsv"
TEMPDIR="_tmp"

if [ -z "$2" ] ; then
  add_file="$1"
else
  add_file="___lexemes_being_added.tsv"
  cat $@ > $add_file
fi

if [ ! -d "$TEMPDIR" ] ; then
  mkdir $TEMPDIR
fi

attrs=(     prono           subcat        bound      origin part             \
  plt            pronu         prop           sem      style symbol         arg)
attr_names=(subcat          subcat        boundaries origin particle         \
  plt            stem-vowel    prop           sem      style symbol         argument)
attr_files=(pronoun-classes subcategories boundaries origin particle-classes \
  plurale-tantum pronunciation proper-classes semantic usage symbol-classes verb-arguments)

file_stub=${add_file##*/}
file_stub=$TEMPDIR/${file_stub/%.tsv}

add_lex_file=${file_stub}.lex.tsv

for (( i = 0 ; i < ${#attrs[@]} ; i++ )) ; do
  add_attr_file[$i]=${file_stub}.${attrs[$i]}.tsv
done

PRON_SUBCATS='adjective|demonstrative|interrogative|personal|quantor|reciprocal|reflexive|relative'

cut -f1,2 $add_file > $add_lex_file
sed -r -n "s/^([^\t]*\t[^\t]*).*(\tsubcat=(${PRON_SUBCATS})[^\t]*).*/\1\2/p" $add_file > ${add_attr_file[0]}
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tsubcat=[^\t]*).*/\1\2/p' $add_file | egrep -v 'subcat=(${PRON_SUBCATS})' > ${add_attr_file[1]}
for (( i = 2 ; i < ${#attrs[@]} ; i++ )) ; do
  sed -r -n "s/^([^\t]*\t[^\t]*).*(\t${attr_names[$i]}=[^\t]*).*/\1\2/p" $add_file > ${add_attr_file[$i]}
done

used_attrs=$(cut -f3- $add_file | tr '\t' '\n' | sed 's/=.*//g' | sort -u)
LEGAL_ATTRS="${attr_names[*]}"
LEGAL_ATTRS="${LEGAL_ATTRS// /|}|$PRON_SUBCATS"
illegals=$(echo "$used_attrs" | egrep -v -x "$LEGAL_ATTRS")
if [ -n "$illegals" ] ; then
  illegals="$(echo ${illegals} | tr '\n' ' ')"
  echo "WARNING: Ignoring unrecognized attribute(s): ${illegals}"
fi

lex_file="$LEXFILE"
for (( i = 0 ; i < ${#attrs[@]} ; i++ )) ; do
  attr_file[$i]="${BASEDIR}/attributes/${attr_files[$i]}.tsv"
done

function join_tsv_data() {
  src_file="$1"
  dest_file="$2"

  if [ ! -s $src_file ] ; then
    return
  fi
  cp -v ${dest_file} ${dest_file}~
  cat ${src_file} ${dest_file}~ | sort -k1,1 | LC_ALL=C uniq > ${dest_file}~~
  cp ${dest_file}~~ ${dest_file}
}

join_tsv_data $add_lex_file $lex_file
for (( i = 0 ; i < ${#attrs[@]} ; i++ )) ; do
  join_tsv_data ${add_attr_file[$i]} ${attr_file[$i]}
done

echo Abovementioned files were modified, old versions are still in ${LEXFILE}~ etc.
echo If all is fine, do commit the result immediately
