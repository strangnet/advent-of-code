MOVE_N = (0, -1)
MOVE_S = (0, 1)
MOVE_E = (1, 0)
MOVE_W = (-1, 0)
MOVE_NE = (1, -1)
MOVE_NW = (-1, -1)
MOVE_SE = (1, 1)
MOVE_SW = (-1, 1)

ALL_MOVES = [MOVE_N, MOVE_S, MOVE_E, MOVE_W, MOVE_NE, MOVE_NW, MOVE_SE, MOVE_SW]

ALL_MOVES_MAS = [MOVE_NE, MOVE_NW, MOVE_SE, MOVE_SW]


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


def valid_moves(
    map: list[str], coordinate: int, all_moves: list[str]
) -> list[tuple[int, int]]:
    moves = []
    for move in all_moves:
        if valid_move(map, coordinate, move):
            moves.append(move)

    return moves


def found_str(
    str: str,
    map: list[str],
    coordinate: tuple[int, int],
    last_move: tuple[int, int] | None = None,
    all_moves: list[str] = ALL_MOVES,
) -> bool:
    found = 0
    if str[0] == map[coordinate[1]][coordinate[0]]:
        if len(str) == 1:
            return True

        moves = []
        vm = valid_moves(map, coordinate, all_moves)
        if last_move is not None:
            if last_move in vm:
                moves = [last_move]
        else:
            moves = vm

        for move in moves:
            found += found_str(
                str[1:],
                map,
                (coordinate[0] + move[0], coordinate[1] + move[1]),
                last_move=move,
                all_moves=all_moves,
            )
    return found


def count_xmas(input_data: list[str]) -> int:
    found_xmas = 0

    for i, line in enumerate(input_data):
        for j, char in enumerate(line):
            if char == "X":
                found_xmas += found_str("XMAS", input_data, (j, i), all_moves=ALL_MOVES)
    return found_xmas


def count_mas(input_data: list[str]) -> int:
    found_mas = 0

    for i, line in enumerate(input_data):
        for j, char in enumerate(line):
            if char == "A":
                found_as_ne = found_str("AS", input_data, (j, i), all_moves=[MOVE_NE])
                found_as_nw = found_str("AS", input_data, (j, i), all_moves=[MOVE_NW])
                found_as_se = found_str("AS", input_data, (j, i), all_moves=[MOVE_SE])
                found_as_sw = found_str("AS", input_data, (j, i), all_moves=[MOVE_SW])
                found_as = found_as_ne + found_as_nw + found_as_se + found_as_sw

                found_am_ne = found_str("AM", input_data, (j, i), all_moves=[MOVE_NE])
                found_am_nw = found_str("AM", input_data, (j, i), all_moves=[MOVE_NW])
                found_am_se = found_str("AM", input_data, (j, i), all_moves=[MOVE_SE])
                found_am_sw = found_str("AM", input_data, (j, i), all_moves=[MOVE_SW])
                found_am = found_am_ne + found_am_nw + found_am_se + found_am_sw

                valid = True
                if (found_as_ne and found_as_sw) or (found_as_nw and found_as_se):
                    valid = False

                if (found_am_ne and found_am_sw) or (found_am_nw and found_am_se):
                    valid = False

                if valid and found_as == 2 and found_am == 2:
                    found_mas += 1

    return found_mas


def main():
    input_data = read_input("input.txt")
    count_x = count_xmas(input_data)
    print(count_x)

    count_m = count_mas(input_data)
    print(count_m)


if __name__ == "__main__":
    main()
