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


def compact_contiguous(data: list):
    fetch_id = len(data) - 1

    while fetch_id > 0:
        while data[fetch_id] == ".":
            fetch_id -= 1
        size = 1
        while fetch_id > 0 and data[fetch_id] == data[fetch_id - 1]:
            size += 1
            fetch_id -= 1

        step_id = 0

        while step_id < fetch_id:
            size2 = 0
            while data[step_id] != ".":
                step_id += 1
            while step_id < fetch_id and data[step_id] == ".":
                step_id += 1
                size2 += 1
            if size2 >= size:
                temp_step = step_id - size2
                temp_fetch = fetch_id + size - 1
                for i in range(size):
                    data[temp_step] = data[temp_fetch]
                    data[temp_fetch] = "."
                    temp_step += 1
                    temp_fetch -= 1
                break

        fetch_id -= 1

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
    uncompressed = uncompress(data)
    compacted = compact(uncompressed.copy())
    compacted_c = compact_contiguous(uncompressed.copy())
    checksummed = checksum(compacted)
    print(checksummed)
    cc = checksum(compacted_c)
    print(cc)


if __name__ == "__main__":
    main()
