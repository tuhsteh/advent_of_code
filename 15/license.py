#!/usr/bin/env python
from util import get_input

#data = get_input(filename = 'sample.txt')[0]
data = get_input()[0]

sequence = []

for d in data.split():
    sequence.append(int(d))

    
def parse(sequence):
    children, metas = sequence[:2]
    sequence = sequence[2:]
    totals = 0

    for i in range(children):
        total, sequence = parse(sequence)
        totals += total

    totals += sum(sequence[:metas])

    if children == 0:
        return (totals, sequence[metas:])
    else:
        return (
            totals,
            sequence[metas:]
        )

total, remaining = parse(sequence)

print('part 1:', total)
