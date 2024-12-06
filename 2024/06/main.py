from copy import deepcopy


MOVE_N = (-1, 0)
MOVE_S = (1, 0)
MOVE_E = (0, 1)
MOVE_W = (0, -1)

current_direction = MOVE_N
current_position = (0, 0)
guard_positions = set()


def read_input(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def parse_input(input_data: str) -> list[list[str]]:
    return [list(line) for line in input_data.split("\n")]


def start_position(patrol_map: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(patrol_map):
        for j, cell in enumerate(row):
            if cell == "^":
                return (i, j)


def is_outside(patrol_map: list[list[str]], position: tuple[int, int]) -> bool:
    return (
        position[0] < 0
        or position[0] >= len(patrol_map)
        or position[1] < 0
        or position[1] >= len(patrol_map[0])
    )


def is_obstacle(patrol_map: list[list[str]], position: tuple[int, int]) -> bool:
    return patrol_map[position[0]][position[1]] == "#"


def next_direction(current_direction: tuple[int, int]) -> tuple[int, int]:
    if current_direction == MOVE_N:
        return MOVE_E
    elif current_direction == MOVE_E:
        return MOVE_S
    elif current_direction == MOVE_S:
        return MOVE_W
    elif current_direction == MOVE_W:
        return MOVE_N


def calculate_visited_position(patrol_map: list[list[str]]) -> int:
    visited_positons = 0

    for i in range(len(patrol_map)):
        for j in range(len(patrol_map[i])):
            if patrol_map[i][j] == "X":
                visited_positons += 1

    return visited_positons


def add_tuples(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return (t1[0] + t2[0], t1[1] + t2[1])


def calculate_next_position(
    current_position: tuple[int, int], current_direction: tuple[int, int]
) -> tuple[int, int]:
    return add_tuples(current_position, current_direction)


def walk_map(
    patrol_map: list[list[str]], start_position: tuple[int, int]
) -> list[list[str]]:
    global current_position
    global current_direction
    global guard_positions

    patrol_map[current_position[0]][current_position[1]] = "X"
    guard_positions.add(current_position)
    next_position = calculate_next_position(current_position, current_direction)
    while not is_outside(patrol_map, next_position):
        patrol_map[current_position[0]][current_position[1]] = "X"
        guard_positions.add(current_position)
        if is_obstacle(patrol_map, next_position):
            current_direction = next_direction(current_direction)
            next_position = calculate_next_position(current_position, current_direction)
        current_position = next_position
        next_position = calculate_next_position(current_position, current_direction)

    patrol_map[current_position[0]][current_position[1]] = "X"
    guard_positions.add(current_position)
    return patrol_map


def is_loopable(patrol_map: list[list[str]], position: tuple[int, int]) -> bool:
    global current_position

    if is_obstacle(patrol_map, position):
        return False
    current_position = start_position(patrol_map)

    patrol_map[position[0]][position[1]] = "#"

    direction = MOVE_N
    visited = set()
    while True:
        if (current_position, direction) in visited:
            patrol_map[position[0]][position[1]] = "."
            return True
        visited.add((current_position, direction))
        next_position = calculate_next_position(current_position, direction)
        if is_outside(patrol_map, next_position):
            patrol_map[position[0]][position[1]] = "."
            return False

        if is_obstacle(patrol_map, next_position):
            direction = next_direction(direction)
            next_position = calculate_next_position(current_position, direction)
        else:
            current_position = next_position


def find_obstacle_locations(original_map: list[list[str]]) -> list[tuple[int, int]]:
    global guard_positions

    obstacles = []

    for position in guard_positions:
        patrol_map = deepcopy(original_map)
        looped = is_loopable(patrol_map, position)
        if looped:
            obstacles.append(position)

    return obstacles


def print_map(a_map: list[list[str]]) -> None:
    for row in a_map:
        print("".join(row))


def main():
    global current_position
    input_data = read_input("input.txt")
    patrol_map = parse_input(input_data)

    current_position = start_position(patrol_map)
    final_map = walk_map(patrol_map, current_position)

    pos = calculate_visited_position(final_map)
    print(pos)

    patrol_map = parse_input(input_data)
    locs = find_obstacle_locations(patrol_map)
    print(len(locs))


if __name__ == "__main__":
    main()
