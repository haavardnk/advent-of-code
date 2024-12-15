"""AoC 2024 Day 14: Restroom Redoubt"""

import sys


def teleport(position):
    x, y = position
    new_x = x
    new_y = y

    if x < 0:
        new_x = x + tile_width
    elif x >= tile_width:
        new_x = x - tile_width

    if y < 0:
        new_y = y + tile_height
    elif y >= tile_height:
        new_y = y - tile_height

    return (new_x, new_y)


def score(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for r in robots:
        if r["p"][0] < tile_width / 2 - 1 and r["p"][1] < tile_height / 2 - 1:
            q1 += 1
        elif r["p"][0] > tile_width / 2 and r["p"][1] < tile_height / 2 - 1:
            q2 += 1
        elif r["p"][0] < tile_width / 2 - 1 and r["p"][1] > tile_height / 2:
            q3 += 1
        elif r["p"][0] > tile_width / 2 and r["p"][1] > tile_height / 2:
            q4 += 1
    return q1 * q2 * q3 * q4


data = [s.strip() for s in sys.stdin.readlines()]
robots = []

tile_width = 101
tile_height = 103
p1, p2 = 0, 0

for line in data:
    p, v = line.split(" ")
    p = p.split("=")[1].split(",")
    p = (int(p[0]), int(p[1]))
    v = v.split("=")[1].split(",")
    v = (int(v[0]), int(v[1]))

    robots.append({"p": p, "v": v})

min_score = float("inf")
for i in range(0, tile_height * tile_width):
    if i == 100:
        p1 = score(robots)
    for r in robots:
        r["p"] = (r["p"][0] + r["v"][0], r["p"][1] + r["v"][1])
        r["p"] = teleport(r["p"])

    if len(set([r["p"] for r in robots])) == len(robots):
        s = score(robots)
        if s < min_score:
            min_score = s
            p2 = i


print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
