#!/usr/bin/python3
import sys
import regex

schematic = sys.stdin.readlines()
schematic = list(map(lambda line: line.rstrip(), schematic))

result = 0
for i,line in enumerate(schematic):
    for m in regex.finditer(r'(?:^|\D)(\d+)(?:\D|$)', line, overlapped=True):
        for k in [i-1, i, i+1]:
            if 0 <= k and k < len(schematic):
                if regex.search(r'[^\.\d]', schematic[k][m.start():m.end()]) != None:
                    result += int(m.group(1))
                    break

print(result)
