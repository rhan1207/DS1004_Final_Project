#!/usr/bin/python

import sys

for line in sys.stdin:
    x = line.strip().split('\t')
    
    if len(x)== 12 or len(x)==13:
    	  
    	k = ','.join([x[10],x[11]])
    	v = ','.join([x[3],x[0]])
    else:
        y = x[0].split(',')
        k = ','.join([y[0],y[1]])
        v = y[2]
    if v:
        print '%s\t%s' %(k, v)

