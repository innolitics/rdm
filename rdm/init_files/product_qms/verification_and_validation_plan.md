---
id: VVP-001
revision: 1
title: Verification and Validation Plan
---

# Approvals

By signing below, the individual indicates he or she has read, understood, and approved the contents of this document.

| Name | Role | Date |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |

# Revision History

| Date | Version | Change Description |
| ---- | ------- | ------------------ |
|      |         |                    |
|      |         |                    |



# Verification and Validation Plan

## Introduction

This document summarizes validation and verification activities. The results of the validation and verification activities can be found in the Test Report document. The Traceability Analysis Report maps these activities to the requirements defined in the Software Requirements Specification.

## Definitions

Verification means confirmation by examination and provision of objective evidence that specified requirements have been fulfilled. In other words, “Did we build the thing right?”



Validation means establishing by objective evidence that device specifications conform with user needs and intended uses. In other words, “Did we build the right thing?”



An end-to-end test examines the functionality of an application through its standard user interface without peering into its internal structures or workings.



A unit test examines an individual software unit that typically cannot be broken down any further.



An integration test examines multiple software units for defects in the interfaces and interactions between them. 



A software item is any identifiable part of a computer program.



A software system is an integrated collection of software items organized to accomplish a specific function or set of functions.



A software unit is a software item that is not subdivided into other software items.



Regression testing is the process of re-running functional and non-functional tests to ensure that previously developed and tested software still performs after a change.

## Verification

Software verification begins with the design reviews, code reviews, and adherence to software standards defined in the Software Plan. These activities are reported in the Revision Level History. [[21.CFR.820.30.f]]

Software verification continues with verification tests run on a continuous basis during the development process to detect any regressions. All tests are automatically run against each proposed software revision before the revision is accepted, a process known as Continuous Integration or CI.

Verification tests include unit tests, integration tests, and end-to-end tests, which are summarized below. A detailed list of verification tests along with their results for the current release is found in the Automatic Verification Test Report.

TODO: Document how verification tests are to be run.

## Validation

Summative validation occurs after a software release candidate has passed all verification testing. In these system-level tests, the software is deployed to a validation testing environment which is as close to the intended deployment environment as possible. Anonymized image data and the full user interface are used to confirm that the software conforms to its intended use, including reporting of results. [[21.CFR.820.30.g]]

Details and results of these validation tests are contained in the Test Report.