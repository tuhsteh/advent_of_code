#!/usr/bin/env python3
#
##Day 1, advent of code
##  find the first repeated "Frequency" that is calculated,
##  given a list of changes to apply.
#
#DEBUG = True
#
#def __log__(msg):
#    if DEBUG:
#        print(msg)
#
#def get_changes(filename = 'input.txt'):
#    f = open(filename, 'r')
#    changes = []
#    try:
#        for line in f.readlines():
##            __log__(int(line))
#            changes.append(int(line))
#    except Exception as e:
#        __log__(e)
#    return changes
#
#
#
#if __name__ == "__main__":
#    __log__('Getting list of inputs...')
##    changes = get_changes('sample1.txt')
#    changes = get_changes()
#    __log__('Done.')
#    result = 0
#    __log__('Applying inputs...')
#    seen = set()
#    seen.add(0)
#    for d in changes:
#        result = result + d
#        __log__('%8d %12d' % (d,result))
#        if result in seen:
#            print('Found a repeated frequency:  %d' % result)
#            break            
#        seen.add(result)
#        __log__(seen)
##    result = 0
#    for d in changes:
#        result = result + d
#        __log__('%8d %12d' % (d,result))
#        if result in seen:
#            print('Found a repeated frequency:  %d' % result)
#            break            
#        seen.add(result)
#    for d in changes:
#        result = result + d
#        __log__('%8d %12d' % (d,result))
#        if result in seen:
#            print('Found a repeated frequency:  %d' % result)
#            break            
#        seen.add(result)
#    for d in changes:
#        result = result + d
#        __log__('%8d %12d' % (d,result))
#        if result in seen:
#            print('Found a repeated frequency:  %d' % result)
#            break            
#        seen.add(result)
#    for d in changes:
#        result = result + d
#        __log__('%8d %12d' % (d,result))
#        if result in seen:
#            print('Found a repeated frequency:  %d' % result)
#            break            
#        seen.add(result)
#    print('Done.  Found %d' % result)


import itertools
data = [int(x) for x in open("input.txt").readlines()]
print(sum(data))

freq = 0
seen = set([0])
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)


