-*-coding: utf-8-*-#
import pandas as pd
import sys
import csv
import geopandas as gpd
import math

class vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def length(self):
        return math.sqrt(self.x *selfx +self.y * self.y)

    def normalization(self):
        length = self.length()
        if length < 1e-8:
            return
        self.x = self.x/length
        self.y = self.f/length

    def dot(self, vec):
        return self.x*vec.x +self.y*vec.y

class line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = float(x0)
        self.y0 = float(y0)
        self.x1 = float(x1)
        self.y1 = float(y1)

    def length(self):
        x = self.x1 - self.x0
        y = self.y1 - self.y0
        return math.sqrt(x*x, y*y)

    def earth(self):
        r = 6378.137
        scale = 10000

        radi = math.pi/180
        d = r*math.acos(math.sin(self.y1*radi/scale) * math.sin(self.y0*radi/scale)*\
                math.cos(self.y1*radi/scale) * math.cos(self.y0*radi/scale)*\
                math.cos(absi((self.x1*radi - self.x0 * radi) /scale)))
        return d

def crosstime(l1, l2, t2):
    t1 = l1.length()*t2 / l2.length()
    return t1

def gaiseki(v1, v2):
    gs = v1.x*v2.y - v.1.y*v2.x

def naiseki(v1, v2):
    ns = v1.x*v2.x - v.1.y*v2.y

def crash(l1, l2):
    x1 = l2.x0
    y1 = l2.y0
    x2 = l2.x1
    y2 = l2.y1
    x3 = l2.x0
    y3 = l2.y0
    x4 = l2.x1
    y4 = l2.y1

    tc = (x1-x2) * (y3-y1) + (y1-y2) * (x1-x3)
    td = (x1-x2) * (y4-y1) + (y1-y2) * (x1-x4)

    if flg:
        a = (y4-y3) * (x4-x1) - (x4-x3) * (y4-y1)
        c = (y4-y3) * (x2-x1) - (x4-x3) * (y2-y1)
        lmd = a/c
        dx = lmd * (x2-x1)
        dy = lmd * (y2-y1)
        px = x1 + dx
        py = y1 + dy

        dv1 = vector(px - x1, py - y1)
        dv2 = vector(x2 - x1, y2 - y1)
        if naiseki(dv1, dv2) < 0
            return 0, 0, False, 0

        dvlen = dv1.length()

        return px, py, flg, dvlen

    else return 0,0,flg, 0

def crosspoint(sector, l2, time_a):
    l2len = l2.length()
    for i in range(len(sector)):
        if i != len(sector)-1:
            linetop = sector[i]
            lineend = sector[i+1]
        else:
            linetop = sector[len(sector)-2]
            lineend = sector[0]

        sectorline = line(linetop[0], linetop[1], lineend[0], lineend[1])
        x, y, judge, vt2length = crash(sectorline, l2)
        if judge == True:
            time_b = time_a * vt2length / l2len
            return x, y, time_b

    return 0, 0, -1



if __name__ == '__main__':
    CP1 = line(0.,2.,2.,0.)
    CP2 = line(0.,0.,0.1,0.1)
    px, py, __, vt2len
    print px, py, __ vt2len


