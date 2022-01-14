---
id: VVP-001
revision: 1
title: Verification and Validation Plan
---

# Purpose

This document describes the plan regarding how {{ device.name }} will be verified and validated.

[[Fulfills FDA-CPSSCMD:v-and-v and 62304:5.5.2]]

# Definitions

**Verification** means confirmation by examination and provision of objective evidence that specified requirements have been fulfilled. In other words, "Did we build the thing right?"

**Validation** means establishing by objective evidence that device specifications conform with user needs and intended uses. In other words, "Did we build the right thing?"

An **end-to-end test** examines the functionality of an software system through its standard user interface without peering into its internal structures or workings.

A **unit test** examines an individual software unit that typically cannot be broken down any further.

An **integration test** examines multiple software units for defects in the interfaces and interactions between them.

An **automated test** is any test that can be run without human input. A **manual test** is any test that requires a human to perform some or all of the test steps.

A **software item** is any identifiable part of a computer program.

A **software system** is an integrated collection of software items organized to accomplish a specific function or set of functions.

A **software unit** is a software item that is not subdivided into other software items.

**Regression testing** is the process of re-running functional and non-functional tests to ensure that previously developed and tested software still performs after a change.

# Verification Activities

Software verification begins with the code reviews and adherence to software standards defined in the Software Plan. The outputs of these activities are recorded in the Revision Level History.

Software verification continues by running all automated tests on a continuous basis during the development process to detect any regressions. Automated tests are automatically run against each proposed software revision before the revision is accepted, a process known as Continuous Integration, or CI. Manual tests are run as needed during development and then for the Software Test Record for a release. Problem reports should be created when failures are detected after CI runs [[62304:5.1.9.f]].

Tests are written, modified, and reviewed during the Unit Implementation and Testing activity and are reviewed for completeness as part of the Release activity. Both activities are described in the Software Plan.

A detailed list of verification tests, the testing environment, and their results are found in the Software Test Record. The Software Test Record is created as part of the Integration and System Testing activity described in the Software Plan.

All final test records must include the Git hash or other objective reference that can be used to identify the exact software tested. Test records should not be created from dirty repositories [[62304:5.1.11]].

The types of tests used to verify {{ device.name }} are described below:

## Unit Tests

TODO: Describe how and when unit test shall be written

## Integration Tests

TODO: Describe how and when integration tests shall be written

## Automated End-to-End Tests

TODO: Describe how and when automated end-to-end tests shall be written

## Manual End-to-End Tests

TODO: Describe how and when manual end-to-end tests shall be written

# Validation Activities

TODO: Describe how we'll validate that the user needs have been met (in software and hardware projects, this is usually handled at the system-level).

# Pass / Fail Criteria

TODO:

This plan should include a pass/fail criteria for the entire test suite.  E.g., you require that all unit tests pass and that all integration tests pass or the cause of the failure is understood and justified

ENDTODO

[[62304:5.7.1.a]]
