---
id: Tool-Validation-Requirements-Based
revision: 1
title: Requirements Based Tool Validation Record Template
---

# Approvals

All approvers shall add a signed commit with their name and roles appended to the table in this section.

This approval indicates all authors certify the contents of the record for accuracy and conformance to the SOP.

| Name | Role | Date |
|---|---|---|
| George Costanza | Self Deprecation SME |
| Jerry Seinfeld | Comedy SME |
| Kramer (Cosmo) | Weird Jokes SME |

# Purpose

This record shall capture the tool validation activity for {{Tool Name and version number}} was performed.

For moderate risk tools either confidence based or requirements based validation is required.

For high risk tools, requirements based validation is required.

# Confidence Based Validation

In a few sentences, identify the reasons we feel this tool is safe to use for our QMS. Here is an example analysis:

Example 1:
GitHub is used by millions of software engineers worldwide and our usage of the tool does not appreciably differ from 
the standard use case. Therefore, we have high confidence that any defects in the tool will impact many people and will be resolved quickly.


# Requirements Based Validation

Optional for moderate risk tools. Required for high risk tools.

# Requirements

List out requirements the tool must fulfill.

Example:

- R1: Tool shall be capable of editing text files.
- R2: Tool shall be capable of saving text files.

# Test Script

For each of the requirements listed above, devise a series of testing steps to prove the tool meets the requirement. Also
specify which requirements each test is validating.

Example:

- Test 1: R1 and R2
  1. Open a text file in the tool.
  1. Make an edit to the text file.
  1. Save the text file.
  1. Open the text file again in the tool.
  1. Assert the change is preserved

# Test Execution:

For each test script, record all steps were executed successfully.

Example:

| Test Name | Result
---|---
Test 1 | Pass
Test 2 | Pass
Test 3 | Pass

