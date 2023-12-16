#!/usr/bin/python3
import sys

def roll(mp):
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
    # roll west
    for r in range(rows):
        prev_empty = 0
        for c in range(cols):
            match mp[r][c]:
                case '#':
                    prev_empty = c+1
                case 'O':
                    mp[r][c] = '.'
                    mp[r][prev_empty] = 'O'
                    prev_empty += 1
    # roll south
    for c in range(cols):
        prev_empty = rows-1
        for r in range(rows-1,-1,-1):
            match mp[r][c]:
                case '#':
                    prev_empty = r-1
                case 'O':
                    mp[r][c] = '.'
                    mp[prev_empty][c] = 'O'
                    prev_empty -= 1
    # roll east
    for r in range(rows):
        prev_empty = cols-1
        for c in range(cols-1,-1,-1):
            match mp[r][c]:
                case '#':
                    prev_empty = c-1
                case 'O':
                    mp[r][c] = '.'
                    mp[r][prev_empty] = 'O'
                    prev_empty -= 1
    return mp

mp = list(map(lambda line: list(line.rstrip()), sys.stdin.readlines()))
rows = len(mp)
cols = len(mp[0])

prev_states = {}
goal = 1000000000
for i in range(goal):
    mp_key = ''.join([''.join(line) for line in mp])
    if mp_key in prev_states:
        cycle_length = i - prev_states[mp_key]
        i += cycle_length * ((goal - i) // cycle_length)
        while i < goal:
            mp = roll(mp)
            i += 1
        break
    else:
        prev_states[mp_key] = i
        mp = roll(mp)


# calculate total load
print(sum([mp[r].count('O')*(rows-r) for r in range(rows)]))
