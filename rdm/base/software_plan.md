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

This document describes a set of activities which will be used during software risk management, development, and maintenance of {{ system.project_name }}.  It is written primarily for software developers.

{{ system.project_name }} is assigned a Class {{ system.safety_class }} software safety class, which means {% if system.safety_class == "A" %}no injury or damage to health{% elif system.safety_class == "B" %}non-serious injury{% else %}death or serious injury{% endif %} could occur if the software fails{% if system.auditor_notes %} [62304:4.3.a]{% endif %}.

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

The **software system** refers to the entire software portion of {{ system.project_name }}.  The software system is decomposed into **software items**, each of which may be further decomposed into smaller software items.  All levels of composition, including the top and bottom levels, can be called a software item.  See the software system design file for a description of how {{ system.project_name }} is decomposed into software items.

**SOUP**, or **software of unknown provenance**, is a software item that is already developed and generally available and that has not been developed for the purpose of being incorporated into the medical device (also known as "off-the-shelf software") or software previously developed for which adequate records of the development processes are not available.

A **problem report** is a record of actual or potential behaviour of a software product that a user or other interested person believes to be unsafe, inappropriate for the intended use or contrary to specification.  Problem reports are stored as GitHub issues tagged with the `bug` label.

A **change request** is a documented specification of a change to be made to the software system.  Change requests are stored as GitHub issues that are not tagged with the `bug` label.  All work on the software project should occur in response to change requests{% if system.auditor_notes %} [62304:8.2.1]{% endif %}.

A **software requirement** is a particular function that the software must support, or some other constraint that the software must fulfill.  Requirements describe the *what*, while specifications and designs specify the *how*.

{% block extra_definitions %}{% endblock %}

## Development Life Cycle Model

{{ system.project_name }} will be developed using an agile (i.e., evolutionary/incremental) software development life cycle model.  The agile strategy develops the software system using a sequence of builds.  Customer needs and software system requirements are partially defined up front, then are refined in each succeeding build{% if system.auditor_notes %} [62304:5.1.1]{% endif %}.

## Roles and Responsibilities

The processes described in this document are designed for a team composed of a project lead and one to eight software developers.  One of the software developers shall be assigned the role of the project lead.  The project lead, working on behalf of the manufacturer, is responsible for the safety and utility of the software system built by the team.

At least one team member must be trained in risk management{% if system.auditor_notes %} [14971:3.3]{% endif %}.

{% block documents %}
## Related Documents

{% if system.auditor_notes %}[This section fulfills 62304:5.1.8]{% endif %}

- The Software Requirements Specification (or SRS) describes what the software needs to accomplish.  It is largely written by the Project Lead during the Requirements Analysis activity, and is reviewed by the Project Lead during the Release activity.  Software developers may clarify and extend the document slightly during the Unit Implementation and Design activity.
- The Software Design Specification (or SDS) describes how the software accomplishes what the SRS requires.  A significant portion is written by the Project Lead during the Architectural Design activity, but many details and specifics are added by Software Developers during the Unit Implementation and Design activity.  It is reviewed for consistency by the Project Lead during the Release activity.
- The Revision History is a listing of changes that have been made during a release; it is slowly built up by software developers during the Implementation and Design activity.  It is reviewed by the Project Lead during the Release activity.
- The Known Anomalies is a list of outstanding issues with the software, and why we do not need to address them.  The document is generated from outstanding problem requests, which are written and verified during the Problem Report Preparation activity.  It is reviewed by the Project Lead during the Release activity.
- The Level of Concern document is written by the Project Lead, in conjunction with the manufacturer, up front.  Its purpose is to help guide the Risk Analysis and inform the FDA.  It may be updated as part of Risk Analysis.  It is reviewed by the Project Lead during the Release activity.

{% endblock %}
{%- block project_details %}{% endblock %}

# Activities

This section of the software plan describes the various activities involved with software development, maintenance, and problem resolution.  The relationship between the inputs and outputs of these activities are displayed in the following diagram and are fully described in the sub-sections below.

Since we are using an evolutionary development life cycle, activities may be performed before their inputs have settled.  As a result, activity inputs and outputs may not be consistent in between releases.

{% if system.auditor_notes %}[This software plan does not explicitly separate the software development process, software maintenance process, configuration management process, problem resolution process, and software-related risk management because we are using an evolutionary software development life cycle and thus the processes overlap with one another significantly.  The activities described here fulfill 62304:5.1.1.a, 5.1.1.b, 5.1.6, and 5.1.9.b as well as, software-related portions 14971:3.4.a, 3.4.b, 3.4.c, and 3.4.e]{% endif %}

## Activity Diagram

![Overview of life-cycle processes](../images/lifecycle-processes.svg)

{% block activity_planning -%}
## Planning

[TODO: address 62304:5.1.7]

**Input:**  System requirements and risk controls

Setup a git repository on GitHub.  All software activity outputs will be stored in this git repository, the associated GitHub issues, or the associated GitHub pull requests, unless explicitly noted otherwise{% if system.auditor_notes %} [62304:5.1.1.b]{% endif %}.  The software developers working on the project are responsible for keeping all software activity outputs within version control at the times specified in the activity descriptions{% if system.auditor_notes %} [62304:5.1.9.c, 5.1.9.d, and 5.1.9.e]{% endif %}.
{% if system.auditor_notes %}
[Note that we do not explicitly use the term "software configuration management" since many developers will be unfamiliar with the term, and instead we use the term "version control."  Git is a version control system that makes it simple to track and record the history of every file it contains in a precise and controller manner.

The requirements listed in sections 5.1.9.a, 5.1.11, 8.1.1, 8.1.3, 8.3, and 9.5 of IEC62304 are fulfilled by our use of Git and GitHub.  Also note that this setup implies that all activity outputs that are stored in the git repository, GitHub issues, or GitHub pull requests are configuration items.  Furthermore, the version of every configuration item comprising the software system configuration is stored in the git repository for the entire history of the project.  Each activity describes the configuration items in more detail.]
{% endif %}

Record details about the project's build process, including tool versions, environment variables, etc. in the file called `README.md` in the top directory of the git repository{% if system.auditor_notes %} [62304:5.1.10]{% endif %}.  The build process must be repeatable and, as appropriate, automated{% if system.auditor_notes %} [62304:5.8.5]{% endif %}.  The `README` should discuss how the build process is made repeatable{% if system.auditor_notes %} [62304:5.8.8]{% endif %}.

Fill in the place-holder sections of this software plan.  Keep this planning document up to date as the project commences{% if system.auditor_notes %} [62304:5.1.2]{% endif %}.

{% block activity_planning_risk_acceptability -%}
In conjunction with the manufacturer's management, review and update as appropriate the:

- qualitative risk severity categories
- qualitative risk probability categories
- qualitative risk levels

contained within the `risk.yml` file{% if system.auditor_notes %} [14971:3.4.d, D.3, D.4, D.8]{% endif %}.
{%- endblock %}

**Output:** The markdown version of this plan document.

**Verification:**

Review the document for typos our outdated information.

Ensure that activity in the software plan specifies:

- the activity inputs
- deliverables (i.e., outputs)
- output verification steps (if there are any)
- which role should perform and verify the activity (if it is not included in the activity diagram){% if system.auditor_notes %} [62304:5.1.6.a and 5.1.6.b]{% endif %}.
{%- endblock %}

## Requirements Analysis

**Input:** System requirements and risk controls

{% if not system.is_software_only_device %}
Record system requirements in {{ system.system_requirements_location }}.  Each system requirement must have a unique identifier so that we can trace software requirements back to the system requirements they fulfill{% if system.auditor_notes %} [62304:5.1.3]{% endif %}.
{% endif %}

To the extent possible, software requirements should be enumerated at the start of the project{% if system.auditor_notes %} [62304:5.2.1]{% endif %}.{% if not system.is_software_only_device %} Software requirements must be tied to one or more originating system requirements via the system requirement's ids{% if system.auditor_notes %} [62304:5.1.1.c]{% endif %}.  If a software requirement can not be tied back to any system requirements, new system requirements should be added.{% endif %}

The appendices have additional guidance about [requirements analysis](#requirements-analysis).

When software requirements are added or changed, re-evaluate the medical device risk analysis{% if system.auditor_notes %} [62304:5.2.4]{% endif %} and ensure that existing software requirements{% if not system.is_software_only_device %}, and system requirements,{% endif %} are re-evaluated and updated as appropriate {% if system.auditor_notes %} [62304:5.2.5]{% endif %}.

**Output:** Software requirements with clearly written descriptions

**Verification:** Ensure software requirements:
{% if not system.is_software_only_device %}
- implement system requirements and are labeled with system requirement ids
- implement risk controls
{%- endif %}
- don't contradict each other
- have unambiguous descriptions
- are stated in terms that permit establishment of test criteria and performance of tests to determine whether the test criteria have been met{% if system.auditor_notes %} [62304:5.2.6]{% endif %}.
{% if system.safety_class != 'A' %}
## Architectural Design

**Input:** Software requirements

Develop an initial software system architecture and document it in the software design specification (or SDS){% if system.auditor_notes %} [62304:5.3.1]{% endif %}.  The SDS should describe how the software system is divided into a hierarchy of software items{% if system.auditor_notes %} [62304:5.4.1]{% endif %}.  Software units are often thought of as being a single function or module, but this is not always appropriate.

{# TODO add discussion about documenting the flow of data #}
Show the software and hardware interfaces between the software items and external software{% if system.auditor_notes %} [62304:5.3.2]{% endif %}.  Prefer block diagrams and flow charts to textual descriptions, and include these diagrams in the SDS.  Indicate which software items are SOUP.

{% if system.safety_class == 'C' %}
Identify any segregation between software items that is essential to risk control, and state how to ensure that the segregation is effective.  For example, one may segregate software items by running them on different processors{% if system.auditor_notes %} [62304:5.3.5]{% endif %}.
{% endif %}
The initial architecture does not need to be complete, since code construction can guide architectural decisions. However, it is worth spending a significant amount of time on the initial architecture.  Once development commences (i.e., the Unit Implementation and Testing activity), update the SDS as the architecture is refined.

**Output:** SDS

**Verification:** Ensure software architecture documented in the SDS:

- implements system and software requirements
- is able to support interfaces between software items and between software items and hardware
- is such that the medical device architecture supports proper operation of any SOUP items{% if system.auditor_notes %} [62304:5.3.6]{% endif %}.
{% endif %}
## Risk Assessment

{% if system.auditor_notes %}[This activity is meant to fulfill sections 4, 5, 6.1, and 6.2 of 14971 with respect to software related risks]{% endif %}

**Input:** Software design specification

See the appendices for an [introduction to software risk management](#risk-management) and details about the format of the `risk.yml` file.

Begin by identifying known and forseeably hazards associated with{% if system.is_software_only_device %} how the software is intended to be used within medical practice{% else %} the device{% endif %}{% if system.auditor_notes %} [14971:4.3]{% endif %}.  It is frequently necessary to consult with a clinical expert to understand and identify hazards in their clinical context.

Next, identify which software items may expose these hazards (i.e., cause hazardous situations){% if system.auditor_notes %} [62304:7.1.1]{% endif %}, and list them, along with the forseeably causes.  Consider:

- whether requirements are appropriate and are meeting the needs of users
- incorrect or incomplete specifications of functionality
- software defects in the software item (including in SOUP)
- how hardware failures or software defects in other items could result in unpredictable operation
- reasonably forseeably misuse by users{% if system.auditor_notes %} [62304:7.1.2]{% endif %}.

If failure or unexpected results from SOUP is a potential cause contributing to a hazardous situation, review the list of anomalies for the SOUP (if any) for known anomalies relevant to this hazardous situation{% if system.auditor_notes %} [62304:7.1.3]{% endif %}.

Include the identified hazards, causes, hazardous situations, and harms in the `risk.yml` file as an individual risk{% if system.auditor_notes %} [62304:7.1.4]{% endif %}.

Finally, estimate the severity and probability of each risk and record this as well{% if system.auditor_notes %} [14971:4.4]{% endif %}.

**Output:** Risk assessment

## Risk Control

**Input:** Risk assessment

Evaluate unmitigated risks listed in `risk.yml`{% if system.auditor_notes %} [14971:5]{% endif %}.{# TODO: for now, evaluating risks based on their probability and severity is a manual process.  This should be automated with a tool sometime in the near future #}

If any of the risks require reduction, then identify appropriate risk control measures.  Consider risk control measure options, in the following order:

1. inherent safety by design (i.e., refactoring or architecting away the risks, or even removing requirements)
2. adding software{% if not system.is_software_only_device %} or hardware{% endif %}
3. providing information to the user in the form of documentation or user interface elements---these should be avoided as much as possible.

Create a change request for the risk control measure.

**Output:** Risk control related change requests

## Division of Labor

**Input:** Design files

Once the architectural designs for new or updated software requirements have been created, the next step is to plan out the steps involved with implementing this design.  In particular, via the creation of one or more change requests.  There are many ways to divide new requirements work into change requests.  As a general rule, requirements which will be addressed sooner should be split up into smaller change requests.  A feature which may not be worked on for several months can be captured in a single change request, which can be split up into smaller more detailed change requests once we are about to begin implementing it.

**Output:** Feature change requests

**Verification:** Not applicable to this activity

## Release Planning

{% if system.auditor_notes %}[This activity addresses 62304:6.3.1, since change requests resulting from maintenance and problem resolution are processed in the same manner in which risk control measures and feature change requests are.]{% endif %}

**Input:** Feature and problem fix change requests

To organize and prioritize the development work, change requests are assigned to GitHub milestones.  Change requests that have not yet been assigned to a GitHub milestone have not yet been approved, and should not be worked on (approval is explicitly required by the IEC62304 standard){% if system.auditor_notes %} [62304:8.2.1, 6.2.4]{% endif %}.

Once a change request is assigned to a milestone, it has been "approved" and may be worked on by a developer.  The project lead will then assign developers to change requests to divide up the work.  Software developers may also assign themselves to change requests, so long as it is not assigned to another developer and they don't have other outstanding tickets they can work on.

The project lead should coordinate with the business owner regarding which change requests to include in a release.  When planning a release:

- Consider outstanding problem reports{% if system.auditor_notes %} [62304:9.4]{% endif %}.
- Look through historical problem reports and attempt to identify any adverse trends.  For example, look to identify certain software items that are failing consistently or have similar causes.  If any trends can be identified, be sure the change requests reverse these trends{% if system.auditor_notes %} [62304:9.6 and 14971:9]{% endif %}.
- Review the `risk.yml` file and verify that change requests for risk control measures have been implemented{% if system.auditor_notes %} [62304:7.3.1 and 7.2.2.c]{% endif %}.
- Review the SOUP items listed in `soup.yml` for SOUP which has become obsolete, SOUP which should be upgraded, and also review the published anomalies lists as appropriate{% if system.auditor_notes %} [62304:6.1.f]{% endif %}.  See the appendices for additional details.  Create change requests as appropriate.

**Output:** The set of change requests which should be implemented for the next release

**Verification:** Not applicable to this activity

{% if system.safety_class == 'C' %}
## Detailed Design

**Input:** Software system design file

Begin a new git branch, as discussed in the Unit Implementation and Testing activity, but before implementing the change request, document a detailed design either within the SDS or as code comments, as appropriate, for each new software item{% if system.auditor_notes %} [62304:5.4.2]{% endif %}.  These detailed designs should be stored as closely as possible to their corresponding source files.  As appropriate, write out function signatures for the essential procedures, functions, classes, and/or modules involved with the change request.

Detailed designs for interfaces between software items and external components (hardware or software) should be included as appropriate{% if system.auditor_notes %} [62304:5.4.3]{% endif %}.

Once you have completed the detailed design, open a pull request and assign the project lead to review the design.

**Output:** Software item designs

**Verification:** Ensure software requirements:

- is not more complicated than it needs to be to meet the requirements
- implements system and software requirements
- is free from contradiction with the software system design file{% if system.auditor_notes %} [62304:5.4.4]{% endif %}.
{% endif %}
## Unit Implementation and Testing

{% if system.auditor_notes %}[This activity addresses 62304:5.5.1]{% endif %}

**Input:** {% if system.safety_class == 'C' %}Detailed software item designs{% else %}Software system design file{% endif %} and software requirements

Create a new Git branch with a name that includes the change request number (e.g., `104-short-description`).  Commit your code changes to this branch and push periodically{% if system.auditor_notes %} [62304:5.1.1.d, 6.1.e and 8.2.2]{% endif %}.  Commit messages should:

- explain why the current changes are being made, as appropriate
- reference the change request it was made in (the `rdm hooks` command can streamline this).

During development, as appropriate:

{% if system.safety_class != 'C' -%}
- Write specifications for new software items.
- Update the software architecture diagrams.{% endif %}
- Analyze how this change request effects the entire software system, whether any software items be refactored or reused{% if system.auditor_notes %} [6.2.3]{% endif %}.
- Consider whether any external systems that the software system interfaces with may be affected{% if system.auditor_notes %} [6.2.3]{% endif %}.
- If software has been released, consider whether any existing data needs to be migrated.
- Write unit tests and new integration tests.
- If SOUP was added, removed, or changed, update the `soup.yaml` file (see the appendices and SOUP Components document for details){% if system.auditor_notes %} [See the SOUP Components document for details about how we meet 62304:5.1.1.d, 5.3.3, 5.3.4, 7.1.3, and 8.1.2]{% endif %}.
- If the change request includes risk control measures, record the risk control measures in the `risk.yml` file along with the residual risk.  Also add new software requirements for the risk control measure and record the software requirement id along with the risk{% if system.auditor_notes %} [14971:6.2 and 62304:7.2.2.a]{% endif %}.
- Perform the risk assessment{% if system.auditor_notes %} [14971:6.6]{% endif %} and risk control activities on any software items (including SOUP) which were are added or modified, including new risk control measures, since they may have introduced new risks{% if system.auditor_notes %} [62304:6.1.c, 7.4 and 7.3.1, since risk control measures will be implemented as part of this activity]{% endif %}.

When work on a change branch is nearing completion, a pull request should be created for this branch.

[TODO: figure out how to fulfill 62304:5.5.2, 5.5.3, an 5.5.4]

**Output:** Code and documentation changes, stored in un-merged git branches with corresponding approved pull requests

**Verification:** Assign at least one other developer to be the reviewer within the GitHub pull request.

Code review should ensure the code changes made in the git branch:

- implements the associated change request
- is consistent with the {% if system.safety_class == 'C' %}related detailed designs{% else %}software system design{% endif %}
{%- if system.safety_class == "C" %}
- follows the project's software standards
{%- endif %}
- includes unit tests or justifies why they are not necessary
- any risk assessments are reasonable
- is covered by existing integration tests or includes a new integration test{% if system.auditor_notes %} [62304:5.5.5 and 8.2.3]{% endif %}.

If the reviewer requested any changes, address them and re-submit the review once they have been addressed.  The reviewer should approve the pull request from within the GitHub user interface{% if system.auditor_notes %} [62304:8.2.4.c]{% endif %}.

{%- if system.safety_class != 'C' %}
Occasionally, due to the absence of other reviewers or due to an internal testing deadline, it may be necessary to skip verification.  When this occurs, the developer should justify why a review wasn't necessary within the pull request comments.
{% endif %}

## Integration

[TODO: address traceability from software items to software system tests; see 62304:5.1.1.c]

**Input:** Unmerged, but approved, pull-request

Merge the approved git branch into the `master` git branch, correct any merge conflicts that occur.  Once the branch has been merged successfully, delete the branch in GitHub{% if system.auditor_notes %} [62304:5.1.5 and 5.6.1]{% endif %}.

**Output:** Merged pull request

## Integration and System Testing

**Input:** Software system built using the changes from this release's change requests

[TODO: write out details about the test record format [62304:9.8, 5.6.7, 5.7.5]]

**Output:** Test record

**Verification:** Ensure code changes:

- the original problem is fixed and the problem report closed{% if system.auditor_notes %} [62304:9.7.a]{% endif %}
- any adverse trends have been reversed{% if system.auditor_notes %} [62304:9.7.b]{% endif %}.

{%- if system.auditor_notes %}[We presume that if our integration tests and system tests are passing, no new problems were introduced, per 62304:9.7.d]{% endif %}

## Release

{% if system.auditor_notes %}[This activity addresses 62304:6.3.2, since development releases and maintenance releases are treated equivalently]{% endif %}

**Input:** Implemented and verified change requests for the current milestone

When a new version of the software is released, the git commit corresponding to the state of the code should be [tagged](https://git-scm.com/book/en/v2/Git-Basics-Tagging) with the version number.

{%- block software_archival_task %}
{%- endblock %}

Archived releases shall be kept until there are no longer supported devices being used that run the version of the software.

{% if system.auditor_notes %}[This section fulfills 62304:5.8.7; note that documentation and configuration items are archived automatically due to the fact that they are stored in Git]{% endif %}

**Output:** An archived software release

**Verification:** Ensure that

- all of the planned change requests have been implemented and integrated{% if system.auditor_notes %} [62304:5.6.2 and 9.7.c]{% endif %}
- the outputs of each activity are in a consistent state{% if system.auditor_notes %} [62304:5.1.6.c, 5.1.6.d, and 5.8.6]{% endif %}
- the software design specification is accurate and up-to-date
- the Unresolved Anomolies Document is up-to-date and none of the anomlies result in unacceptable risk{% if system.auditor_notes %} [62304:5.8.2 and 5.8.3]{% endif %}
- the Revision Level History Document is up-to-date{% if system.auditor_notes %} [62304:5.8.4]{% endif %}
- Integration and System Testing has been completed after the last change request was integrated{% if system.auditor_notes %} [62304:5.8.1]{% endif %}

{# TODO: add details about 14971:7 and 8 #}

## Problem Analysis

Feedback from users, internal testers, and software developers will be recorded in {{ system.feedback_location }}{% if system.auditor_notes %} [62304:6.1.a, 6.1.b and 6.2.1.1; details about where direct customer feedback is recorded and tracked is not handled here.  It is assumed that other processes (e.g., perhaps part of the broader quality management system) will handle this.  We also do not go into detail here regarding what criteria should be used to determine whether feedback is considered a problem, as required by 6.1.b]{% endif %}.

## Prepare Problem Report

{% if system.auditor_notes %}[This activity addresses 62304:6.2.1.2]{% endif %}

**Input:** Feedback from users or other members of the development team

A problem report should be created whenever:

1. a user reports a problem while using a released version of the software system, or
2. when an internal user reports a new problem that has been found during software development or maintenance on the master git branch{% if system.auditor_notes %} [62304:5.1.1.e and 5.1.9.f]{% endif %}.  Note that small software bugs and test-failures, especially recently introduced bugs discovered by software developer working on the project, do not require a problem report.  Problem reports provide a useful historical record of bugs, which can be used to identify software items which are especially risky.

When creating a new problem report, include in the description:

{# TODO: add "steps to recreate" #}
- The software item where the bug occurred (if known)
- If reported by a user, steps to recreate it
- If found in released software, the criticality of the problem
- Any relevant relevant information that can be used to investigate the problem{% if system.auditor_notes %} [62304:9.1]{% endif %}.

**Output:** The problem report

## Problem Investigation

{% if system.auditor_notes %}[This activity addresses 62304:6.1.d and 6.2.2]{% endif %}

**Input:** The problem report

1. Investigate the problem and if possible identify the cause and record it in the problem report
2. Evaluate the problem's relevance to safety using the software risk analysis activity{% if system.auditor_notes %} [62304:6.2.1.3]{% endif %}
3. Consider whether the software items implicated in the investigation have the proper safety class, and address as appropriate{% if system.auditor_notes %} [62304:6.2.2]{% endif %}
4. Summarize the conclusions from the investigation in the problem report
5. Create a change request for actions needed to correct the problem (also include an issue reference to the problem report{% if system.auditor_notes %} [62304:8.2.4.a and 8.2.4.b]{% endif %}), or document the rationale for taking no action and tag the problem report with the `wontfix` label{% if system.auditor_notes %} [62304:9.2]{% endif %}.

**If the problem affects devices that have been released, make sure that quality control is aware of the situation and has enough information to decide whether and how to notify affected parties, including users and regulators.  Record who you notified in the problem report{% if system.auditor_notes %} [62304:9.3 and 6.2.5; this document does not specify the process by which quality assurance will inform users, when they must inform users, etc.  It is assumed these details are handled in another process, and that all that the software developers must do is pass along the appropriate details to quality assurance.]{% endif %}.**

**Output:** Details about the problem investigation documented in the problem report and either unapproved change requests or justification as to why change requests weren't necessary

# Appendices

The subsections here provide guidance on following the software risk management, development, and maintenance activities.

## Requirements Analysis

Writing software requirements is an art and a science; one must find balance between precision and usefulness.
{% if not system.is_software_only_device %}
The distinction between system requirements and software requirements can be challenging.  System requirements describe the requirements of the entire system, including software and hardware.  Software requirements must be traceable to all of the system requirements that they help fulfill.  Software requirements are usually more detailed than the system requirements they refer to.  Many system requirements will be fulfilled using both hardware and software.
{% endif %}
The distinction between software requirements and the specifications is {% if not system.is_software_only_device %}also {% endif %}typically challenging.  Requirements should:

- not imply solution
- be verifiable
- be short, ideally one or two sentences long.

Specifications, on the other hand, should:

- be one of possibly many solutions
- be detailed.

Software requirements are often categorized as one of the following types{% if system.auditor_notes %} [62304:5.2.2 and 5.2.3]{% endif %}:

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

Software requirements that implement risk controls should be tied to their originating risk control by tagging them with labels that match the risk control ids{% if system.auditor_notes %} [62304:5.1.1.c]{% endif %}.

## Risk Management

This subsection provides a brief introduction to risk management in the context of software development.

**Safety** is freedom from unacceptable risk.  Note that it does not mean that there is no risk, as that is impossible.  The perception of risk can depend greatly on cultural, socio-economic and educational background, the actual and perceived state of health of the patient, as well as whether the hazard was avoidable.

Our obligation as medical device software developers is to develop safe devices, while balancing economic constraints---a device that is never made can not help patients, so there may be risk associated with not bringing a device to market if the device meets a clinical problem.

**Risk** is the combination of the probability of harm and the severity of that harm.

**Harm** is physical injury or damage of health of people (patients or users), or damage to property or the environment.

A **hazard** is a potential source of harm.

A **hazardous situation** is a circumstance in which people, property, or the environment is exposed to one or more hazard(s).  Not every hazardous situation leads to harm.

Software is not itself a hazard because it can not directly cause harm, but software can contribute towards producing hazardous situations.

{# TODO: add diagram from 14971 displaying the various components of risk #}

{# TODO: add guidance on risk identification #}

{# TODO: add guidance on risk estimation #}

{# TODO: discuss probabilities of software events #}

{# TODO: add details about the `risk.yml` file format #}

## SOUP

Information in the `soup.yaml` file may duplicate information found in other files (e.g., `requirements.txt` or `package.json`).

Sometimes, especially when working on software items with low levels of concern, it can be appropriate to lump a few SOUP packages into a single item within the `soup.yml` file.

The `soup.yaml` should contain a sequence of mappings, each containing the keys in parenthesis below.  Some keys are optional.  All values must be strings.

The header of each sub-section contains the `title` of the SOUP{% if system.auditor_notes %} [62304:8.1.2.a]{% endif %}.

The `manufacturer` is the name of the company that developed the SOUP.  If the manufacturer field is absent, then this SOUP was developed collaboratively by the free open-source software community, and does not have a manufacturer in the traditional sense{% if system.auditor_notes %} [62304:8.1.2.b]{% endif %}.

The `version` of each SOUP is a unique identifier, which specifies the version of the SOUP which is used in the software{% if system.auditor_notes %} [62304:8.1.2.c]{% endif %}.  The version may follow varying formats, such as `1.0.13`, `1.2r5`, or even `2021-05-05`, as appropriate.

{%- if system.safety_class != "A" %}
The `purpose` of each SOUP describes the functional and performance requirements that are necessary for its intended use{% if system.auditor_notes %} [62304:5.3.3]{% endif %}.

The `requirements` will be present if there are any noteworthy hardware and software requirements for the SOUP to function properly within the system{% if system.auditor_notes %} [62304:5.3.4]{% endif %}.

The known `anomalies` present in the SOUP which may affect the functioning of {{ system.project_name }} should be recorded, as should the `anomaly_reference`, a location of the published anomalies list{% if system.auditor_notes %} [62304:7.1.3]{% endif %}.

When reviewing open anomalies:
- Follow a risk based approach; concentrate on high priority anomalies (assuming the SOUP manufacturer provides such a categorization).
- If the list of known anomalies is large (e.g., more than 100), without prioritization, then sample the list as appropriate for the risk associated with the SOUP.
- When possible, focus the review on anomalies which affect portions of SOUP which are used by {{ system.project_name }}.
{% endif -%}
