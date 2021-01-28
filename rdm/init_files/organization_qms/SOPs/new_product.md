---
revision: 1
title: SOP Change SOP
---
# Approvals

| Name | Role                | Date |
| ---- | ------------------- | ---- |
|      | Quality Systems SME |      |

# Training Record

By signing below you have acknowledged you have read and understood this document.

| Name | Role | Date |
| ---- | ---- | ---- |
|      |      |      |

# Purpose

This SOP describes how to add a new product under the quality management system.

# Change History

| Change Description | Date             |
| ------------------ | ---------------- |
| Initial version    | January 20, 2021 |

# Required Roles to Execute

The following user roles are required to execute this SOP:

- All roles listed in the quality manual are required

# Required Roles to Review

The following user roles are required for initial approval, periodic review, and change approval of this SOP:

- Quality Systems SME

# Required Inputs and Dependencies

The following inputs are required for the execution of this SOP:

- This SOP does not require any inputs

# Outputs

The SOP shall produce the following outputs:

- A product code git repository with RDM installed.
- A DHF directory in a file sharing platform. [[21.CFR.820.30.j]]

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
   Give the branch a descriptive name and use snake case such as: `new_product/name_of_product`
1. Make the necessary changes to the SOP.
1. Commit the changes to Git version control. 
1. Create a new directory under Box with the name of the product. 
1. Add a new row in `documents/product_registry.md`

