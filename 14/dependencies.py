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

reml = sorted(allsteps)
done_time = {}
busy_until = [0, 0, 0, 0, 0]
order = ''
time = 0
while reml:
    if all(t > time for t in busy_until):
        time = min(busy_until)
    for i, c in enumerate(reml):
        if all(d in done_time and done_time[d] <= time for d in deps[c]):
            order += c
            for ib, b in enumerate(busy_until):
                if b <= time:
                    busy_until[ib] = time + 60 + ord(c) - 64
                    done_time[c] = busy_until[ib]
                    break
            print(c, 'starts at', time, 'done at', done_time[c])
            del reml[i]
            break
    else:
        time = min(t for t in busy_until if t > time)

print(max(busy_until))
