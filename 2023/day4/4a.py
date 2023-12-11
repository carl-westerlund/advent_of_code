#!/usr/bin/python3
import fileinput

total_score = 0
for card in fileinput.input():
    [winning, numbers] = card.split(':')[1].split('|')
    winning = winning.split()
    numbers = numbers.split()
    num_winning = 0
    for n in numbers:
        if n in winning:
            num_winning += 1
    if num_winning > 0:
        total_score += 2**(num_winning-1)

print(total_score)
