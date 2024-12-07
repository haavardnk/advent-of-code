"""AoC 2024 Day 07: Bridge Repair"""

import sys
from itertools import product


data = [s.strip() for s in sys.stdin.readlines()]

p1 = 0
p2 = 0


def check_eq(total, nums, operators) -> bool:
    for ops in product(operators, repeat=len(nums) - 1):
        s = nums[0]
        for i, op in enumerate(ops):
            if op == "+":
                s += nums[i + 1]
            elif op == "*":
                s *= nums[i + 1]
            elif op == "||":
                s = int(str(s) + str(nums[i + 1]))
        if s == total:
            return True
    return False


for line in data:
    total, nums = line.split(":")
    total = int(total)
    nums = list(map(int, nums.split()))
    if check_eq(total, nums, ["+", "*"]):
        p1 += total
    if check_eq(total, nums, ["+", "*", "||"]):
        p2 += total

print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
