#!/usr/bin/env python

#Day 1, advent of code
#  calculate current "Frequency", given a list of changes to apply.

DEBUG = True

def __log__(msg):
    if DEBUG:
        print(msg)

def get_changes(filename = 'input.txt'):
    f = open(filename, 'r')
    changes = []
    try:
        for line in f.readlines():
            __log__(int(line))
            changes.append(int(line))
    except Exception as e:
        __log__(e)
    return changes

def apply_change(current_value, change):
    return current_value + change



if __name__ == "__main__":
    __log__('Getting list of inputs...')
    changes = get_changes()
    __log__('Done.')
    result = 0
    __log__('Applying inputs...')
    for d in changes:
        result = apply_change(result,d)
        __log__('%8d %12d' % (d,result))
    print(result)
