from typing import Callable


def read_input(file_path: str) -> list[list[int]]:
    with open(file_path, "r") as file:
        return [list(map(int, line.split())) for line in file]


def calculate_safe_reports(lists: list[list[int]]) -> int:
    counter = 0
    for list in lists:
        safe = is_safe(list)
        counter += 1 if safe else 0
    return counter


def is_safe(list: list[int]) -> bool:
    safe = True
    deviation = 0
    for i in range(1, len(list)):
        diff = list[i] - list[i - 1]
        if diff == 0:
            safe = False
            break

        if abs(diff) not in range(1, 4):
            safe = False
            break

        dev = abs(diff) / diff
        if deviation == 0:
            deviation = dev
        elif deviation != dev:
            safe = False
            break

    return safe


def is_safe_with_dampener(list: list[int]) -> bool:
    if is_safe(list):
        return True
    for i in range(len(list)):
        if is_safe(list[:i] + list[i + 1 :]):
            print(i)
            return True

    return False


def calculate_safe_reports_with_dampener(lists: list[list[int]]) -> int:
    counter = 0
    for list in lists:
        safe = is_safe_with_dampener(list)
        counter += 1 if safe else 0
    return counter


def main():
    print("Day 02 - 2024")
    input_data = read_input("input.txt")
    print(calculate_safe_reports(input_data))
    print(calculate_safe_reports_with_dampener(input_data))


if __name__ == "__main__":
    main()
