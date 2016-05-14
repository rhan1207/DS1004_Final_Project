#!/usr/bin/python

import sys

for line in sys.stdin:
    x = line.strip().split('\t')
    
    if len(x)== 12 or len(x)==13:
    	  
    	k = ','.join([x[9],x[10],x[11]])
    	v = ','.join([x[7],x[0]])
    elif len(x) ==2:
        y = x[0].split(',')
        k = ','.join([y[0],y[1],y[2]])
        v = y[3]
    if v:
        print '%s\t%s' %(k, v)

