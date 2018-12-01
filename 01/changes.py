#!/usr/bin/env python

#Day 1, advent of code
#  calculate current "Frequency", given a list of changes to apply.

def get_changes(filename = 'input.txt'):
    return [int(c) for c in open(filename,'r').readlines()]


if __name__ == "__main__":
    changes = get_changes()
    print(sum(changes))
