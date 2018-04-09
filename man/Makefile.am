## Process this file with automake to produce Makefile.in

bootstrappable=omorfi-analyse-text.1 omorfi-hyphenate.1 omorfi-generate.1\
			   omorfi-spell.1 omorfi-analyse-tokenised.1 omorfi-segment.1
broken=omorfi-factorise.1 omorfi-conllu.1 omorfi-disambiguate-text.1 \
	   omorfi-tokenise.1 omorfi-vislcg.1

dist_man1_MANS=$(bootstrappable) $(broken)

bootstrap: 
	for f in $(bootstrappable) ; do \
		help2man -s 1 -o $$f -N -S OMORFI `echo $$f | sed 's/.1/.sh/'`; \
	done

htmls:
	for f in $(bootstrappable) $(broken) ; do \
		groff -mandoc -Thtml $$f > $$f.html ;\
	done
