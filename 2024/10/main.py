def construct_map(data: str) -> list[list[int]]:
    return [[int(char) for char in line] for line in data.splitlines()]


def read_input(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def find_trails(map: list[list[int]]) -> tuple[int, int]:
    c = 0
    u = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                found = find_ends(map, i, j, [])
                c += found[0]
                u += found[1]
    return c, u


def find_ends(
    map: list[list[int]], i: int, j: int, found: list[tuple[int, int]]
) -> tuple[int, int]:
    if map[i][j] == 9:
        sum = 0
        ends = 1
        if (i, j) not in found:
            found.append((i, j))
            sum = 1
        return sum, ends

    map_height = len(map)
    map_width = len(map[0])

    sum = 0
    ends = 0
    for coord in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= coord[0] < map_height and 0 <= coord[1] < map_width:
            found_ends = [0, 0]
            if map[coord[0]][coord[1]] == map[i][j] + 1:
                found_ends = find_ends(map, coord[0], coord[1], found)
            sum += found_ends[0]
            ends += found_ends[1]
    return sum, ends


def main():
    data = read_input("input.txt")
    map = construct_map(data)
    print(find_trails(map))


if __name__ == "__main__":
    main()
