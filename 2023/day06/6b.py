#!/usr/bin/python3
import sys

# binary_search returns the last integer in the range [low, high-1]
# for which the condition f is false.
def binary_search(low, high, f):
    if low + 1 >= high:
        return low
    mid = (high + low) // 2
    if f(mid):
        return binary_search(low, mid, f)
    else:
        return binary_search(mid, high, f)

[times, distances] = sys.stdin.readlines()
time = int(times.split(':')[1].strip().replace(' ', ''))
distance = int(distances.split(':')[1].strip().replace(' ', ''))

n = 0
print(binary_search(time//2, time,   lambda x : x*(time-x) < distance) -
      binary_search(0,      time//2, lambda x : x*(time-x) > distance))
