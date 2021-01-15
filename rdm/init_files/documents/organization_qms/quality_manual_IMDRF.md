---
id: Quality-Manual
revision: 1
title: Quality Manual
---

# Purpose

This document shall document the quality manual for {{ system.project_name }}.

The quality manual shall contain:

- the scope of of the quality management system and justification for exclusion or non-application
- documented standard operating procedures (SOPs) or references to them
- description of the interaction between SOPs or references to them

An effective quality management system shall include the following principles:

- An organizational structure that provides leadership, accountability, and governance with adequate resources to assure the safety, effectiveness, and performance of SaMD.
- A set of SaMD lifecycle support process that are scalable for the size of the organization and are applied consistently across all realization and use processes
- A set of realization and use processes that are scalable for the type of SaMD and the size of the organization; and that takes into account important elements requried for assuring the safety, effectivness, and performance of SaMD. 

# Leadership Structure

[[IMDRF.SAMD.N23.2015:6.1]]

Organization shall appoint one or more individuals to be the quality systems SME to be responsible  

# User Roles and Qualifications

[[IMDRF.N23:6.2.1]]

The following roles are necessary to carry out the requirements of the QMS.

- Lead software engineer
    - Shall be well versed in translating software design to implementation
    - Shall be responsible for developer mentorship
    - Shall have all qualification of a software engineering SME
- Software engineering SME
    - Shall have technical expertise sufficient to foresee sequences of events within the software that could lead to hazardous situations
    - Shall have expertise necessary to evaluate technical practicability of a risk control measure.
    - Shall be well versed in software engineering best practices necessary to create a conforming product.
    - Shall be well versed in our software design and development process.
    - Shall understand the clinical aspects of the use of the software.
- PHI compliance officer
    - Shall understand applicable PHI compliance regulations including HIPAA.
- Service engineer
    - Shall be trained to conduct postmarket support activities including diagnosing field issues, communicating with customers, executing SOPs related to issue logging, investigation, and triaging. 
    - Shall be capable of troubleshooting postmarket issues.
    - Shall be responsible for updating the service engineering manual.
- Product manager
    - Shall have clinical and industry expertise to bridge the gap between customers and company to create a product that fulfills customer's needs.
    - Shall be well versed in requirements and user needs gathering.
- Project manager  
    - Shall be capable of managing project deadlines, deliverables, product backlogs, sprint rituals.
    - Shall interface with product management and engineering to ensure user needs and requirements are met.
    - Shall manage cost, time, scope, and quality constraints.
- Customer liaison
    - Shall be well versed in the users manual and intended use of the device
    - Shall possess good communication skills necessary to interact with customers
- Medical SME
    - Shall have sufficient medical expertise sufficient to foresee hazardous situations from the normal and abnormal use of the medical device in clinical use.
- Cybersecurity SME
    - Shall be well versed in cybersecurity requirements as required by regulatory bodies.
- Risk analysis SME
    - Shall understand our risk management process.
    - Shall understand ISO 14971 and other applicable standards necessary to make ongoing changes to our risk management process.
- Quality systems SME
    - Shall understand our risk management process.
    - Shall understand ISO 13485 and other applicable standards necessary to make ongoing changes to our quality management system.
- Regulatory SME
    - Shall understand all applicable requirements for achieving regulatory clearance with all applicable regulatory bodies.
    

# Quality Objectives

The following quality objectives must be met:

- Reduce customer complaints
- Product defects as low as possible
- Customer feedback response as fast as possible
- Product releases have as few unresolved anomalies as possible
- Risk to patients minimized as low as reasonable
- CAPA shall be resolved in the shortest time as reasonable
- Periodic reviews as described in this quality manual shall be conduced on time
- Customer satisfaction shall be as high as possible
- Product requirements shall be met

The quality objectives shall be reviewed periodically and updated as necessary through corrective action preventive action. 

Top management shall develop project specific plans that are customer focused.


# New SOP SOP

The need to create a new SOP may arise from a variety of places including a CAPA, internal audit, product feedback, etc. 

Refer the New SOP SOP in the SOPs directory of the QMS repository. 

# SOP Change SOP

Organization shall have a procedure for improving existing SOPs

# SOP Removal SOP

Organization shall have a procedure for retiring existing SOPs.

# SaMD Lifecycle Support Process

[[IMDRF.N23:7.0, IMDRF.N23:7.1]]

For each product the organization shall have a SaMD product lifecycle process. This may be waterfall, agile, or a combination of the two. Required regulatory submissions usually means some degree of a waterfall process is required, however, the core development process may be more agile.

The SaMD product realization, planning, and development process is outlined in the regulatory documentation manager. 

Refer to the new product SOP.

# Risk Management

[[IMDRF.N23:7.2]]

Refer to the risk management process.

User based risk
Application based risk
Device based risk
Environment based risk
Security based risk

# Document and Record Control

[[IMDRF.N23:7.3]]

Records generated to demonstrate QMS conformity shall be appropriately identified, stored, protected, and retained for the lifetime of the company.

The QMS shall provide mechanisms for:

IMDRF Requirement | QMS Implementation
---|---
Reviewing and approving documents before use. | Documents are reviewed and approved in a feature branch before merging into master thus preventing their use until reviewed and approved
Ensuring current versions of applicable documents are available at points of use to help prevent the use of obsolete documents | All users of the QMS must ensure they are on the `master` branch and run a `git pull` to ensure they have the latest version. Alternatively, if GitHub is used as the frontend, the view will always default to master and will be up to date.
Retaining obsolete documentation for an established period | Git will retain all history, including obsolete documentation, for an indefinite period of time.
Controlling documents against unauthorized or unintended changes | Signed commits in git prevents unauthorized changes. Unintended changes are unlikely because of the deliberate nature of performing git actions.
Maintaining and updating documents across all SaMD lifecycle process. | Each SOP will be periodically reviewed on a schedule based on the level of risk.

# Configuration Management and Control

[[IMDRF.N23:7.4]]

The QMS shall control configurable items, including source code, releases, documents, and software tools in order to maintain the integrity and traceability of the configuration throughout the SaMD lifecycle. 

Item | Configuration Management Plan
---|---
Source code | Shall be stored in git version control.
Releases | Shall be archived in the respective device DHF.
Documents | Shall be stored in git version control and archived in DHF.
Software Tools | Shall be stored in git version control and archived in the device DHF. Refer to the tools inventory document for a list of approved tools and risk level.

# Measurement, Analysis, and Improvement Processes and Products

[[IMDRF.N23:7.5]]

## Required Activities

Logging and tracking of complaints.

Clearing technical issues

Determining problem causes and actions to address them

Track critical quality characteristics of products developed

Analysis of customer complaints, problem reports, bug reports, nonconformity to requirements (defects), service reports, and trends of processes and products should be used to evaluate the quality of the SaMD and SaMD process.

Corrective and preventive action SOP

SaMD containment of nonconforming product. Our software design and development process does not allow nonconforming product to be released to customers. 

Organization shall keep a record of customer complaints.

Organization shall, from time to time, shall request customer feedback reviews.

# Manage Outsourced Processes, Activities, and Products

[[IMDRF.N23:7.5]]

Refer to new vendor SOP.

# Manage Commercial-off-the-shelf (COTS) Products

Refer to QMS tools validation SOP and product SOUP validation SOP.

# Requirements Management

[[IMDRF.N23:8.1]]

Requirements shall be captured in the requirements.yml. 

# Design

[[IMDRF.N23:8.2]]

The purpose of design is to define software architecture, components, and interfaces based on requirements. Refer to the software plan.

# Development

[[IMDRF.N23:8.3]]

The development activity transforms the design into implementation. Refer to the software plan.

# Verification and Validation

[[IMDRF.N23:8.4]]

Refer to the Verification and Validation plan.

# Deployment

[[IMDRF.N23:8.5]]

TODO: Write SOPs on deploying new installations, training, configuration, for a new customer. Also detail procedures for distributing upgrades and maintenance releases.

# Maintenance

[[IMDRF.N23:8.6]]

Maintenance activities originate from software lifecycle processes such as service monitoring, customer feedback, in-house testing, usability studies, cybersecurity findings, and socio-technological changes. Refer to the software plan.

# Decommissioning 

[[IMDRF.N23:8.7]]

Organization shall have an end of life plan for all products. This includes sunsetting older versions that are no longer supported. 
