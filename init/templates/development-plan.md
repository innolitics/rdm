{% block software_development_life_cycle %}
# Software Development Life Cycle Model

[ISO62304, Section 5.1.1]

The {{ software_system }} will be developed using an evolutionary software development life cycle model.

The "evolutionary" strategy develops the software system using a sequence of builds.  Customer needs and software system requirements are partially defined up front, then are refined in each succeeding build.
{% endblock %}

# Processes

[ISO62304, Section 5.1.1.a]

Development of {{ software_product }} will be performed using the life cycle processes described in IEC62304:2006.

## Requirements Gathering Activity

{% if is_software_only_device %}
If they have not been recorded already, the first task wil be to decide on system requirements and record them.  The system requirements may be recorded in external software (e.g. Greenlight Guru).  Each system requirement requires a unique identifier so that we can trace our software requirements back to the system requirements.
{% endif %}

The initial set of software requirements should be gathered and recorded in a file titled `software-requirements.yml`.  Each requirement will have a unique id beginning with the letter "r-", a description {% if is_software_only_device %}, an optional list of software requirement ids{% endif %}, and a type, according to the following format:

```
r-1:
  type: functional
  description: A concise, unambiguous, verifiable description of the requirement.
  {% if is_software_only_device %}system_requirements: 23, 45, 46{% endif %}
r-2:
  type: input
  description: Another description, which should not contradict other requirements.
  {% if is_software_only_device %}system_requirements: 3, 45{% endif %}
```

Software requirements must be categorized as one of the following types [^1]:

a) Functional and capability requirements (`"functional"`)

– performance (e.g., purpose of software, timing requirements),
– physical characteristics (e.g., code language, platform, operating system),
– computing environment (e.g., hardware, memory size, processing unit, time zone, network infrastructure) under which the software is to perform, and
– need for compatibility with upgrades or multiple SOUP or other device versions.

b) Sofware system inputs and outputs (`"input"` or `"output"`)

- data characteristics (e.g., numerical, alpha-numeric, format) ranges,
- limits, and
- defaults.

c) Interfaces between the software system and other systems (`"interface"`)

d) Software-driven alarms, warnings, and operator messages (`"alert"`)

e) Security requirements (`"security"`)

– those related to the compromise of sensitive information,
– authentication,
– authorization,
– audit trail, and
– communication integrity.

f) Usability engineering requirements that are sensitive to human errors and training (`"usability"`)

– support for manual operations,
– human-equipment interactions,
– constraints on personnel, and
– areas needing concentrated human attention.

g) Data definitions and database requirements (`"data"`)

h) Installation and acceptance requirements of the delivered medical device software at the operation and maintenance site or sites (`"installation"`)

i) Requirements related to methods of operation and maintenance (`"maintenance"`)

j) User documentation to be developed (`"user-documentation"`)

k) User maintenance requirements (`"user-maintenance"`)

l) Regulatory requirements (`"regulatory`)

m) Risk control measures (`"risk-control"`)

Any risk control measures that will be implemented in software should be included as requirements of type `"risk-control"`.  Also, whenever software requi

# Traceability

# Documents

1. Software Development Plan (this document)
2. Risk Management File

# References

1. ISO62304:2006 Section 5.2.2
