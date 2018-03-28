---
category: PLAN
id: PLAN-001
revision: 1
title: Software Plan
manufacturer_name: {{ system.manufacturer_name }}
---

# Purpose

Engineering is about optimizing. To do it one must first know what is being optimized.

*Some students go to school because they need the degree to get a job. These students optimize their actions to get the best grades for the least amount of work.  The best students go to school to learn, and while they often try to get good grades, they optimize their actions so as to learn as much as they can.*

*Likewise, some companies follow regulations to get certified to sell their products. They optimize everything they do to get past the regulators at the lowest cost.  The best companies follow the regulations in order to make the products safer and better, and while they are careful to fulfill the relevant regulations, they optimize their regulatory process to make their products as safe and useful as is feasible.*

This document describes a set of processes which will be used during the development and maintenance of {{ system.project_name }}.  It is written primarily for software developers, and it should contain all of the context for a new developer to understand and work within the processes described.

These processes are designed to be compliant with the IEC62304 standard, however, their main purpose is to help build safe and useful medical software.

# Overview

## Definitions

A **processes** is a set of interrelated or interacting activities that transform inputs into outputs.

An **activity** is a set of one or more interrelated or interacting tasks.

A **task** is a single piece of work that needs to be done.  Note that we do not explicitly demarcate tasks in this document.

Three terms identify the software decomposition.  The top level is the **software system**. The lowest level that is not further decomposed is the **software unit**.  All levels of composition, including the top and bottom levels, can be called **software items**.  A software system, then, is composed of one or more software items, and each software item is composed of one or more software units or decomposable software items.  The responsibility is left to the manufacturer to provide the definition and granularity of the software items and software units.

**SOUP**, or **software of unknown provenance**, is a software item that is already developed and generally available and that has not been developed for the purpose of being incorporated into the medical device (also known as "off-the-shelf software") or software previously developed for which adequate records of the development processes are not available.

A **problem report** is a record of actual or potential behaviour of a software product that a user or other interested person believes to be unsafe, inappropriate for the intended use or contrary to specification.  Stored as a Github issue with the `problem` label.

A **software requirement** is a documented aspect of how the software system should work, see [Appendix A](#architectural-design) for examples.  Software requirements are stored as a Github issue with the `requirement` label.

A **change request** is a documented specification of a change to be made to a software product.  Change requests are stored as Github issues that do not have the `problem` or `requirement` labels.  All work on the software project should occur in response to change requests.

## Roles and Responsibilities

These processes were developed for small software development teams composed of a project lead and one to four software developers.  The primary responsibilities of these roles are:

1. Project Lead
    - requirements gathering
    - risk analysis
    - system architecture
    - work assignment
    - verifying pull requests
2. Software Developer
    - refining requirements
    - refining system architecture
    - unit level architecture
    - implementation
    - unit and integration tests
    - investigating problem reports.

The project lead, working on behalf of the manufacturer, is ultimately responsible for the safety and utility of the software system.

## Version Control

{% if system.auditor_notes %}[This section describes our software configuration management, but does not explicitly use the term "software configuration management" since many developers will be unfamiliar with the term.  Note that Git is a version control system that makes it simple to track and record the history of every file it contains.]{% endif %}

A Github-hosted Git repository should be setup at the start of the software development planning activity.

All activity outputs will be stored in

- the git repository, or
- Github issues associated with that repository, or
- Github pull requests associated with that repository

unless explicitly noted otherwise in the activity descriptions{% if system.auditor_notes %} [5.1.9.a and 8.1.1; note that this implies that all activity outputs that are stored in the git repository, Github issues, or Github pull requests are configuration items.  Each activity describes the configuration items in more detail.]{% endif %}.

## Github Issues, Labels, and Milestones

Github issues are used to represent software requirements, problem reports, and change requests.  These three items are distinguished using labels.

- Software requirements are tagged with the `requirement` label
- Problem reports are tagged with the `problem` label
- All other issues are change requests.

{% if system.is_software_only_device %}
Software requirements may also be tagged with labels tracing them back to system requirements.
{% endif %}

Github issues are usually created by the project lead, however, other members of the development team may also create them.

The project lead shall create Github milestones for each planned software release or internal development milestone (e.g. beta testing).  The project lead should then associate Github issues with milestones as appropriate and should assignment them to software developers.  Software developers may also assign themselves to issues within the current milestone, so long as that issue was not already assigned to another developer.  Issues that have not been associated with a milestone should not be worked on.  A milestone is complete once all of its:

- software requirements are closed, indicating they are implemented
- problem reports are closed, indicating the problems have been addressed
- change requests are closed, indicating that the corresponding changes have been implemented.

Only the project lead is permitted to move issues into a milestone.

## Branches and Pull Requests

The master branch of the git repository should contain the most up-to-date tested version of the software system.  New development shall occur within other Git branches.  When work on the branch is nearing completion, a Github pull request should be created from this branch.  The project lead shall review and verify the changes in the branch, suggesting changes if necessary {% if system.auditor_notes %}[5.5.1]{% endif %}.

Git commits should be split into logical chunks, and Git commit messages should:

- explain why the current changes are being made, especially when it is not obvious
- reference software requirements using Github issue references (e.g., if the Github issue number 142 is worked on in a commit, its commit message should contain `#142`)

{% if system.safety_class != "A" %}
When a chunk of work---such as the architectural design, detailed designs, or software unit implementation---is completed and ready for verification, create a pull request and assign it to be reviewed by the appropriate person on the project.

The person who made the commits can not be the same person who reviewed them.

The reviewer should perform the appropriate verification steps and should record them as comments in the pull request.  If verification is going to be delayed until later, this should be noted.
{% endif %}


## Software Dependencies (SOUP)

SOUP, Software of Unknown Provenance, is software that is already developed and generally available and that has not been developed for the purpose of being incorporated into the medical device software (also known as "off-the-shelf software") or software previously developed for which adequate records of the development processes are not available.

The use of SOUP presents was not developed foIEC62304 requires that SOUP be tracked and handled carefully especially with regards to risks.

## Reproducible Builds

# Development Process

## Development Life Cycle Model

{{ system.project_name }} will be developed using an evolutionary software development life cycle model.  The evolutionary strategy develops the software system using a sequence of builds.  Customer needs and software system requirements are partially defined up front, then are refined in each succeeding build{% if system.auditor_notes %} [5.1.1]{% endif %}.

## Development Planning Activity

The project lead is responsible for keeping this planning document up to date{% if system.auditor_notes %} [5.1.2]{% endif %}.

{# TODO: address [5.1.3.b] #}

Each development activity should indicate its required inputs, deliverables (also referred to as outputs), and any output verification steps{% if system.auditor_notes %} [5.1.6.a and 5.1.6.b]{% endif %}.  Since we are using an evolutionary development life cycle, activities typically are performed before their inputs are fully settled.  As a result, activity inputs and outputs may not be internally consistent during the development process.

{# TODO: indicate that only software requirements that are marked for a particular Github milestone must be done by release #}

Before each software release, the team should verify the deliverables of each development activity to ensure they are in a consistent state{% if system.auditor_notes %} [5.1.6.c]{% endif %}.  The project lead should accept the release based on the consistency of the various development activity outputs{% if system.auditor_notes %} [5.1.6.d]{% endif %}.

{% if system.safety_class == "C" %}
Software standards (e.g., PEP8 on a python project) should be agreed upon and recorded in this document.  To the extent possible, checking against these stnadards should be performed in an automated fassion (e.g., using a linter which is run on a git-commit hook){% if system.auditor_notes %} [5.1.4.a]{% endif %}.
{% endif %}

**Input:** Nothing, besides a general understanding of the project goals.

**Output:** The markdown version of this plan document.

## Requirements Analysis Activity

{% if not system.is_software_only_device %}
System requirements are recorded in {{ system.system_requirements_location }}.  Each system requirement requires a unique identifier so that we can trace its related software requirements back to it{% if system.auditor_notes %} [5.1.3.b]{% endif %}.
{% endif %}

{# TODO: discuss risk analysis location; clarify how risk controls will be traced to software requirements. #}

Software requirements are recorded in the form of Github issues that have been tagged with the `requirement` label{% if system.auditor_notes %} [5.2.1]{% endif %}.  See [this guide](https://guides.github.com/features/issues/) for details about using Github issues.  See [Appendix A](#requirements-analysis) for a list of the different types of requirements, and some best practices for defining them{% if system.auditor_notes %} [5.2.2 and 5.2.3]{% endif %}.

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

# Problem Resolution Process

## Prepare Problem Report Activity

Problem reports are stored as Github issues tagged with the `problem` label.

When creating a new problem report, include in the issue description:

{# TODO: add "steps to recreate" #}

- The type of problem
- The scope of the problem
- The criticality of the problem
- Any relevant relevant information that can be used to investigate the problem{% if system.auditor_notes %} [9.1]{% endif %}.

{# TODO add examples and guidance regarding type, scope, and criticality; see [9.1] #}

**Input:** Feedback from users or other members of the development team.

**Output:** Properly formatted and labeled Github issues.

## Investigate Problem Activity

1. Investigate the problem and if possible identify the cause and record it in comments in the Github issue.
2. Evaluate the problem's relevance to safety using the software risk management process {# TODO: add more details about this #}
3. Document the outcome of the investigation and evaluation
4. Create a Github issue tagged with the label `request` for actions needed to correct the problem (also include an issue reference to the problem report{% if system.auditor_notes %} [8.2.4.b]{% endif %}), or document the rationale for taking no action{% if system.auditor_notes %} [9.2]{% endif %}.
5. Look through recent problem reports and attempt to identify any adverse trends.  E.g., look to identify certain software items that are failing consistently or have similar causes.  If any trends can be identified, be sure the change requests reverse these trends{% if system.auditor_notes %} [9.6]{% endif %}.

{# TODO: add unit tests to reproduce the failure #}

**If the problem affects devices that have been released, the software developer will make sure management is aware of the situation and has enough information to decide whether and how to notify affected parties{% if system.auditor_notes %} [9.3]{% endif %}.**

**Input:** Github issue containing relevant details about the problem.

**Output:** Details about the problem investigation documented in the problem report and either unapproved change requests or justification as to why change requests weren't necessary.

## Implement Change Requests

Once the change requests have been approved, implement them according to our change control process{% if system.auditor_notes %} [9.4]{% endif %}.

**Input:** Approved change requests

**Output:** Code changes required to implement change requests

**Output Verification:** Ensure code changes:

- all of the change requests have been implemented and merged into the `master` branch
- the original problem is fixed and the problem report closed
- any adverse trends have been reversed{% if system.auditor_notes %} [9.7]{% endif %}.

{% if system.safety_class != "A" %}
{% if system.auditor_notes %}[We presume that if our integration tests and system tests are passing, no new problems were introduced, per 9.7.d]{% endif %}
{% endif %}

{# TODO: be sure 9.8 is addressed #}

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

{# TODO add discussion about documenting the flow of data #}
