"""AoC 2024 Day 16: Reindeer Maze"""

from collections import defaultdict, deque
from math import inf
import sys


def solve(start_position, maze):
    seats = set()
    seen = defaultdict(lambda: inf)
    dq = deque()

    path = set()
    path.add(start_position)
    dq.append((start_position, (1, 0), 0, path))

    lowest_score = inf
    while dq:
        position, direction, score, path = dq.popleft()

        if score > seen[(position, direction)] or score > lowest_score:
            continue

        seen[(position, direction)] = score

        if maze[position[1]][position[0]] == "E":
            if score < lowest_score:
                lowest_score = score
                seats = path
            elif score == lowest_score:
                seats.update(path)
            continue

        dx, dy = direction
        x, y = position
        new_position = (x + dx, y + dy)
        if maze[new_position[1]][new_position[0]] != "#":
            new_path = path.copy()
            new_path.add(new_position)
            dq.append((new_position, direction, score + 1, new_path))

        new_direction = (dy, dx)
        dq.append((position, new_direction, score + 1000, path))

        new_direction = (-dy, -dx)
        dq.append((position, new_direction, score + 1000, path))

    return lowest_score, seats


maze = [list(s.strip()) for s in sys.stdin.readlines()]

for y, line in enumerate(maze):
    if "S" in line:
        start_position = (line.index("S"), y)

score, visited = solve(start_position, maze)

print(f"Solution for part 1: {score}")
print(f"Solution for part 2: {len(visited)}")
