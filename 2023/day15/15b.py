#!/usr/bin/python3
import sys

def hash(string):
    v = 0
    for c in string:
        v += ord(c)
        v = v * 17
        v = v % 256
    return v

instructions = sys.stdin.readline().rstrip().split(',')

boxes = [[] for i in range(256)]
for instr in instructions:
    if '-' in instr:
        label = instr.rstrip('-')
        box = hash(label)
        for (l, f) in boxes[box]:
            if l == label:
                boxes[box].remove((l,f))
                break
    elif '=' in instr:
        (label, focal) = instr.split('=')
        focal = int(focal)
        box = hash(label)
        found = False
        for i, (l, f) in enumerate(boxes[box]):
            if l == label:
                boxes[box][i] = (l, focal)
                found = True
                break
        if not found:
            boxes[box].append((label, focal))

result = 0
for i, box in enumerate(boxes):
    for j, (l, f) in enumerate(box):
        result += (i+1) * (j+1) * f

print(result)
