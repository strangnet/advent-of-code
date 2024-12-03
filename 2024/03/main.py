def read_input(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def parse_input(input_data: str) -> int:
    import re

    pattern = r"mul\((?P<a>\d+),(?P<b>\d+)\)"
    matches = re.finditer(pattern, input_data)
    return sum(int(match.group("a")) * int(match.group("b")) for match in matches)


def main():
    print("Day 03 - 2024")
    input_data = read_input("input.txt")
    print(parse_input(input_data))


if __name__ == "__main__":
    main()
