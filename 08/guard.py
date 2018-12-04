#!/usr/bin/env python
from util import get_input
from collections import defaultdict
import dateparser
import re

data = get_input(filename='input.txt')
data.sort()
guards = defaultdict(list)
times = defaultdict(int)

guard_id = None
start = None
end = None

for line in data:
    time, action = line.split('] ')

    time = dateparser.parse(time[1:])
    
    if action.startswith('Guard'):
        guard_id = int(re.findall(r'\#(\d+)', action)[0])
    if action.startswith('falls'):
        start = time
    if action.startswith('wakes'):
        end = time
        guards[guard_id].append((start.minute, end.minute))
        times[guard_id] += (end - start).seconds

(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([
    (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
    for minute in range(60)], key=lambda i: i[1])

print(guard)
print(minute)
print(guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
    for minute in range(60) for guard in guards], key=lambda i: i[2])

print(guard * minute)
        
        
        