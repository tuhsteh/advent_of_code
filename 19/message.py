#!/usr/bin/env python

from util import get_input
import re

#data = get_input(filename = 'sample.txt')
data = get_input()
points = []
for d in data:
    x,y,vx,vy = list(map(int, re.findall(r'-?\d+',d)))
    points.append([x,y,vx,vy])
    
for t in range(100000):
    min_x = min([x for x,y,_,_ in points])
    max_x = max([x for x,y,_,_ in points])
    min_y = min([y for x,y,_,_ in points])
    max_y = max([y for x,y,_,_ in points])
    W = 100
    if min_x+W >= max_x and min_y + W >= max_y:
        print(t,min_x, max_x, min_y, max_y)
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                if (x,y) in [(px,py) for px,py,_,_ in points]:
                    print('#', end=''),
                else:
                    print('.', end=''),
            print()

    for p in points:
        p[0] += p[2]
        p[1] += p[3]
