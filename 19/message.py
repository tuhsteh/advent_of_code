#!/usr/bin/env python

from util import get_input
from collections import defaultdict
import re
import operator

#data = get_input(filename = 'sample.txt')
data = get_input()
points = []
for d in data:
    x,y,dx,dy = list(map(int, re.findall(r'-?\d+',d)))
    points.append((x,y,dx,dy))
    
max_x = max([p[0] for p in points])
max_y = max([p[1] for p in points])
min_x = min([p[0] for p in points])
min_y = min([p[1] for p in points])


print(points)

print('%d, %d' % (max_x, max_y))
print('%d, %d' % (min_x, min_y))

def init_sky():
    sky = []
    for x in range(0,max_x+3*abs(min_x)):
        row = []
        for y in range(0,max_y+3*abs(min_y)):
            row.append('.')
        sky.append(row)
    for row in sky:
        print(''.join(row))
    return sky

def print_sky(points, iteration):
    sky = init_sky()
    x,y,dx,dy = None,None,None,None
    try:
        for p in points:
            x,y,dx,dy = p
            x += abs(min_x)
            y += abs(min_y)
            px,py = list(map(operator.mul, [dx,dy], [iteration,iteration]))
            x += px
            y += py
            sky[y][x] = '#'
    except IndexError as e:
        print('%d, %d, %d, %d' % (x,y,dx,dy))
    for row in sky:
        print(''.join(row))


#import ipdb
#ipdb.set_trace()
        
for i in range(10):
    print('-'*40)
    print_sky(points,i)
