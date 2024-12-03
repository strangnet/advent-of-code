from main import calculate_safe_reports, read_input


def test_calculate_safe_reports():
    lists = read_input("test_input.txt")
    assert calculate_safe_reports(lists) == 2
