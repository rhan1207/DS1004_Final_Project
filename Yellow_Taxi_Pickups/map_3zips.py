#!/usr/bin/python

import sys
import numpy as np


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Polygon:
    def __init__(self,points):
        self.points = points
        self.nvert = len(points)
        
        minx = maxx = points[0].x
        miny = maxy = points[0].y
        for i in range(1,self.nvert):
            minx = min(minx,points[i].x)
            miny = min(miny,points[i].y)
            maxx = max(maxx,points[i].x)
            maxy = max(maxy,points[i].y)
        self.bound = (minx,miny,maxx,maxy)
    
    def contains(self,pt):
        firstX = self.points[0].x
        firstY = self.points[0].y
        testx = pt.x
        testy = pt.y
        c = False
        j = 0
        i = 1
        nvert = self.nvert
        while (i < nvert):
            vi = self.points[i]
            vj = self.points[j]
            
            if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
                c = not(c)
            
            if(vi.x == firstX and vi.y == firstY):
                i = i + 1
                if (i < nvert):
                    vi = self.points[i]
                    firstX = vi.x
                    firstY = vi.y
            j = i
            i = i + 1
        return c
    
    def bounds(self):
        return self.bound



zip10031 = [Point(-73.949294,40.836721),
            Point(-73.949725,40.832675),
            Point(-73.941268,40.829123),
            Point(-73.940285,40.83047),
            Point(-73.938771,40.829855),
            Point(-73.939365,40.828342),
            Point(-73.942907,40.823298),
            Point(-73.948619,40.821506),
            Point(-73.950891,40.818417),
            Point(-73.95315,40.817651),
            Point(-73.95886,40.819991),
            Point(-73.958761,40.821615),
            Point(-73.955217,40.826422),
            Point(-73.949294,40.836721)]


zip10032 = [Point(-73.940285,40.83047),
            Point(-73.941268,40.829123),
            Point(-73.949725,40.832675),
            Point(-73.949294,40.836721),
            Point(-73.94604,40.844786),
            Point(-73.946923,40.847753),
            Point(-73.947003,40.850744),
            Point(-73.942946,40.849912),
            Point(-73.942282,40.848444),
            Point(-73.943166,40.845729),
            Point(-73.938834,40.844825),
            Point(-73.934637,40.843016),
            Point(-73.93492,40.839312),
            Point(-73.939162,40.833299),
            Point(-73.940285,40.83047)]


zip10452 = [Point(-73.911105,40.845179),
            Point(-73.913106,40.839879),
            Point(-73.913606,40.838779),
            Point(-73.918806,40.833279),
            Point(-73.920006,40.830979),
            Point(-73.923906,40.827379),
            Point(-73.928306,40.829179),
            Point(-73.931313,40.829482),
            Point(-73.933068,40.82892),
            Point(-73.933406,40.833179),
            Point(-73.933006,40.835679),
            Point(-73.929695,40.842195),
            Point(-73.928211,40.845405),
            Point(-73.928106,40.845579),
            Point(-73.911105,40.845179)]

def FindZipCode(zipDict, lon, lat):
    
    keys = zipDict.keys()
    keyOut = keys[0]
    
    crd = zipDict[keyOut].split(",")
    zipLon = float(crd[1])
    zipLat = float(crd[0])
    min = (lon - zipLon)**2 + (lat - zipLat)**2
    
    for key in keys:
        crd = zipDict[key].split(",")
        zipLon = float(crd[1])
        zipLat = float(crd[0])
        distSq = (lon - zipLon)**2 + (lat - zipLat)**2
        
        if distSq < min:
            min = distSq
            keyOut = key
    return keyOut



ply_10031 = Polygon(zip10031)
ply_10032 = Polygon(zip10032)
ply_10452 = Polygon(zip10452)

for line in sys.stdin:
    #count = count + 1
    l = line.strip().split(",")
    if l[0] != "vendor_name" and l[0] != "vendor_id" and l[0] != "":
        plon = float(l[5])
        plat = float(l[6])
        #dlon = float(l[9])
        #dlat = float(l[10])
        
        pt = Point(plon, plat)
        if ply_10031.contains(pt):
            print "%s\t%d" % ("10031",1)
        elif ply_10032.contains(pt):
            print "%s\t%d" % ("10032",1)
        elif ply_10452.contains(pt):
            print "%s\t%d" % ("10452",1)





