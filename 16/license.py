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
    scores = []
    totals = 0

    for i in range(children):
        total, score, sequence = parse(sequence)
        totals += total
        scores.append(score)

    totals += sum(sequence[:metas])

    if children == 0:
        return (totals, sum(sequence[:metas]), sequence[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in sequence[:metas] if k > 0 and k <= len(scores)),
            sequence[metas:]
        )

total, value, remaining = parse(sequence)

print('part 1:', total)
print('part 2:', value)