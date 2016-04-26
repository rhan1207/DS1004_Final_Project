#!/usr/bin/python

import sys
for line in sys.stdin:    
    line = line.strip().split(' ')
    if line[1] != 'BLOCK' and len(line)==4:
        print '%s,%s,%s\t%d' %(line[1],line[2],line[3],1)
    

