#!/usr/bin/python3
import sys

pipes = list(map(lambda line : line.rstrip(), sys.stdin.readlines()))
rows = len(pipes)
cols = len(pipes[0])
pipes += ['.'*cols]     # this will enable us to determine what is inside and what is outside
rows += 1
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

def move(R,C,D):
    match D:
        case 'N':
            return (R-1,C)
        case 'S':
            return (R+1,C)
        case 'E':
            return (R,C+1)
        case 'W':
            return (R,C-1)

# Find (one) direction of the loop from the starting node
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
        start_direction = direction

# Now we go through the loop again and create a new map containing only this loop.
# While we do this, we try painting the right side.
# If this turns out to be the outside, we simply redo everything while painting
# the left side instead.
loop_map = [['.']*cols for _ in pipes]
inside_search = []

def paint_adjacent(R, C, D, hand):
    if hand == "left":
        match D:
            case 'N':
                C = C-1
            case 'S':
                C = C+1
            case 'E':
                R = R-1
            case 'W':
                R = R+1
    if hand == "right":
        match D:
            case 'N':
                C = C+1
            case 'S':
                C = C-1
            case 'E':
                R = R+1
            case 'W':
                R = R-1
    if 0 <= R < rows and 0 <= C < cols and loop_map[R][C] == '.':
        loop_map[R][C] = 'i'
        inside_search.append((R,C))

def move_paint(R, C, D):
    paint_adjacent(R,C,direction,hand)
    (R,C) = move(R,C,D)
    paint_adjacent(R,C,direction,hand)
    loop_map[R][C] = '#'
    return (R,C)

for hand in ["right", "left"]:
    # go around the loop while painting on the (hand)-hand side
    direction = start_direction
    (r,c) = move_paint(*start, direction)
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
        (r,c) = move_paint(r,c, direction)
        direction = opposite_direction[direction]
        d += 1
    loop_map[r][c] = '#'
    paint_adjacent(r,c, opposite_direction[direction], hand)

    # bfs to complete the inside
    while inside_search:
        (r,c) = inside_search.pop()
        if loop_map[r][c] != 'i':
            continue
        for (R,C) in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
            if 0 <= R < rows and 0 <= C < cols and loop_map[R][C] == '.':
                loop_map[R][C] = 'i'
                inside_search.append((R, C))
    if loop_map[-1][0] == '.':  # this means we chose hand correctly
        print(sum(map(lambda line: line.count('i'), loop_map)))
        break
    loop_map = [['.']*cols for _ in pipes]
