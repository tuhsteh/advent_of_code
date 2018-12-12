#!/usr/bin/env python
import numpy

serial = 5153


def power(x, y):
    rack_id = x + 10
    begin = rack_id * y
    increase = begin + serial
    set_level = increase * rack_id
    keep = set_level // 100 % 10
    return (keep - 5)

grid = numpy.fromfunction(power, (300, 300))


width = 3
windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
maximum = int(windows.max())
location = numpy.where(windows == maximum)
print(width, maximum, location[0][0], location[1][0])
