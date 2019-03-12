{%- block front_matter -%}
---
category: RELEASE
id: RELEASE-001
revision: 1
title: Release
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}
{% block purpose %}
# Purpose

The purpose of this document is to list the problem reports associated with the software within {{ system.project_name }}, along with their associated change requests, or the rationale for taking no action.

# Scope

The scope of this document is the software system within the {{ system.project_name }} product.
{%- endblock %}
{% block definitions %}
{%- endblock %}
{% block known_anomalies %}
# Problem Reports
{% for pr in problem_reports %}
## {{ pr.title }}

**Identifier:** {{ pr.id }}

**Created On:** {{ pr.created_on }}

**Description:**

{{ pr.description }}
{% endfor %}
{%- endblock %}
