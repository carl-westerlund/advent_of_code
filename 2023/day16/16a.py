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

mp = list(map(lambda line: line.rstrip(), sys.stdin.readlines()))
rows = len(mp)
cols = len(mp[0])

dirs = "nwse"
visited = {d : [[False]*cols for _ in range(rows)] for d in dirs}   # lookup with visited[dir][r][c]

mp_feature = { '.' : {'n':'n',  's':'s',  'w':'w',  'e':'e'},
               '/' : {'n':'e',  'e':'n',  's':'w',  'w':'s'},
              '\\' : {'n':'w',  'w':'n',  's':'e',  'e':'s'},
               '|' : {'n':'n',  's':'s',  'w':'ns', 'e':'ns'},
               '-' : {'n':'we', 's':'we', 'w':'w',  'e':'e'} }

queue = [(0,0,'e')]
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

print(num_energized)
