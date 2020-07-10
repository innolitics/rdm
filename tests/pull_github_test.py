from rdm.project_management.github import extract_issue_numbers_from_commit_message


def test_extract_issue_numbers_from_commit_message():
    assert extract_issue_numbers_from_commit_message('''
        Some brief description w/ a 123

        - Stuff 55
        - Other Things
        - #45

        Issue #23

        Issues #45 #43
    ''') == ['45', '23', '45', '43']
