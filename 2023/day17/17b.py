#!/usr/bin/python3
import sys
import heapq

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

mp = list(map(lambda line: list(map(int, list(line.rstrip()))), sys.stdin.readlines()))
rows = len(mp)
cols = len(mp[0])

dirs = "nwse"
visited = {d : [[False]*cols for _ in range(rows)] for d in dirs}
queue = [(0,0,0,'e'), (0,0,0,'s')]  # heat loss so far, row, column, direction
while queue:
    (loss, r, c, d) = heapq.heappop(queue)
    if (r,c) == (rows-1, cols-1):
        final_loss = loss
        break
    if visited[d][r][c]:
        continue
    visited[d][r][c] = True
    for i in range(10):
        (r,c) = move(r,c,d)
        if r < 0 or r >= rows or c < 0 or c >= cols:
            break
        loss += mp[r][c]
        if i >= 3:
            for new_d in ("ns" if d in "we" else "we"):
                heapq.heappush(queue, (loss, r, c, new_d))

print(final_loss)
