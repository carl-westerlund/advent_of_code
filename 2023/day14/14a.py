#!/usr/bin/python3
import sys

mp = list(map(lambda line: list(line.rstrip()), sys.stdin.readlines()))
rows = len(mp)
cols = len(mp[0])

# roll north
for c in range(cols):
    prev_empty = 0
    for r in range(rows):
        match mp[r][c]:
            case '#':
                prev_empty = r+1
            case 'O':
                mp[r][c] = '.'
                mp[prev_empty][c] = 'O'
                prev_empty += 1

# calculate total load
print(sum([mp[r].count('O')*(rows-r) for r in range(rows)]))
