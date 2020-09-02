---
id: SDS-001
revision: 1
title: Software Design Specification
---

# Purpose

This document describes *how* {{ system.project_name }} shall fulfill the requirements described in the software requirements specification. It discusses the computation hardware the software will be expected run on, the software system's architecture, functional specifications associated with each software requirement, and user interface mockups.

It is written primarily for engineers working on {{ system.project_name }}, who have the source code available, in addition to this document.

[[The legacy Software option of 62304:4.4 is not in use here.]]

# Scope

This document applies to {{ system.project_name }} release {{ system.release_id }}.

# Definitions

The **Food and Drug Administration (FDA)** is a United State government agency responsible for protecting the public health by ensuring the safety, efficacy, and security of human and veterinary drugs, biological products, and medical devices.

The **Health Insurance Portability and Accountability Act** (HIPAA) is a United States law designed to provide privacy standards to protect patients' medical records and other health information provided to health plans, doctors, hospitals and other healthcare providers.

**Protected Health Information** (PHI) means individually identifiable information that is created by {{ system.project_name }} and relates to the past, present, or future physical or mental health or condition of any individual, the provision of health care to an individual, or the past, present, or future payment for the provision of health care to an individual.

**UI** is an acronym for user interface.

# Software Items

## Architecture Design Chart

TODO: Add a block diagram showing a detailed depiction of functional units and software items.  You may also want to include state diagrams as well as flow charts [[:This is required by the FDAGeneralSoftwareGuidance]]

## Software Item A

## Software Item B

# SOUP Software Items

This section enumerates the SOUP software items present within {{ system.project_name }}.

{% for s in soup %}
## {{ s.title }}

**Manufacturer:**
{% if s.manufacturer is defined %}
{{ s.manufacturer }}
{% else %}
SOUP was developed collaboratively by the free open-source software community, and does not have a manufacturer in the traditional sense.
{% endif %}
**Version:**

`{{ s.version }}`
{% if system.safety_class != "A" %}
**Functional and Performance Requirements:**

{{ s.purpose }}

**Hardware & Software Requirements:**
{% if s.requirements is defined %}
{{ s.requirements }}
{% else %}
No noteworthy software or hardware requirements.
{% endif %}
**Known Anomalies:**
{% if s.anomaly_reference is not defined %}
Known anomaly list is not available.
{% else %}
{% if s.relevant_anomalies is not defined %}
No anomalies found that would result in incorrect behaviour for {{ system.project_name }} leading to a hazardous situation.
{% else %}
{{ s.anomalies }}
{% endif %}
**Open Anomaly List (Reference Only):**

`{{ s.anomaly_reference }}`
{%- endif %}
{%- endif %}
{% endfor %}

# Functional Specifications
{% for requirement in requirements %}
## {{ requirement.title }}

*Requirement ID:* {{ requirement.id }}

*Requirement:* {{ requirement.description }}
{% if 'specifications' in requirement %}

*Functional Specifications:*
{{ requirement.specifications }}
{%- endif %}
{%- endfor %}

# User Interface Mockups

TODO: If you have user interface mockups, this is a good place to put them.  One strategy is to include a sub-section for each screen, along with its own image file.  Here are some examples of various image file formats that RDM supports.

## Screen One (PNG)

Use something like: `![Screen One](../images/uimockups/example-ui-mockup-001.png)`

Which produces:

![Screen One](../images/uimockups/example-ui-mockup-001.png)

## Screen Two (SVG)

Use something like: `![Screen Two](../images/uimockups/example-ui-mockup-002.svg)`

Which produces:

![Screen Two](../images/uimockups/example-ui-mockup-002.svg)

## Screen Three (JPG)

Use something like: `![Screen Three](../images/uimockups/example-ui-mockup-003.jpg)`

Which produces:

![Screen Three](../images/uimockups/example-ui-mockup-003.jpg)
