#!/usr/bin/python3
import fileinput
import regex

result = 0
for line in fileinput.input():
    line = line.rstrip()
    digits = regex.findall("([0-9]|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True)
    nameToDigit = {"one"   : '1',
                   "two"   : '2',
                   "three" : '3',
                   "four"  : '4',
                   "five"  : '5',
                   "six"   : '6',
                   "seven" : '7',
                   "eight" : '8',
                   "nine"  : '9' }
    digits = list(map(nameToDigit.get, digits, digits))
    result += int(digits[0] + digits[-1])
print(result)
