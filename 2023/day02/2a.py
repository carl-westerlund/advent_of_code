#!/usr/bin/python3
import fileinput
import re

result = 0
for line in fileinput.input():
    line = line.rstrip()
    gameID = re.search("Game (\d+):", line).group(1)
    if     (all(int(x) <= 12 for x in re.findall("(\d+) red",   line))
        and all(int(x) <= 13 for x in re.findall("(\d+) green", line))
        and all(int(x) <= 14 for x in re.findall("(\d+) blue",  line))):
        result += int(gameID)

print(result)
