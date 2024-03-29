---
id: RMP-001
revision: 1
title: Risk Management Plan
---

TODO: This document is currently in-progress, and as such, it is not comprehensive. Note that it currently conflicts slightly with the risk-related activities in the software plan. These issues will be rectified in a future RDM update. For devices with hardware, risk-management is typically conducted at the system-level.

# Purpose

This risk management plan describes the activites that are performed in order to identify hazards and hazardous situations, estimate and evaluate the associated risks, control these risks, and monitor the effectiveness of the risk control measures. These steps will be performed throughout the life cycle of the medical device.

This risk management plan is intended to fulfill the requirements of ISO 14971:2019.

[[FDA-SW:rmf-plan]]

# Scope

This document applies to all life-cycle phases of {{device.name}} [[14971:3.4.a]].

# Personnel Qualifications

TODO: Fill this in; consider using `data/people.yml` to generate a table as appropriate.

[[14971:3.3 and 14971:3.4.b]]

14971:3.4.c Risk management plan: requirements
14971:3.4.e Risk management plan: verification

# Risk Evaluation and Criteria for Risk Acceptability

Risk evaluation is quantified according to the Risk Acceptability Matrix:

| | {% for freq in risk.risk_probability_levels %} {{ freq.label }} | {% endfor %}
| -- | {% for freq in risk.risk_probability_levels %} -- | {% endfor %}
{% for severity in risk.risk_severity_levels %}{% set outer_loop = loop %}| {{ severity.label }} | {% for val in risk.risk_acceptability_matrix[outer_loop.index0] %} {{ val }} |{% endfor %}
{% endfor %}

Risk probability levels are defined as follows:

| Risk Probability Label | Definition |
| --                     | --         |
{% for freq in risk.risk_probability_levels %}| {{ freq.label }} | {{ freq.description }} |
{% endfor %}

Risk severity levels are defined as follows:

| Risk Severity Label | Definition |
| --                     | --         |
{% for severity in risk.risk_severity_levels %}| {{ severity.label }} | {{ severity.description }} |
{% endfor %}

Finally, risk acceptability levels are defined according to the following
criteria:

| Risk Level | Acceptance Criteria |
| --                     | --         |
{% for level in risk.risk_levels %}| {{ level.label }} | {{ level.description }} |
{% endfor %}

[[14971:3.4.d]]

# Risk Management Activity

## Intended Use, Reasonably Foreseeable Misuse, and Safety Characteristics

TODO

## Identify Hazards and Hazardous Situations

TODO: Consult ISO/TR 29471 for specific recommended risk identification
techniques

## Estimate Risk

TODO

## Risk Control

TODO

## Risk Control Verification

TODO

## Post Production

TODO

[[14971:3.4.f]]