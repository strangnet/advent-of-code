from main import (
    calculate_next_position,
    calculate_visited_position,
    is_outside,
    next_direction,
    parse_input,
    read_input,
    MOVE_E,
    MOVE_N,
    MOVE_S,
    MOVE_W,
)


def test_is_outside():
    patrol_map = [
        [".", ".", "#", ".", "."],
    ]
    assert is_outside(patrol_map, (0, -1))
    assert not is_outside(patrol_map, (0, 0))
    assert not is_outside(patrol_map, (0, 1))
    assert not is_outside(patrol_map, (0, 2))
    assert not is_outside(patrol_map, (0, 3))
    assert not is_outside(patrol_map, (0, 4))
    assert is_outside(patrol_map, (0, 5))
    assert is_outside(patrol_map, (-1, 0))
    assert is_outside(patrol_map, (1, 0))


def test_calculate_visited_position():
    input_data = read_input("test_input.txt")
    patrol_map = parse_input(input_data)
    assert calculate_visited_position(patrol_map) == 0

    patrol_map = [
        ["X", "X", "X", "X", "X"],
    ]
    assert calculate_visited_position(patrol_map) == 5


def test_calculate_next_position():
    assert calculate_next_position((0, 0), MOVE_N) == (-1, 0)  # Move up decreases row
    assert calculate_next_position((0, 0), MOVE_S) == (1, 0)  # Move down increases row
    assert calculate_next_position((0, 0), MOVE_E) == (
        0,
        1,
    )  # Move right increases column
    assert calculate_next_position((0, 0), MOVE_W) == (
        0,
        -1,
    )  # Move left decreases column

    # Test from non-zero starting positions
    assert calculate_next_position((2, 3), MOVE_N) == (1, 3)
    assert calculate_next_position((2, 3), MOVE_S) == (3, 3)
    assert calculate_next_position((2, 3), MOVE_E) == (2, 4)
    assert calculate_next_position((2, 3), MOVE_W) == (2, 2)


def test_calculate_next_direction():
    assert next_direction(MOVE_N) == MOVE_E
    assert next_direction(MOVE_E) == MOVE_S
    assert next_direction(MOVE_S) == MOVE_W
    assert next_direction(MOVE_W) == MOVE_N
