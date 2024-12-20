with open("input.txt", "r") as f:
    data = f.read()

maze = [list(line) for line in data.split("\n")]
mw = len(maze[0])
mh = len(maze)

for y, line in enumerate(maze):
    for x, col in enumerate(line):
        if col == "S":
            start = (x, y)
            maze[y][x] = "."
        if col == "E":
            end = (x, y)
            maze[y][x] = "."

sx, sy = start
ex, ey = end

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

queue = [start]
visited = set()
time = {}
cheats = []
ps = 0
while queue:
    cx, cy = queue.pop(0)
    visited.add((cx, cy))
    time[(cx, cy)] = ps
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if (nx, ny) == (ex, ey):
            visited.add((nx, ny))
            ps += 1
            time[(nx, ny)] = ps
            break
        if (nx, ny) in visited:
            continue
        if maze[ny][nx] == "#":
            tx, ty = nx + dx, ny + dy
            if 0 <= tx < mw and 0 <= ty < mh:
                if maze[ty][tx] == "." and (tx, ty) not in visited:
                    cheats.append(((tx, ty), ps + 2))
            continue
        queue.append((nx, ny))
    ps += 1

cg = {}
for k, v in cheats:
    s = time[k] - v
    if s in cg:
        cg[s] += 1
    else:
        cg[s] = 1

filtered_cg = {k: v for k, v in cg.items() if k >= 100}
print("Sum of values:", sum(filtered_cg.values()))
