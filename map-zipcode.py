#!/usr/bin/python

import sys
for line in sys.stdin:
    x = line.strip().split('\t')
    
    if len(x)== 12 or len(x)==13:
    	  
    	k = ','.join([x[10],x[11])
    	v = ','.join(x[0:9])
    else:
    	k = ','.join([x[0],x[1])
    	v = ','.join(x[2:7])
    if v:
        print '%s\t%s' %(k, v)