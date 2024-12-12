"""AoC 2024 Day 12: Garden Groups"""

import sys


def find_region(x, y, plant) -> list:
    region = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(nx, ny) -> bool:
        return (
            0 <= nx < len(data)
            and 0 <= ny < len(data)
            and data[ny][nx] == plant
            and (nx, ny) not in visited
        )

    def search(cx, cy):
        visited.add((cx, cy))
        region.add((cx, cy))
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny):
                search(nx, ny)

    search(x, y)

    return region


def find_fence_length(region) -> int:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return sum(
        (x + dx, y + dy) not in region for x, y in region for dx, dy in directions
    )


def find_bulk_fence_length(region) -> int:
    sides = 0
    for x, y in region:
        if (x + 1, y) not in region and (
            (x, y - 1) not in region or (x + 1, y - 1) in region
        ):
            sides += 1
        if (x - 1, y) not in region and (
            (x, y - 1) not in region or (x - 1, y - 1) in region
        ):
            sides += 1
        if (x, y + 1) not in region and (
            (x - 1, y) not in region or (x - 1, y + 1) in region
        ):
            sides += 1
        if (x, y - 1) not in region and (
            (x - 1, y) not in region or (x - 1, y - 1) in region
        ):
            sides += 1
    return sides


data = [s.strip() for s in sys.stdin.readlines()]
regions = []
visited = set()

for y, line in enumerate(data):
    for x, plant in enumerate(line):
        if (x, y) in visited:
            continue
        regions.append(find_region(x, y, plant))

p1 = sum(find_fence_length(region) * len(region) for region in regions)
p2 = sum(find_bulk_fence_length(region) * len(region) for region in regions)

print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
