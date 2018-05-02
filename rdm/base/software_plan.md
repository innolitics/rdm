{% block front_matter -%}
---
category: PLAN
id: PLAN-001
revision: 1
title: Software Plan
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}
{% block purpose %}
# Purpose

Engineering is about optimizing. To do it one must first know what is being optimized.

Some students go to school because they need the degree to get a job. These students optimize their actions to get the best grades for the least amount of work.  The best students go to school to learn, and while they often try to get good grades, they optimize their actions so as to learn as much as they can.

Likewise, some companies follow regulations to get certified to sell their products. They optimize everything they do to get past the regulators at the lowest cost.  The best companies follow the regulations in order to make the products safer and better, and while they are careful to fulfill the relevant regulations, they optimize their regulatory process to make their products as safe and useful as is feasible.

This document describes a set of processes which will be used during the development and maintenance of {{ system.project_name }}. It is written primarily for software developers, and it should contain all of the context for a new developer to understand and work within the processes described.

{{ system.project_name }} is assigned a Class {{ system.safety_class }} software safety class, which means {% if system.safety_class == "A" %}no injury or damage to health{% elif system.safety_class == "B" %}non-serious injury{% else %}death or serious injury{% endif %} could occur if the software fails{% if system.auditor_notes %} [4.3.a]{% endif %}.

The primary purpose of this document is to help developers ensure {{ system.project_name }} is safe and useful.  The secondary purpose is to comply with {{ system.standard }}.
{%- if system.auditor_notes %}

[In order to assist auditors and regulators, we have included section references to {{ system.standard }} as well as occasional comments throughout this document.  These references and comments are always placed inside square brackets, and they are not present in the software-developer version of the document.  Other than these comments, the software-developer version is identical to the auditor version of this document.]{% endif %}
{% endblock %}
# Overview

## Definitions
{% if system.auditor_notes %}
[Most of these definitions are very similar to the {{ system.standard }} definitions, however, they have been simplified and clarified as appropriate for a better understanding by software developers.]
{% endif %}
A **process** is a set of interrelated or interacting activities that transform inputs into outputs.

An **activity** is a set of one or more interrelated or interacting tasks.

A **task** is a single piece of work that needs to be done.  Note that we do not explicitly demarcate tasks in this document.

Three terms identify the software decomposition.  The top level is the **software system**. The lowest level that is not further decomposed is the **software unit**.  All levels of composition, including the top and bottom levels, can be called **software items**.  A software system, then, is composed of one or more software items, and each software item is composed of one or more software units or decomposable software items.  See the software system design file for a description of how {{ system.project_name }} is decomposed into software items.

**SOUP**, or **software of unknown provenance**, is a software item that is already developed and generally available and that has not been developed for the purpose of being incorporated into the medical device (also known as "off-the-shelf software") or software previously developed for which adequate records of the development processes are not available.

A **problem report** is a record of actual or potential behaviour of a software product that a user or other interested person believes to be unsafe, inappropriate for the intended use or contrary to specification.  Problem reports are stored as GitHub issues with the `problem` label.

A **software requirement** is a particular function that the software must support, or some other constraint that the software must fulfill.  Requirements describe the *what*, while specifications and designs specify the *how*.

A **change request** is a documented specification of a change to be made to a software product.  Change requests are stored as GitHub issues that do not have the `problem` label.  All work on the software project should occur in response to change requests{% if system.auditor_notes %} [8.2.1]{% endif %}.
{% block extra_definitions %}
{%- endblock %}
## Development Life Cycle Model

{{ system.project_name }} will be developed using an evolutionary software development life cycle model.  The evolutionary strategy develops the software system using a sequence of builds.  Customer needs and software system requirements are partially defined up front, then are refined in each succeeding build{% if system.auditor_notes %} [5.1.1]{% endif %}.

## Roles and Responsibilities

The processes described in this document are designed for a team composed of a project lead and one to four software developers.  The project lead, working on behalf of the manufacturer, is responsible for the safety and utility of the software system built by the team.

## Diagram of Software Activities

![Overview of life-cycle processes](../images/lifecycle-processes.svg)

## Version Control

A git repository, hosted on GitHub, should be setup at the start of the software development planning activity.  All software development and maintenance activity outputs will be stored in this git repository, the associated GitHub issues, or the associated GitHub pull requests, unless explicitly noted otherwise in the activity description{% if system.auditor_notes %} [5.1.1.b]{% endif %}.
{% if system.auditor_notes %}
[This section describes our software configuration management, but does not explicitly use the term "software configuration management" since many developers will be unfamiliar with the term.  Note that Git is a version control system that makes it simple to track and record the history of every file it contains.

The requirements listed in sections 5.1.9.a, 5.1.11, 8.1.1, 8.1.3, and 8.3 of {{ system.standard }} are fulfilled by our use of Git and GitHub.  Also note that this setup implies that all activity outputs that are stored in the git repository, GitHub issues, or GitHub pull requests are configuration items.  Furthermore, the version of every configuration item comprising the software system configuration is stored in the git repository for the entire history of the project.  Each activity describes the configuration items in more detail.]
{% endif %}
## GitHub Issues, Labels, and Milestones

[GitHub issues](https://guides.github.com/features/issues/) are used to represent change requests and problem reports.  Problem reports have the `problem` label, and any GitHub issue that does not have a `problem` label is a change request.

Problem reports are typically created in response to feedback gathered from external users, or in response to anomalies detected during testing.

Change requests are created at the start of the unit implementation activity or during the problem investigation activity.  Change requests should be labeled with one or more software requirements.

In order to organize and prioritize the development work, change requests are assigned to GitHub milestones.  Change requests that have not yet been assigned to a GitHub milestone have not yet been approved, and should not be worked on since approval explicitly required by {{ system.standard }}{% if system.auditor_notes %} [8.2.1]{% endif %}.

Project leads associate change requests with milestones during release planning.  Once a change request is assigned to a milestone, it has been "approved" and may be worked on by a developer.  The project lead will then assign developers to change requests to divide up the work.  Software developers may also assign themselves to change requests, so long as it is not assigned to another developer and they don't have other outstanding tickets they can work on.

## Branches and Pull Requests

Change requests are implemented using [GitHub flow](https://guides.github.com/introduction/flow/).

When beginning work on a change request with an id of `104`, developers should open a new Git branch named `104-short-description`.  All development work should occur in Git branches{% if system.auditor_notes %} [5.1.1.d]{% endif %}.

The `master` branch of the git repository should contain the most up-to-date tested version of the software system.  When work on a change branch is nearing completion, a GitHub pull request should be created for this branch.  The project lead shall review and verify the changes in the change branch, suggesting changes if necessary {% if system.auditor_notes %}[5.5.1]{% endif %}.  Once these changes have been made re-verified, the developer should merge the change branch into the master branch.

Code changes should be split into logically separated commits, and commit messages should:

- explain why the current changes are being made, especially when it is not obvious
- reference the change request it was made in (the `rdm hooks` command can streamline this).

## Software Dependencies (SOUP)

SOUP, Software of Unknown Provenance, is software that is already developed and generally available and

- that has not been developed for the purpose of being incorporated into the medical device software (also known as "off-the-shelf software"), or
- software previously developed for which adequate records of the development processes are not available.

All SOUP used in {{ system.project_name }} must be recorded in a YAML file called `soup.yaml`, which we will refer to as our "software dependencies file."  The software dependencies file must contain a sequence of mappings each containing the following key and values:

- `title` - the name of the dependency{% if system.auditor_notes %} [8.1.2.a]{% endif %}
- `manufacturer` - the organization that maintains the tool{% if system.auditor_notes %} [8.1.2.b]{% endif %}
- `version` - e.g., `1.0.13`{% if system.auditor_notes %} [8.1.2.c]{% endif %}
- `type` - `production` or `development`
{%- if system.safety_class != "A" %}
- `requirements` - sequence of functional and performance requirements{% if system.auditor_notes %} [5.3.3]{% endif %}
- `hardware` - sequence of any hardware requirements{% if system.auditor_notes %} [5.3.4]{% endif %}
- `software` - sequence of any software requirements{% if system.auditor_notes %} [5.3.4]{% endif %}
- `anomaly_list` - URL to published anomaly sequence{% if system.auditor_notes %} [7.1.3]{% endif %}
{%- endif %}
- `purpose` - a brief explanation of how the SOUP is used in {{ system.project_name }}.

The `manufacturer` field may be `null` if the software is an open source project with no managing organization.

The `version` field may follow varying formats, such as `1.0.13`, `1.2r5`, or even `2021-05-05`.

The `type` field indicates whether the SOUP must be present while the software is being used in `production`, or if it is only necessary during `development`.  For example, a compiler or testing tool is a `development` dependency{% if system.auditor_notes %} [5.1.1.d]{% endif %}.
{% if system.safety_class != "A" %}
The `requirements` field should be a sequence of requirements that {{ system.project_name }} has for the SOUP.  For example, the SOUP must provide a web server that is compliant with the HTTP1.1 standard.

The `hardware` sequence should be any known specific hardware requirements needed for the SOUP's intended use in {{ system.project_name }}.  There is no need to get carried away with this field; most of the time it will be `null`, since usually there are no specific hardware requirements.  Examples include processor type and speed, memory type and size.

The `software` sequence should include any secondary dependencies.  Each secondary dependency should have the same format as the top-level sequence, and may have its own dependencies.

The `anomaly_list` should be a URL pointing to the SOUP's published sequence of known anomalies.  It may be `null` if no sequence is known.
{% endif %}
Whenever a change request requires new software dependencies to be added, removed, or changed, the software dependencies file should be updated within the same pull request.

The software dependencies file may cause duplication with other software development files (e.g., `requirements.txt` or `package.json`).  Also, it is recognized that keeping track of secondary dependencies can require significant effort---think carefully before adding new SOUP to {{ system.project_name }}.
{% block documents %}
## Documents

TODO: add a a list of document types
{% endblock %}
{%- block development_tools %}
## Development Tools
{% endblock %}
{%- block development_standards %}
## Development Standards
{% endblock %}

# Development Process
{% if system.auditor_notes %}
[This development process fulfills 5.1.1.a]
{% endif %}
## Development Planning Activity

**Input:** Nothing

**Performed by:** Project lead

At the start of the project, the project lead should fill in the place-holder sections of this document.  The planning document must be kept up to date as the project commences{% if system.auditor_notes %} [5.1.2]{% endif %}.

Each development activity should indicate its:

- required inputs
- which role should perform the activity
- deliverables (also referred to as outputs)
- output verification steps (if there are any)
- which role should perform the verification{% if system.auditor_notes %} [5.1.6.a and 5.1.6.b]{% endif %}.

Since we are using an evolutionary development life cycle, activities typically are performed before their inputs have settled.  As a result, activity inputs and outputs may not be consistent inbetween releases.

Before each software release, the team should verify the deliverables of each development activity to ensure they are in a consistent state{% if system.auditor_notes %} [5.1.6.c]{% endif %}.  The project lead should accept the release based on the consistency of the various development activity outputs{% if system.auditor_notes %} [5.1.6.d]{% endif %}.
{% if system.safety_class == "C" %}
Software standards (e.g., PEP8 on a python project) should be agreed upon and recorded in this document.  To the extent possible, checking against these standards should be performed in an automated fashion (e.g., using a linter which is run on a git-commit hook){% if system.auditor_notes %} [5.1.4.a]{% endif %}.
{% endif %}
**Output:** The markdown version of this plan document.

## Requirements Analysis Activity

**Input:** System requirements and risk controls

**Performed by:** Project lead
{% if not system.is_software_only_device %}
System requirements are recorded in {{ system.system_requirements_location }}.  Each system requirement must have a unique identifier so that we can trace it to any software requirements that fulfill it{% if system.auditor_notes %} [5.1.3.b]{% endif %}.
{% endif %}
{# TODO: discuss risk analysis location; clarify how risk controls will be traced to software requirements. #}
Writing software requirements is an art and a science; one must find balance between precision and usefulness.
{% if not system.is_software_only_device %}
The distinction between system requirements and software requirements can be ambiguous.  System requirements describe the requirements of the entire system, including software and hardware.  Software requirements must be tracable to all of the system requirements that they help fulfill.  Software requirements are usually more detailed than the system requirements they refer to.  Many system requirements will be fufilled using both hardware and software.
{% endif %}
The distinction between software requirements and the design is {% if not system.is_software_only_device %}also {% endif %}typically ambiguous.  Requirements should:

- not imply solution
- be verifiable
- be short, ideally one or two sentences long.

Software requirements are often categorized as one of the following types{% if system.auditor_notes %} [5.2.2 and 5.2.3]{% endif %}:

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

m. Risk control measures

Software requirements that implement risk controls should be tied to their originating risk control by tagging them with labels that match the risk control ids{% if system.auditor_notes %} [5.1.1.c]{% endif %}.

To the extent possible, software requirements should be enumerated at the start of the project{% if system.auditor_notes %} [5.2.1]{% endif %}.  If an existing requirement becomes irrelevant, it should be tagged with the `obsolete` label. {% if not system.is_software_only_device %} Software requirements must be tied to one or more originating system requirements by tagging them with labels that match the system requirement ids{% if system.auditor_notes %} [5.1.1.c]{% endif %}.  If a software requirement can not be tied back to any system requirements, new system requirements should be added.{% endif %}

When software requirements are added or changed, re-evaluate the medical device risk analysis{% if system.auditor_notes %} [5.2.4]{% endif %} and ensure that existing software requirements{% if not system.is_software_only_device %}, and system requirements,{% endif %} are re-evaluated and updated as appropriate {% if system.auditor_notes %} [5.2.5]{% endif %}.

**Output:** Software requirements with clearly written descriptions

**Verified By:** Project lead

**Verification:** Ensure software requirements:
{% if not system.is_software_only_device %}
- implement system requirements and are labeled with system requirement ids
- implement risk controls and are labeled with risk control ids
{%- endif %}
- don't contradict each other
- have unambiguous descriptions
- are stated in terms that permit establishment of test criteria and performance of tests to determine whether the test criteria have been met{% if system.auditor_notes %} [5.2.6]{% endif %}.
{% if system.safety_class != 'A' %}
## Architectural Design Activity

**Input:** Software requirements

After the initial set of requirements have been gathered, develop an initial software system architecture and document it in a file named `DESIGN.md` in the root of the project's git repository{% if system.auditor_notes %} [5.3.1]{% endif %}.  This file, which we will refer to as the software system design file, should describe how the software system is divided into software items, and whether these software items are further divided, and so on until the software items are divided no further{% if system.auditor_notes %} [5.4.1]{% endif %}.

Software units are often thought of as being a single function or module, but this is not always appropriate.  Software units must be able to be tested independently, and software items should be divided in a way such that parallels the directory structure of the project.

{# TODO discuss limitations regarding how software items can be divided up in more detail #}
{# TODO add discussion about documenting the flow of data #}
Show the software and hardware interfaces between the software items and external software components{% if system.auditor_notes %} [5.3.2]{% endif %}.  Prefer block diagrams and flow charts to textual descriptions, and include these diagrams in the design file.

Indicate which software items are SOUP.  Include a section in the design files that specifies functional and performance requirements for any SOUP items{% if system.auditor_notes %} [5.3.3]{% endif %}, as well as any hardware or software that is necessary for its intended use{% if system.auditor_notes %} [5.3.4]{% endif %}.
{% if system.safety_class == 'C' %}
Identify any segregation between software items that is essential to risk control, and state how to ensure that the segregation is effective.  For example, one may segregate software items by running them on different processors{% if system.auditor_notes %} [5.3.5]{% endif %}.
{% endif %}
The initial architecture does not need to be complete or final, since code construction often helps guide architectural decisions, however, it is worth spending a significant amount of time on the initial architecture.

**Output:** Design files

**Verification:** Ensure software architecture documented in the design files:

- implements system and software requirements
- is able to support interfaces between software items and between software items and hardware
- is such that the medical device architecture supports proper operation of any SOUP items{% if system.auditor_notes %} [5.3.6]{% endif %}.
{% endif %}
{% if system.safety_class == 'C' %}
## Detailed Design Activity

**Input:** Software system design file

In addition to the software system design file, each software item requires its own detailed design{% if system.auditor_notes %} [5.4.2]{% endif %}.  These detailed designs should be stored as close as possible to their corresponding source files.  For example if a software item is a:

- directory then its detailed design should be stored in a file called `DESIGN.md` in that directory
- file then its detailed design should be stored in a block comment at the top of the file
- function then its detailed design should be stored in a block comment adjacent to the function.

The location of these detailed designs should be indicated in the software system design file.

Detailed designs for interfaces between software items and external components (hardware or software) should be included as appropriate{% if system.auditor_notes %} [5.4.3]{% endif %}.

**Output:** Software item designs

**Verification:** Ensure software requirements:

- implements system and software requirements
- is free from contradiction with the software system design file{% if system.auditor_notes %} [5.4.4]{% endif %}.
{% endif %}
## Unit Implementation Activity

**Input:** {% if system.safety_class == 'C' %}Detailed software item designs{% else %}Software system design file{% endif %} and software requirements

Implement, or partially implement, one or more software items in a new git branch.
Write unit tests and new integration tests as appropriate.

{# TODO: figure out how to fulfill 5.5.2, 5.5.3, an 5.5.4 #}
**Output:** Code changes, stored in un-merged git branches with corresponding pull requests

**Verification:** Ensure the code changes made in the git branch:

- implements the associated change request
- is consistent with the {% if system.safety_class == 'C' %}related detailed designs{% else %}software system design{% endif %}
{%- if system.safety_class == "C" %}
- follows the project's software standards
{%- endif %}
- includes unit tests or justifies why they are not necessary
- is covered by existing integration tests or includes a new integration test{% if system.auditor_notes %} [5.5.5]{% endif %}.
{% if system.safety_class != 'A' %}
## Integration and Integration Testing Activity

{# TODO: address traceability from software items to software system tests; see 5.1.1.c #}

## System Testing Activity
{% endif %}
## Release Activity

**Input:** Implemented and verified change requests for the current milestone

When a new version of the software is released, the git commit corresponding to the state of the code should be [tagged](https://git-scm.com/book/en/v2/Git-Basics-Tagging) with the version number.

{# TODO: add 5.8.1 - 5.8.8 needed for class B and C #}

**Output:** A software release.

# Maintenance Process

## Problem Analysis Activity

Feedback from users, internal testers, and software developers will be recorded in {{ system.feedback_location }}{% if system.auditor_notes %} [6.2.1.1]{% endif %}.
{% block risk_management_process %}
# Risk Management Process
{% endblock %}
# Problem Resolution Process

## Prepare Problem Report Activity

**Input:** Feedback from users or other members of the development team.

Problem reports are stored as GitHub issues tagged with the `problem` label.

When creating a new problem report, include in the issue description:

{# TODO: add "steps to recreate" #}
- The type of problem
- The scope of the problem
- The criticality of the problem
- Any relevant relevant information that can be used to investigate the problem{% if system.auditor_notes %} [9.1]{% endif %}.

{# TODO add examples and guidance regarding type, scope, and criticality; see [9.1] #}
**Output:** Properly formatted and labeled GitHub issues.

## Problem Investigation Activity

**Input:** GitHub issue containing relevant details about the problem.

1. Investigate the problem and if possible identify the cause and record it in comments in the GitHub issue.
2. Evaluate the problem's relevance to safety using the software risk management process {# TODO: add more details about this #}
3. Document the outcome of the investigation and evaluation
4. Create a GitHub issue tagged with the label `request` for actions needed to correct the problem (also include an issue reference to the problem report{% if system.auditor_notes %} [8.2.4.b]{% endif %}), or document the rationale for taking no action{% if system.auditor_notes %} [9.2]{% endif %}.
5. Look through recent problem reports and attempt to identify any adverse trends.  E.g., look to identify certain software items that are failing consistently or have similar causes.  If any trends can be identified, be sure the change requests reverse these trends{% if system.auditor_notes %} [9.6]{% endif %}.

{# TODO: add unit tests to reproduce the failure #}

**If the problem affects devices that have been released, the software developer will make sure quality control is aware of the situation and has enough information to decide whether and how to notify affected parties{% if system.auditor_notes %} [9.3]{% endif %}.**

**Output:** Details about the problem investigation documented in the problem report and either unapproved change requests or justification as to why change requests weren't necessary.

## Implement Change Requests

**Input:** Approved change requests

Once the change requests have been approved, implement them according to our change control process{% if system.auditor_notes %} [9.4]{% endif %}.

**Output:** Code changes required to implement change requests

**Verification:** Ensure code changes:

- all of the change requests have been implemented and merged into the `master` branch
- the original problem is fixed and the problem report closed
- any adverse trends have been reversed{% if system.auditor_notes %} [9.7]{% endif %}.

{%- if system.safety_class != "A" %}
{%- if system.auditor_notes %}[We presume that if our integration tests and system tests are passing, no new problems were introduced, per 9.7.d]{% endif %}
{% endif %}

{# TODO: be sure 9.8 is addressed #}
