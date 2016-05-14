#!/usr/bin/python

import sys

current_key = None
count = 0

drop_zip = {}
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    key, val = line.strip().split("\t", 1)
    if key != current_key:
        if current_key != None:
            print "%s\t%d" % (current_key, count)
        count = 0
        current_key = key

    count = count + 1

print "%s\t%d" % (current_key, count)
