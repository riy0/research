#-*-coding:utf-8-*-
import pandas as pd
import sys
import csv
import geopandas as gpd
import math
import height_mesh as hig

class PlanePoint:
    def __init__(self, time, planename, x, y, alt, ptype):
        self.time = time
        self.timevalue = self.time_cal(time)
        self.planename = planename
        self.x = x
        self.y = y
        self.alt = alt
        self.ptype = ptype

    def time_cal(self, planetime):
        hour = int(planetime[0:2])
        minu = int(planetime[3:5])
        sec = int(planetime[6:8])
        return hour*3600 + minu*60 +sec

class PlaneManage:
    def __init__(self, carats, height_range, vec, min_height, safety_step):
        dataReader = hig.height(carats, height_range, vec, min_height, safety_step)

        allplane = {}
        for row in dataReader:
            planename = row[1]
            if not allplane.has_key(planename):
                allplane[planename] = []
            plane = PlanePoint(row[0],row[1],row[3]*10000, row[2]*10000, row[4], row[5], row[6])
            allplane[planename].append(plane)

        self.allplane = allplane

    def plane(self.name):
        return self.allplane[name]

    def planename(self):
        return self.allplane.keys()

if __name__ == '__main__':
    PM = PlaneManage(sys.argv[1], 200, 0, 7000, 1)

    P =  PM.plane_stable('FLT0389')
    for i in P:
        print i.judge, i.time

