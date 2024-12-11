"""AoC 2024 Day 11: Plutonian Pebbles"""

from functools import cache
import sys


def split_stone(n: int) -> tuple[int, int]:
    string_n = str(n)
    half = len(string_n) // 2
    return int(string_n[:half]), int(string_n[half:])


@cache
def count(stone: int, blinks: int):
    if blinks == 0:
        return 1

    if stone == 0:
        return count(1, blinks - 1)

    elif len(str(stone)) % 2 == 0:
        first, second = split_stone(stone)
        return count(first, blinks - 1) + count(second, blinks - 1)

    else:
        return count(stone * 2024, blinks - 1)


data = sys.stdin.read()
stones = [int(item) for item in data.split()]

print(f"Solution for part 1: {sum(count(stone, 25) for stone in stones)}")
print(f"Solution for part 2: {sum(count(stone, 75) for stone in stones)}")
