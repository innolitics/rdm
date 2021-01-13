---
id: SOP Removal SOP
revision: 1
title: SOP Removal SOP
---

# Purpose

This SOP describes how to change existing SOPs. 

# Approvals

| Name | Role | Date |
|---|---|---|
| Yujan Shrestha | Quality Systems SME | January 12, 2021

# Change History

| Change Description | Date
| --- | ---
| Initial version | January 12, 2021

# Required Roles to Execute

The following user roles are required to execute this SOP:

- Quality Systems SME
- All roles under "Required Roles to Review" for the SOP to be changed
- All roles under "Required Roles to Execute" for the SOP to be changed

# Required Roles to Review

The following user roles are required for initial approval, periodic review, and change approval of this SOP:

- Quality Systems SME

# Required Inputs and Dependencies

The following inputs are required for the execution of this SOP:

- The SOP to be removed. 
- This SOP cannot be removed.

# Outputs

The SOP shall produce the following outputs:

- An SOP removal record.

# Risk Level

Low: Error in SOP or SOP execution is unlikely to result in patient harm.

# Periodic Review

Low: Review once a year.

# Record Template

The record for SOP execution is a new SOP revision and additions to the "Change History" section
in the SOP to be changed. 

# Work Instruction

1. Ensure your local quality manual Git repository is up to date. Ensure you are on the `master` branch and perform a `git pull`
1. Create a new branch in the quality manual Git repository. 
   Give the branch a descriptive name and use snake case such as: `remove_sop/new_complaint_sop`
1. Copy `templates/remove_sop.md` to records and follow the instructions there.
1. Add the newly created record to version control and capture approvals.
1. Delete the SOP file.
1. Commit the changes to Git version control.
1. Create a pull request. Add all approvers.
1. Merge the pull request to `master` once approved.
