#-*-coding:utf-8-*-
import height as hei
import planemanage as Pmana
import steady_pointlocation as spl
import crosspoint as cp
import distance as dist
import sys
import pandas as pd
import geopandas as gpd
import average as ave
import csv
import time

def time_cal(planetime):
    hour = int(planetime[0:2])
    minu = int(planetime[3:5])
    sec = int(planetime[6:8])
    return hour * 3600 + minu*60 + sec

def column(fp, csvlist):
    for i in csvlist[:-1]:
        fp.write(str(i) + ",")
    fp.write(str(csvlist[-1]) + "\n")

def sub_main(acc, plane_path, step, height_range, file, vec, min_height, safety_step):
    ave.average("counter", init_flag = True)
    ave.average("time", init_flag = True)
    ave.average("distance", init_flag = True)

    pm = Pmana.PlaneManage(plane_path, height_range, vec, min_height, safety_step)

    sectors = gpd.GeoDataFrame.from_file('mesh.shp')
    sectorinfo = {}
    for i, row in sectors.iterrows


