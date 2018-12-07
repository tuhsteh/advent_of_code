#!/usr/bin/env python
from util import get_input
from collections import defaultdict, deque
import re

data = get_input()

allsteps = set()
deps = defaultdict(set)
for d in data:
    s1,s2 = re.findall(r'[sS]tep (\w)',d)
    deps[s2].add(s1)
    allsteps.add(s1)
    allsteps.add(s2)

print(deps)
print(allsteps)


reml = sorted(allsteps)
done = set()
order = ''
while reml:
    for i, c in enumerate(reml):
        if not (deps[c] - done):
            order += c
            done.add(c)
            del reml[i]
            break
print(order)
