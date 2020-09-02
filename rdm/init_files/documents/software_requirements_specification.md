---
id: SRS-001
revision: 1
title: Software Requirements Specification
---

# Purpose

This document describe *what* {{ system.project_name }} software must do.

This document is meant to be read and agreed-upon by the project owners and by software developers during design and construction.

{% if not system.is_software_only_device %}
The document also provides traceability between system requirements and software requirements.
{% endif %}

# Scope

This document applies to {{ system.project_name }} release {{ system.release_id }}.

# Definitions

The **Food and Drug Administration (FDA)** is a United State government agency responsible for protecting the public health by ensuring the safety, efficacy, and security of human and veterinary drugs, biological products, and medical devices.

The **Health Insurance Portability and Accountability Act** (HIPAA) is a United States law designed to provide privacy standards to protect patients' medical records and other health information provided to health plans, doctors, hospitals and other healthcare providers.

**Protected Health Information** (PHI) means individually identifiable information that is created by {{ system.project_name }} and relates to the past, present, or future physical or mental health or condition of any individual, the provision of health care to an individual, or the past, present, or future payment for the provision of health care to an individual.

A **User** is a person who interacts with (i.e., operates or handles) the device.



**UI** is an acronym for user interface.

# Users

TODO: Device Users are anyone who interacts with (i.e., operates or handles) the device.  Different users will have different requirements, so it is useful to enumerate all of them so that no important requirements are missed.  A few common stakeholders are listed below for convenience.

There may be several different types of users, in which case it is worth adding more sections for each type.

- Physical size, strength, and stamina,
- Physical dexterity, flexibility, and coordination,
- Sensory abilities (i.e., vision, hearing, tactile sensitivity),
- Cognitive abilities, including memory,
- Medical condition for which the device is being used,
- Comorbidities (i.e., multiple conditions or diseases),
- Literacy and language skills,
- General health status,
- Mental and emotional state,
- Level of education and health literacy relative to the medical condition involved,
- General knowledge of similar types of devices,
- Knowledge of and experience with the particular device,
- Ability to learn and adapt to a new device, and
- Willingness and motivation to learn to use a new device.

ENDTODO

This section enumerates the types of device users, describe their characteristics, and why they are interested in the device [[FDA-HFE:5.1]].

## Patient

TODO: write in details, or remove this section

## Physician

TODO: write in details, or remove this section

## Hospital IT Personnel

TODO: write in details, or remove this section

# Use Environments

TODO:

You should evaluate and understand relevant characteristics of all intended use environments and describe them for the purpose of HFE/UE evaluation and design. These characteristics should be taken into account during the medical device development process, so that devices might be more accommodating of the conditions of use that could affect their use safety and effectiveness.

The environments in which medical devices are used might include a variety of conditions that could determine optimal user interface design. Medical devices might be used in clinical environments or non-clinical environments, community settings or moving vehicles. Examples of environmental use conditions include the following:

- The lighting level might be low or high, making it hard to see device displays or controls.
- The noise level might be high, making it hard to hear device operation feedback or audible alerts and alarms or to distinguish one alarm from another.
- The room could contain multiple models of the same device, component or accessory, making it difficult to identify and select the correct one.
- The room might be full of equipment or clutter or busy with other people and activities, making it difficult for people to maneuver in the space and providing distractions that could confuse or overwhelm the device user.
- The device might be used in a moving vehicle, subjecting the device and the user to jostling and vibration that could make it difficult for the user to read a display or perform fine motor movements.

You should evaluate and understand relevant characteristics of all intended use environments and describe them for the purpose of HFE/UE evaluation and design. These characteristics should be taken into account during the medical device development process, so that devices might be more accommodating of the conditions of use that could affect their use safety and effectiveness.

ENDTODO

This section enumerates the environments in which the {{ system.project_name }} will be used [[FDA-HFE:5.2]].

## Radiology Reading Room

TODO: write in details, or remove this section

## Radiologist's Home

TODO: write in details, or remove this section

# Use Cases

## Problem X

Brief description.

## Problem Y

Brief description.

# Requirement Details
{% for requirement in requirements %}
## {{ requirement.title }}

*Requirement ID:* {{ requirement.id }}

{{ requirement.description }}
{% endfor %}

# Traceability Tables
{% if system.is_software_only_device %}
## Software Requirements Table

[[ Each requirement has a unique id satisfying 62304:5.2.6.e]]
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
{%- endif %}
