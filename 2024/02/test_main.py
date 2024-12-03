from main import (
    calculate_safe_reports,
    calculate_safe_reports_with_dampener,
    read_input,
)


def test_calculate_safe_reports():
    lists = read_input("test_input.txt")
    assert calculate_safe_reports(lists) == 2


def test_calculate_safe_reports_with_dampener():
    lists = read_input("test_input.txt")
    assert calculate_safe_reports_with_dampener(lists) == 4
