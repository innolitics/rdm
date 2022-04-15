---
id: UA-001
revision: 1
title: Unresolved Anomalies
---

# Purpose

The purpose of this document is to provide a list of all the problem reports for known software anomalies in the device.

[[FDA-SW:ua]]

# Scope

This document applies to {{device.name}}, and includes changes made in release {{device.version}}.

# Known Anomalies

This section includes a list of outstanding problem reports (i.e., known anomalies). Each problem report includes a description of the problem, its impact on device performance, and any plans or timeframes for correcting the problem (where appropriate).

{% for cr in history.change_requests|selectattr('is_problem_report')|rejectattr('change_ids') %}
## {{cr.title}}

**Identifier:** {% if cr.url is defined %}[{{cr.id}}]({{cr.url}}){% else %}{{cr.id}}{% endif %}

**Description:**

{{cr.content}}
{% endfor %}