import numpy as np


def read_input(file_path) -> list[str]:
    with open(file_path, "r") as file:
        return file.read().split("\n\n")


def main():
    input = read_input("input.txt")
    prizes = 0
    cost = 0
    for i in input:
        lines = i.split("\n")
        button_a_x = int(lines[0].split("Button A: ")[1].split(",")[0].split("+")[1])
        button_a_y = int(lines[0].split("Button A: ")[1].split(",")[1].split("+")[1])
        button_b_x = int(lines[1].split("Button B: ")[1].split(",")[0].split("+")[1])
        button_b_y = int(lines[1].split("Button B: ")[1].split(",")[1].split("+")[1])
        prize_x = int(lines[2].split("Prize: ")[1].split(",")[0].split("=")[1]) + 1e13
        prize_y = int(lines[2].split("Prize: ")[1].split(",")[1].split("=")[1]) + 1e13
        a = np.array([[button_a_x, button_b_x], [button_a_y, button_b_y]])
        b = np.array([prize_x, prize_y])
        sol = np.linalg.solve(a, b)
        if (
            float(format(sol[0], ".2f")).is_integer()
            and float(format(sol[1], ".2f")).is_integer()
        ):
            cost += int(sol[0] * 3 + sol[1] * 1)
            prizes += 1

    print(cost, prizes)


if __name__ == "__main__":
    main()
