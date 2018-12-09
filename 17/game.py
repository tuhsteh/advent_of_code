#!/usr/bin/env python
from util import get_input
from collections import deque, defaultdict
import re

def high_score(players, last):
    scores = defaultdict(int)
    circle = deque([0])
    player = 0
    
    for marble in range(1, last + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
        player = (player + 1) % players
    
    return max(scores.values()) if scores else 0

input = get_input()[0]
players, last = list(map(int, re.findall(r'\d+',input)))

print(high_score(players,last))
    