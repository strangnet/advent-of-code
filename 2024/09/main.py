def uncompress(data: str):
    output = []
    id = 0
    for i, char in enumerate(data):
        if i % 2 == 0:
            output += [id] * int(char)
            id += 1
        else:
            output += "." * int(char)
    return output


def compact(data: list):
    fetch_id = len(data) - 1
    step_id = 0

    while data[step_id] != ".":
        step_id += 1

    while data[fetch_id] == ".":
        fetch_id -= 1

    while step_id < fetch_id:
        data[step_id] = data[fetch_id]
        data[fetch_id] = "."
        while data[fetch_id] == ".":
            fetch_id -= 1
        while data[step_id] != ".":
            step_id += 1

    return data


def checksum(data: str | list) -> str:
    output = 0
    for i, char in enumerate(data):
        if char == ".":
            continue
        output += i * int(char)
    return output


def read_input(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def main():
    data = read_input("input.txt")
    compacted = compact(uncompress(data))
    checksummed = checksum(compacted)
    print(checksummed)


if __name__ == "__main__":
    main()
