#!/usr/bin/python3
import sys
import regex

schematic = sys.stdin.readlines()
schematic = list(map(lambda line: line.rstrip(), schematic))

gearlabels = {}
for i,line in enumerate(schematic):
    for m in regex.finditer(r'(?:^|\D)(\d+)(?:\D|$)', line, overlapped=True):
        for k in [i-1, i, i+1]:
            if 0 <= k and k < len(schematic):
                for gear in regex.finditer(r'\*', schematic[k][m.start():m.end()]):
                    l = m.start() + gear.start()
                    if not (k, l) in gearlabels:
                        gearlabels[k,l] = []
                    gearlabels[k,l].append(int(m.group(1)))
                    break

result = 0
for _,labels in gearlabels.items():
    if len(labels) == 2:
        result += labels[0] * labels[1]
print(result)
