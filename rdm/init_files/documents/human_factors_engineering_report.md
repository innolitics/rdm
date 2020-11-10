##1. Conclusion

The {{ system.project_name }} has been found to be safe and effective for the intended users, uses and use environments.

All known critical tasks enumerated in {{ system.task_location }} were passed by a 15 representative participants of each intended user population(s) of {{ system.project_name }}.

The human factors validation testing process is described in the software plan in the Human Factors Validation section.

TODO:

Briefly summarize the HFE/UE results. Consider:
    - any notes in {{ system.task_location }}
    - residual use-related risk (that could not be mitigated by design alterations).

ENDTODO

##2. Descriptions of Intended Device Users, Uses, Use Environments, and Training

TODO:

Enumerate the:
 - intended user population(s)
 - intended use and operational contexts of use
 - use environments and conditions that could affect user interactions with the device
 - training intended for users as defined in the Software Requirements Specification.
 (See SDS)

ENDTODO

##3. Description of Device User Interface

TODO: Add software item design created in the detailed design step of the software plan.

##4. Summary of known use problems

TODO:

Enumerate the:
  - use errors from similar medical devices [[62366-1:5.3]]
  - use errors from previous models of the {{ system.project_name }} [[62366-1:5.3]]

ENDTODO

##5. Analysis of Hazards and Risks Associated With use of the Device

The following risks have been associated with the use of {{ system.project_name }}:

{{ system.risk_matrix_location }}

The {{ system.project_name }} has been designed to mitigate as many hazards and risks as possible associated with the device.

##6. Summary of Preliminary Analyses and Evaluations

Formative analysis of the {{ system.project_name }} is evaluated through the GitHub review system. Each review follows the unit implementation and testing protocol explained in the software plan. All iterations of software design are reviewed by the project lead.

TODO: Explain key findings from this review process and describe design modifications made in response to the findings.

## Description and Categorization of Critical Tasks

Critical tasks are identified during the risk assessment of the {{ system.project_name }}, and extended (when necessary) during the unit implementation and testing protocol. Tasks which, if performed incorrectly or not performed at all, would cause more than negligible harm to the patient or user are considered critical tasks.

{{ system.task_location }}

## Details of Human Factors Validation Testing

Human factors validation testing was conducted through { #TODO: Choose a form of human factors validation testing (simulation, actual use, or clinical study) #}. This type of testing was chosen because { #TODO: Explain rationale for the type of testing chosen}. It was conducted { #TODO describe use environment #}.

Validation tests included 15 persons from each of the proceeding user groups:

TODO: Enumerate the user profile(s) for the device (See SDS and Section 2 of this report).

Below are all of the tasks performed during the human factors validation testing. With each task, use errors, close calls, and use problems are recorded.

{% for task in task.tasks %}
*{{ task.description.title }}*

{% if task.description.training_provided %}
- Training provided: {{ task.description.training_provided }}
{% endif %}

- Successful performance: {{ task.description.success }}

{% if task.results.errors %}
- Errors:
{% for error in task.results.errors %}
    - {{ task.results.errors }}
{% endfor %}
{% endif %}

{% if task.results.close_calls %}
- Close calls:
{% for close_call in task.results.close_calls %}
    - {{ task.results.close_call }}
{% endfor %}
{% endif %}

{% if task.results.problems %}
- Use problems:
{% for error in task.results.problems %}
    - {{ task.results.problem }}
{% endfor %}
{% endif %}

- Test results:
    - Participant feedback: {{ task.results.interview_feedback }}
    - Overview: {{ task.results.results_overview }}
{% endfor %}

TODO: Add analysis of the use errors and implications for additional risk elimination or reduction.
