#!/usr/bin/python3
import sys

def invert(x):
    return {'.':'#', '#':'.'}[x]

# Note: if the maps can have more than 100 columns, the output
# of find_reflections needs to be implemented more carefully.
def calc(mp):
    rows = len(mp)
    cols = len(mp[0])
    orig_reflection = find_reflections(mp)[0]
    for R in range(rows):
        orig_line = mp[R]
        for C in range(cols):
            mp[R] = ''.join([orig_line[c] if c!=C else invert(orig_line[c]) for c in range(cols)])
            reflections = find_reflections(mp)
            if orig_reflection in reflections:
                reflections.remove(orig_reflection)
            if len(reflections) == 1:
                return reflections[0]
        mp[R] = orig_line

def find_reflections(mp):
    reflections = []
    rows = len(mp)
    cols = len(mp[0])
    for r in range(rows-1):
        valid = True
        for dr in range(rows-1):
            if r-dr < 0 or r+dr+1 >= rows:
                if dr == 0:
                    valid = False
                break
            if mp[r-dr] != mp[r+dr+1]:
                valid = False
                break
        if valid:
            reflections.append((r+1)*100)
    for c in range(cols-1):
        valid = True
        for dc in range(cols-1):
            if c-dc < 0 or c+dc+1 >= cols:
                if dc == 0:
                    valid = False
                break
            if [mp[r][c-dc] for r in range(rows)] != [mp[r][c+dc+1] for r in range(rows)]:
                valid = False
                break
        if valid:
            reflections.append(c+1)
    return reflections

result = 0
mp = []
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        result += calc(mp)
        mp = []
    else:
        mp.append(line)
result += calc(mp)
print(result)
