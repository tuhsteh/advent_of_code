#!/usr/bin/env python
from util import get_input
from collections import defaultdict
import re

data = get_input(filename = 'sorted_input.txt')
guards = defaultdict(list)


def parse_log(log):
    date = log.split(' ')[0].strip('[')
    time = log.split(' ')[1].strip(']')
    msg = ' '.join(log.split(' ')[2:])
    time = 60 * (int(time.split(':')[0])) + (int(time.split(':')[1]))
    return date, time, msg


def get_sleep_minutes(i, data, guards):
    start = None
    end = None
    while True:
        i += 1
        date, time, msg = parse_log(data[i])
        if -1 < msg.find('Guard'):
            return
        if -1 < msg.find('asleep'):
            start = time
        if -1 < msg.find('wakes'):
            end = time
        if start is not None and end is not None:
            guards[guard_id].extend([t for t in range(start,end)])
            start = None
            end = None
    


for i in range(len(data)):
    date, time, msg = parse_log(data[i])
    
    import ipdb
    ipdb.set_trace()
    
    if -1 < msg.find('Guard'):
        guard_id = re.findall(r'\#(\d+)', msg)[0]
        guards[guard_id] = list()
        get_sleep_minutes(i, data, guards)

max = -1
sleepy_guard = None
for g in guards:
    total_minutes = len(g)
    if total_minutes > max:
        sleepy_guard = g
        max = total_minutes

print(sleepy_guard)
print(max)


    
        
        
        