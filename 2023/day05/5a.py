#!/usr/bin/python3
import sys

seeds = list(map(int, sys.stdin.readline().split(':')[1].split()))
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        updated = [False]*len(seeds)
    elif line[-1] != ':':
        [dest_start, source_start, length] = list(map(int, line.split()))
        for i,seed in enumerate(seeds):
            if not updated[i] and (source_start <= seed and seed <= source_start+length):
                seeds[i] = dest_start + (seed - source_start)
                updated[i] = True

print(sorted(seeds)[0])
