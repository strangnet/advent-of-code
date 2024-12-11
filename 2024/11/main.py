def read_input(file_path) -> list[int]:
    with open(file_path, "r") as file:
        return [int(line) for line in file.read().split(" ")]


def split_until(data: list[int], current: int, until: int):
    if current == until:
        return data
    else:
        res = []
        for item in data:
            if item == 0:
                res.append(1)
            elif len(str(item)) % 2 == 0:
                i = len(str(item)) // 2
                a = int(str(item)[:i])
                b = int(str(item)[i:])

                res.append(a)
                res.append(b)
            else:
                res.append(item * 2024)

        return split_until(res, current + 1, until)


def main():
    input_data = read_input("input.txt")
    print(input_data)
    split_data = split_until(input_data, 0, 25)
    print(len(split_data))


if __name__ == "__main__":
    main()
