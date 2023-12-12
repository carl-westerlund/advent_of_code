#!/usr/bin/python3
import sys

data = list(map(lambda tup: (tup[0], int(tup[1])),
            map(lambda line: tuple(line.split()),
                sys.stdin.readlines())))

def all_same(items):
    return len(set(items)) == 1

card_ranks = "23456789TJQKA"
def hand_to_rank(hand):
    shand = sorted(hand)
    cards = list(map(lambda c: card_ranks.find(c), list(hand)))
    if all_same(shand):  # 5 of a kind
        return (7, cards)
    if all_same(shand[:-1]) or all_same(shand[1:]):  # 4 of a kind
        return (6, cards)
    if len(set(hand)) == 2:  # full house
        return (5, cards)
    if all_same(shand[:-2]) or all_same(shand[1:-1]) or all_same(shand[2:]):  # 3 of a kind
        return (4, cards)
    if len(set(hand)) == 3:  # Two pairs
        return (3, cards)
    if len(set(hand)) == 4:  # Pair
        return (2, cards)
    return (1, cards)


print(sum(map(lambda tup: (tup[0]+1)*tup[1][1], enumerate(sorted(data, key=(lambda tup: hand_to_rank(tup[0])))))))
