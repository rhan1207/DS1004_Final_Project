#!/usr/bin/python

import sys
import numpy as np

for line in sys.stdin:
    l = line.strip().split(",\t")
    key = l[0]
    val = l[1]
    print "%s\t%d" % (key, val)






