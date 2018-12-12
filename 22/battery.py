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

biggest_max = -1000
biggest_location = None
biggest_width = None
try:
    for width in range(3, 300):
        if width % 10 == 0:
            print('checking box size of %d' % width)
        windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
        maximum = int(windows.max())
        location = numpy.where(windows == maximum)
        if maximum > biggest_max:
            biggest_max = maximum
            biggest_location = location
            biggest_width = width
except KeyboardInterrupt:
     print(biggest_width, biggest_max, biggest_location[0][0], biggest_location[1][0])
