"""AoC 2024 Day 02: Red-Nosed Reports"""

import sys


def valid_report(levels) -> bool:
    inc = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    dec = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))

    return inc or dec


def valid_one_removed(levels) -> bool:
    for i in range(len(levels)):
        if valid_report(levels[:i] + levels[i + 1 :]):
            return True
    return False


def part_01(reports) -> int:
    res = 0
    for levels in reports:
        if valid_report(levels):
            res += 1

    return res


def part_02(reports) -> int:
    res = 0
    for levels in reports:
        if valid_report(levels) or valid_one_removed(levels):
            res += 1

    return res


data = [s.strip().split(" ") for s in sys.stdin.readlines()]
data = [[int(item) for item in line] for line in data]

sol_01 = part_01(data)
sol_02 = part_02(data)

print(f"Solution for part 1: {sol_01}")
print(f"Solution for part 2: {sol_02}")
