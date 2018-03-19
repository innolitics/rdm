# Regulatory Documentation Manager

## Philosophy

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

## Limitations

- Only support software safety classification "A" requirements (we plan on adding "B" and "C" requirements soon)
- Only support using Github as your project manager (we plan on adding support for Jira, Trello, and Pivotal over time)
- Assumes that the risk management process is stored elsewhere (we plan on adding support for ISO14971's risk management process soon)
- Only supports a single _software system_
- Only support using git as your version control system
- Assumes the whole software system is in a single git repository
