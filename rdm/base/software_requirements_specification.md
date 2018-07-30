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

The purpose of this document is to list the requirements that describe *what* the {{ system.project_name }} software must fulfill, as well as the agreed upon specifications regarding *how* the software will accomplish this at a non-technical, high level of abstraction.

This document is meant to be read and agreed to by the project sponsor, and to be used by the software development team during design and construction.
{% if not system.is_software_only_device %}
The document also provides traceability between software requirements and the system requirements.
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
{% if 'specifications' in requirement %}
---

{{ requirement.specifications }}
{%- endif %}
{%- endfor %}
{%- endblock %}
{% block ui_mockups %}
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
