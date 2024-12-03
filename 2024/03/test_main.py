from main import parse_input, clean_parse, read_input


def test_parse_input():
    input_data = read_input("test_input.txt")
    assert parse_input(input_data) == 161


def test_parse_input2():
    input_data = read_input("test_input2.txt")
    assert clean_parse(input_data) == 48
