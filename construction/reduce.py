#!/usr/bin/python

import sys

current_key = None
counts = [0,0,0,0,0,0]

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    key, val = line.strip().split("\t", 1)
    yearCounts = val.strip().split(",")
    if key != current_key:
        if current_key != None:
            print "%s,%d,%d,%d,%d,%d,%d" % (current_key, counts[0], counts[1], counts[2], counts[3], counts[4], counts[5])
        counts = [0,0,0,0,0,0]
        current_key = key

    counts[0] = counts[0] + int(yearCounts[0])
    counts[1] = counts[1] + int(yearCounts[1])
    counts[2] = counts[2] + int(yearCounts[2])
    counts[3] = counts[3] + int(yearCounts[3])
    counts[4] = counts[4] + int(yearCounts[4])
    counts[5] = counts[5] + int(yearCounts[5])

print "%s,%d,%d,%d,%d,%d,%d" % (current_key, counts[0], counts[1], counts[2], counts[3], counts[4], counts[5])