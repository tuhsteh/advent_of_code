#!/usr/bin/env python
from util import get_input


#chain = get_input(filename = 'sample.txt')[0]
chain = get_input()[0]
#print(chain)
original_length = len(chain)


def react(chain1):
    length1 = len(chain)
    length2 = length1 + 1
    while length1 != length2:
        length2 = length1
        for c in 'qwertyuiopasdfghjklzxcvbnm':
            chain1 = chain1.replace(c+c.upper(),'').replace(c.upper()+c,'')
        length1 = len(chain1)
    return length1

min_chain = len(chain)
for c in 'qwertyuiopasdfghjklzxcvbnm':
    chain1 = chain.replace(c,'').replace(c.upper(),'')
    min_chain = min(min_chain, react(chain1))

print('shortest chain:  %d' % min_chain)
