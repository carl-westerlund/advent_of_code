#!/usr/bin/python3
import sys

pipes = list(map(lambda line : line.rstrip(), sys.stdin.readlines()))
rows = len(pipes)
cols = len(pipes[0])
for r in range(len(pipes)):
    if (c := pipes[r].find('S')) != -1:
        start = (r,c)
        break

pipe_directions = {'|' : "NS",
                   '-' : "EW",
                   'L' : "NE",
                   'J' : "NW",
                   '7' : "SW",
                   'F' : "SE",
                   'S' : "NSEW"}
opposite_direction = {'N' : 'S',
                      'S' : 'N',
                      'E' : 'W',
                      'W' : 'E'}

def move(R,C, direction):
    match direction:
        case 'N':
            return (R-1,C)
        case 'S':
            return (R+1,C)
        case 'E':
            return (R,C+1)
        case 'W':
            return (R,C-1)

for direction in "NSEW":
    (r,c) = move(*start, direction)
    direction = opposite_direction[direction]
    d = 1
    while (r,c) != start:
        if not (0 <= r < rows and 0 <= c < cols):
            break
        if pipes[r][c] == '.':
            break
        if not direction in pipe_directions[pipes[r][c]]:
            break
        direction = pipe_directions[pipes[r][c]].replace(direction,"")
        (r,c) = move(r,c, direction)
        direction = opposite_direction[direction]
        d += 1
    if (r,c) == start:
        print(d//2)
        break
