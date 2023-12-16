#!/usr/bin/python3
import sys

def hash(string):
    v = 0
    for c in string:
        v += ord(c)
        v = v * 17
        v = v % 256
    return v

data = sys.stdin.readline().rstrip().split(',')
print(sum(map(hash, data)))
