---
id: CYBSEC-001
revision: 1
title: Cybersecurity Risk Management Report
---

# Purpose

The purpose of this document is to demonstrate the cybersecurity design controls and risk management found in {{device.name}} for FDA reviewers in a format that closely follows the 2018 Draft Guidance, "Content of Premarket Submissions for Management of Cybersecurity in Medical Devices".

# Scope

This document applies to {{device.name}} release {{device.version}}.

# Cybersecurity Risk Tier

TODO: Select the appropriate cybersecurity risk tier, based on your device. Three possible wordings are provided for your convenience below. Include additional justification for your selection as appropriate.

---

{{device.name}} is Tier 1, "Higher Cybersecurity Risk," because

1. The device is capable of connecting to another medical or non-medical product, to a network, or to the Internet, and
2. A cybersecurity incident affecting the device could directly result in patient harm to multiple patients.

---

{{device.name}} is Tier 2, "Normal Cybersecurity Risk," because the device is _not_ capable of connecting to another medical or non-medical product, to a network, or to the Internet.

---

{{device.name}} is Tier 2, "Normal Cybersecurity Risk," because although the device is capable of connecting to another medical or non-medical product, to a network, or to the Internet, it a cybersecurity incident affecting the device could directly result in patient harm to multiple patients.

---

ENDTODO

[[FDA-CYBER:4.1]]

# System Diagrams

TODO: Add System Diagrams that are sufficiently detailed to permit an understanding of how the specific device design elements are incorporated into a system-level and holistic picture. Analysis of the entire system is necessary to understand the manufacturer’s threat model and the device within the larger ecosystem. System diagrams should include:

- Network, architecture, flow, and state diagrams.
- The interfaces, components, assets, communication pathways, protocols, and network ports.
- Authentication mechanisms and controls for each communicating asset or component of the system including web sites, servers, interoperable systems, cloud stores, etc.
- Users’ roles and level of responsibility if they interact with these assets or communication channels.
- Use of cryptographic methods should include descriptions of the method used and the type and level of cryptographic key usage and their style of use throughout your system (one-time use, key length, the standard employed, symmetric or otherwise, etc.). Descriptions should also include details of cryptographic protection for firmware and software updates.

If you have diagrams like these in other documents, such as your software design specification, then includes links to the 

ENDTODO

[[These system diagrams fulfill FDA-CYBER:7.A.3, FDA-CYBER:7.A.3.a, FDA-CYBER:7.A.3.b, FDA-CYBER:7.A.3.c, FDA-CYBER:7.A.3.d, and FDA-CYBER:7.A.3.e]]

# Software Updates and Patches

TODO: Write a summary describing the design features that permit validated software updates and patches as needed throughout the life cycle of the medical device to continue to ensure its safety and effectiveness.

[[FDA-CYBER:7.A.4]]

# Cybersecurity Design Controls

TODO: Tier 1 devices should demonstrate how all design controls listed below are implemented. To do this, we recommend listing the associated requirements. Tier 2 devices may provide a risk-based rationale for why specific design controls are not appropriate.

This section enumerates all of the design controls recommended by the FDA for easy review by an FDA auditor.

## Limit Access to Trusted Users & Devices Only

*Limit access to devices through the authentication of users.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.a.i]]


*Use automatic timed methods to terminate sessions within the system where appropriate for the use environment.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.a.ii]]


*Employ a layered authorization model by differentiating privileges based on the user role or device functions.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.a.iii]]


*Use appropriate authentication (e.g., multi-factor authentication to permit privileged device access to system administrators, service technicians, maintenance personnel).*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.a.iv]]


*Strengthen password protection. Do not use credentials that are hardcoded, default, easily guessed, easily compromised. Limit public access to passwords used for privileged device access.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.a.v]]


*Consider physical locks on devices and their communication ports to minimize tampering.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.a.vi]]

# Authenticate and Check Authorization of Safety-Critical Commands


*Use authentication to prevent unauthorized access to device functions and to prevent unauthorized (arbitrary) software execution.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.i]]


*Require user authentication before permitting software or firmware updates, including those affecting the operating system, applications, and anti-malware.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.ii]]


*Use cryptographically strong authentication resident on the device to authenticate personnel, messages, commands and as applicable, all other communication pathways.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.ii]]


*Authenticate all external connections. For example, if a device connects to an offsite server, then it and the server should mutually authenticate, even if the connection is initiated over one or more existing trusted channels.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.iv]]


*Authenticate firmware and software. Verify signatures of software/firmware content, version numbers, and other metadata. The version numbers intended to be installed should themselves be signed/have MACs. Devices should be electronically identifiable (e.g., model number, serial number) to authorized users.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.v]]


*Perform authorization checks based on authentication credentials or other irrefutable evidence. For example, a medical device programmer should have elevated privileges that are granted based on cryptographic authentication or a signal of intent that cannot physically be produced by another device, e.g., a home monitor, with a software-based attack.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.vi]]


*Devices should be designed to “deny by default,” i.e., that which is not expressly permitted by a device is denied by default. For example, the device should generally reject all unauthorized TCP, USB, Bluetooth, serial connections.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.vii]]


*The principle of least privilege should be applied to allow only the level of access necessary to perform a function.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.1.b.viii]]


## Code Integrity


*Only allow installation of cryptographically verified firmware/software updates. Ensure that a new update is more recent than the currently installed version to prevent downgrade attacks.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.a.i]]


*Where feasible, ensure that the integrity of software is validated prior to execution, e.g., 'whitelisting' based on digital signatures.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.a.ii]]


## Data Integrity


*Verify the integrity of all incoming data (ensuring it is not modified in transit or at rest, and it is well-formed/compliant with the expected protocol/specification).*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.b.i]]


*Ensure capability of secure data transfer to and from the device, and when appropriate, use methods for encryption and authentication of the end points with which data is being transferred.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.b.ii]]


*Protect the integrity of data necessary to ensure the safety and essential performance of the device.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.b.iii]]


*Use current NIST recommended standards for cryptography (e.g., FIPS 140-2, NIST26 Suite B27), or equivalent-strength cryptographic protection for communications channels.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.b.iv]]


*Use unique per device cryptographically secure communication keys to prevent leveraging the knowledge of one key to access a multitude of devices.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.b.v]]


## Execution Integrity

*Where feasible, use industry-accepted best practices to maintain/verify integrity of code while it is being executed on the device.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.2.c.i]]


## Maintain Confidentiality of Data

*Manufacturers should ensure the confidentiality of any/all data whose disclosure could lead to patient harm (e.g., through use of credentials, encryption). Loss of confidentiality of credentials could be used by a threat to effect multi-patient harm. Lack of encryption to protect sensitive information "at rest" and “in transit” can expose this information to misuse that can lead to patient harm. Other harms, such as loss of confidential protected health information (PHI), are not considered “patient harms” for the purposes of this guidance.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.A.3]]


## Detect Cybersecurity Events in a Timely Fashion

*Implement design features that allow for security compromises to be detected, recognized, logged, timed, and acted upon during normal use.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.1.a]]


*Devices should be designed to permit routine security and antivirus scanning such that the safety and essential performance of the device is not impacted.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.1.b]]


*Ensure the design enables forensic evidence capture. The design should include mechanisms to create and store log files for security events. Documentation should include how and where the log file is located, stored, recycled, archived, and how it could be consumed by automated analysis software (e.g. Intrusion Detection System, IDS). Examples of security events include but are not limited to configuration changes, network anomalies, login attempts, and anomalous traffic (e.g., sending requests to unknown entities).*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.1.c]]


*The device design should limit the potential impact of vulnerabilities by specifying a secure configuration. Secure configurations may include endpoint protections such as anti-malware, firewall/firewall rules, whitelisting, defining security event parameters, logging parameters, physical security detection.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.1.d]]


*The device design should enable software configuration management and permit tracking and control of software changes to be electronically obtainable (i.e., machine readable) by authorized users.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.1.e]]


*The product life-cycle, including its design, should facilitate a variant analysis of a vulnerability across device models and product lines.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.1.f]]


*The device design should provide a CBOM in a machine readable, electronic format to be consumed automatically.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.1.g]]


## Respond to and Contain the Impact of a Potential Cybersecurity Incident

*The device should be designed to notify users upon detection of a potential cybersecurity breach.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.2.a]]


*The device should be designed to anticipate the need for software patches and updates to address future cybersecurity vulnerabilities.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.2.b]]


*The device should be designed to facilitate the rapid verification, validation, and testing of patches and updates.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.2.c]]


*The design architecture should facilitate the rapid deployment of patches and updates.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.2.d]]


## Design the Device to Recover Capabilities or Services that were Impaired Due to a Cybersecurity Incident

*Implement device features that protect critical functionality and data, even when the device’s cybersecurity has been compromised.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.3.b]]


*The design should provide methods for retention and recovery of device configuration by an authenticated privileged user.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.3.c]]


*The design should specify the level of autonomous functionality (resilience) any component of the system possesses when its communication capabilities with the rest of the system are disrupted including disruption of significant duration.*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.3.d]]


*Devices should be designed to be resilient to possible cybersecurity incident scenarios such as network outages, Denial of Service attacks, excessive bandwidth usage by other products, disrupted quality of service (QoS), and excessive jitter (i.e., a variation in the delay of received packets).*

TODO: demonstrate how this is implemented, e.g., by printing out the associated software requirements. If Tier 2, provide a risk-based rationale for why this specific design control isn't appropriate.

[[FDA-CYBER:V.B.3.e]]

## Additional Controls

TODO: List additional cybersecurity controls here


# Risk Management

## System Level Threat Model

TODO: Create a system level threat model that includes a consideration of system level risks, including but not limited to risks related to the supply chain (e.g., to ensure the device remains free of malware), design, production, and deployment (i.e., into a connected/networked environment). Its possible this could be combined with the systems diagrams.

[[FDA-CYBER:7.B.1]]

## Cybersecurity Risk Assessment

TODO: List out all cybersecurity risks. The tables shown here should probably be produced by filtering out data from `risk.yml` somehow. Ideally, the software engineers would be able to use the same process for safety and security risks. Note that TIR57 suggests keeping these processes separate, in part because the cybersecurity risk analysis doesn't require the full multi-domain risk team. That said, we already split the full risk management process from the software-specific risk process, thus splitting it again doesn't make sense. That said, there should probably be one cybersecurity expert on the software team. Perhaps this person should be added to the CODEOWNERS file for parts of the system that involve cybersecurity.
