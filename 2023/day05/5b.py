#!/usr/bin/python3
import sys

seeds_data = list(map(int, sys.stdin.readline().split(':')[1].split()))
seeds = []
i = 0
while i < len(seeds_data):
    seeds.append((seeds_data[i], seeds_data[i+1]))
    i += 2

for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        updated = [False] * len(seeds)
    elif line[-1] != ':':
        [dest_start, source_start, map_length] = list(map(int, line.split()))
        i = 0
        while i < len(seeds):
            (seed_start, seed_length) = seeds[i]
            if not updated[i]:
                source_end = source_start + map_length      # not inclusive
                seed_end   = seed_start   + seed_length     # not inclusive
                if seed_start < source_start and source_start < seed_end:
                    new_length = source_start - seed_start
                    seeds.append((seed_start, new_length))
                    updated.append(False)
                    seeds[i] = (source_start, seed_length - new_length)
                    i -= 1
                elif seed_start < source_end and source_end < seed_end:
                    new_length = seed_end - source_end
                    seeds.append((source_end, new_length))
                    updated.append(False)
                    seeds[i] = (seed_start, seed_length - new_length)
                    i -= 1
                elif source_start <= seed_start and seed_end <= source_end:
                    seeds[i] = (dest_start + (seed_start-source_start), seed_length)
                    updated[i] = True
            i += 1

print(sorted(seeds)[0][0])
