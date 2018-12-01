#!/usr/bin/env python3

#Day 1, advent of code
#  find the first repeated "Frequency" that is calculated,
#  given a list of changes to apply.

DEBUG = False

def __log__(msg):
    if DEBUG:
        print(msg)

def get_changes(filename = 'input.txt'):
    return [int(c) for c in open(filename,'r').readlines()]

def look_for_dupe(changes):
    result = 0
    loop_count = 0
    seen = set([0])
    while True:
        loop_count += 1
        for d in changes:
            result = result + d
            __log__('%8d %12d' % (d,result))
            if result in seen:
                print('Found a repeated frequency after %d loops:  %d' % (loop_count, result))
                return           
            seen.add(result)
            __log__(seen)





if __name__ == "__main__":
    __log__('Getting list of inputs...')
#    changes = get_changes('sample1.txt')
    changes = get_changes()
    __log__('Done.')
    __log__('Applying inputs...')
    look_for_dupe(changes)

            
import itertools
data = [int(x) for x in open('input.txt','r').readlines()]
print(sum(data))

freq = 0
seen = set([0])
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)

print('again, pythonic.')
from itertools import accumulate, cycle
seen = set([0])
print(next(f for f in accumulate(cycle(data)) if f in seen or seen.add(f)))
