filename = "input.txt"

cache = {}


def is_valid(design, patterns):
    if design not in cache:
        if len(design) == 0:
            return True

        found = False
        for pattern in [p for p in patterns if len(p) <= len(design)]:
            if design.startswith(pattern):
                found |= is_valid(design[len(pattern) :], patterns)
            cache[design] = found

    return cache[design]


def main():
    with open(filename, "r") as f:
        data = f.read()

    input = data.split("\n\n")
    patterns = input[0].split(", ")
    designs = input[1].split("\n")

    p = 0
    for design in designs:
        p += (
            1
            if is_valid(
                design,
                patterns,
            )
            else 0
        )

    print(p)


if __name__ == "__main__":
    main()
