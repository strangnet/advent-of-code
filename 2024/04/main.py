MOVE_N = (0, -1)
MOVE_S = (0, 1)
MOVE_E = (1, 0)
MOVE_W = (-1, 0)
MOVE_NE = (1, -1)
MOVE_NW = (-1, -1)
MOVE_SE = (1, 1)
MOVE_SW = (-1, 1)

ALL_MOVES = [MOVE_N, MOVE_S, MOVE_E, MOVE_W, MOVE_NE, MOVE_NW, MOVE_SE, MOVE_SW]


def valid_move(
    map: list[list[str]], coordinate: tuple[int, int], move: tuple[int, int]
) -> bool:
    size_x = len(map[0])
    size_y = len(map)

    new_x = coordinate[0] + move[0]
    new_y = coordinate[1] + move[1]

    if new_x >= 0 and new_x < size_x and new_y >= 0 and new_y < size_y:
        return True

    return False


def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def valid_moves(map: list[str], coordinate: int) -> list[tuple[int, int]]:
    moves = []
    for move in ALL_MOVES:
        if valid_move(map, coordinate, move):
            moves.append(move)

    return moves


def found_str(
    str: str,
    map: list[str],
    coordinate: tuple[int, int],
    last_move: tuple[int, int] | None = None,
) -> bool:
    found = 0
    if str[0] == map[coordinate[1]][coordinate[0]]:
        if len(str) == 1:
            return True

        moves = []
        vm = valid_moves(map, coordinate)
        if last_move is not None:
            if last_move in vm:
                moves = [last_move]
        else:
            moves = vm

        for move in moves:
            found += found_str(
                str[1:], map, (coordinate[0] + move[0], coordinate[1] + move[1]), move
            )
    return found


def count_xmas(input_data: list[str]) -> int:
    found_xmas = 0

    for i, line in enumerate(input_data):
        for j, char in enumerate(line):
            if char == "X":
                found_xmas += found_str("XMAS", input_data, (j, i))
    return found_xmas


def main():
    input_data = read_input("input.txt")
    count = count_xmas(input_data)
    print(count)


if __name__ == "__main__":
    main()
