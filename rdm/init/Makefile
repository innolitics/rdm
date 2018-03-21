.SUFFIXES:
.SECONDARY:

DATA_FILES := $(wildcard data/*.yml)
TEMPLATES := $(wildcard templates/*.md)
RELEASE_DOCUMENTS := $(patsubst documents/%.md,release/%.md,$(wildcard documents/*.md))
RELEASE_PDFS := $(patsubst documents/%.md,release/%.pdf,$(wildcard documents/*.md))

all: $(RELEASE_DOCUMENTS)

pdfs: $(RELEASE_PDFS)

release/%.md: documents/%.md $(DATA_FILES) $(TEMPLATES)
	@mkdir -p $(@D)
	rdm render $< $(DATA_FILES) > $@

tmp/%.raw.tex: release/%.md
	@mkdir -p $(@D)
	pandoc $< -f markdown_github -t latex -o $@ --standalone -V geometry:margin=1.25in

# TODO: setup a custom latex documentclass instead of using sed to provide customization
tmp/%.tex: tmp/%.raw.tex
	cat $< | sed \
		-e '/\\setcounter{secnumdepth}{0}/d' \
		-e '0,/\\section/{s/\\section\(.*\)/\\title\1\n\\maketitle\n\\tableofcontents\n\\pagebreak\n/}' \
		> $@

release/%.pdf: tmp/%.tex
	latexmk -pdf -jobname="./$(basename $@)" $<

.PHONY:
clean:
	rm -rf release tmp
