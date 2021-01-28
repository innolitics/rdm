---
revision: 1
title: SOP Creation SOP
---
# Approvals

| Name | Role | Date |
|---|---|---|
| | | |

# Training Record

By signing below you have acknowledged you have read and understood this document.

| Name | Role | Date |
| ---- | ---- | ---- |
|      |      |      |

# Purpose

This SOP shall be invoked when a new SOP needs to be created [[21.CFR.820.20.e]]. New SOPs may be created for a variety of reasons such as:

- Coming into conformance to existing or new regulations
- A result of a corrective action / preventative action


# Required Roles to Execute

At least a Quality systems SME is required to execute this SOP. Other SMEs shall be involved as necessary.

# Required Roles to Review

The following user roles are required for initial approval, periodic review, and change approval of this SOP:

- Quality systems SME

# Required Inputs and Dependencies

This SOP does not have any required inputs.

# Outputs

The output of this SOP is a new file in the SOPs directory of the quality manual. Additionally, new a new record template
shall be created in the record_templates directory of the quality manual. 

# Risk Level

Low: Error in SOP or SOP execution is unlikely to result in nonconforming product or patient harm.

# Periodic Review

Low: Only review when SOP is used.

# Record Template

A record of execution for this SOP is a new SOP. The template is found in the `templates/new_sop.md` file.

# Work Instruction

1. Ensure your local quality manual Git repository is up to date. Ensure you are on the `master` branch and perform a `git pull`
1. Create a new branch in the quality manual Git repository. 
   Give the branch a descriptive name and use snake case such as: `new_sop/new_complaint_sop`
1. Make a copy of the `templates/new_sop.md` file. Give the filename the name of the SOP. Use `snake_case` for the filename.
1. Open the new SOP file in a text editor of choice.
1. Fill in each section with relevant content for the new SOP.
1. Commit the newly added files. Push the files up to GitHub.
1. In GitHub, create Pull Request for the newly created branch. Add reviewers until all roles listed under the section "Required Roles to Review" have been fulfilled. 
1. Once all reviewers have been satisfied with the SOP, each reviewer shall add their name to the approvals table in Github. This creates a signed commit that constitutes an electronic signature. [[21.CFR.820.40.a]]
