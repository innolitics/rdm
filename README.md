<a href="https://travis-ci.org/innolitics/rdm">
  <img src="https://travis-ci.org/innolitics/rdm.svg?branch=master">
</a>

# Regulatory Documentation Manager

## Philosophy on Regulations

Engineering is about optimizing. To do it one must first know what is being optimized.

Some students go to school because they need the degree to get a job.  These students optimize their actions to get the best grades for the least amount of work.

The best students go to school to learn, and while they often try to get good grades, they optimize their actions so as to learn as much as they can.

Likewise, some companies follow regulations to get certified to sell their products.  They optimize everything they do to get past the regulators for the lowest cost.

The best companies follow the regulations with a degree of faith that these regulations will make their products better and safer.

## Introduction

Our Regulatory Documentation Manager (RDM) is a set of templates and python scripts for streamlining the process of complying with the IEC62304 standard.  We believe that IEC62304 is a good standard, and that it makes our software better and safer for for the medical practioners and patients that interact with our client's software.

RDM is designed to be used by software developers.

Many companies have other employees manage their regulatory documentation because the time costs are too high to have software developers manage the regulatory documentation directly.  We believe that software developers are in the best position to handle most of the tasks required by IEC62304.

RDM integrates tightly into modern software development workflows.  Essentially, when a new project is started, developers

1. Install RDM (using `pip install rdm`)
2. Generate a set of template documents, which are stored in the git repository (using `rdm init`)
3. Edit a relatively small number of global configuration variables in a generated file
4. Fill in an initial list of _software requirements_ in a YAML file, each with a unique id.  This file is stored in the git repository.
5. Generate a top-level architecture document, also stored in the repository, which may subdivide the project into smaller _software items_.
6. Tickets (e.g. Github Issues) are labeled with one or more requirement ids.
7. Each commit messages must include a reference to the ticket that is being worked on.
8. Pull requests must be reviewed, and certain standardized comments are placed in reviews to confirm validation.
9. Write new architecture documents as new _software items_ are implemented.
10. Once a new _release_ is cut, generate a set of IEC62304 documents using `rdm release`.  RDM will check the various YAML and architecture files for consistent, and then generate a set of markdown files.
11. These markdown files can then be converted to PDFs or Word documents using a tool such as [Pandoc](https://pandoc.org).

## Design Goals

1. Provide a generic template that covers common use-cases but is customizable.
2. Provide readable documents; e.g., other 62304 templates include many short deeply nested sub-sections.  We use a maximum of two levels of nesting.  We also provide flags (e.g., for different safety classes) that prune out irrelevant parts of the document, so that the documents only include what is necessary for the particular project.
3. Focused on software developers; the plan documents are intended to read and used frequently by the software developers on the team.  Thus, wherever there was a tradeoff between making it easy to read for developers vs regulators/auditors, we optimized for developers.  For example, we re-order IEC62304 sections to follow a more logical order for developers at the cost of being less parallel to IEC62304's structure.
4. Easy auditablility.  In order to make it easier for regulators/auditors to read the document, we include auditor comments and links back to IEC62304.  These links and notes are hidden by default, but there is a flag that enables turning them on.  This way, we can use the "official" version without comments during our day-to-day work, but we can give the auditors two copies—both the "official" version and the "auditor" version that has all these extra notes.
5. Provide beautiful documents.  We believe making beautiful looking documents will encourage people to read and update them.
6. Make it as easy as possible to "upgrade" your documents when new versions of 62304 and related standards are developed.

## Dependencies

- Python 3.4+
- Make
- Jinja2 2.7+
- PyYAML
- Pandoc and Latex (optional, required for PDFs)
- Reportlab and Svglib (optional, required to include SVGs in PDFs)

## Installation

`pip install rdm`

or, if you need svg support:

`pip install rdm[svg]`

## References

References to IEC62304:2006 are indicate in square brackets throughout the RDM documentation.  For example, [5.1.9] refers to section 5.1.9 of the IEC62304:2006 standard.

Words in italics refer to technical terms from IEC62304 (in the standard, these terms are written in small caps, but we think small caps are distracting, so we used italics instead).

## Medical Devices with vs. without Hardware Components

RDM is designed to work well for medical devices with and without hardware components.

Medical devices that contain a hardware component must comply with a larger body of standards, for example IEC60601-1.  When this is the case, the _software requirements_ must be tied to the larger _system requirements_.

RDM works well with "software only devices" (also known as Software as a Medical Device, SaMD).  In this case, the _software requirements_ and _system requirements_ are equivalent [5.2.1].

## Identifier Namespaces

There are various "regulatory items" that need to be tracked with unique identifiers.  Identifiers must be unique within their respective namespace.  In particular:

- system requirements (if the software system is part of a larger medical device system)
- software requirements
- software items
- hazardous situations
- risk controls

## User Guide

Run `rdm init` to generate a set of base IEC62304 documents for a project.  By default these documents are placed in the current working directory in a new directory named `regulatory`.

This directory contains a `Makefile` and a few directories.

- Regulatory documents templates are in the `documents` directory; by default these documents inherit from templates that are stored in the `rdm` package, thus, when you upgrade your `rdm` version your base templates may change.
- Data files are stored in the `data` directory; data stored in these data files are available when rendering the markdown templates.
- Images are stored in the `images` directory
- Temporarily generated files are stored in `tmp`
- The final compiled release documents (both markdown and pdf) are stored in the `release` directory

We are using the [Jinja templating language](http://jinja.pocoo.org/docs/latest/templates/).

## Document Formats

Documents are produced in two different formats.

1. [Github-Flavored Markdown](https://guides.github.com/features/mastering-markdown/) with standardized YAML front matter
2. PDFs

Typically, the current markdown version of the relevant documents are stored in the git repository, so that they can be easily browsed and linked to by developers.

The PDF versions are generated for submission to regulatory bodies or for upload to other quality management systems.

## Template Locations

The base templates are stored in the rdm package.  The sections included in here are typically not edited by users.

When you run `rdm init`, templates that inherit from the base templates are copied into your project repository.  You are expected to edit these files.

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

## Limitations

- The default templates were written with small softwre teams in mind (e.g., 2 - 5 developers).
- Only support using Github as your project manager (we plan on adding support for Jira, Trello, and Pivotal over time)
- Assumes that the risk management process is stored elsewhere (we plan on adding support for ISO14971's risk management process soon)
- Only supports a single _software system_
- Only support using git as your version control system
- Assumes the whole software system is in a single git repository
- Assumes the whole software system has a single saftey classification
