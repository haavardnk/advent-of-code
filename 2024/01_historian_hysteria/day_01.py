"""AoC 2024 Day 01: Historian Hysteria"""

import sys


def part_01(x, y) -> int:
    return sum(abs(a - b) for a, b in zip(x, y))


def part_02(x, y) -> int:
    return sum(x_val * y.count(x_val) for x_val in x)


data = [s.strip().split("  ") for s in sys.stdin.readlines()]
x, y = (sorted(map(int, t)) for t in zip(*data))

sol_01 = part_01(x, y)
sol_02 = part_02(x, y)

print(f"Solution for part 1: {sol_01}")
print(f"Solution for part 2: {sol_02}")
