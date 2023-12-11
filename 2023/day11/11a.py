#!/usr/bin/python3
import sys

univ = list(map(lambda line: list(line.rstrip()), sys.stdin.readlines()))
rows = len(univ)
cols = len(univ[0])

empty_rows = [r for r in range(rows) if univ[r] == ['.']*cols]
empty_cols = [c for c in range(cols) if all([(univ[r][c] == '.') for r in range(rows)])]
for c in reversed(empty_cols):
    for r in range(rows):
        univ[r].insert(c, '.')
cols = len(univ[0])
for r in reversed(empty_rows):
    univ.insert(r, ['.']*cols)
rows = len(univ)

galaxies = []
for r in range(rows):
    for c in range(cols):
        if univ[r][c] == '#':
            galaxies.append((r,c))

total_distance = 0
for i,(r1,c1) in enumerate(galaxies):
    for (r2,c2) in galaxies[(i+1):]:
        total_distance += abs(r1-r2) + abs(c1-c2)

print(total_distance)
