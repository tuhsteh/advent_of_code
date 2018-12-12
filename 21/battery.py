#!/usr/bin/env python


serial = 5153


def power(x, y, serial):
    rack_id = x + 10
    increase = rack_id * y
    set_level = increase * rack_id
    keep = set_level // 100 % 10
    return (keep - 5)

def add_cells(cells):
    sum = 0
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            sum+= cells[i][j]
    return sum

max_power = -1000000
max_x, max_y = 0,0
for x in range(1, 300-3):
    for y in range(1, 300-3):
        cells = [[0,0,0],[0,0,0],[0,0,0]]
        for a in range(3):
            for b in range(3):
                cells[a][b] = power(x+a,y+b,serial)
#
#        import ipdb
#        ipdb.set_trace()

        total = add_cells(cells)
        if total > max_power:
            max_x,max_y = x,y
            max_power = total

print('max_power %d, x %d, y %d' % (max_power,max_x,max_y))
