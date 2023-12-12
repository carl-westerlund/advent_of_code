#!/usr/bin/python3
import sys

[times, distances] = sys.stdin.readlines()
times = list(map(int, times.split(':')[1].split()))
distances = list(map(int, distances.split(':')[1].split()))

result = 1
for time, distance in zip(times, distances):
    n = 0
    for t in range(1, time):
        if t * (time - t) > distance:
            n += 1
    result *= n
print(result)
