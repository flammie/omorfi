## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose
HREGEX_FLAGS=$(HFST_FLAGS)

WEIGHT_TARGETS=weights.voikko.hfst weights.fiwiki.hfst weights.omorfi.hfst \
			   weights.no.hfst
hfstfidatadir=$(datadir)/hfst/fi_FI/
hfstfidata_DATA=$(WEIGHT_TARGETS)
noinst_DATA=analysis-sigma-star.hfst surface-sigma-star.hfst sigma-star.hfst

REGEX_SRCS=voikko.tags.regex omorfi.tags.regex no-tags.regex \
		   surface-sigma-star.regex sigma-star.regex

EXTRA_DIST=$(REGEX_SRCS) train-tokens.bash fiwiki.tokens.weights.strings

# disabling weights
weights.no.hfst: sigma-star.hfst
	ln -sf $< $@

# weighting scheme from voikko spell checker
weights.voikko.hfst: voikko.tags.hfst sigma-star.hfst
	$(HREP) $(HFST_FLAGS) voikko.tags.hfst -f 0 |\
		$(HMINUS) -1 sigma-star.hfst |\
		$(HMIN) $(HFST_FLAGS) -o no-tags.hfst
	$(HCAT) $(HFST_FLAGS) no-tags.hfst voikko.tags.hfst |\
		$(HCAT) $(HFST_FLAGS) -2 no-tags.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 |\
		$(HMIN) $(HFST_FLAGS) -o $@
	-rm -f no-tags.hfst

# our custom weighting scheme
weights.omorfi.hfst: omorfi.tags.hfst sigma-star.hfst
	$(HREP) $(HFST_FLAGS) omorfi.tags.hfst -f 0 |\
		$(HMINUS) -1 sigma-star.hfst |\
		$(HMIN) $(HFST_FLAGS) -o no-tags.hfst
	$(HCAT) $(HFST_FLAGS) no-tags.hfst omorfi.tags.hfst |\
		$(HCAT) $(HFST_FLAGS) -2 no-tags.hfst |\
		$(HREP) $(HFST_FLAGS) -f 1 |\
		$(HMIN) $(HFST_FLAGS) -o $@

# weighting scheme counted from Finnish wikipedia
fiwiki.tokens.weights.strings: train-tokens.bash
	@echo To regenerate corpus data for frequency training,
	@echo download Finnish wikipedia from
	@echo 	http://download.wikimedia.org/fiwiki/
	@echo and run train-tokens.bash

weights.fiwiki.hfst: fiwiki.tokens.weights.hfst
	-ln -sf $< $@

fiwiki.tags.regex: train-tags.bash
	@echo To regenerate corpus data for frequency training,
	@echo download Finnish wikipedia from
	@echo 	http://download.wikimedia.org/fiwiki/
	@echo and run train-tags.bash

weights.fiwiki.tags.hfst: fiwiki.tags.hfst no-tags.hfst
	$(HCAT) $(HFST_FLAGS) no-tags.hfst fiwiki.tags.hfst |\
		$(HCAT) $(HFST_FLAGS) -2 no-tags.hfst |\
		$(HMIN) $(HFST_FLAGS) -o $@

# generic compilation for most tag weighting sets
%.hfst: %.strings
	$(HS2F) $(HFST_FLAGS) -e '@0@' -i $< -j |\
		$(HMIN) $(HFST_FLAGS) -o $@

%.hfst: %.regex 
	$(HREGEX) $(HREGEX_FLAGS) -i $< -j |\
		$(HMIN) $(HFST_FLAGS) -o $@

clean-local:
	-rm -f *.hfst *.ol

