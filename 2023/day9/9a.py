#!/usr/bin/python3
import sys

result = 0
for line in sys.stdin:
    seqs = [list(map(int, line.split()))]
    while not all([x == 0 for x in seqs[-1]]):
        seq = seqs[-1]
        seqs.append([y-x for (x,y) in zip(seq, seq[1:])])
    n = 0
    for i in range(len(seqs)-1, -1, -1):
        n += seqs[i][-1]
    result += n
print(result)
