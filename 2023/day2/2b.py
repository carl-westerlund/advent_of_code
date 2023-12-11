#!/usr/bin/python3
import fileinput
import re

result = 0
for line in fileinput.input():
    line = line.rstrip()
    gameID = re.search("Game (\d+):", line).group(1)
    result += (max(map(int, re.findall("(\d+) red",   line))) *
               max(map(int, re.findall("(\d+) green", line))) *
               max(map(int, re.findall("(\d+) blue",  line))))

print(result)
