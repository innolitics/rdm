---
id: TESTREC-001
title: Software Test Record
---

# Purpose

The purpose of this document is to record the status of the software tests run for {{ system.project_name }}.

# Scope

The scope of this document is the software system within the {{ system.project_name }} product.

# Verification

I, FULL DEVELOPER NAME, verify that the results recorded here are complete and accurate.

Tests were performed on DATE TESTS COMPLETED.

The tests meet our specified pass fail criteria (see Test Plan section of the Software Plan).

# Test Environment

TODO: Describe the test environment.  This section should include all of the information necessary for someone to reproduce the tests.  For example, it could be wise to include a list of all the environment variables, installed system packages and versions, the git hash, hardware used, etc.  It should also include any relevant testing tools.

# Test Results

TODO: List of all the tests, split into sections by type.  You can use the three subsections below as a starting point.

TODO: List any problems that were found during testing, and, if relevant, the problem report ids.

It is ok if some tests do not trace to any particular requirements, however all requirements must be covered by some tests (if they are not, add tests).

## Unit Tests
[[These are the results of automated unit testing 62304:9.8.a]]
TODO: document any anomilies encountered [[62304:9.8.b]]
TODO: document the software version tested [[62304:9.8.c]]
TODO: document any relevant configuration [[62304:9.8.d]]
TODO: document the relavent tools used to run these tests [[62304:9.8.e]]
TODO: document the date tested [[62304:9.8.f]]
TODO: document the identity of the tester if any manual steps were required[[62304:9.8.g]].

| Test Name | Test Status | Requirement IDs | Notes |
| --- | --- | --- | --- |
{% for test_name in unit_test_record -%}
| {{ test_name }} | {{ unit_test_record[test_name].result }} | {{ unit_test_record[test_name].req_ids }} | {% if unit_test_record[test_name].note is defined %}{{ unit_test_record[test_name].note }}{% endif %} |
{% endfor %}

## Integration Tests
[[These are the results of automated integration testing 62304:5.6.3 62304:5.6.4 62304:9.8.a]]
TODO: document any anomilies encountered [[62304:9.8.b]]
TODO: document the software version tested [[62304:9.8.c]]
TODO: document any relevant configuration [[62304:9.8.d]]
TODO: document the relavent tools used to run these tests [[62304:9.8.e]]
TODO: document the date tested [[62304:9.8.f]]
TODO: document the identity of the tester if any manual steps were required[[62304:9.8.g]].

| Test Name | Test Status | Requirement IDs | Notes |
| --- | --- | --- | --- |
{% for test_name in integration_test_record -%}
| {{ test_name }} | {{ integration_test_record[test_name].result }} | {{ integration_test_record[test_name].req_ids }} | {% if integration_test_record[test_name].note is defined %}{{ integration_test_record[test_name].note }}{% endif %} |
{% endfor %}

## Manual Tests
[[These are the results of automated integration testing 62304:5.6.3 and 62304:5.6.4]]
TODO: document any anomilies encountered [[62304:9.8.b]]
TODO: document the software version tested [[62304:9.8.c]]
TODO: document any relevant configuration [[62304:9.8.d]]
TODO: document the relavent tools used to run these tests [[62304:9.8.e]]
TODO: document the date tested [[62304:9.8.f]]
TODO: document the identity of the tester [[62304:9.8.g]

| Test Name | Step | Test Status | Requirement IDs | Notes |
| --- | --- | --- | --- | --- |
{% for manual_test in manual_tests -%}
{% for manual_step in manual_test.steps -%}
| {{ manual_test.name }} | {{ manual_step.step }} | {{ manual_step.result }} | {{ manual_step.req_ids }} | {% if manual_step.note is defined %}{{ manual_step.note }}{% endif %} |
{% endfor -%}
{% endfor -%}
