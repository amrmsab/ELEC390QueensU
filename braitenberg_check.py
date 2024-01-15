def test_braitenberg_submission():
    try:
        with open('braitenberg/submission.md', 'r', encoding='utf-8') as file:
            submission_no = file.readline().strip()
            user_no = file.readline().strip()
    except FileNotFoundError:
        print(f"File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    assert submission_no.isdigit(), "Input must contain only numerical digits"
    assert len(submission_no) == 5, "Input must contain exactly 5 digits"
    assert len(user_no) > 1, "User name is not provided"
