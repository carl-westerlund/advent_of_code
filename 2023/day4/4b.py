#!/usr/bin/python3
import sys

cards = sys.stdin.readlines()
num_cards = [1]*len(cards)

for i,card in enumerate(cards):
    [winning, numbers] = card.split(':')[1].split('|')
    winning = winning.split()
    numbers = numbers.split()
    num_winning = 0
    for n in numbers:
        if n in winning:
            num_winning += 1
            num_cards[i+num_winning] += num_cards[i]

print(sum(num_cards))
