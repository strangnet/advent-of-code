from main import correct_update, validate_update, read_input, parse_input


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


def test_correct_update():
    input_data = read_input("test_input.txt")
    parsed_rules, _ = parse_input(input_data)

    valid, value = correct_update(parsed_rules, [75, 97, 47, 61, 53])
    assert valid
    assert value == 47

    valid, value = correct_update(parsed_rules, [61, 13, 29])
    assert valid
    assert value == 29

    valid, value = correct_update(parsed_rules, [97, 13, 74, 29, 47])
    assert valid
    assert value == 47
