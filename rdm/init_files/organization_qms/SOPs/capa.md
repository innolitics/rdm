---
revision: 1
title: CAPA SOP
---
# Approvals

All approvers shall add a signed commit with their name and roles appended to the table in this section.

| Name | Role                | Date |
| ---- | ------------------- | ---- |
|      | Quality Systems SME |      |

# Training Record

| Name | Role | Date |
| ---- | ---- | ---- |
|      |      |      |

# Purpose

This SOP shall describe the process for creating, executing, and concluding a corrective action / preventative action (CAPA).[[21.CFR.820.100]]

# Change History

The change history section shall contain a brief summary of changes made in this revision.

| Change Description | Date |
| ------------------ | ---- |
| Initial version    |      |

# Required Roles to Execute

The following user roles are required to execute this SOP:

- Quality Systems SME
- All roles necessary to execute the CAPA 

# Required Roles to Review

The following user roles are required for initial approval, periodic review, and change approval of this SOP:

- Quality Systems SME

# Required Inputs and Dependencies

The following inputs are required for the execution of this SOP:

- The event(s) that lead to initiating this CAPA

# Outputs

The SOP shall produce the following outputs:

- A CAPA record
- Potentially one or more changed, removed, or new SOPs

# Risk Level

High: Error in SOP or SOP execution is likely to result in patient harm.

# Periodic Review

Author shall insert the review periodicity depending on the risk level.

High: Review every six months.

# Record Template

Refer to `templates/capa_record.md`

# Work Instruction

1. Ensure you are on the `master` branch of the QMS git repository it is up to date.
1. Create a new branch called `capa/name_of_capa`
1. Create a copy of the CAPA record template to `records`
1. Fill out the CAPA record as requested in the record template.
1. Close the CAPA by merging the branch into `master`. Merging into master signifies the CAPA has been resolved and is ready to be executed. 
