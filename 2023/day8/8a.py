#!/usr/bin/python3
import sys

turns = sys.stdin.readline().rstrip()
N = len(turns)
sys.stdin.readline()
connections = {}
for line in sys.stdin:
    (origin, dest) = line.split('=')
    (left, right) = dest.split(',')
    connections[origin.strip()] = (left.strip(' ('), right.strip(' )\n'))

pos = "AAA"
i = 0
while True:
    if pos == "ZZZ":
        break
    match turns[i % N]:
        case 'L':
            pos = connections[pos][0]
        case 'R':
            pos = connections[pos][1]
    i += 1
print(i)
