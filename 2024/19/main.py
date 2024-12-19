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


def all_valid(design, patterns):
    if design not in cache:
        if len(design) == 0:
            return 1

        cache[design] = 0
        for pattern in [p for p in patterns if len(p) <= len(design)]:
            if design.startswith(pattern):
                cache[design] += all_valid(design[len(pattern) :], patterns)

    return cache[design]


def main():
    global cache
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

    cache = {}
    p = 0
    for design in designs:
        p += all_valid(design, patterns)

    print(p)


if __name__ == "__main__":
    main()
