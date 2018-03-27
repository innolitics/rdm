---
category: PLAN
id: PLAN-001
revision: 1
title: Software Plan
company_name: {{ system.company_name }}
---

# Purpose

This document outlines how software developers should develop, maintain, and configure {{ system.project_name }}.  It includes the software development plan and the software maintenance plan.  All software life cycle process are described in this document.

# Development Process

## Development Life Cycle Model

{{ system.project_name }} will be developed using an evolutionary software development life cycle model.  The evolutionary strategy develops the software system using a sequence of builds.  Customer needs and software system requirements are partially defined up front, then are refined in each succeeding build{% if system.auditor_notes %} [5.1.1]{% endif %}.

## Development Planning Activity

The project lead is responsible for keeping this planning document up to date{% if system.auditor_notes %} [5.1.2]{% endif %}.

{# TODO: address [5.1.3.b] #}

Each development activity should indicate its required inputs, deliverables (also referred to as outputs), and output verification steps{% if system.auditor_notes %} [5.1.6.a and 5.1.6.b]{% endif %}.  Since we are using an evolutionary development life cycle, activities typically are performed before their inputs are fully settled.  As a result, activity inputs and outputs may not be internally consistent during the development process.

{# TODO: indicate that only software requirements that are marked for a particular Github milestone must be done by release #}

Before each software release, the team should verify the deliverables of each development activity to ensure they are in a consistent state{% if system.auditor_notes %} [5.1.6.c]{% endif %}.  The project lead should accept the release based on the consistency of the various development activity outputs{% if system.auditor_notes %} [5.1.6.d]{% endif %}.

{% if system.safety_class == "C" %}
Software standards (e.g., PEP8 on a python project) should be agreed upon and recorded in this document.  To the extent possible, checking against these stnadards should be performed in an automated fassion (e.g., using a linter which is run on a git-commit hook){% if system.auditor_notes %} [5.1.4.a]{% endif %}.
{% endif %}

## Requirements Analysis Activity

{% if not system.is_software_only_device %}
System requirements are recorded in {{ system.system_requirements_location }}.  Each system requirement requires a unique identifier so that we can trace its related software requirements back to it{% if system.auditor_notes %} [5.1.3.b]{% endif %}.
{% endif %}

{# TODO: discuss risk analysis location; clarify how risk controls will be traced to software requirements. #}

Software requirements are recorded in the form of Github Issues that have been tagged with the `requirement` label{% if system.auditor_notes %} [5.2.1]{% endif %}.  See [this guide](https://guides.github.com/features/issues/) for details about using Github Issues.  See [Appendix A](#requirements-analysis) for a list of the different types of requirements, and some best practices for defining them{% if system.auditor_notes %} [5.2.2 and 5.2.3]{% endif %}.

To the extent possible, software requirements should be enumerated at the start of the project.  If an existing requirement becomes irrelevant, it should be tagged with the `obsolete` label. {% if not system.is_software_only_device %} Software requirements should be tied to their originating system requirements by tagging them with labels that match the system requirement ids. {% endif %}

When software requirements are added or changed, re-evaluate the medical device risk analysis{% if system.auditor_notes %} [5.2.4]{% endif %} and ensure that existing software requirements{% if not system.is_software_only_device %}, and system requirements,{% endif %} are re-evaluated and updated as appropriate {% if system.auditor_notes %} [5.2.5]{% endif %}.

**Input:** System requirements and risk controls

**Output:** Labeled Github issues with clearly written descriptions

**Output Verification:** Ensure software requirements:

{% if not system.is_software_only_device %}
- implement system requirements and are labeled with system requirement ids
- implement risk controls and are labeled with risk control ids{% endif %}
- don't contradict each other
- have unambiguous descriptions
- are stated in terms that permit establishment of test criteria and performance of tests to determine whether the test criteria have been met{% if system.auditor_notes %} [5.2.6]{% endif %}.

{% if system.safety_class != 'A' %}
## Architectural Design Activity

Follow the [version control workflow](#appendix-b---version-control-workflow) when performing and verifying this activity.

After the initial set of requirements have been gathered, develop an initial software system architecture and document it in a file named `DESIGN.md` in the root of the project's git repository{% if system.auditor_notes %} [5.3.1]{% endif %}.  This file, which we will refer to as the software system design file, should describe how the software system is divided into software items, and whether these software items are further divided, and so on until the software items are divided no further{% if system.auditor_notes %} [5.4.1]{% endif %}.  See [Appendix A](#architectural-design) for some guidance on how to divide a software system into items.

Show the software and hardware interfaces between the software items and external software components{% if system.auditor_notes %} [5.3.2]{% endif %}.  Prefer block diagrams and flow charts to textual descriptions, and include these diagrams in the design file.

Indicate which software items are SOUP.  Include a section in the design files that specifies functional and performance requirements for any SOUP items{% if system.auditor_notes %} [5.3.3]{% endif %}, as well as any hardware or software that is necessary for its intended use{% if system.auditor_notes %} [5.3.4]{% endif %}.

{% if system.safety_class == 'C' %}
Identify any segregation between software items that is essential to risk control, and state how to ensure that the segregation is effective.  For example, one may segregate software items by running them on different processors{% if system.auditor_notes %} [5.3.5]{% endif %}.
{% endif %}

The initial architecture does not need to be complete or final, since code construction often helps guide architectural decisions, however, it is worth spending a significant amount of time on the initial architecture.

**Input:** Software requirements

**Output:** Design files

**Output Verification:** Ensure software architecture documented in the design files:

- implements system and software requirements
- is able to support interfaces between software items and between software items and hardware
- is such that the medical device architecture supports proper operation of any SOUP items{% if system.auditor_notes %} [5.3.6]{% endif %}.
{% endif %}

{% if system.safety_class == 'C' %}
## Detailed Design Activity

Follow the [version control workflow](#appendix-b---version-control-workflow) when performing and verifying this activity.

In addition to the software system design file, each software item requires its own detailed design{% if system.auditor_notes %} [5.4.2]{% endif %}.  These detailed designs should be stored as close as possible to their corresponding source files.  For example:

- if a software item is a directory, its detailed design should be stored in a file called `DESIGN.md` in that directory
- if a software item is a file, its detailed design should be stored in a block comment at the top of the file
- if a software item is a function, its detailed design should be stored in a block comment adjacent to the function.

The location of these detailed designs should be indicated in the software system design file.

Detailed designs for interfaces between software items and external components (hardware or software) should be included as appropriate{% if system.auditor_notes %} [5.4.3]{% endif %}.

**Input:** Software system design file

**Output:** Software item designs

**Output Verification:** Ensure software requirements:

- implements system and software requirements
- is free from contradiction with the software system design file{% if system.auditor_notes %} [5.4.4]{% endif %}.

{% endif %}

## Unit Implementation and Verification Activity

Follow the [version control workflow](#appendix-b---version-control-workflow) when performing and verifying this activity.

Implement, or partially implement, one or more software items in a new git branch.
Write unit tests and new integration tests as appropriate.

{# TODO: figure out how to fulfill 5.5.2, 5.5.3, an 5.5.4 #}

**Input:** {% if system.safety_class == 'C' %}Detailed software item designs{% else %}Software system design file{% endif %} and software requirements

**Output:** Code changes, stored in un-merged git branches with corresponding pull requests

**Output Verification:** Ensure the code changes made in the git branch:

- completes any software requirements it claims to close
- is consistent with the {% if system.safety_class == 'C' %}related detailed designs{% else %}software system design{% endif %}
{% if system.safety_class == "C" %}
- follows the project's software standards
{% endif %}
- includes unit tests or justifies why they are not necessary
- is covered by existing integration tests or includes a new integration test{% if system.auditor_notes %} [5.5.5]{% endif %}.

{% if system.safety_class != 'A' %}
## Integration and Integration Testing Activity
## System Testing Activity
{% endif %}

## Release Activity

When a new version of the software is released, the git commit corresponding to the state of the code should be tagged with the version number.

# Maintenance Process

## Problem and Modification Analysis

Feedback from users, internal testers, and software developers will be recorded in {{ system.feedback_location }}{% if system.auditor_notes %} [6.2.1.1]{% endif %}.

# Risk Management Process

# Configuration Management Process

# Problem Resolution Process

## Prepare Problem Report

Problem reports are stored as Github Issues tagged with the `problem` label.

When creating a new problem report, include in the issue description:

- The type of problem
- The scope of the problem
- The criticality of the problem
- Any relevant relevant information that can be used to investigate the problem{% if system.auditor_notes %} [9.1]{% endif %}.

## Investigate Problem

The software developer assigned to the problem report should:

- Investigate the problem and if possible identify the cause and record it in comments in the Github issue
- Evaluate the problem’s relevance to safety using the software risk management process 
- Document the outcome of the investigation and evaluation; and
- Create a Github issue tagged with the label `request` for actions needed to correct the problem, or document the rationale for taking no action{% if system.auditor_notes %} [9.2]{% endif %}.

## Advise Relevant Parties

# Documents

1. Software Development Plan (this document)
2. Risk Management File

# Definitions

Many of these definitions were taken from IEC62304:2006.

#### Process

a set of interrelated or interacting activities that transform inputs into outputs

#### Activity

a set of one or more interrelated or interacting tasks

#### Task

a single piece of work that needs to be done

NOTE we do not explicitly demarcate tasks in this document

#### Software System

integrated collection of software items organized to accomplish a specific function or set of functions

#### Software Item

any identifiable part of a computer program

NOTE Three terms identify the software decomposition. The top level is the software system. The lowest level that is not further decomposed is the software unit. All levels of composition, including the top and bottom levels, can be called software items. A software system, then, is composed of one or more software items, and each software item is composed of one or more software units or decomposable software items. The responsibility is left to the manufacturer to provide the definition and granularity of the software items and software units.

#### Software Unit

software item that is not subdivided into other items

#### SOUP

**software of unknown provenance (acronym)**

software item that is already developed and generally available and that has not been
developed for the purpose of being incorporated into the medical device (also known as "off-the-shelf software") or software previously developed for which adequate records of the development processes are not available

# References

1. IEC62304:2006

# Appendix A - Guidance

## Requirements Analysis

Writing software requirements is an art and a science; one must find balance between precision and usefulness.

Software requirements are often categorized as one of the following types:

a. Functional and capability requirements
  - performance (e.g., purpose of software, timing requirements),
  - physical characteristics (e.g., code language, platform, operating system),
  - computing environment (e.g., hardware, memory size, processing unit, time zone, network infrastructure) under which the software is to perform, and
  - need for compatibility with upgrades or multiple SOUP or other device versions.

b. Sofware system inputs and outputs
  - data characteristics (e.g., numerical, alpha-numeric, format) ranges,
  - limits, and
  - defaults.

c. Interfaces between the software system and other systems

d. Software-driven alarms, warnings, and operator messages

e. Security requirements
  - those related to the compromise of sensitive information,
  - authentication,
  - authorization,
  - audit trail, and
  - communication integrity.

f. Usability engineering requirements that are sensitive to human errors and training
  - support for manual operations,
  - human-equipment interactions,
  - constraints on personnel, and
  - areas needing concentrated human attention.

g. Data definitions and database requirements

h. Installation and acceptance requirements of the delivered medical device software at the operation and maintenance site or sites

i. Requirements related to methods of operation and maintenance

j. User documentation to be developed

k. User maintenance requirements

l. Regulatory requirements

{% if system.safety_class != "A" %}
m. Risk control measures
{% endif %}

## Architectural Design

Software units are often thought of as being a single function or module, but this is not always appropriate.  Software units must be able to be tested independently, and software items should be divided in a way such that parallels the directory structure of the project.

{# TODO discuss limitations regarding how software items can be divided up in more detail #}

# Appendix B - Version Control Workflow

All source code, software designs, and related files should be stored within this Git repository{% if system.auditor_notes %} [5.1.4.c and 5.1.4.b]{% endif %}.

The master branch of the git repository should contain the most up-to-date tested version of the software system.  New development should usually occur within separate Git branches.  These branches can be merged into the master branch after the changes in them have been verified.  If, for some reason, it is necessary to commit new work directly on the master branch, justify why this was necessary in the git commit message{% if system.auditor_notes %}[5.5.1]{% endif %}.

Git commits should be split into logical chunks, and Git commit messages should:

- explain why the current changes are being made, especially when it is not obvious
- reference software requirements using Github issue references (e.g., if the Github issue number 142 is worked on in a commit, its commit message should contain `#142`)

{% if system.safety_class != "A" %}
When a chunk of work---such as the architectural design, detailed designs, or software unit implementation---is completed and ready for verification, create a pull request and assign it to be reviewed by the appropriate person on the project.

The person who made the commits can not be the same person who reviewed them.

The reviewer should perform the appropriate verification steps and should record them as comments in the pull request.  If verification is going to be delayed until later, this should be noted.
{% endif %}
