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
    for x in box_ids:
        for y in box_ids:
            diff = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    diff += 1
            if diff == 1:
                ans = []
                for i in range(len(x)):
                    if x[i] == y[i]:
                        ans.append(x[i])
                print(''.join(ans))
#                print('1 difference:  ' + x.strip() + ' ' + y.strip())
    