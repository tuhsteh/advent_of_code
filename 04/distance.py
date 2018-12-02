#!/usr/bin/env python

def get_input(filename = 'input.txt'):
    return [c for c in open(filename,'r').readlines()]


def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res


if __name__ == "__main__":
    box_ids = get_input()
    neighbors = set()
    for box_id in box_ids:
        for box_id2 in box_ids:
            if LD(box_id, box_id2) == 1:
                print('%s, %s' % (box_id, box_id2))
                neighbors.add(box_id)
                neighbors.add(box_id2)
    print(neighbors)
    print(len(neighbors))
    