{%- block front_matter -%}
---
category: KNANOM
id: KNANOM-001
revision: 1
title: Known Anomalies
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}
{% block purpose %}
# Purpose

The purpose of this document is to list the known anomalies which are present in the software within {{ system.project_name }}.

# Scope

The scope of this document is the software system within the {{ system.project_name }} product.
{%- endblock %}
{% block definitions %}
{%- endblock %}
{% block known_anomalies %}
# Known Anomalies
{% for ka in known_anomalies %}
## {{ ka.title }}

**Identifier:** {{ ka.id }}

**Created On:** {{ ka.created_on }}

**Description:**

{{ ka.description }}
{% endfor %}
{%- endblock %}
