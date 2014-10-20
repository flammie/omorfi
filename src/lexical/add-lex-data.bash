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

file_stub=${add_file##*/}
file_stub=$TEMPDIR/${file_stub/%.tsv}
add_lex_file=${file_stub}.lex.tsv
add_bound_file=${file_stub}.bound.tsv
add_origin_file=${file_stub}.origin.tsv
add_part_file=${file_stub}.part.tsv
add_plt_file=${file_stub}.plt.tsv
add_prono_file=${file_stub}.prono.tsv
add_pronu_file=${file_stub}.pronu.tsv
add_prop_file=${file_stub}.prop.tsv
add_sem_file=${file_stub}.sem.tsv
add_style_file=${file_stub}.style.tsv
add_subcat_file=${file_stub}.subcat.tsv
add_symbol_file=${file_stub}.symbol.tsv
add_arg_file=${file_stub}.arg.tsv

PRON_SUBCATS='adjective|demonstrative|interrogative|personal|quantor|reciprocal|reflexive|relative'

cut -f1,2 $add_file > $add_lex_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tboundaries=[^\t]*).*/\1\2/p' $add_file > $add_bound_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\torigin=[^\t]*).*/\1\2/p' $add_file > $add_origin_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tparticle=[^\t]*).*/\1\2/p' $add_file > $add_part_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tplt=[^\t]*).*/\1\2/p' $add_file > $add_plt_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tstem-vowel=[^\t]*).*/\1\2/p' $add_file > $add_pronu_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tprop=[^\t]*).*/\1\2/p' $add_file > $add_prop_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tsem=[^\t]*).*/\1\2/p' $add_file > $add_sem_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tsymbol=[^\t]*).*/\1\2/p' $add_file > $add_symbol_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tstyle=[^\t]*).*/\1\2/p' $add_file > $add_style_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\targument=[^\t]*).*/\1\2/p' $add_file > $add_arg_file
sed -r -n "s/^([^\t]*\t[^\t]*).*(\tsubcat=(${PRON_SUBCATS})[^\t]*).*/\1\2/p" $add_file > $add_prono_file
sed -r -n 's/^([^\t]*\t[^\t]*).*(\tsubcat=[^\t]*).*/\1\2/p' $add_file | egrep -v 'subcat=(${PRON_SUBCATS})' > $add_subcat_file

lex_file="$LEXFILE"
bound_file="${BASEDIR}/attributes/boundaries.tsv"
origin_file="${BASEDIR}/attributes/origin.tsv"
part_file="${BASEDIR}/attributes/particle-classes.tsv"
plt_file="${BASEDIR}/attributes/plurale-tantum.tsv"
prono_file="${BASEDIR}/attributes/pronoun-classes.tsv"
pronu_file="${BASEDIR}/attributes/pronunciation.tsv"
prop_file="${BASEDIR}/attributes/proper-classes.tsv"
sem_file="${BASEDIR}/attributes/semantic.tsv"
subcat_file="${BASEDIR}/attributes/subcategories.tsv"
symbol_file="${BASEDIR}/attributes/symbol-classes.tsv"
style_file="${BASEDIR}/attributes/usage.tsv"
arg_file="${BASEDIR}/attributes/verb-arguments.tsv"


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
join_tsv_data $add_bound_file $bound_file
join_tsv_data $add_origin_file $origin_file
join_tsv_data $add_part_file $part_file
join_tsv_data $add_plt_file $plt_file
join_tsv_data $add_prono_file $prono_file
join_tsv_data $add_pronu_file $pronu_file
join_tsv_data $add_prop_file $prop_file
join_tsv_data $add_sem_file $sem_file
join_tsv_data $add_subcat_file $subcat_file
join_tsv_data $add_symbol_file $symbol_file
join_tsv_data $add_style_file $style_file
join_tsv_data $add_arg_file $arg_file

echo Abovementioned files were modified, old versions are still in ${LEXFILE}~ etc.
echo If all is fine, do commit the result immediately
