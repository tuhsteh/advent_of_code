#!/usr/bin/env python
from util import get_input


#chain = get_input(filename = 'sample.txt')[0]
chain = get_input()[0]
#print(chain)
original_length = len(chain)

chain1 = chain
length1 = len(chain)
length2 = length1 + 1
while length1 != length2:
    length2 = length1
    for c in 'qwertyuiopasdfghjklzxcvbnm':
        chain1 = chain1.replace(c+c.upper(),'').replace(c.upper()+c,'')
    length1 = len(chain1)

#print("resulting polymer:  %s" % chain1)
print("old length:  %d" % original_length)
print("reacted length:  %d" % length1)
