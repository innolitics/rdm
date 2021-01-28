---
revision: 1
title: New Tool Validation SOP
---

# Approvals

All approvers shall add a signed commit with their name and roles appended to the table in this section.

| Name | Role | Date |
|---|---|---|
|  | Regulatory SME ||

# Training Record

By signing below you have acknowledged you have read and understood this document.

| Name | Role | Date |
| ---- | ---- | ---- |
|      |      |      |

# Purpose

This SOP details the process to validate a new tool for use within the quality management system. [[21.CFR.820.70.i]]

As a software as a medical device manufacturer, most of our tools will be software. Any tool to be used as part of the
quality management system shall be validated using this procedure before use.

# Triggers

This SOP must be executed every time the organization wishes to use a new software tool to execute the QMS.

# Change History

The change history section shall contain a brief summary of changes made in this revision.

| Change Description | Date             |
| ------------------ | ---------------- |
| Initial version    | January 20, 2021 |

# Required Roles to Execute

The following user roles are required to execute this SOP:

- Quality Systems SME
- Any SME necessary to validate the tool.

# Required Roles to Review

The following user roles are required for initial approval, periodic review, and change approval of this SOP:

- Quality Systems SME

# Required Inputs and Dependencies

The following inputs are required for the execution of this SOP:

# Outputs

- A validation record in the records directory of the QMS git repository.
- An entry in the tools registry document.


# Risk Level

Medium: Error in SOP or SOP execution is moderately likely in patient harm.

# Periodic Review

Medium: Review once a year.

# Record Template

Found in `templates/new_tool_validation.md`

# Work Instruction

1. Ensure you are on `master` and your git repository is up to date
1. Create a new branch called `new_tool_validation/`
1. Copy the record template `templates/new_tool_validation.md` into `records/new_tool_validation/name_of_tool.md`
1. Follow instructions on the record template.
1. Upon finishing tool validation, record completion in `documents/tools_registry.md`
1. Open a pull request and add necessary reviewers.

