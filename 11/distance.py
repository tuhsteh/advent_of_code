#!/usr/bin/env python3
from util import get_input
from collections import defaultdict

data = get_input()

Points = []
for d in data:
    x,y = [int(s.strip()) for s in d.split(',')]
    Points.append((x,y))
print(len(Points))

min_x = min([x for x,y in Points])
min_y = min([y for x,y in Points])
max_x = max([x for x,y in Points])
max_y = max([y for x,y in Points])

print("extent of width:  %d - %d" % (min_x, max_x))
print("extent of height: %d - %d" % (min_y, max_y))

def dist(point1, point2):
    x1,y1 = point1[0],point1[1]
    x2,y2 = point2[0],point2[1]
    return abs(x1-x2) + abs(y1-y2)

def closest(x,y):
    distances = [(dist(p, (x,y)), p) for p in Points]
    distances.sort()
    if distances[0][0] < distances[1][0]:
        return distances[0][1]
    else:
        return (-1,-1)

def score_around(W):
    score = defaultdict(int)
    for x in range(min_x-W, max_x+W):
        for y in range(min_y-W, max_y+W):
            score[closest(x,y)] += 1
    return score


S2 = score_around(400)
S3 = score_around(600)

best = [(S2[k] if S2[k]==S3[k] else 0, k) for k in S2.keys()]
best.sort()
for area, p in best:
    print(area, p)
