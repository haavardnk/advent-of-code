"""AoC 2024 Day 03: Mull It Over"""

import sys
from parse import findall


def parse_string(string):
    return findall("mul({x:d},{y:d})", string)


def part_01(data) -> int:
    res = 0
    mul_list = [m for m in parse_string(data)]

    for m in mul_list:
        res += m["x"] * m["y"]

    return res


def part_02(data) -> int:
    res = 0
    mul_list = parse_string(data)

    prev_end_index = 0
    enabled_muls = []
    mul_enabled = True

    for m in mul_list:
        start_index = m.spans["x"][1]
        end_index = m.spans["y"][1]
        preceding_text = data[prev_end_index:start_index]

        if "don't" in preceding_text:
            mul_enabled = False
        elif "do" in preceding_text:
            mul_enabled = True

        if mul_enabled:
            enabled_muls.append(m)

        prev_end_index = end_index

    for m in enabled_muls:
        res += m["x"] * m["y"]

    return res


data = "".join([s.strip() for s in sys.stdin.readlines()])

sol_01 = part_01(data)
sol_02 = part_02(data)

print(f"Solution for part 1: {sol_01}")
print(f"Solution for part 2: {sol_02}")
