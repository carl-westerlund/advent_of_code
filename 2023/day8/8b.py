#!/usr/bin/python3
import sys
import heapq
from functools import lru_cache, reduce
from math import lcm

turns = sys.stdin.readline().rstrip()
N = len(turns)
sys.stdin.readline()
connections = {}
pos = []
for line in sys.stdin:
    (origin, dest) = line.split('=')
    (left, right) = dest.split(',')
    origin = origin.strip()
    connections[origin] = (left.strip(' ('), right.strip(' )\n'))
    if origin[-1] == 'A':
        heapq.heappush(pos, (0, origin))


@lru_cache(maxsize=None)
def next_Z(pos, i):
    d = 0
    while True:
        if d > 0 and pos[-1] == 'Z':
            break
        match turns[(i+d) % N]:
            case 'L':
                pos = connections[pos][0]
            case 'R':
                pos = connections[pos][1]
        d += 1
    return (pos, d)


# maxd = 1
# while pos[0][0] != maxd:
#     (d, p) = heapq.heappop(pos)
#     (p, extra_d) = next_Z(p, d % N)
#     d = d + extra_d
#     maxd = max(maxd, d)
#     heapq.heappush(pos, (d, p))
# print(maxd)

# I hate the fact that to solve this problem in a reasonable
# amount of time it was necessary to exploit the extremly
# artificial input data.
# The general (but slow) solution can be found by replacing
# the code below with the one in comments above.

print(reduce(lcm, map(lambda tup: next_Z(tup[1],0)[1], pos)))
