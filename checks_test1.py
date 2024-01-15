def test1():
  try:
    with open('setup/submission.md', 'r', encoding='utf-8') as file:
      submission_no = file.readline().strip()
  except FileNotFoundError:
    print(f"File not found: {file_path}")
  except Exception as e:
    print(f"An error occurred: {e}")
  assert submission_no.isdigit(), "Input must contain only numerical digits"
  assert len(submission_no) == 5, "Input must contain exactly 5 digits"
