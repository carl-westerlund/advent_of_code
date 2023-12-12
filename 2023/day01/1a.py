#!/usr/bin/python3
import fileinput
import re

result = 0
for line in fileinput.input():
    line = line.rstrip()
    digits = re.findall("[0-9]", line)
    result += int(digits[0] + digits[-1])
print(result)
