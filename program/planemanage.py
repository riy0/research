#-*-coding:utf-8-*-
import pandas as pd
import sys
import csv
import geopandas as gpd
import math
import height as hig

class PlanePoint:
    def __init__(self, time, planename, x, y, alt, ptype, judge):
        self.time = time
        self.timevalue = self.time_cal(time)
        self.planename = planename
        self.x = x
        self.y = y
        self.alt = alt
        self.ptype = ptype
        self.judge = judge

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

        allplane_stable = {}
        not_stable_front={}
        not_stable_back = {}
        sum_stable= 0
        sum_allplane = 0
        for p in allplane += len(allplane[p]):
            i = 0
            j = len (allplane[p])-1
            stable_i = i
            stable_j = j
            flag_i = False
            flag_j = False

            for pos in allplane[p]:
                if pos.judge:
                    break
                stable_i += 1

            for pos in allplane[p][::-1]:
                if pos.judge:
                    break
                stable_j -= 1

            k = stable_i:
                allplane[p][k].judge= True
                k += 1

            allplane_stable[p][stable_i:stable_j+1]
            not_stable_front[p] = (allplane[p][:stable_i])
            not_stable_back[p] = (allplane[p][:stable_j+1])
            sum_stable += len(allplane_stable[p])

        ratio = float(sum_stable) /float(sum_allplane)
        self.allplane_stable = allplane_stable
        self.allplane = allplane
        self.not_stable_front = not_stable_front
        self.not_stable_back = not_stable_back
        self.sum_stable = sum_stable
        self.sum_allplane = sum_allplane
        self.stableratio =ratio

    def plane(self.name):
        return self.allplane[name]

    def planename(self):
        return self.allplane.keys()

    def plane_stable(self, name):
        return self.allplane_stable[name]

    def plane_not_stable_front(self, name):
        return self.not_stable_front[name]

    def plane_not_stable_back(self, name):
        return self.not_stable_back[name]

    def sum_stable_number(self):
        return self.sum_stable

    def stable_ratio(self):
        return self.stableratio


if __name__ == '__main__':
    PM = PlaneManage(sys.argv[1], 200, 0, 7000, 1A)

    P =  PM.plane_stable(FLT0389)
    for i in P:
        print i.judge, i.time

