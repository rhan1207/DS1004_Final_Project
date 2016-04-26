#!/usr/bin/python
import sys
fares = []
trips =[]
current_key = None
for line in sys.stdin:
	line  =line.strip()
	k,v = line.split('\t')
	if k.split(',')[0] != 'block' and k.split(',')[0] != 'LOT':
		if current_key ==None:
			current_key =k
			if len(v.split(','))== 2:
				fares.append(v)
			else:
				trips.append(v)
		else:
			if k == current_key:
				if len(v.split(','))== 2:
					fares.append(v)
				else:
					trips.append(v)
			else:
				for i in trips:
					for j in fares:
						print current_key+'\t'+ i+','+j 
				fares = []
				trips =[]
				current_key = k
				if len(v.split(','))== 2:
					fares.append(v)
				else:
					trips.append(v)
for i in trips:
    for j in fares:
        print current_key+'\t'+ i+','+j 
