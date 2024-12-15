"""AoC 2024 Day 15: Warehouse Woes"""

import sys


def parse(data, part2=False):
    grid = []
    moves = ""
    m = False
    for line in data:
        if line.startswith("#"):
            if part2:
                line = (
                    line.replace("#", "##")
                    .replace("O", "[]")
                    .replace(".", "..")
                    .replace("@", "@.")
                )
            grid.append(list(line))
        if not line:
            m = True
        if m:
            moves += line
    return grid, moves


def search_y(grid, x, y, dy, small_boxes, big_boxes):
    cur_possible = False
    next_possible = True
    direction = -1 if dy == -1 else 1
    start = y - 1 if dy == -1 else y + 1
    end = -1 if dy == -1 else len(grid)
    for i in range(start, end, direction):
        cell = grid[i][x]
        if cell == "#":
            return cur_possible and next_possible
        elif cell == "O":
            small_boxes.append((x, i))
        elif cell == ".":
            cur_possible = True
            return cur_possible and next_possible
        elif cell == "[":
            big_boxes.add(((x, i), (x + 1, i)))
            next_possible = search_y(grid, x + 1, i, dy, small_boxes, big_boxes)
            if not next_possible:
                return False
        elif cell == "]":
            big_boxes.add(((x - 1, i), (x, i)))
            next_possible = search_y(grid, x - 1, i, dy, small_boxes, big_boxes)
            if not next_possible:
                return False


def move_robot(grid, x, y, dx, dy):
    new_position = (x, y)
    move_possible = False
    small_boxes = []
    big_boxes = set()
    if dx != 0:
        direction = -1 if dx == -1 else 1
        start = x - 1 if dx == -1 else x + 1
        end = -1 if dx == -1 else len(grid[y])

        for i in range(start, end, direction):
            if grid[y][i] == "#":
                break
            elif grid[y][i] == "O":
                small_boxes.append((i, y))
            elif grid[y][i] == "[" and direction == 1:
                big_boxes.add(((i, y), (i + 1, y)))
            elif grid[y][i] == "]" and direction == -1:
                big_boxes.add(((i - 1, y), (i, y)))
            elif grid[y][i] == ".":
                move_possible = True
                break

    if dy != 0:
        move_possible = search_y(grid, x, y, dy, small_boxes, big_boxes)

    if move_possible:
        if dx:
            new_position = (x + dx, y)
            grid[y][x + dx] = "@"
            grid[y][x] = "."

            for box in small_boxes:
                grid[y][box[0] + dx] = "O"
            for box in big_boxes:
                grid[y][box[0][0] + dx] = "["
                grid[y][box[1][0] + dx] = "]"
        if dy:
            for box in small_boxes:
                grid[box[1] + dy][x] = "O"
            for box in big_boxes:
                grid[box[0][1]][box[0][0]] = "."
                grid[box[0][1]][box[1][0]] = "."
            for box in big_boxes:
                grid[box[0][1] + dy][box[0][0]] = "["
                grid[box[0][1] + dy][box[1][0]] = "]"

            new_position = (x, y + dy)
            grid[y + dy][x] = "@"
            grid[y][x] = "."

    return new_position


def solve(grid, moves):
    position = None
    for i, line in enumerate(grid):
        if "@" in line:
            position = (line.index("@"), i)

    for i, move in enumerate(moves):
        if move == "<":
            position = move_robot(grid, position[0], position[1], -1, 0)
        elif move == ">":
            position = move_robot(grid, position[0], position[1], 1, 0)
        elif move == "^":
            position = move_robot(grid, position[0], position[1], 0, -1)
        elif move == "v":
            position = move_robot(grid, position[0], position[1], 0, 1)

    res = 0
    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if pos in ["[", "O"]:
                res += 100 * y + x
    return res


data = [s.strip() for s in sys.stdin.readlines()]

print(f"Solution for part 1: {solve(*parse(data, False))}")
print(f"Solution for part 2: {solve(*parse(data, True))}")
