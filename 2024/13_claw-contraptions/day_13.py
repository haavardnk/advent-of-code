"""AoC 2024 Day 13: Claw Contraption"""

import sys
import numpy as np


def solve(machine, part2: bool):
    vars = np.array(
        [[machine["A"][0], machine["B"][0]], [machine["A"][1], machine["B"][1]]]
    )
    consts = np.array(
        [
            machine["Prize"][0] + 10000000000000 * part2,
            machine["Prize"][1] + 10000000000000 * part2,
        ]
    )

    a, b = np.linalg.solve(vars, consts)
    a = round(a)
    b = round(b)

    if (
        vars[0][0] * a + vars[0][1] * b == consts[0]
        and vars[1][0] * a + vars[1][1] * b == consts[1]
    ):
        return 3 * a + b
    else:
        return 0


data = [s.strip() for s in sys.stdin.readlines()]
claw_machines = [{}]
for line in data:
    if line:
        x, y = line.split(":")[1].split(",")
        if line.startswith("Button A:"):
            claw_machines[-1]["A"] = (int(x.split("+")[1]), int(y.split("+")[1]))
        elif line.startswith("Button B:"):
            claw_machines[-1]["B"] = (int(x.split("+")[1]), int(y.split("+")[1]))
        elif line.startswith("Prize:"):
            claw_machines[-1]["Prize"] = (int(x.split("=")[1]), int(y.split("=")[1]))
    else:
        claw_machines.append({})


p1 = sum(solve(machine, False) for machine in claw_machines)
p2 = sum(solve(machine, True) for machine in claw_machines)

print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
