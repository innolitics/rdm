<a href="https://travis-ci.org/innolitics/rdm">
  <img src="https://travis-ci.org/innolitics/rdm.svg?branch=master">
</a>

# Regulatory Documentation Manager

## Introduction

Our Regulatory Documentation Manager (RDM) is a set of templates and python scripts for generating regulatory documents for software that is a, or is embedded in, medical devices.  We use it at [Innolitics](https://innolitics). RDM is especially well-suited for early-stage software-only medical devices when the team doesn't have existing regulatory expertise.

## Quick Start

```
pip install rdm
rdm init
cd regulatory
make
# regulatory documents stored in the "release" directory
```

## Philosophy on Regulations

Engineering is about optimizing. To do it one must first know what is being optimized.

Some students go to school because they need the degree to get a job.  These students optimize their actions to get the best grades for the least amount of work.

The best students go to school to learn, and while they often try to get good grades, they optimize their actions so as to learn as much as they can.

Likewise, some companies follow regulations to get certified to sell their products.  They optimize everything they do to get past the regulators for the lowest cost.

The best companies follow the regulations with a degree of faith that these regulations will make their products better and safer.

## Typical Workflow

RDM is designed to be used within a typical software development workflow.  When a new project is started, developers

1. Install RDM using `pip install rdm`
2. Generate a set of documents, which are stored in the git repository, using `rdm init`
3. Edit configuration variables in the generated files
4. Write _software requirements_ in a YAML file, also stored in the git repository
5. Generate a top-level architecture document, also stored in the repository, which may subdivide the project into smaller _software items_
6. Tickets (e.g. Github Issues) are labeled with one or more requirement ids
7. Each commit messages must include a reference to the ticket that is being worked on
8. Pull requests must be reviewed, and certain standardized comments are placed in reviews to confirm validation
9. Write new architecture documents as new _software items_ are implemented
10. Once a new _release_ is cut, generate a set of IEC62304 documents using `rdm release`
11. These markdown files can then be converted to PDFs or Word documents using a tool such as [Pandoc](https://pandoc.org)

## Design Goals

1. Provide a set of template regulatory documents that covers common use-cases.
2. Focus on software developers ease-of-use; the plan documents are intended to read and used frequently by the software developers on the team.  Thus, wherever there was a tradeoff between making it easy to read for developers vs regulators/auditors, we optimized for developers.  For example, we re-order IEC62304 sections to follow a more logical order for developers at the cost of being less parallel to IEC62304's structure.
3. Easy auditablility.  In order to make it easier for regulators/auditors to read the document, we include auditor comments and links back to IEC62304.  These links and notes are hidden by default, but there is a flag that enables turning them on.  This way, we can use the "official" version without comments during our day-to-day work, but we can give the auditors two copies—both the "official" version and the "auditor" version that has all these extra notes. The auditor notes make it easier to tweak the existing tempaltes, since you will know whether a section of the template is required or not.
4. Provide readable documents; e.g., other 62304 templates include many short deeply nested sub-sections.  We use a maximum of two levels of nesting.  We also provide flags (e.g., for different safety classes) that prune out irrelevant parts of the document, so that the documents only include what is necessary for the particular project.
5. Provide beautiful documents.  We believe making beautiful looking documents will encourage people to read and update them.

## Dependencies

- Python 3.5+
- Make
- Jinja2 2.7+
- PyYAML
- gitpython
- jsonschema
- pygithub (optional, required when using Github as your project manager)
- Pandoc and Latex (optional, required for PDF generation)
- Reportlab and Svglib (optional, required to include SVGs in PDFs)

## Installation

`pip install rdm`

or, if you need svg and github support:

`pip install rdm[svg,github]`

## References

References to regulatory documents are made in double square brackets throughout the RDM documentation.  For example, [[62304:5.1.9]] refers to section 5.1.9 of the IEC62304:2006 standard.

## Medical Devices with Hardware Components

RDM is designed to work well for medical devices with and without hardware components.

Medical devices that contain a hardware component must comply with a larger body of standards, for example IEC60601-1.  When this is the case, the _software requirements_ must be tied to the larger _system requirements_.

RDM works well with "software only devices" (also known as Software as a Medical Device, SaMD).  In this case, the _software requirements_ and _system requirements_ are equivalent [5.2.1].

## User Guide

Run `rdm init` to generate a set of base IEC62304 documents for a project.  By default these documents are placed in the current working directory in a new directory named `regulatory`.

This directory contains a `Makefile` and a few directories.

- Regulatory documents templates are in the `documents` directory; by default these documents inherit from templates that are stored in the `rdm` package, thus, when you upgrade your `rdm` version your base templates may change.
- Data files are stored in the `data` directory; data stored in these data files are available when rendering the markdown templates.
- Images are stored in the `images` directory
- Temporarily generated files are stored in `tmp`
- The final compiled release documents (both markdown and pdf) are stored in the `release` directory

### Templating

We use the [Jinja templating language](http://jinja.pocoo.org/docs/latest/templates/), with a few modifications.

We add `first_pass_output` to the rendering context, which is useful when you need to inspect the rendered document to generate, e.g., definition lists. This object has two useful properties:

- `first_pass_output.source` contains the complete output of a first pass generation of the document.
- `first_pass_output.lines` contains the same output as list of lines.

We also include few optional [extensions](http://jinja.pocoo.org/docs/2.10/extensions/). Extensions are set in `system.yml`.

For example
```yaml
md_extensions:
  - 'rdm.md_extensions.audit_notes.AuditNoteExclusionExtension'
  - 'rdm.md_extensions.section_numbers.SectionNumberExtension'
  - 'rdm.md_extensions.vocabulary_extension.VocabularyExtension'
```

### Auditor Notes Extension

We have added some features to make it more convenient to include auditor
notes.  Auditor notes are references that will be convenient to an auditor but
add a lot of extraneous information to others.  In the `system.yml` file
`auditor_notes` can be set true or false.  This can be used directly using the
jinja `if` mechanism:

```html
{% if system.auditor_notes %}
Some auditor only information.
{% endif %}
```

There are many of situations where all that is needed for auditors is a simple reference like 

```html
Some specification [62304:6.2.4].
```

while the reference should be excluded when `system.auditor_notes` is false:

```html
Some specification.
```

While the verbose jinja `if` mechanism could be used to control this,
a custom syntax is available when `AuditNoteExtension` is loaded.
The custom syntax simply uses double brackets like `[[62304:6.2.4]]`
to indicate a reference should only be included for auditors.

Including this single line in the document:

```html
{% if system.auditor_notes %}{% audit_notes %}{% endif %}
``` 

will control how double bracketed items will appear.

For example

```html
Some specification [[62304:6.2.4]].
```

will appear as

```html
Some specification.
```

when `system.auditor_notes` is false.

(Notice the single leading space after "specification" has been removed.)

When `system.auditor_notes` is true it will appear as:

```html
Some specification [62304:6.2.4].
```
(Notice the single leading space after "specification" has been retained.)

It is also possible to apply custom formats for individual document tags.
If the tag `{% audit_notes %}` is encountered then the default format is used.
A custom format dictionary can also be supplied inside the tag: `{% audit_notes some_format_dictionary %}`

For example `62304` documents could be given a custom bold format by placing a dictionary in `system.yml`:

```yaml
audit_notes: true
auditor_note_formats:
  62304: "{spacing}**[IEC {tag}{content}]**"
```

Using the tag {% audit_notes system.auditor_note_formats %} will cause `62304` tags to appear as:

Some specification **[IEC 62304:6.2.4]**.

(The `{spacing}` in the format string above ensures that a leading space, if present, is retained)

Unwanted tags can be removed by using an empty string for the format.

### Section Numbers Extension

The `SectionNumberExtension` will automatically add section numbering.
This will convert section number markdown like:

```html
## Some Topic
```

Will be replaced by something similar to:

```
## 2.1 Some Topic
```

### Vocabulary Extension

The `VocabularyExtension` extends `first_pass_output` to include a dictionary of words found in the trial first pass.
The set of words can then be accessed as a jinja variable using `{{ first_pass_output.words }}`.
More convenient is testing whether a particular word is in the document:

```html
{% if first_pass_output.has(`foobot`) %}
*foobot*: Automated process that implements foo.
{% endif %}
```

The above definition of the example word `foobot` would only be included if the full document actually uses the word.
Case insensitive versions of `words` and `has` are available as `words_ignore_case` and `has_ignore_case`.

## Document Formats

Documents are produced in two different formats.

1. [Github-Flavored Markdown](https://guides.github.com/features/mastering-markdown/) with standardized YAML front matter
2. PDFs

Typically, the current markdown version of the relevant documents are stored in the git repository, so that they can be easily browsed and linked to by developers.

Compile the release markdown documents using:

```
make
```

The PDF versions are generated for submission to regulatory bodies or for upload to other quality management systems.

Compile the release PDF documents using:

```
make pdfs
```

### YAML Front Matter for the PDF Documents

The Markdown document format contains YAML front matter, which is used to generate the title page, headers, and footers in the associated PDFs.

For example, your markdown YAML front matter may be:

```
---
id: PLAN-001
revision: 1
title: Software Plan
---
```

The required `title` value is used for the document title page and in the header.

The required `id` value is the document id. This is show in the title page and in the header.

The optional `revision` value is printed on the title page and in the header, if present. Revisions are not typically required for records.

The manufacturer name, which is stored in the `system.yml` data document, is also show on the title page.

## Images

Both the markdown and PDFs support images.

Images in the markdown documents the path the images will usually look like:

```
![image label](../images/my-image.svg)
```

We suggest using SVGs because they are resolution independent.  SVGs are converted to PDFs to be included in the latex (and then PDF) version of the documents.

Images must be able to fit within a single page of a pdf document for the formatting to look normal.

Note that svglib has several limitations.  As of April 2018, these include:

- stylesheets are not supported (only the style attribute)
- clipping is limited to single paths, no mask support
- color gradients are not supported.

Also note that markdown does not support having spaces in links, thus image names can not have spaces.

By default, images are stretched to full page width.

## RDM's Limitations

- The default templates were written with small softwre teams in mind (e.g., 2 - 5 developers).
- Only supports Github as your project manager (we plan on adding support for Gitlab, Jira, Trello, and Pivotal over time)
- Assumes that the risk management process is stored elsewhere (we plan on adding support for ISO14971's risk management process soon)
- Only supports a single _software system_
- Only support using git as your version control system
- Assumes the whole software system is in a single git repository
- Default templates assume the whole software system has a single saftey classification
