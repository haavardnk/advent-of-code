"""AoC 2024 Day 19: Linen Layout"""

from functools import cache
import sys


@cache
def count_ways(design):
    if not design:
        return 1

    ways = 0
    for towel in towels:
        if design.startswith(towel):
            remaining_design = design[len(towel) :]
            ways += count_ways(remaining_design)

    return ways


data = [s.strip() for s in sys.stdin.readlines()]
towels = [t.strip() for t in data[0].split(",")]
designs = data[2:]

p1, p2 = 0, 0
for design in designs:
    ways = count_ways(design)
    if ways:
        p1 += 1
    p2 += ways


print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
