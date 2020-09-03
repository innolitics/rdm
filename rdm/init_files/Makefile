SHELL := /bin/bash -o pipefail -e
.SUFFIXES:
.SECONDARY:
.DELETE_ON_ERROR:

CONFIG := config.yml
DATA_FILES := $(wildcard data/*.yml)
RELEASE_DOCUMENTS := $(patsubst documents/%.md,release/markup/%.md,$(wildcard documents/*.md))
RELEASE_PDFS := $(patsubst documents/%.md,release/pdf/%.pdf,$(wildcard documents/*.md))

all: $(RELEASE_DOCUMENTS)

pdfs: $(RELEASE_PDFS)

release/markup/%.md: documents/%.md $(CONFIG) $(DATA_FILES)
	@mkdir -p $(@D)
	@mkdir -p release/tmp/images
	rdm render --base=release/markup $< $(CONFIG) $(DATA_FILES) > $@

release/tmp/%.tex: release/markup/%.md
	@mkdir -p $(@D)
	@mkdir -p release/tmp/images
	rdm tex  --download-to=release/tmp/images --base=release/tmp $< $(DATA_FILES) > $@

release/pdf/%.pdf: release/tmp/%.pdf
	@mkdir -p $(@D)
	cp $< $@

release/tmp/%.pdf: release/tmp/%.tex
	cd $(dir $<) && latexmk -pdf $(notdir $<)

.PHONY:
data/history.yml: $(CONFIG)
	rdm pull $< > $@

.PHONY:
clean:
	rm -rf release/pdf release/tmp
