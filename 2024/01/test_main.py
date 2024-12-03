from main import calculate_distances, count_appearances, read_input


def test_calculate_distances():
    lists = read_input("test_input.txt")
    assert calculate_distances(lists) == 11


def test_count_appearances():
    lists = read_input("test_input.txt")
    assert count_appearances(lists) == 31
