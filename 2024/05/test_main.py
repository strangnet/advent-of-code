from main import validate_update, read_input, parse_input


def test_validate_update():
    input_data = read_input("test_input.txt")
    parsed_rules, parsed_updates = parse_input(input_data)

    valid_results = [
        (True, 61),
        (True, 53),
        (True, 29),
        (False, 0),
        (False, 0),
        (False, 0),
    ]
    for i, update in enumerate(parsed_updates):
        valid, value = validate_update(parsed_rules, update)
        assert valid == valid_results[i][0]
        assert value == valid_results[i][1]
