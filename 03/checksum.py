#!/usr/bin/env python

from collections import Counter

def get_input(filename = 'input.txt'):
    return [c for c in open(filename,'r').readlines()]


def match_2(box_id):
    b = Counter(box_id)
    twos = [x for x in b.most_common() if x[1] == 2]
    return 0 < len(twos)

def match_3(box_id):
    b = Counter(box_id)
    threes = [x for x in b.most_common() if x[1] == 3]
    return 0 < len(threes)

if __name__ == "__main__":
    box_ids = get_input()
    twos = 0
    threes = 0
    for box_id in box_ids:
        if match_2(box_id):
            twos += 1
        if match_3(box_id):
            threes += 1
    print(twos * threes)