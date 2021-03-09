---
revision: 1
title: Generate Quality Metrics SOP
---

# Approvals

All approvers shall add a signed commit with their name and roles appended to the table in this section.

| Name | Role | Date |
|---|---|---|
|      |      |      |
|      |      |      |
|      |      ||

# Training Record

By signing below you have acknowledged you have read and understood this document.

| Name | Role | Date |
| ---- | ---- | ---- |
|      |      |      |

# Purpose

Author shall clearly identify the purpose of this SOP. What does this SOP do? When should this SOP be invoked?

# Triggers

This SOP is usually created as a result of a CAPA. 

# Change History

The change history section shall contain a brief summary of changes made in this revision.

| Change Description | Date             |
| ------------------ | ---------------- |
| Initial version    | January 20, 2021 |

# Required Roles to Execute

The following user roles are required to execute this SOP:

- Quality Systems SME
- Engineering SME

# Required Roles to Review

The following user roles are required for initial approval, periodic review, and change approval of this SOP:

- Quality Systems SME

# Required Inputs and Dependencies

The following inputs are required for the execution of this SOP:

- Example input: All code review records from the code review SOP for the last year.

# Outputs

The SOP shall produce the following outputs:

- Example output: A record to capture a review was performed on an SOP.

# Risk Level

Low: Error in SOP or SOP execution is unlikely to result in patient harm.

# Periodic Review

Low: Review once a year.

# Record Template

Refer to `templates/quality_metrics_record.md`

# Work Instruction

A step by step recipe for executing the SOP.

1. Extract and / or compute all quality metrics as stated in the quality manual.
2. Create a new branch called `generate_quality_metrics/YYYY_MM_DD`. Replace the YYYY_MM_DD with todays date.
3. Create a copy of `templates/quality_metrics_record.md` under `records/generate_quality_metrics/YYYY_MM_DD.md`
4. Record the values of quality metrics in this record.
5. Commit the changes, push the branch, and submit a pull request for review.

