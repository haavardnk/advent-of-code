"""AoC 2024 Day 10: Hoof It"""

import sys


def in_bounds(x, y) -> bool:
    return 0 <= x < len(data) and 0 <= y < len(data)


def check_adjacent(pos: tuple, data: list, elevation: int) -> list:
    positions = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_pos = pos[0] + dx, pos[1] + dy
        if in_bounds(*new_pos) and data[new_pos[1]][new_pos[0]] == elevation + 1:
            positions.append(new_pos)

    return positions


data = [s.strip() for s in sys.stdin.readlines()]
data = [[int(item) for item in line] for line in data]

start_positions = []

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 0:
            start_positions.append((x, y))


def solve(part2: bool) -> int:
    score = 0
    for position in start_positions:
        elevation = 0
        visited = set()
        cur_pos = [position]

        while elevation < 9:
            next_pos = []
            for pos in cur_pos:
                if part2:
                    next_pos.extend(check_adjacent(pos, data, elevation))
                else:
                    if (pos, elevation) not in visited:
                        visited.add((pos, elevation))
                        next_pos.extend(check_adjacent(pos, data, elevation))
            cur_pos = next_pos
            elevation += 1

        score += len(cur_pos) if part2 else len(set(cur_pos))

    return score


p1 = solve(False)
p2 = solve(True)

print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
