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

This document describes a set of activities which will be used during the development and maintenance of {{ system.project_name }}. It is written primarily for software developers.

{{ system.project_name }} is assigned a Class {{ system.safety_class }} software safety class, which means {% if system.safety_class == "A" %}no injury or damage to health{% elif system.safety_class == "B" %}non-serious injury{% else %}death or serious injury{% endif %} could occur if the software fails{% if system.auditor_notes %} [4.3.a]{% endif %}.

The primary purpose of this document is to help developers ensure {{ system.project_name }} is safe and useful while also allowing developers to be productive.  The secondary purpose is to comply with {{ system.standard }}.
{%- if system.auditor_notes %}

[In order to assist auditors and regulators, we have included section references to {{ system.standard }} as well as occasional comments throughout this document.  These references and comments are always placed inside square brackets, and they are not present in the software-developer version of the document.  Other than these comments, the software-developer version is identical to the auditor version of this document.]{% endif %}
{% endblock %}
# Overview

## Definitions
{% if system.auditor_notes %}
[Most of these definitions are very similar to the {{ system.standard }} definitions, however, they have been simplified and clarified as appropriate for a better understanding by software developers.]
{% endif %}
An **activity** is a set of one or more interrelated or interacting tasks.  An activity has an input, an output, and often an explicit verification task{% if system.auditor_notes %} [We do not explicitly demarcate tasks in this document]{% endif %}.

Three terms identify the software decomposition.  The top level is the **software system**. The lowest level that is not further decomposed is the **software unit**.  All levels of composition, including the top and bottom levels, can be called **software items**.  A software system, then, is composed of one or more software items, and each software item is composed of one or more software units or decomposable software items.  See the software system design file for a description of how {{ system.project_name }} is decomposed into software items.

**SOUP**, or **software of unknown provenance**, is a software item that is already developed and generally available and that has not been developed for the purpose of being incorporated into the medical device (also known as "off-the-shelf software") or software previously developed for which adequate records of the development processes are not available.

A **problem report** is a record of actual or potential behaviour of a software product that a user or other interested person believes to be unsafe, inappropriate for the intended use or contrary to specification.  Problem reports are stored as GitHub issues with the `bug` label.

A **change request** is a documented specification of a change to be made to a software product.  Change requests are stored as GitHub issues that do not have the `bug` label.  All work on the software project should occur in response to change requests{% if system.auditor_notes %} [8.2.1]{% endif %}.

A **software requirement** is a particular function that the software must support, or some other constraint that the software must fulfill.  Requirements describe the *what*, while specifications and designs specify the *how*.

{% block extra_definitions %}
{%- endblock %}
## Development Life Cycle Model

{{ system.project_name }} will be developed using an agile (i.e., evolutionary/incremental) software development life cycle model.  The agile strategy develops the software system using a sequence of builds.  Customer needs and software system requirements are partially defined up front, then are refined in each succeeding build{% if system.auditor_notes %} [5.1.1]{% endif %}.

## Roles and Responsibilities

The processes described in this document are designed for a team composed of a project lead and one to eight software developers.  One of the software developers shall be assigned the role of the project lead.  The project lead, working on behalf of the manufacturer, is responsible for the safety and utility of the software system built by the team.

{% block documents %}
## Related Documents

[TODO: address 5.1.8]

- SRS
- SDS
- Revision History
- Unaddressed Anomolies
- Problem Reports
- Test Records
- README

{% endblock %}
{%- block project_details %}{% endblock %}

# Activities

This section of the software plan describes the various activities involved with software development, maintenance, and problem resolution.  The relationship between the inputs and outputs of these activities are displayed in the following diagram and are fully described in the sub-sections below.

Since we are using an evolutionary development life cycle, activities may be performed before their inputs have settled.  As a result, activity inputs and outputs may not be consistent in between releases.

{% if system.auditor_notes %}[This software plan does not explicitly separate the software development process, software maintenance process, configuration management process, and problem resolution process because we are using an evolutionary software development life cycle and thus the processes overlap with one another significantly.  The activities described here fulfill 5.1.1.a, 5.1.1.b, 5.1.6, and 5.1.9.b]{% endif %}

## Activity Diagram

![Overview of life-cycle processes](../images/lifecycle-processes.svg)

## Planning

[TODO: address 5.1.7]

**Input:**  System requirements and risk controls

Setup a git repository on GitHub.  All software activity outputs will be stored in this git repository, the associated GitHub issues, or the associated GitHub pull requests, unless explicitly noted otherwise{% if system.auditor_notes %} [5.1.1.b]{% endif %}.  The software developers working on the project are responsible for keeping all software activity outputs within version control at the times specified in the activity descriptions{% if system.auditor_notes %} [5.1.9.c, 5.1.9.d, and 5.1.9.e]{% endif %}.
{% if system.auditor_notes %}
[Note that we do not explicitly use the term "software configuration management" since many developers will be unfamiliar with the term, and instead we use the term "version control."  Git is a version control system that makes it simple to track and record the history of every file it contains in a precise and controller manner.

The requirements listed in sections 5.1.9.a, 5.1.11, 8.1.1, 8.1.3, 8.3, and 9.5 of {{ system.standard }} are fulfilled by our use of Git and GitHub.  Also note that this setup implies that all activity outputs that are stored in the git repository, GitHub issues, or GitHub pull requests are configuration items.  Furthermore, the version of every configuration item comprising the software system configuration is stored in the git repository for the entire history of the project.  Each activity describes the configuration items in more detail.]
{% endif %}

Details about the project's build process, including tool versions, environment variables, etc. should be recorded in the file called `README.md` in the top directory of the git repository{% if system.auditor_notes %} [5.1.10]{% endif %}.  The build process must be repeatable and, as appropriate, automated{% if system.auditor_notes %} [5.8.5]{% endif %}.  The `README` should discuss how the build process is made repeatable{% if system.auditor_notes %} [5.8.8]{% endif %}.

At the start of the project, the project lead should fill in the place-holder sections of this software plan.  The planning document must be kept up to date as the project commences{% if system.auditor_notes %} [5.1.2]{% endif %}.

**Output:** The markdown version of this plan document.

**Verification:**

Review the document for typos our outdated information.

Ensure that activity in the software plan specifies:

- the activity inputs
- deliverables (i.e., outputs)
- output verification steps (if there are any)
- which role should perform and verify the activity (if it is not included in the activity diagram){% if system.auditor_notes %} [5.1.6.a and 5.1.6.b]{% endif %}.

## Requirements Analysis

**Input:** System requirements and risk controls

{% if not system.is_software_only_device %}
Record system requirements in {{ system.system_requirements_location }}.  Each system requirement must have a unique identifier so that we can trace software requirements back to the system requirements they fulfill{% if system.auditor_notes %} [5.1.3]{% endif %}.
{% endif %}
[TODO: discuss risk analysis location; clarify how risk controls will be traced to software requirements.]
Writing software requirements is an art and a science; one must find balance between precision and usefulness.
{% if not system.is_software_only_device %}
The distinction between system requirements and software requirements can be challenging.  System requirements describe the requirements of the entire system, including software and hardware.  Software requirements must be traceable to all of the system requirements that they help fulfill.  Software requirements are usually more detailed than the system requirements they refer to.  Many system requirements will be fulfilled using both hardware and software.
{% endif %}
The distinction between software requirements and the design is {% if not system.is_software_only_device %}also {% endif %}typically challenging.  Requirements should:

- not imply solution
- be verifiable
- be short, ideally one or two sentences long.

Software requirements are often categorized as one of the following types{% if system.auditor_notes %} [5.2.2 and 5.2.3]{% endif %}:

a. Functional and capability requirements
  - performance (e.g., purpose of software, timing requirements),
  - physical characteristics (e.g., code language, platform, operating system),
  - computing environment (e.g., hardware, memory size, processing unit, time zone, network infrastructure) under which the software is to perform, and
  - need for compatibility with upgrades or multiple SOUP or other device versions.

b. Software system inputs and outputs
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

To the extent possible, software requirements should be enumerated at the start of the project{% if system.auditor_notes %} [5.2.1]{% endif %}.{% if not system.is_software_only_device %} Software requirements must be tied to one or more originating system requirements via the system requirement's ids{% if system.auditor_notes %} [5.1.1.c]{% endif %}.  If a software requirement can not be tied back to any system requirements, new system requirements should be added.{% endif %}

When software requirements are added or changed, re-evaluate the medical device risk analysis{% if system.auditor_notes %} [5.2.4]{% endif %} and ensure that existing software requirements{% if not system.is_software_only_device %}, and system requirements,{% endif %} are re-evaluated and updated as appropriate {% if system.auditor_notes %} [5.2.5]{% endif %}.

**Output:** Software requirements with clearly written descriptions

**Verification:** Ensure software requirements:
{% if not system.is_software_only_device %}
- implement system requirements and are labeled with system requirement ids
- implement risk controls and are labeled with risk control ids
{%- endif %}
- don't contradict each other
- have unambiguous descriptions
- are stated in terms that permit establishment of test criteria and performance of tests to determine whether the test criteria have been met{% if system.auditor_notes %} [5.2.6]{% endif %}.
{% if system.safety_class != 'A' %}
## Architectural Design

**Input:** Software requirements

After the initial set of requirements have been gathered, develop an initial software system architecture and document it in the software design specification (or SDS){% if system.auditor_notes %} [5.3.1]{% endif %}.  The SDS should describe how the software system is divided into software items, and whether these software items are further divided, and so on until the software items are divided no further{% if system.auditor_notes %} [5.4.1]{% endif %}.

Software units are often thought of as being a single function or module, but this is not always appropriate.  Software units must be able to be tested independently, and software items should be divided in a way such that parallels the directory structure of the project.

{# TODO discuss limitations regarding how software items can be divided up in more detail #}
{# TODO add discussion about documenting the flow of data #}
Show the software and hardware interfaces between the software items and external software components{% if system.auditor_notes %} [5.3.2]{% endif %}.  Prefer block diagrams and flow charts to textual descriptions, and include these diagrams in the SDS.

Indicate which software items are SOUP.  Include a section in the SDS that specifies functional and performance requirements for any SOUP items{% if system.auditor_notes %} [5.3.3]{% endif %}, as well as any hardware or software that is necessary for its intended use{% if system.auditor_notes %} [5.3.4]{% endif %}.
{% if system.safety_class == 'C' %}
Identify any segregation between software items that is essential to risk control, and state how to ensure that the segregation is effective.  For example, one may segregate software items by running them on different processors{% if system.auditor_notes %} [5.3.5]{% endif %}.
{% endif %}
The initial architecture does not need to be complete or final, since code construction often helps guide architectural decisions, however, it is worth spending a significant amount of time on the initial architecture.  Once development commences (i.e., the Unit Implementation and Testing activity), update the SDS as the architecture is refined.

**Output:** SDS

**Verification:** Ensure software architecture documented in the SDS:

- implements system and software requirements
- is able to support interfaces between software items and between software items and hardware
- is such that the medical device architecture supports proper operation of any SOUP items{% if system.auditor_notes %} [5.3.6]{% endif %}.
{% endif %}
## Division of Labor

**Input:** Design files

Once the architectural designs for new or updated software requirements have been created, the next step is to plan out the steps involved with implementing this design.  In particular, via the creation of one or more change requests.  There are many ways to divide new requirements work into change requests.  As a general rule, requirements which will be addressed sooner should be split up into smaller change requests.  A feature which may not be worked on for several months can be captured in a single change request, which can be split up into smaller more detailed change requests once we are about to begin implementing it.

**Output:** Feature change requests

**Verification:** Not applicable to this activity

## Release Planning

**Input:** Feature and problem fix change requests

In order to organize and prioritize the development work, change requests are assigned to GitHub milestones.  Change requests that have not yet been assigned to a GitHub milestone have not yet been approved, and should not be worked on since approval explicitly required by {{ system.standard }}{% if system.auditor_notes %} [8.2.1]{% endif %}.

Once a change request is assigned to a milestone, it has been "approved" and may be worked on by a developer.  The project lead will then assign developers to change requests to divide up the work.  Software developers may also assign themselves to change requests, so long as it is not assigned to another developer and they don't have other outstanding tickets they can work on.

The project lead is responsible for coordinating with the business owner regarding which features to prioritize for a release.  Also, any outstanding problem reports must be addressed by the end of the release{% if system.auditor_notes %} [9.4]{% endif %}.

[TODO: add details about 6.1.f here]

**Output:** The set of change requests which should be implemented for the next release

**Verification:** Not applicable to this activity

{% if system.safety_class == 'C' %}
## Detailed Design

**Input:** Software system design file

Begin a new git branch, as discussed in the Unit Implementation and Testing activity, but before implementing the change request, document a detailed design either within the SDS or as code comments, as appropriate, for each new software item{% if system.auditor_notes %} [5.4.2]{% endif %}.  These detailed designs should be stored as closely as possible to their corresponding source files.  As appropriate, write out function signatures for the essential procedures, functions, classes, and/or modules involved with the change request.

Detailed designs for interfaces between software items and external components (hardware or software) should be included as appropriate{% if system.auditor_notes %} [5.4.3]{% endif %}.

Once you have completed the detailed design, open a pull request and assign the project lead to review the design.

**Output:** Software item designs

**Verification:** Ensure software requirements:

- is not more complicated than it needs to be to meet the requirements
- implements system and software requirements
- is free from contradiction with the software system design file{% if system.auditor_notes %} [5.4.4]{% endif %}.
{% endif %}
## Unit Implementation and Testing

{% if system.auditor_notes %}[This activity addresses 5.5.1]{% endif %}

**Input:** {% if system.safety_class == 'C' %}Detailed software item designs{% else %}Software system design file{% endif %} and software requirements

When beginning work on a change request with an id of `104`, developers should open a new Git branch named `104-short-description` (or `feature/104-short-description`).  All development work should be committed and pushed periodically within this Git branch{% if system.auditor_notes %} [5.1.1.d and 8.2.2]{% endif %}.  Commit messages should:

- explain why the current changes are being made, especially when it is not obvious
- reference the change request it was made in (the `rdm hooks` command can streamline this).

Write unit tests and new integration tests as appropriate.

If new software dependencies are added, removed, or changed, the `soup.yaml` file should be updated.  See the SOUP Components document for additional details.  Note that the information in the `soup.yaml` file may duplicate information found in other files (e.g., `requirements.txt` or `package.json`).  Also, it is recognized that keeping track of secondary dependencies can require significant effort---think carefully before adding new SOUP to {{ system.project_name }}{% if system.auditor_notes %} [See the SOUP Components document for details about how 5.1.1.d, 5.3.3, 5.3.4, 7.1.3, and 8.1.2 are met]{% endif %}.

When work on a change branch is nearing completion, a GitHub pull request should be created for this branch.

[TODO: figure out how to fulfill 5.5.2, 5.5.3, an 5.5.4]

**Output:** Code changes, stored in un-merged git branches with corresponding approved pull requests

**Verification:** Assign at least one other developer to be the reviewer within the GitHub pull request.

Code review should ensure the code changes made in the git branch:

- implements the associated change request
- is consistent with the {% if system.safety_class == 'C' %}related detailed designs{% else %}software system design{% endif %}
{%- if system.safety_class == "C" %}
- follows the project's software standards
{%- endif %}
- includes unit tests or justifies why they are not necessary
- is covered by existing integration tests or includes a new integration test{% if system.auditor_notes %} [5.5.5 and 8.2.3]{% endif %}.

If the reviewer requested any changes, address them and re-submit the review once they have been addressed.  The reviewer should approve the pull request from within the GitHub user interface{% if system.auditor_notes %} [8.2.4.c]{% endif %}.

{%- if system.safety_class != 'C' %}
Occasionally, due to the absence of other reviewers or due to an internal testing deadline, it may be necessary to skip verification.  When this occurs, the developer should justify why a review wasn't necessary within the pull request comments.
{% endif %}

## Integration

[TODO: address traceability from software items to software system tests; see 5.1.1.c]

**Input:** Unmerged, but approved, pull-request

Merge the approved git branch into the `master` git branch, correct any merge conflicts that occur.  Once the branch has been merged successfully, delete the branch in GitHub{% if system.auditor_notes %} [5.1.5 and 5.6.1]{% endif %}.

**Output:** Merged pull request

## Integration and System Testing

**Input:** Software system built using the changes from this release's change requests

[TODO: write out details about the test record format [9.8, 5.6.7, 5.7.5]]

**Output:** Test record

**Verification:** Ensure code changes:

- the original problem is fixed and the problem report closed{% if system.auditor_notes %} [9.7.a]{% endif %}
- any adverse trends have been reversed{% if system.auditor_notes %} [9.7.b]{% endif %}.

{%- if system.auditor_notes %}[We presume that if our integration tests and system tests are passing, no new problems were introduced, per 9.7.d]{% endif %}

## Release

**Input:** Implemented and verified change requests for the current milestone

When a new version of the software is released, the git commit corresponding to the state of the code should be [tagged](https://git-scm.com/book/en/v2/Git-Basics-Tagging) with the version number.

{%- block software_archival_task %}
{%- endblock %}

Archived releases shall be kept until there are no longer supported devices being used that run the version of the software.

{% if system.auditor_notes %}[This section fulfills 5.8.7; note that documentation and configuration items are archived automatically due to the fact that they are stored in Git]{% endif %}

**Output:** An archived software release

**Verification:** Ensure that

- all of the planned change requests have been implemented and integrated{% if system.auditor_notes %} [5.6.2 and 9.7.c]{% endif %}
- the outputs of each activity are in a consistent state{% if system.auditor_notes %} [5.1.6.c, 5.1.6.d, and 5.8.6]{% endif %}
- the SDS is accurate and up-to-date
- the Unresolved Anomolies Document is up-to-date and none of the anomlies result in unacceptable risk{% if system.auditor_notes %} [5.8.2 and 5.8.3]{% endif %}
- the Revision Level History Document is up-to-date{% if system.auditor_notes %} [5.8.4]{% endif %}
- Integration and System Testing has been completed after the last change request was integrated{% if system.auditor_notes %} [5.8.1]{% endif %}

## Problem Analysis

Feedback from users, internal testers, and software developers will be recorded in {{ system.feedback_location }}{% if system.auditor_notes %} [6.2.1.1]{% endif %}.

## Prepare Problem Report

**Input:** Feedback from users or other members of the development team

A problem report should be created whenever:

1. a user reports a problem while using a released version of the software system, or
2. when an internal user reports a new problem that has been found during software development or maintenance{% if system.auditor_notes %} [5.1.1.e and 5.1.9.f]{% endif %}.

When creating a new problem report, include in the description:

{# TODO: add "steps to recreate" #}
- The type of problem
- The scope of the problem
- The criticality of the problem
- Any relevant relevant information that can be used to investigate the problem{% if system.auditor_notes %} [9.1]{% endif %}.

{# TODO add examples and guidance regarding type, scope, and criticality; see [9.1] #}
**Output:** The problem report (a properly formatted and labeled GitHub issue)

## Problem Investigation

**Input:** The problem report

1. Investigate the problem and if possible identify the cause and record it in the problem report
2. Evaluate the problem's relevance to safety using the software risk management process {# TODO: add more details about this #}
3. Summarize the conclusions from the investigation in the problem report
4. Create a change request for actions needed to correct the problem (also include an issue reference to the problem report{% if system.auditor_notes %} [8.2.4.a and 8.2.4.b]{% endif %}), or document the rationale for taking no action and tag the problem report with the `wontfix` label{% if system.auditor_notes %} [9.2]{% endif %}.
5. Look through recent problem reports and attempt to identify any adverse trends.  E.g., look to identify certain software items that are failing consistently or have similar causes.  If any trends can be identified, be sure the change requests reverse these trends{% if system.auditor_notes %} [9.6]{% endif %}.

**If the problem affects devices that have been released, make sure that quality control is aware of the situation and has enough information to decide whether and how to notify affected parties.  Record who you notified in the problem report{% if system.auditor_notes %} [9.3]{% endif %}.**

**Output:** Details about the problem investigation documented in the problem report and either unapproved change requests or justification as to why change requests weren't necessary
