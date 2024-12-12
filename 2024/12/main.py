from colorama import Fore, Style


def read_input(file_path) -> list[list[int]]:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


fencing = list[list[int]]
found = set()
regions = list[list[tuple[int, int]]]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def add_tuples(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def valid_direction(
    x: int, y: int, direction: tuple[int, int], width: int, height: int
) -> bool:
    next_pos = add_tuples((x, y), direction)
    if 0 <= next_pos[0] < width and 0 <= next_pos[1] < height and next_pos not in found:
        return True
    return False


def next_plots(input_data: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
    pos = []
    for direction in DIRECTIONS:
        if valid_direction(x, y, direction, len(input_data[0]), len(input_data)):
            pos.append(add_tuples((x, y), direction))

    return pos


def find_fencing(input_data: list[list[str]]):
    global fencing
    height = len(input_data)
    width = len(input_data[0])

    fencing = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            fence_count = 0
            plot = input_data[y][x]
            for n in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x + n[0] < 0:
                    fence_count += 1
                if x + n[0] >= width:
                    fence_count += 1
                if y + n[1] < 0:
                    fence_count += 1
                if y + n[1] >= height:
                    fence_count += 1
                neighbour = (x + n[0], y + n[1])
                if 0 <= neighbour[0] < width and 0 <= neighbour[1] < height:
                    if input_data[neighbour[1]][neighbour[0]] != plot:
                        fence_count += 1

            fencing[y][x] = fence_count


def plot_count(input_data: list[list[str]]) -> int:
    return len(input_data) * len(input_data[0])


def find_connected_plots(
    input_data: list[list[str]], x: int, y: int
) -> list[tuple[int, int]]:
    target_value = input_data[y][x]
    connected = []
    to_check = [(x, y)]

    while to_check:
        current = to_check.pop()
        if current not in connected:
            connected.append(current)
            found.add(current)

            # Check all adjacent positions
            for direction in DIRECTIONS:
                next_pos = add_tuples(current, direction)
                nx, ny = next_pos

                # Check if position is valid and has matching value
                if (
                    0 <= nx < len(input_data[0])
                    and 0 <= ny < len(input_data)
                    and input_data[ny][nx] == target_value
                    and next_pos not in connected
                ):
                    to_check.append(next_pos)

    return connected


def print_map(input_data: list[list[str]]):
    for row in input_data:
        print("".join(row))


def print_connected(input_data: list[list[str]], connected: list[tuple[int, int]]):
    for y in range(len(input_data)):
        for x in range(len(input_data[0])):
            if (x, y) in connected:
                print(Fore.RED + "o", end="")
            else:
                print(Style.RESET_ALL + input_data[y][x], end="")
        print(Style.RESET_ALL)


def calc_fencing(connected: list[tuple[int, int]]) -> int:
    return sum(fencing[y][x] for x, y in connected)


def calc_fencing2(connected: list[tuple[int, int]]) -> int:
    for x, y in connected:
        print(f"({x}, {y}) ({fencing[y][x]})")
    return 0


def main():
    input_data = read_input("test_input3.txt")
    # print_map(input_data)
    find_fencing(input_data)
    # print(" ")

    sum = 0
    for y in range(len(input_data)):
        for x in range(len(input_data[0])):
            if (x, y) not in found:
                c = find_connected_plots(input_data, x, y)
                print_connected(input_data, c)

                print(f"Found {len(c)} connected plots")
                sum += len(c) * calc_fencing2(c)
                print(" ")

    print(f"Total fencing: {sum}")


if __name__ == "__main__":
    main()
