{%- block front_matter -%}
---
category: SRS
id: SRS-001
revision: 1
title: Software Requirements Specification
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}
{% block purpose %}
# Purpose

The purpose of this document is to list the requirements that describe *what* the {{ system.project_name }} {{ system.release_id }} software must fulfill.

This document is meant to be read and agreed-upon by the project owners and by software developers during design and construction.
{% if not system.is_software_only_device %}
The document also provides traceability between system requirements and software requirements.

# Scope

The scope of this SRS applies in its entirety to the {{ system.project_name }} {{ system.release_id }} product.
{%- endif %}
{%- endblock %}
{% block definitions %}
{%- endblock %}
{% block project_scope %}
{%- endblock %}
{% block stakeholders %}
{%- endblock %}
{% block use_cases %}
{%- endblock %}
{% block requirements %}
# Requirement Details
{% for requirement in requirements %}
## {{ requirement.title }}

{{ requirement.description }}
{% endfor %}
{%- endblock %}
{% block traceability_tables %}
# Traceability Tables
{% if system.is_software_only_device %}
## Software Requirements Table

| ID | Title |
| --- | --- |
{%- for requirement in requirements %}
| {{ requirement.id }} | {{ requirement.title }} |
{%- endfor %}
{% else %}
## Software Requirements Table

| Soft. Req. ID | System Req. IDs | Title |
| --- | --- | --- |
{%- for requirement in requirements %}
| {{ requirement.id }} | {{ requirement.system_requirements|join(', ') }} | {{ requirement.title }} |
{%- endfor %}

## System Requirements Mapping

| System Req. ID | Soft. Req. IDs |
| --- | --- |
{%- for system_requirement_id, software_requirement_ids in requirements|invert_dependencies('id', 'system_requirements') %}
| {{ system_requirement_id }} | {{ software_requirement_ids|sort|join(', ') }} |
{%- endfor %}
{%- endif %}
{%- endblock %}
{%- block extra_end %}
{%- endblock %}
