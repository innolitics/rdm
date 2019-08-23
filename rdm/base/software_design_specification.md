{%- block front_matter -%}
---
category: SDS
id: SDS-001
revision: 1
title: Software Design Specification
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}
{% block purpose %}
# Purpose

The purpose of this document is to describe *how* the {{ system.project_name }} {{ system.release_id }} software shall fulfill the software requirements.  It discusses the environment that that software will run in, the software system's architecture, functional specifications associated with each software requirement, and user interface mockups.

This document is written primarily for software and hardware engineers working on {{ system.project_name }}, who have the source code available in addition to this document.

# Scope

The scope of this SDS applies in its entirety to the {{ system.project_name }} {{ system.release_id }} product.
{%- endblock %}
{% block definitions %}
{%- endblock %}
{% block architecture %}
{%- endblock %}
{% block soup %}
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
{%- endblock %}
{% block functional_specifications %}
# Functional Specifications
{% for requirement in requirements %}
## {{ requirement.title }}

*Requirement:* {{ requirement.description }}
{% if 'specifications' in requirement %}

*Functional Specifications:*
{{ requirement.specifications }}
{%- endif %}
{%- endfor %}
{%- endblock %}
{% block ui_mockups %}
{%- endblock %}
