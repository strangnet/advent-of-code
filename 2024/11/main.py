from concurrent.futures import ThreadPoolExecutor
import threading


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


lookup = {}


def recursive_split(data: list[int], until: int) -> int:
    res = 0
    for item in data:
        res += split_item(item, until)
    return res


def split_item(item: int, until: int):
    if until == 0:
        return 1

    if (item, until) not in lookup:
        res = 0
        if item == 0:
            res = split_item(1, until - 1)
        elif len(str(item)) % 2 == 0:
            i = len(str(item)) // 2

            res += split_item(int(str(item)[:i]), until - 1)
            res += split_item(int(str(item)[i:]), until - 1)
        else:
            res += split_item(item * 2024, until - 1)

        lookup[(item, until)] = res
    return lookup[(item, until)]


def main():
    input_data = read_input("input.txt")
    print(input_data)
    split_data = split_until(input_data.copy(), 0, 25)
    print(len(split_data))
    print(recursive_split(input_data.copy(), 75))
    print(len(lookup))


if __name__ == "__main__":
    main()
