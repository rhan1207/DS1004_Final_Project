#!/usr/bin/python

import sys
import numpy as np
#count = 0
# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    l = line.strip().split(",")
    if l[0] != "Source":
        zip = str(l[13])
        print "%s,\t%d" % (key,1)


