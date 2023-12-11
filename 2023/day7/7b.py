#!/usr/bin/python3
import sys

data = list(map(lambda tup: (tup[0], int(tup[1])),
            map(lambda line: tuple(line.split()),
                sys.stdin.readlines())))

def all_same(items):
    return len(set(items)) == 1

card_ranks = "J23456789TQKA"
def hand_to_rank_no_joker(hand):
    shand = sorted(hand)
    if all_same(shand):  # 5 of a kind
        return 7
    if all_same(shand[:-1]) or all_same(shand[1:]):  # 4 of a kind
        return 6
    if len(set(hand)) == 2:  # full house
        return 5
    if all_same(shand[:-2]) or all_same(shand[1:-1]) or all_same(shand[2:]):  # 3 of a kind
        return 4
    if len(set(hand)) == 3:  # Two pairs
        return 3
    if len(set(hand)) == 4:  # Pair
        return 2
    return 1

def hand_to_rank(hand):
    best_rank = 0
    cards = list(map(lambda c: card_ranks.find(c), list(hand)))
    for c in card_ranks[1:]:
        new_hand = hand.replace('J', c)
        best_rank = max(best_rank, hand_to_rank_no_joker(new_hand))
    return (best_rank, cards)


print(sum(map(lambda tup: (tup[0]+1)*tup[1][1], enumerate(sorted(data, key=(lambda tup: hand_to_rank(tup[0])))))))
