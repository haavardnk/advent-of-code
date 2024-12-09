"""AoC 2024 Day 09: Disk Fragmenter"""

import sys


def find_empty(blocks: list, n: int):
    for i in range(len(blocks) - n + 1):
        if all(block == "." for block in blocks[i : i + n]):
            return i
    return None


def compact(blocks: list, group: bool):
    compacted = blocks[:]
    for i in reversed(range(len(compacted))):
        id = compacted[i]
        if id != ".":
            if group:
                file = [i for i, val in enumerate(compacted) if val == id]
                empty = find_empty(compacted, len(file))
                if empty is not None and empty < file[0]:
                    for j in file:
                        compacted[j] = "."
                    for j in range(len(file)):
                        compacted[empty + j] = id
                elif compacted.index(".") > file[0]:
                    break
            else:
                empty = compacted.index(".")
                if empty < i:
                    compacted[empty], compacted[i] = compacted[i], "."
                else:
                    break

    return compacted


disk_map = sys.stdin.read()

blocks = []
file_id = 0
for i, char in enumerate(disk_map):
    segment = [file_id] * int(char) if i % 2 == 0 else ["."] * int(char)
    blocks.extend(segment)
    file_id += i % 2


p1 = sum(i * int(id) for i, id in enumerate(compact(blocks, False)) if id != ".")
p2 = sum(i * int(id) for i, id in enumerate(compact(blocks, True)) if id != ".")


print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
