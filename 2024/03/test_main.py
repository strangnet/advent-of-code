from main import parse_input, read_input


def test_parse_input():
    input_data = read_input("test_input.txt")
    assert parse_input(input_data) == 161
