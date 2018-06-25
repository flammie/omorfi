## Process this file with automake to produce Makefile.in

dist_man1_MANS=omorfi-analyse-text.1 omorfi-hyphenate.1 omorfi-generate.1\
			   omorfi-spell.1 omorfi-analyse-tokenised.1 omorfi-segment.1\
			   omorfi-factorise.1 omorfi-conllu.1 omorfi-disambiguate-text.1 \
			   omorfi-tokenise.1 omorfi-vislcg.1 omorfi-freq-evals.1 \
			   omorfi-lookup.1

%.1:
	help2man -s 1 -o $@ -N -S OMORFI `echo $@ | sed 's/.1/.sh/'`

