"""AoC 2024 Day 18: RAM Run"""

from collections import deque
from math import inf
import sys


def in_bounds(x, y, memory) -> bool:
    return 0 <= x < len(memory[0]) and 0 <= y < len(memory)


def solve(memory):
    seen = set()
    dq = deque()
    dq.append(((0, 0), 0))

    while dq:
        position, score = dq.popleft()

        if position in seen:
            continue

        seen.add(position)

        if position == (len(memory[0]) - 1, len(memory) - 1):
            return score

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            dx, dy = direction
            x, y = position
            new_position = (x + dx, y + dy)
            if (
                in_bounds(new_position[0], new_position[1], memory)
                and memory[new_position[1]][new_position[0]] != "#"
            ):
                dq.append((new_position, score + 1))

    return inf


data = [s.strip() for s in sys.stdin.readlines()]
bytes = []
for line in data:
    byte = (int(line.split(",")[0]), (int(line.split(",")[1])))
    bytes.append(byte)

memory = [["." for _ in range(71)] for _ in range(71)]

for i in range(1024):
    x, y = bytes[i]
    memory[y][x] = "#"
p1 = solve(memory)

for i in range(1024, len(bytes)):
    x, y = bytes[i]
    memory[y][x] = "#"

    if solve(memory) == inf:
        p2 = f"{x},{y}"
        break


print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
