SHELL := /bin/bash -o pipefail -e
.SUFFIXES:
.SECONDARY:
.DELETE_ON_ERROR:

CONFIG := config.yml
DATA_FILES := $(wildcard data/*.yml)
RELEASE_DOCUMENTS := $(patsubst documents/%.md,release/%.md,$(wildcard documents/*.md))
RELEASE_PDFS := $(patsubst documents/%.md,release/%.pdf,$(wildcard documents/*.md))

all: $(RELEASE_DOCUMENTS)

pdfs: $(RELEASE_PDFS)

release/%.md: documents/%.md $(CONFIG) $(DATA_FILES)
	@mkdir -p $(@D)
	rdm render $< $(CONFIG) $(DATA_FILES) > $@

tmp/%.tex: release/%.md
	@mkdir -p $(@D)
	rdm tex $< $(DATA_FILES) > $@

release/%.pdf: tmp/%.pdf
	cp $< $@

tmp/%.pdf: tmp/%.tex
	latexmk -pdf -jobname="./$(basename $@)" $<

.PHONY:
data/history.yml: $(CONFIG)
	rdm pull $< > $@

.PHONY:
clean:
	rm -rf release/**.pdf tmp
