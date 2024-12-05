"""AoC 2024 Day 05: Print Queue"""

import sys

data = [s.strip() for s in sys.stdin.readlines()]

p1 = 0
p2 = 0

rules = []
print_queues = []
incorrect = []

for line in data:
    if "|" in line:
        rules.append(list(map(int, line.split("|"))))
    elif "," in line:
        print_queues.append(list(map(int, line.split(","))))

for i, pages in enumerate(print_queues):
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[0]) > pages.index(rule[1]):
                incorrect.append(pages)
                break

for pages in [i for i in print_queues if i not in incorrect]:
    p1 += int(pages[int(len(pages) / 2)])

for i, pages in enumerate(incorrect):
    rerun = True
    while rerun:
        corrected = 0
        for rule in rules:
            if set(rule).issubset(pages):
                j0, j1 = pages.index(rule[0]), pages.index(rule[1])
                if j0 < j1:
                    incorrect[i][j0] = rule[1]
                    incorrect[i][j1] = rule[0]
                    corrected += 1

        if corrected == 0:
            rerun = False

for pages in incorrect:
    p2 += int(pages[int(len(pages) / 2)])


print(f"Solution for part 1: {p1}")
print(f"Solution for part 2: {p2}")
