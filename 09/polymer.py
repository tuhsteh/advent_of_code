#!/usr/bin/env python
from util import get_input


chain = get_input(filename = 'sample.txt')[0]
print(chain)

import ipdb
ipdb.set_trace()

while True:
    i = 0
    changes = 0
    for i in range(0, len(chain)-1):
        print(i)
        changes = 0
        try:
            char1,char2 = chain[i],chain[i+1]
            print('%s%s' % (char1,char2))
            if char1.lower() == char2.lower():
                print('chars are same letter:  %s %s' % (char1,char2))
                if char1 is not char2:
                    print('removing %s and %s' % (char1,char2))
                    chain = chain[:i] + chain[i+2:]
                    print('chain:  %s' % chain)
                    changes = 1
        except:
            pass
            i = 0
    i = 0
    if changes == 0:
        break

print(chain)

