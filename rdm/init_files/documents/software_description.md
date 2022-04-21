---
id: SD-001
revision: 1
title: Software Description
---

# Purpose

This document provides an overview of the operationally significant features of the software within {{device.name}}, using a format that is familiar to FDA reviewers.

[[FDA-SW:sd]]

# Scope

This document applies to {{device.name}} release {{device.version}}.

TODO: Read through the sections below and fill in all the details as appropriate. You may want to reference [Section VI.B](https://innolitics.com/articles/premarket-submissions-for-device-software-functions/#b-software-description) of the 2021 Draft Guidance titled, "Content of Premarket Submissions for Device Software Functions".

# Software Specifics

**What programming languages and compiler versions are used? What hardware platforms are used?**

TODO: Fill this in, or refer to another document

**What operating systems are used (if applicable)?**

TODO: Fill this in, or refer to another document

**Does the device use Off-The-Shelf (OTS) software(s)?**

Yes. Please refer to the Software Design Specification for a list of the OTS used in {{device.name}}.

**What is the intended release version? If the intended release version is different from the documentation’s version, explain the differences.**

The intended release version is {{device.version}}. The documentation's version is the same.

# Software Operation

**Who operates the software (user)? The patient, a caregiver, a healthcare professional, or a combination thereof?**

See the "Users" section of the Software Requirements Specification.

**What is the intended patient population?**

TODO: Fill this in, or refer to another document

**Does the software function focus on a specific disease, condition, patient characteristic or demographic?**

TODO: Fill this in, or refer to another document

**Does the software provide information that is directly applicable to a specific disease or condition?**

TODO: Fill this in, or refer to another document

**If the software performs an analysis of data, what is the analysis methodology? What is the evidence base used for this methodology?**

TODO: Refer to the appropriate sections of the SDS

**Does the software impact or replace any otherwise manual or clinician performed actions? What are the workflow steps and assumptions (from beginning to end state)?**

TODO: Fill this in, refer to another document, or indicate it's not applicable

**If the device is AI/ML-enabled, what populations or samples have informed the model(s)? What steps were taken to identify and address potential biases and limitations of the model(s)?**

TODO: Fill this in, refer to another document, or indicate it's not applicable

# Software Inputs and Outputs

**What are the inputs and their format?**

TODO: Refer to the appropriate sections of the SRS or SDS. Example inputs and outputs include data, images (specify modality), measurements (specify units), sensor/attachments, report, questionnaires, etc.

**Who or what provides the inputs?**

TODO: Fill this in, or refer to other documents. Example responses include: user, other medical devices, other non-medical devices or software.

**Is the device designed to be interoperable?**

TODO: Fill this in, or refer to other documents, such as the architecture design chart and/or the appropriate sections of the SDS. Another way to ask the question is: does the device transmit, exchange, and/or use information through an electronic interface with another medical/nonmedical product, system, or device? If yes, list the other products that the device interfaces with, and what methods, standards, and specifications are used to interact and/or communicate with other medical/nonmedical products, systems, or devices.

**What are the outputs and their format?**

TODO: Refer to where in the submission the performance testing of the outputs, including test setup, acceptance criteria, and results, are located. Examples: testing for accuracy and repeatability of output measurements, parametric analyses, model outputs, device generated segmentation contours, medical image enhancements.

**To whom are the outputs provided?**

TODO: Fill in this section, or refer to other documents. Examples responses include: patients, caregivers, healthcare professionals, technicians, researchers, health records, interoperable systems.

**What is the data or information flow of the software?**

TODO: Refer to the appropriate parts of the architectural diagrams. Examples: inputs or outputs transmitted locally, via cloud storage, by disk or drive, or wirelessly.

**Does the software interact with any networked devices? Does the software use cloud or network storage?**

TODO: Update this response as appropriate

Yes, the software interacts with networked devices.

Yes, the software uses cloud or network storage.

# Other Device Functions

This device does not contain any other device functions.

TODO: Medical products may contain several functions, some of which are subject to FDA’s regulatory oversight as medical devices, while others are not. The draft text for this section indicates there are no other device functions, but if the device is a multiple function device product and includes software function(s) that are considered “other functions” please refer to the guidance titled "Multiple Function Device Product: Policy and Considerations," and add additional information to this section as appropriate. In particular, see section VII.B, which says:

For a multiple function device product, the device description should include a description of the “other function(s)” that could adversely impact the device function-under-review and should address how the device function-under-review is impacted by each of the “other functions.”

If the device function-under-review could be positively impacted by the “other function,” and the labeling reflects the positive impact (labeled positive impact), the device description should include the information outlined above in regard to the positive impact of the “other function” on the device function-under-review.

Sponsors may also describe “other functions” that either do not have an impact or could have a positive impact that is not suggested in the labeling of the device function-under-review, to provide an explanation of how the device functions overall.

ENDTODO

[[FDA-SW:sd-other]]

# Additional Information

TODO: Consider and provide any additional information that will help capture all of the unique aspects of your device's software function and will streamline or further FDA’s understanding of the device’s functionality to facilitate the review of a submission. Additional content should focus on the high risk parts of the device. Note also that more information is not necessarily better. Remove this section if no additional information needs to be added.