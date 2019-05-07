{%- block front_matter -%}
---
category: TESTREC
id: TESTREC-001
revision: 1
title: Software Test Record
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}
{% block purpose %}
# Purpose

The purpose of this document is to record the status of the software tests run for {{ system.project_name }}.

# Scope

The scope of this document is the software system within the {{ system.project_name }} product.
{%- endblock %}
{% block definitions %}
{%- endblock %}
{% block verification %}
{% endblock %}
{% block test_environment %}
{% endblock %}
{% block test_results %}
{% endblock %}
