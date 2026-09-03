import os
import sys
import pytest


def find_test_file(file_name):
    for root, _, files in os.walk("tests"):
        if file_name in files:
            return os.path.join(root, file_name)
    return None


if len(sys.argv) < 2:
    sys.exit(1)

file_name = sys.argv[1]

test_file = find_test_file(file_name)

if not test_file:
    raise FileNotFoundError(
        f"Test file not found: {file_name}"
    )

folder_name = os.path.basename(
    os.path.dirname(test_file)
)

report_dir = os.path.join(
    "reports",
    folder_name
)

os.makedirs(report_dir, exist_ok=True)

report_path = os.path.join(
    report_dir,
    "report.html"
)

pytest.main([
    "-v",
    "-s",
    test_file,
    f"--html={report_path}",
    "--self-contained-html"
])