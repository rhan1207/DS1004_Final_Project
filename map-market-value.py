#!/usr/bin/python

import sys
for line in sys.stdin:    
    x = line.strip().split('\t')
    
    y = x[1].split(',')
    k = y[0]
    v = y[1]
    print '%s\t%s' %(k, v)



