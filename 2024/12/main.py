def read_input(file_path) -> list[list[int]]:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


fencing = list[list[int]]


def find_fencing(input_data: str):
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


def main():
    input_data = read_input("test_input.txt")
    print(input_data)
    find_fencing(input_data)
    print(fencing)


if __name__ == "__main__":
    main()
