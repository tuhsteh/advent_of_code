#!/usr/bin/env python

from util import get_input
import re
from collections import defaultdict


data = get_input()
claims = []
for d in data:
#    claim_id, start_x, start_y, width, height
    numbers = list(map(int, re.findall(r'-?\d+', d)))
    claims.append(numbers)

material = defaultdict(list)
overlaps = {}
for (claim_id, start_x, start_y, width, height) in claims:
    overlaps[claim_id] = set()
    for i in range(start_x, start_x + width):
        for j in range(start_y, start_y + height):
            if material[(i,j)]:
                for number in material[(i,j)]:
                    overlaps[number].add(claim_id)
                    overlaps[claim_id].add(number)
            material[(i,j)].append(claim_id)

print("square inches of overlap:  %d" % len([cut for cut in material if len(material[cut]) > 1]))
print("areas that don't overlap:  %s" % [cut for cut in overlaps if len(overlaps[cut]) == 0][0])
    
    
    