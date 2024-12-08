import itertools


def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read()


def find_antennas(input) -> dict[str, list[tuple[int, int]]]:
    antennas = {}
    for i, line in enumerate(input.split("\n")):
        for j, char in enumerate(line):
            if char.isalpha() or char.isdigit():
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((i, j))
    return antennas


def calculate_distance(antenna1, antenna2) -> tuple[int, int]:
    return (antenna1[0] - antenna2[0]), (antenna1[1] - antenna2[1])


def find_anti_nodes(antennas: dict[str, list[tuple[int, int]]]):
    an = set()
    for antenna, nodes in antennas.items():
        combinations = list(itertools.combinations(nodes, 2))
        for node_pair in combinations:
            distance = calculate_distance(node_pair[0], node_pair[1])
            anti_nodes = (
                add_tuples(node_pair[0], distance),
                add_tuples(node_pair[1], (-distance[0], -distance[1])),
            )
            for anti_node in anti_nodes:
                an.add(anti_node)
    return an


def find_anti_nodes_with_harmonics(
    antennas: dict[str, list[tuple[int, int]]], width: int, height: int
):
    an = set()
    for antenna, nodes in antennas.items():
        combinations = list(itertools.combinations(nodes, 2))
        for node_pair in combinations:
            distance = calculate_distance(node_pair[0], node_pair[1])
            round = -1  # now we're talking! :)
            while True:
                round += 1
                anti_node = add_tuples(
                    node_pair[0], (distance[0] * round, distance[1] * round)
                )
                if (
                    anti_node[0] >= height
                    or anti_node[1] >= width
                    or anti_node[0] < 0
                    or anti_node[1] < 0
                ):
                    break
                an.add(anti_node)
            round = -1
            while True:
                round += 1
                anti_node = add_tuples(
                    node_pair[1], (-distance[0] * round, -distance[1] * round)
                )
                if (
                    anti_node[0] >= height
                    or anti_node[1] >= width
                    or anti_node[0] < 0
                    or anti_node[1] < 0
                ):
                    break
                an.add(anti_node)
    return an


def add_tuples(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return (t1[0] + t2[0], t1[1] + t2[1])


def main():
    input = read_input("input.txt")
    width = len(input.split("\n")[0])
    height = len(input.split("\n"))
    antennas = find_antennas(input)
    anti_nodes = find_anti_nodes(antennas)
    count = 0
    for node in anti_nodes:
        if (node[0] < height and node[1] < width) and (node[0] >= 0 and node[1] >= 0):
            count += 1
    print(f"count: {count}")
    anh = find_anti_nodes_with_harmonics(antennas, width, height)
    print(f"count with harmonics: {len(anh)}")


if __name__ == "__main__":
    main()
