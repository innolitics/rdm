---
id: SOP Review SOP
revision: 1
title: SOP Review SOP
---

# Approvals

All approvers shall add a signed commit with their name and roles appended to the table in this section.

| Name | Role | Date |
|---|---|---|
| George Costanza | Self Deprecation SME |
| Jerry Seinfeld | Comedy SME |
| Kramer (Cosmo) | Weird Jokes SME |

# Purpose

This SOP shall describe how to conduct SOP reviews. 

# Change History

The change history section shall contain a brief summary of changes made in this revision.

| Change Description | Date
| --- | ---
| Initial version | January 12, 2021


# Required Roles to Execute

The following user roles are required to execute this SOP:

- Quality Systems SME
- All roles under "Required Roles to review" for the SOP under review 

# Required Roles to Review

The following user roles are required for initial approval, periodic review, and change approval of this SOP:

- Quality Systems SME

# Required Inputs and Dependencies

The following inputs are required for the execution of this SOP:

- The SOP under review

# Outputs

The SOP shall produce the following outputs:

- An SOP review record

# Risk Level

Low: Error in SOP or SOP execution is unlikely to result in patient harm.

# Periodic Review

Low: Only review when SOP is used.

# Record Template

Author shall reference or include the template used to create a record capturing the SOP execution.

# Work Instruction

1. Ensure your local quality manual Git repository is up to date. Ensure you are on the `master` branch and perform a `git pull`
1. Create a new branch in the quality manual Git repository. 
   Give the branch a descriptive name and use snake case such as: `review_sop/new_complaint_sop`
1. Copy `templates/review_sop.md` to `records`.
1. Add the newly created record to version control and capture approvals.
1. Commit the changes to Git version control.
1. Create a pull request. Add all approvers.
1. Merge the pull request to `master` once approved.
