#!/usr/bin/python

import sys
for line in sys.stdin:    
    x = line.strip().split('\t')
    
    if len(x)==58:
        k = x[3]
        v = ','.join([x[-15],x[0]])
   
    else:
        y = x[1].split(",")
        k = y[1]
        v = y[0]
    if v:
        
        print '%s\t%s' %(k, v)




