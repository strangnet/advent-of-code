def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def parse_rules(rules: list[str]) -> list[tuple[int, int]]:
    return [tuple(int(x) for x in rule.split("|")) for rule in rules]


def parse_input(input_data: list[str]) -> tuple[list[str], list[str]]:
    separator_index = input_data.index("")

    rules = input_data[:separator_index]
    updates = input_data[separator_index + 1 :]

    parsed_rules = parse_rules(rules)

    return parsed_rules, [[int(x) for x in update.split(",")] for update in updates]


def validate_update(
    rules: list[tuple[int, int]], update: list[int]
) -> tuple[bool, int]:
    index = {}
    for i, num in enumerate(update):
        index[num] = i

    for a, b in rules:
        if a in index and b in index and not (index[a] < index[b]):
            return False, 0

    return True, update[len(update) // 2]


def main():
    input_data = read_input("input.txt")
    parsed_rules, parsed_updates = parse_input(input_data)

    checksum = 0
    for update in parsed_updates:
        valid, value = validate_update(parsed_rules, update)
        if valid:
            checksum += value

    print(checksum)


if __name__ == "__main__":
    main()
