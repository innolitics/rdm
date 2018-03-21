.SUFFIXES:

DATA_FILES := $(wildcard data/*.yml)
TEMPLATES := $(wildcard templates/*.md)
RELEASE_DOCUMENTS := $(patsubst documents/%.md,release/%.md,$(wildcard documents/*.md))
RELEASE_PDFS := $(patsubst documents/%.md,release/%.pdf,$(wildcard documents/*.md))

all: $(RELEASE_DOCUMENTS)

pdfs: $(RELEASE_PDFS)

release/%.md: documents/%.md $(DATA_FILES) $(TEMPLATES)
	@mkdir -p $(@D)
	rdm render $< $(DATA_FILES) > $@

release/%.pdf: release/%.md
	pandoc $< -f markdown_github -t latex -o $@ -V geometry:margin=1.25in

.PHONY:
clean:
	rm -rf release
