{% extends "base/software_plan.md" %}

{% block development_standards %}
## Development Standards

TODO: The technical lead should keep an up-to-date list of development standards here (e.g., PEP8 on a Python project).

If the software system's safety classification is not level C (the highest), you may delete this section.

{% if system.auditor_notes %}[This section fulfills 5.1.4.a]{% endif %}
{% endblock %}

{% block development_methods %}
## Development Methods

TODO: The technical lead should keep an up-to-date list of development methods here (e.g., Test Driven Development) if relevant.

If the software system's safety classification is not level C (the highest), you may delete this section.

{% if system.auditor_notes %}[This section fulfills 5.1.4.b]{% endif %}
{% endblock %}

{% block development_tools %}
## Development Tools

TODO: The technical lead should keep an up-to-date list of development tools here, such as linters and versions.

If the software system's safety classification is not level C (the highest), you may delete this section.

{% if system.auditor_notes %}[This section fulfills 5.1.4.c]{% endif %}
{% endblock %}
