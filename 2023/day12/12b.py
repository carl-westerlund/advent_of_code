#!/usr/bin/python3
import sys
from functools import cache

@cache
def num_arrs(arr, sizes, size_index):
    if size_index == len(sizes):
        if not '#' in arr:
            return 1
        else:
            return 0
    if arr == "" and size_index < len(sizes):
        return 0
    result = 0
    if arr[0] in ".?":
        result += num_arrs(arr[1:], sizes, size_index)
    size = sizes[size_index]
    if len(arr) >= size and all([x in "#?" for x in arr[:size]]) and (len(arr) == size or arr[size] != '#'):
        result += num_arrs(arr[size+1:], sizes, size_index+1)
    return result


result = 0
for line in sys.stdin:
    [arr, sizes] = line.split()
    arr = (arr+"?")*4 + arr
    sizes = list(map(int, sizes.split(',')))*5
    result += num_arrs(arr, tuple(sizes), 0)
print(result)
