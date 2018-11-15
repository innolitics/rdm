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
