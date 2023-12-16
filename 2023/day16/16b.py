#!/usr/bin/python3
import sys

def move(r, c, d):
    match d:
        case 'n':
            return (r-1, c)
        case 's':
            return (r+1, c)
        case 'w':
            return (r, c-1)
        case 'e':
            return (r, c+1)

dirs = "nwse"
mp_feature = { '.' : {'n':'n',  's':'s',  'w':'w',  'e':'e'},
               '/' : {'n':'e',  'e':'n',  's':'w',  'w':'s'},
              '\\' : {'n':'w',  'w':'n',  's':'e',  'e':'s'},
               '|' : {'n':'n',  's':'s',  'w':'ns', 'e':'ns'},
               '-' : {'n':'we', 's':'we', 'w':'w',  'e':'e'} }

def calc_num_energized(mp, r, c, d):
    rows = len(mp)
    cols = len(mp[0])
    visited = {d : [[False]*cols for _ in range(rows)] for d in dirs}   # lookup with visited[dir][r][c]
    queue = [(r, c, d)]
    while queue:
        (r, c, d) = queue.pop()
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[d][r][c]:
            continue
        visited[d][r][c] = True
        for nd in mp_feature[mp[r][c]][d]:
            queue.append((*move(r, c, nd), nd))

    num_energized = 0
    for r in range(rows):
        for c in range(cols):
            if visited['n'][r][c] or visited['w'][r][c] or visited['s'][r][c] or visited['e'][r][c]:
                num_energized += 1
    return num_energized


mp = list(map(lambda line: line.rstrip(), sys.stdin.readlines()))
rows = len(mp)
cols = len(mp[0])

max_num_energized = 0
for c in range(cols):
    max_num_energized = max(max_num_energized, calc_num_energized(mp, 0, c, 's'))
for c in range(cols):
    max_num_energized = max(max_num_energized, calc_num_energized(mp, rows-1, c, 'n'))
for r in range(rows):
    max_num_energized = max(max_num_energized, calc_num_energized(mp, r, 0, 'e'))
for r in range(rows):
    max_num_energized = max(max_num_energized, calc_num_energized(mp, r, cols-1, 'w'))

print(max_num_energized)
