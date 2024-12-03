def read_input(file_path: str) -> list[list[int]]:
    with open(file_path, "r") as file:
        return [list(map(int, line.split())) for line in file]


def calculate_safe_reports(lists: list[list[int]]) -> int:
    counter = 0
    for list in lists:
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

        counter += 1 if safe else 0
    return counter


def main():
    print("Day 02 - 2024")
    input_data = read_input("input.txt")
    print(calculate_safe_reports(input_data))


if __name__ == "__main__":
    main()
