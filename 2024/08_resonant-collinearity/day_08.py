"""AoC 2024 Day 08: Resonant Collinearity"""

import sys
from collections import defaultdict

data = [s.strip() for s in sys.stdin.readlines()]
antennas = defaultdict(list)
antinodes = set()
antinodes2 = set()


def in_bounds(x, y) -> bool:
    return 0 <= x < len(data) and 0 <= y < len(data)


for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            antennas[char].append((x, y))

for positions in antennas.values():
    for i, p1 in enumerate(positions):
        for j, p2 in enumerate(positions):
            if i == j:
                continue
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]

            for node in [(p1[0] - dx, p1[1] - dy), (p2[0] + dx, p2[1] + dy)]:
                if in_bounds(*node):
                    antinodes.add(node)

            k = 0
            while True:
                node1 = (p1[0] - k * dx, p1[1] - k * dy)
                if in_bounds(node1[0], node1[1]):
                    antinodes2.add(node1)
                else:
                    break
                k += 1
            k = 0

            while True:
                node2 = (p2[0] + k * dx, p2[1] + k * dy)
                if in_bounds(node2[0], node2[1]):
                    antinodes2.add(node2)
                else:
                    break
                k += 1

print(f"Solution for part 1: {len(antinodes)}")
print(f"Solution for part 2: {len(antinodes2)}")
