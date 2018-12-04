#!/usr/bin/env python
from util import get_input
from collections import defaultdict
import dateparser
import re

data = get_input(filename='input.txt')
data.sort()
guards = defaultdict(list)
times = defaultdict(int)


# def parse_log(log):
#     date = log.split(' ')[0].strip('[')
#     time = log.split(' ')[1].strip(']')
#     msg = ' '.join(log.split(' ')[2:])
#     time = 60 * (int(time.split(':')[0])) + (int(time.split(':')[1]))
#     return date, time, msg
#
#
# def get_sleep_minutes(i, data, guards):
#     start = None
#     end = None
#     while True:
#         i += 1
#         try:
#             date, time, msg = parse_log(data[i])
#         except Exception as e:
#             print("after %d loops, %s" % (i,e))
#             return i
#         if -1 < msg.find('Guard'):
#             return i
#         if -1 < msg.find('asleep'):
#             start = time
#         if -1 < msg.find('wakes'):
#             end = time
#         if start is not None and end is not None:
#             guards[guard_id].extend([t for t in range(start,end)])
#             start = None
#             end = None

guard_id = None
start = None
end = None

# import ipdb
# ipdb.set_trace()

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

# import ipdb
# ipdb.set_trace()

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

print('part 2:', guard * minute)
        
        
        