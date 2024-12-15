def print_board(board):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            print(cell, end="")
        print()


def main():
    board = []
    instructions = ""
    with open("input.txt", "r") as f:
        chunks = f.read().split("\n\n")

    board = [list(row) for row in chunks[0].split("\n")]
    print_board(board)
    instructions = chunks[1]

    for c, row in enumerate(board):
        for r, cell in enumerate(row):
            if cell == "@":
                robot = (c, r)

    move = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    for line in instructions.split("\n"):
        for instr in line:
            d_x, d_y = move[instr]
            new_x = robot[0] + d_x
            new_y = robot[1] + d_y

            boxes_to_move = []
            while board[new_y][new_x] == "O":
                boxes_to_move.append((new_x, new_y))
                new_x += d_x
                new_y += d_y

            if board[new_y][new_x] == "#":
                continue
            else:
                if board[new_y][new_x] != ".":
                    continue
                else:
                    for a, b in boxes_to_move[::-1]:
                        board[new_y][new_x] = "O"
                        new_x = a
                        new_y = b
                    board[robot[1]][robot[0]] = "."
                    robot = (robot[0] + d_x, robot[1] + d_y)

    board[robot[1]][robot[0]] = "@"
    print_board(board)

    gps_sum = 0
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == "O":
                gps_sum += 100 * y + x

    print(gps_sum)


if __name__ == "__main__":
    main()
