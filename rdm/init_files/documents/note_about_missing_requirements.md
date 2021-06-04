---
id: NOTE-001
revision: 1
title: Note About Missing Requirements
---

# Purpose

This document lists IEC62304 regulatory requirements that aren't addressed by the other documents in this folder.

It is a record of items that must be handled elsewhere to be IEC62304 compliant.It isn't meant to be given to regulatory bodies, and can be deleted if it is no longer used.

# Scope

This document applies to {{ device.name }} release {{ device.version }}.

# Quality Management System

The IEC62304 activities are meant to be part of a quality management system [[62304:4.1]]. The quality management system requires several activities that aren't included here.

Feedback and complaints must be gathered and incorporated into release planning [[14971:9 and 14971:3.4.f]]. These activities are not included here.

# Risk Management

A few risk management tasks are not included. We hope to include all of these in a future release.

Personnel must be qualified for the tasks they perform. In particular, risk management tasks must be performed by people with experience in those tasks [[14971:3.3 and 13485:6.2]].

The risk management report is not currently included in an RDM activity [[14971:8.a, 14971:8.b, 14971:8.c]].

Residual risk evaluation [[14971:6.4]], risk/benefit analysis [[14971:6.5]], risk control completeness [[14971:6.7]], and the evaluation of residual risk acceptability [[14971:7]] are not currently addressed.

# 62304 Class C Software

A few requirements for developing class C software aren't addressed yet:

- 62304:5.5.4.a Additional Software Unit Acceptance Criteria: proper event sequence
- 62304:5.5.4.b Additional Software Unit Acceptance Criteria: data and control flow
- 62304:5.5.4.c Additional Software Unit Acceptance Criteria: planned resource allocation
- 62304:5.5.4.d Additional Software Unit Acceptance Criteria: fault handling
- 62304:5.5.4.e Additional Software Unit Acceptance Criteria: initialization of variables
- 62304:5.5.4.f Additional Software Unit Acceptance Criteria: self-diagnostics
- 62304:5.5.4.g Additional Software Unit Acceptance Criteria: memory management and memory overflows
- 62304:5.5.4.h Additional Software Unit Acceptance Criteria: boundary conditions
