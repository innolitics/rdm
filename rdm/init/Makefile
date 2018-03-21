.SUFFIXES:

DATA_FILES := $(wildcard data/*.yml)
TEMPLATES := $(wildcard templates/*.md)
RELEASE_DOCUMENTS := $(patsubst documents/%.md,release/%.md,$(wildcard documents/*.md))

all: $(RELEASE_DOCUMENTS)

release/%.md: documents/%.md $(DATA_FILES) $(TEMPLATES)
	@mkdir -p $(@D)
	rdm render $< $(DATA_FILES) > $@

.PHONY:
clean:
	rm -rf release
