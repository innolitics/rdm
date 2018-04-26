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

# Requirements Tables

{% if system.is_software_only_device %}

## Software Requirements Table

| Software Requirement ID | Title |
| --- | --- |
{%- for requirement in requirements %}
| {{ requirement.id }} | {{ requirement.title }} |
{%- endfor %}

{% else %}

## Software Requirements Table

| Software Requirement ID | System Requirement IDs Title |
| --- | --- | --- |
{%- for requirement in requirements %}
| {{ requirement.id }} | {{ requirement.system_requirements|join(', ') }} | {{ requirement.title }} |
{%- endfor %}

## System Requirements Mapping

| System Requirement ID | Software Requirement IDs |
| --- | --- |
{%- for requirement in requirements %}
| {{ requirement.id }} | {{ requirement.system_requirements|join(', ') }} |
{%- endfor %}
{% endif %}

# Requirement Details
{% block requirements %}

{% for requirement in requirements %}
## {{ requirement.title }}

{{ requirement.description }}

{% endfor %}
{% endblock %}
