#!/usr/bin/env python3
from util import get_input
import re
from collections import defaultdict
data = get_input()

Points = []
for d in data:
    x,y = [int(s.strip()) for s in d.split(',')]
    Points.append((x,y))
print(len(Points))
min_x = min(x for x,y in Points)-int(10000/len(Points))-1
max_x = max(x for x,y in Points)+int(10000/len(Points))+1
min_y = min(y for x,y in Points)-int(10000/len(Points))-1
max_y = max(y for x,y in Points)+int(10000/len(Points))+1

print("extent of width:  %d - %d" % (min_x, max_x))
print("extent of height: %d - %d" % (min_y, max_y))


mapping = {}

in_region = set()
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        closest = Points[0]
        closest_dist = (1 << 31)
        dist_sum = 0
        for (px, py) in Points:
            dist = abs(px - x) + abs(py - y)
            dist_sum += dist
        if dist < closest_dist:
            closest = (px, py)
            closest_dist = dist
        elif dist == closest_dist and closest != (px, py):
            closest = None
        mapping[(x, y)] = closest
        if dist_sum < 10000:
            in_region.add((x, y))

rev_mapping = defaultdict(int)
for h in mapping:
    if not mapping[h]:
        continue
    if h[0] in (min_x, max_x) or h[1] in (min_y, max_y):
        rev_mapping[mapping[h]] -= (1 << 31)
    rev_mapping[mapping[h]] += 1
print("a", max(rev_mapping.values()))
print("b", len(in_region))
