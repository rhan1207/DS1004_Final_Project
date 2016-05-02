#!/usr/bin/python

import sys

for line in sys.stdin:
    x = line.strip().split('\t')
    
    
    y = x[1].split(',')
    print '%s\t%s' %(y[0],y[1])
