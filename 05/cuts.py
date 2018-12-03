#!/usr/bin/env python

from util import get_input
import re
from collections import defaultdict


data = get_input()
claims = []
for d in data:
#    claim_id, start_x, start_y, width, height
    claims.append(list(map(int, re.findall(r'\d+', d))))

    
material = defaultdict(list)
for (claim_id, start_x, start_y, width, height) in claims:
    for i in range(start_x, start_x + width):
        for j in range(start_y, start_y + height):
            material[(i,j)].append(claim_id)

print("square inches of overlap:  %d" % len([cut for cut in material if len(material[cut]) > 1]))
    
    
    