#!/usr/bin/python3
import sys

univ = list(map(lambda line: list(line.rstrip()), sys.stdin.readlines()))
rows = len(univ)
cols = len(univ[0])
row_dist = [1]*rows
col_dist = [1]*cols

for r in range(rows):
    if univ[r] == ['.']*cols:
        row_dist[r] = 1000000
for c in range(cols):
    if all([univ[r][c] == '.' for r in range(rows)]):
        col_dist[c] = 1000000

galaxies = []
for r in range(rows):
    for c in range(cols):
        if univ[r][c] == '#':
            galaxies.append((r,c))

total_distance = 0
for i,(r1,c1) in enumerate(galaxies):
    for (r2,c2) in galaxies[(i+1):]:
        total_distance += (sum(row_dist[min(r1,r2):max(r1,r2)]) +
                          sum(col_dist[min(c1,c2):max(c1,c2)]))

print(total_distance)
