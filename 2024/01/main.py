def read_input(file_path: str) -> tuple[list[int], list[int]]:
    lists: tuple[list[int], list[int]] = ([], [])
    with open(file_path, "r") as file:
        for line in file:
            a, b = map(int, line.split())
            lists[0].append(a)
            lists[1].append(b)
    lists[0].sort()
    lists[1].sort()
    return lists


def calculate_distances(lists: tuple[list[int], list[int]]) -> int:
    total_distance = 0
    for a, b in zip(lists[0], lists[1]):
        total_distance += abs(a - b)
    return total_distance


def count_appearances(lists: tuple[list[int], list[int]]) -> int:
    counter = 0
    appearances = {}
    for a in lists[1]:
        appearances[a] = appearances.get(a, 0) + 1
    for b in lists[0]:
        counter += b * appearances[b] if b in appearances else 0
    return counter


def main():
    print("Day 01 - 2024")
    input_data = read_input("input.txt")
    print(calculate_distances(input_data))
    print(count_appearances(input_data))


if __name__ == "__main__":
    main()
