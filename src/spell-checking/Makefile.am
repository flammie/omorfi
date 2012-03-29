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
				   error.simple-edit-distance-1.hfst \
				   error.simple-edit-distance-2.hfst \
				   error.simple-edit-distance-3.hfst \
				   error.simple-edit-distance-4.hfst \
				   error.edit-distance-infinity.hfst \
				   error.edit-distance-0.hfstol \
				   error.edit-distance-1.hfstol \
				   error.edit-distance-2.hfstol \
				   error.edit-distance-3.hfstol \
				   error.edit-distance-4.hfstol \
				   error.simple-edit-distance-1.hfstol \
				   error.simple-edit-distance-2.hfstol \
				   error.simple-edit-distance-3.hfstol \
				   error.simple-edit-distance-4.hfstol \
				   error.edit-distance-infinity.hfstol


EXTRA_DIST=$(suggestion_SRCS)
hfstfidatadir=$(datadir)/hfst/fi_FI/
hfstfidata_DATA=$(suggestion_TARGETS)

error.edit-distance-4.hfst: error.edit-distance-2.hfst
	$(HCAT) $(HFST_FLAGS) $< $< -o $@ 

error.edit-distance-3.hfst: error.edit-distance-1.hfst error.edit-distance-2.hfst
	$(HCAT) $(HFST_FLAGS) error.edit-distance-1.hfst error.edit-distance-2.hfst  -v -o $@

error.edit-distance-2.hfst: edit-distance-1.hfst
	$(HCAT) $(HFST_FLAGS) $< $< -v -o $@

error.edit-distance-1.hfst: edit-distance-1.hfst
	-ln -sf $< $@

error.edit-distance-0.hfst: edit-distance-0.hfst
	-ln -sf $< $@

error.simple-edit-distance-4.hfst: error.simple-edit-distance-2.hfst
	$(HCAT) $(HFST_FLAGS) $< $< -o $@ 

error.simple-edit-distance-3.hfst: error.simple-edit-distance-1.hfst error.simple-edit-distance-2.hfst
	$(HCAT) $(HFST_FLAGS) error.simple-edit-distance-1.hfst error.simple-edit-distance-2.hfst  -v -o $@

error.simple-edit-distance-2.hfst: error.simple-edit-distance-1.hfst
	$(HCAT) $(HFST_FLAGS) $< $< -v -o $@

error.simple-edit-distance-1.hfst: edit-distance-1.hfst
	-ln -sf $< $@

error.edit-distance-infinity.hfst: edit-distance-infinity.hfst
	-ln -sf $< $@

%.hfst: %.text
	$(HT2F) $(HFST_FLAGS) -i $< -e '@0@' -o $@

%.hfstol: %.hfst
	$(HF2F) $(HFST_FLAGS) -f olw -i $< -o $@

clean-local:
	-rm -f *.hfst *.ol

