#!/usr/bin/python

import sys
import numpy as np
#count = 0
# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    l = line.strip().split(",")
    if l[0] != "Source" and len(l)>13 and len(str(l[13])) ==5:
        zip = str(l[13])
        date = l[6]
        try:
			int(zip)
			print "%s\t%s" % (zip,(str(int(u'2009' in date)) + "," + str(int(u'2010' in date)) + "," + str(int(u'2011' in date)) + "," + str(int(u'2012' in date)) + "," + str(int(u'2013' in date)) + "," + str(int(u'2014' in date))))
        except:
            zip = 1
        #print "%s\t%s" % (zip,str(int(u'2009' in date)) + "," + str(int(u'2010' in date)) + "," + str(int(u'2011' in date)) + "," + str(int(u'2012' in date)) + "," + str(int(u'2013' in date)) + "," + str(int(u'2014' in date)))