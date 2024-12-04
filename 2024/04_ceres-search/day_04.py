"""AoC 2024 Day 04: Ceres Search"""

import sys


def check_pattern(rows, x, y, dx, dy, pattern) -> bool:
    if (
        x >= len(rows)
        or x + (len(pattern) - 1) * dx < 0
        or y + (len(pattern) - 1) * dy < 0
        or x + (len(pattern) - 1) * dx >= len(rows[y])
        or y + (len(pattern) - 1) * dy >= len(rows)
    ):
        return False

    return all(
        (rows[y + i * dy][x + i * dx] == pattern[i] for i in range(len(pattern)))
    )


def part_01(rows) -> int:
    res = 0
    pattern = "XMAS"
    dx_dy = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
    ]

    for x, y in ((x, y) for y in range(len(rows)) for x in range(len(rows[y]))):
        for dx, dy in dx_dy:
            if check_pattern(data, x, y, dx, dy, pattern):
                res += 1

    return res


def part_02(rows) -> int:
    res = 0
    patterns = ["MAS", "SAM"]

    for x, y in ((x, y) for y in range(len(rows)) for x in range(len(rows[y]))):
        if any(check_pattern(rows, x, y, 1, 1, p1) for p1 in patterns) or any(
            check_pattern(rows, x + 2, y, -1, 1, p2) for p2 in patterns
        ):
            res += 1

    return res


data = [s.strip() for s in sys.stdin.readlines()]

print(f"Solution for part 1: {part_01(data)}")
print(f"Solution for part 2: {part_02(data)}")
