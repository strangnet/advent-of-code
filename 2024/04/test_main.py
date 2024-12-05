from main import (
    MOVE_N,
    MOVE_E,
    MOVE_S,
    MOVE_W,
    count_xmas,
    count_mas,
    read_input,
    valid_move,
)


def test_valid_move():
    assert not valid_move([["M", "M", "M"], ["S", "A", "M"]], (0, 0), MOVE_N)
    assert valid_move([["M", "M", "M"], ["S", "A", "M"]], (0, 0), MOVE_E)
    assert not valid_move([["M", "M", "M"], ["S", "A", "M"]], (0, 0), MOVE_W)
    assert valid_move([["M", "M", "M"], ["S", "A", "M"]], (0, 0), MOVE_S)


def test_count_xmas():
    assert count_xmas(read_input("test_input.txt")) == 18


def test_count_mas():
    assert count_mas(read_input("test_input.txt")) == 9
