## Process this file with automake to produce Makefile.in

HFST_FLAGS=--verbose

suggestion_SRCS=\
				edit-distance-0.text \
				edit-distance-1.text \
				simple-edit-distance-1.text \
				edit-distance-infinity.text
suggestion_TARGETS=error.edit-distance-0.hfst\
				   error.edit-distance-1.hfst error.edit-distance-2.hfst \
				   error.edit-distance-3.hfst error.edit-distance-4.hfst \
				   error.edit-distance-infinity.hfst


EXTRA_DIST=$(suggestion_SRCS)
hfstfidatadir=$(datadir)/hfst/fi_FI/
hfstfidata_DATA=$(suggestion_TARGETS)

edit-distance-4.hfst: edit-distance-2.hfst
	$(HCAT) $(HFST_FLAGS) $< $< -o $@

edit-distance-3.hfst: edit-distance-1.hfst edit-distance-2.hfst
	$(HCAT) $(HFST_FLAGS) edit-distance-1.hfst edit-distance-2.hfst -o $@

edit-distance-2.hfst: edit-distance-1.hfst
	$(HCAT) $(HFST_FLAGS) $< $< -v -o $@

error.edit-distance-4.hfst: edit-distance-3.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -o $@ -i $<

error.edit-distance-3.hfst: edit-distance-3.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -o $@ -i $<

error.edit-distance-2.hfst: edit-distance-2.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -o $@ -i $<

error.edit-distance-1.hfst: edit-distance-1.hfst
	-$(HF2F) $(HFST_FLAGS) -f olw -o $@ -i $<

error.edit-distance-0.hfst: edit-distance-0.hfst
	-$(HF2F) $(HFST_FLAGS) -f olw -o $@ -i $<

error.edit-distance-infinity.hfst: edit-distance-infinity.hfst
	-$(HF2F) $(HFST_FLAGS) -f olw -o $@ -i $<

%.hfst: %.text
	$(HT2F) $(HFST_FLAGS) -i $< -e '@0@' -o $@


clean-local:
	-rm -f *.hfst *.ol

