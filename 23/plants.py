#!/usr/bin/env python

import collections
import re

def nextg(cur, recipe):
    start = min(cur)
    end = max(cur)
    x = set()

    for i in range(start - 3, end + 4):
        pat = ''.join('#' if i + k in cur else '.' for k in [-2, -1, 0, 1, 2])
        if pat in recipe:
            x.add(i)

    return x

def viz(cur):
    print(''.join('#' if i in cur else '.' for i in range(-5, 120)))

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    print(lines)

    init = lines[0][len('initial state: '):]
    recipe = set()
    for l in lines[2:]:
        if l[-1] == '#':  # I forgot this line the first time around.
            recipe.add(l[:5]) 

    cur = set(i for i, c in enumerate(init) if c == '#')

    for i in range(20):
        cur = nextg(cur, recipe)
        if i == 19: 
            print(sum(cur))
