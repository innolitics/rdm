{%- block front_matter -%}
---
category: SRS
id: SRS-001
revision: 1
title: Software Requirements Specification
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}

# Purpose
{% block purpose %}

The purpose of this document is to list the requirements that describe *what* the {{ system.project_name }} software must fulfill, as well as the agreed upon specifications regarding *how* the software will accomplish this.

{% if not system.is_software_only_device %}
The software requirements are tied back to the system requirements.
{% endif %}
{% endblock %}

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
{% endif %}

# Requirement Details
{% block requirements %}

{% for requirement in requirements %}
## {{ requirement.title }}

{{ requirement.description }}

{% endfor %}
{% endblock %}
