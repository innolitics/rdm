{% extends "base/software_requirements_specification.md" %}

{% block definitions %}
# Definitions

The **Food and Drug Administration (FDA)** is a United State government agency responsible for protecting the public health by ensuring the safety, efficacy, and security of human and veterinary drugs, biological products, and medical devicese

The **Health Insurance Portability and Accountability Act** (HIPAA) is a United States law designed to provide privacy standards to protect patients' medical records and other health information provided to health plans, doctors, hospitals and other healthcare providers.

**Protected Health Information** (PHI) means individually identifiable information that is created by {{ system.project_name }} and relates to the past, present, or future physical or mental health or condition of any individual, the provision of health care to an individual, or the past, present, or future payment for the provision of health care to an individual.

**UI** is an acronym for user interface.

{%- endblock %}
{% block project_scope %}
# Project Purpose

A brief statement of what the software is intended to do, and what benefit it will bring to the software owners.

Here is an example project purpose for a medical image viewer designed for patients:

> To provide an MRI, CT, and X-ray viewer that is welcoming for patients and non-technical users.  It does not need all of the functions that professional DICOM viewers have.  The software should be easy to integrate with other software projects, as it will be licensed to other software developers for a fee.

{%- endblock %}
{% block stakeholders %}
# Stakeholders

Stakeholders are anyone who is affected by or interested in the project.  This section of the document should list out the project stakeholders and describe them and why they are interested in the project.  Different stakeholders have different requirements for the project, so it is useful to enumerate all of them so that no important requirements are missed.  As with every step in the requirements process, the goal is to be optimally valuable.  It is easy to go overboard and list out 30 or 40 stakeholders, but this is usually not optimally valuable on smaller projects.  For example, a worker at an electronics recycling plant is a stakeholder, but startups and small companies don't have time to consider their requirements for a project.  A few common stakeholders are listed below for convenience.

## Project Owner

The project owner wants the project to be profitable.

## Project Sponsor

The project sponsor is the primary decision maker who acts on behalf of the owner.

## Customer

The purchaser wants the device to produce value for their organization.

- Where are the customers geographically?
- How many customers are there?
- Is the customer also the user, or are they buying on behalf of users within a larger organization?

## Patient

The {{ system.project_name }} is ultimately used to help patients.

## User

The user wants the device to make their job easier.  There may be several different types of users, in which case it is worth adding more sections for each type.

- What part of their work do they want to improve using the project?
- What is the background of the user?
- What is their education level?
- What is their age?
- What motivates them at their work?

## Advanced User

The advanced user is typically part of a smaller group of users, who uses the software more frequently than normal users, and thus has more requirements.

## Service Engineer

The service engineer wants the software to capture information so that it is easy to detect and debug problems.

## Regulator

The FDA wants to ensure that the {{ system.project_name }} device is safe, and they want to be able to do so as quickly and efficiently as possible.

The Human Health Services (HHS), who are responsible for enforcing HIPAA, want to ensure that private health information is not leaked out to the public.

Regulators in other jurisdictions will have similar requirements.

{%- endblock %}
{% block use_cases %}
# Use Cases

## Problem X

Brief description.

## Problem Y

Brief description.
{%- endblock %}
{% block ui_mockups %}
# User Interface Mockups

If you have user interface mockups, this is a good place to put them.  One strategy is to include a sub-section for each screen, along with its own SVG file.

## Screen One

Use something like: `![Screen One](../images/mockups/screen-one.svg)`

## Screen Two

Use something like: `![Screen One](../images/mockups/screen-two.svg)`
{%- endblock %}
