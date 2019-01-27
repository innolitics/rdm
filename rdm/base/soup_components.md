{%- block front_matter -%}
---
category: SOUP
id: SOUP-001
revision: 1
title: SOUP Components
manufacturer_name: {{ system.manufacturer_name }}
---
{%- endblock %}
{% block purpose %}
# Purpose

The purpose of this document is to list the Software of Unknown Provence (SOUP) components used within {{ system.project_name }}, and to provide requirements, hazard-analysis, and identify known anomalies.

# Scope

The scope of this document is the software system within {{ system.project_name }}.
{%- endblock %}
{% block definitions %}
{%- endblock %}
{% block overall_comments %}
{%- endblock %}
{% block soup_list %}
# SOUP Components

This section enumerates the SOUP components present within {{ system.project_name }}.  This listing is generated from the YAML data file named `soup.yaml`.  Developers must update this file as discussed in the software plan.  The `soup.yaml` shall contain a sequence of mappings, each containing the keys in parenthesis below.  Note some keys are optional.  All values must be strings.

The header of each sub-section contains the title (`title`) of the SOUP component{% if system.auditor_notes %} [8.1.2.a]{% endif %}.

The **manufacturer** (`manufacturer`) is the name of the company that developed the SOUP component.  If the manufacturer field is absent, then this SOUP component was developed collaboratively by the free open-source software community, and does not have a manufacturer in the traditional sense{% if system.auditor_notes %} [8.1.2.b]{% endif %}.

The **version** (`version`) of each SOUP component is a unique identifier, which specifies the version of the SOUP component which is used in the software{% if system.auditor_notes %} [8.1.2.c]{% endif %}.  The version may follow varying formats, such as `1.0.13`, `1.2r5`, or even `2021-05-05`, as appropriate.

{%- if system.safety_class != "A" %}
The **purpose** (`purpose`) of each SOUP component describes the functional and performance requirements that are necessary for its intended use{% if system.auditor_notes %} [5.3.3]{% endif %}.

The **hardware & software requirements** (`requirements`) will be present if there are any noteworthy hardware and software requirements for the SOUP component to function properly within the system{% if system.auditor_notes %} [5.3.4]{% endif %}.

The **known anomalies** (`anomalies`) present in the SOUP which may affect the functioning of {{ system.project_name }} are listed, as is a reference to the **open anomaly list** (`anomaly_reference`) location of the published anomalies list (for each reference of developers){% if system.auditor_notes %} [7.1.3]{% endif %}.

Our approach to reviewing open anomalies is as follows:
- Review anomalies using risk based approach where applicable; concentrate on high priority anomalies (assuming the SOUP manufacturer provides such a categorization).
- If the list of known anomalies is large (e.g., more than 100), without prioritization, then sample the list.
- When possible, focus the review on anomalies which affect portions of SOUP which are used by {{ system.project_name }}.

{%- endif %}

{% for s in soup %}
## {{ s.title }}
{% if s.manufacturer is defined %}
**Manufacturer:**

{{ s.manufacturer }}
{% endif %}
**Version:**

`{{ s.version }}`
{% if system.safety_class != "A" %}
**Purpose:**

{{ s.purpose }}
{% if s.requirements is defined %}
**Hardware & Software Requirements:**

{{ s.requirements }}
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
