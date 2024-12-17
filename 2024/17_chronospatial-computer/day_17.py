"""AoC 2024 Day 17: Chronospatial Computer"""

import sys


def combo_operand(operand, A, B, C):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C


def run(A, B, C, program) -> list:
    pointer = 0
    output = []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        if opcode == 0:
            A = A // 2 ** combo_operand(operand, A, B, C)
            pointer += 2
        elif opcode == 1:
            B = B ^ operand
            pointer += 2
        elif opcode == 2:
            B = combo_operand(operand, A, B, C) % 8
            pointer += 2
        elif opcode == 3:
            if A == 0:
                pointer += 2
            else:
                pointer = operand
        elif opcode == 4:
            B = B ^ C
            pointer += 2
        elif opcode == 5:
            output.append(combo_operand(operand, A, B, C) % 8)
            pointer += 2
        elif opcode == 6:
            B = A // 2 ** combo_operand(operand, A, B, C)
            pointer += 2
        elif opcode == 7:
            C = A // 2 ** combo_operand(operand, A, B, C)
            pointer += 2
    return output


data = [s.strip() for s in sys.stdin.readlines()]
for line in data:
    if "A" in line:
        A = int(line.split(":")[1])
    if "B" in line:
        B = int(line.split(":")[1])
    if "C" in line:
        C = int(line.split(":")[1])
    if "Program" in line:
        program = [int(p) for p in line.split(":")[1].split(",")]

candidates = [0]
for length in range(1, len(program) + 1):
    out = []
    for c in candidates:
        for i in range(8):
            a = 8 * c + i
            if run(a, 0, 0, program) == program[-length:]:
                out.append(a)
    candidates = out


print(f"Solution for part 1: {",".join([str(x) for x in run(A, B, C, program)])}")
print(f"Solution for part 2: {min(candidates)}")
