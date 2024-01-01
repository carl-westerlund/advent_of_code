#!/usr/bin/python3
import sys

# The shoelace formula assumes that the polygon is simple,
# which is true in the test case, but it isn't always true.

def move(r, c, d, dist):
    match d:
        case 'U':
            return (r - dist, c)
        case 'D':
            return (r + dist, c)
        case 'L':
            return (r, c - dist)
        case 'R':
            return (r, c + dist)

(r,c) = (0,0)
pts = [(0,0)]
for line in sys.stdin:
    [d, dist, _] = line.rstrip().split()
    dist = int(dist)
    (r, c) = move(r, c, d, dist)
    pts.append((r,c))

pts.append(pts[-1])
path_length = 0
area = 0
for i in range(len(pts)-1):
    path_length += abs(pts[i][0] - pts[i+1][0]) + abs(pts[i][1] - pts[i+1][1])
    area += pts[i][0]*pts[i+1][1] - pts[i+1][0]*pts[i][1]

area = abs(area)
area = (area + path_length) // 2 + 1
print(area)
