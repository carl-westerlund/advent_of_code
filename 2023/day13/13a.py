#!/usr/bin/python3
import sys

def calc(mp):
    result = 0
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
            result += (r+1)*100
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
            result += c+1
    return result

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
