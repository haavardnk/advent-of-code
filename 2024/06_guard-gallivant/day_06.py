"""AoC 2024 Day 06: Guard Gallivant"""

from copy import deepcopy
from enum import Enum
import sys


def in_bounds(x, y) -> bool:
    return 0 <= x < len(grid[y]) - 1 and 0 <= y < len(grid) - 1


class Direction(Enum):
    Left = (-1, 0)
    Right = (1, 0)
    Up = (0, -1)
    Down = (0, 1)


direction_change = {
    Direction.Left: Direction.Up,
    Direction.Right: Direction.Down,
    Direction.Up: Direction.Right,
    Direction.Down: Direction.Left,
}

grid = [list(s.strip()) for s in sys.stdin.readlines()]

cur_pos = None
start_direction = None
visited = []

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char in "<>^v":
            cur_pos = (x, y)
            visited.append(cur_pos)
            if char == "<":
                start_direction = Direction.Left
            elif char == ">":
                start_direction = Direction.Right
            elif char == "^":
                start_direction = Direction.Up
            elif char == "v":
                start_direction = Direction.Down

direction = start_direction

while in_bounds(*cur_pos):
    next_pos = (cur_pos[0] + direction.value[0], cur_pos[1] + direction.value[1])
    if grid[next_pos[1]][next_pos[0]] == "#":
        direction = direction_change.get(direction)
        continue

    cur_pos = next_pos
    if cur_pos not in visited:
        visited.append(cur_pos)

p1 = len(visited)

obstructions = set()
positions = set(visited)
positions.remove(visited[0])

for pos in positions:
    grid2 = deepcopy(grid)
    grid2[pos[1]][pos[0]] = "#"
    cur_pos = visited[0]
    direction = start_direction
    loop = []

    while in_bounds(*cur_pos):
        next_pos = (cur_pos[0] + direction.value[0], cur_pos[1] + direction.value[1])

        if (next_pos, direction) in loop:
            obstructions.add(pos)
            break

        if grid2[next_pos[1]][next_pos[0]] == "#":
            direction = direction_change.get(direction)
            continue

        cur_pos = next_pos
        loop.append((cur_pos, direction))

p2 = len(obstructions)

print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
