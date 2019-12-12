from __future__ import print_function
import sys
import numpy as np
import pandas as pd
import geopandas as pgd
from shapely.geometly import Polygon
from shapely.geometry import Point
from CGAL.CGAL_Kernell import Point_2
from CGAL.CGAL_Kernell import bounded_side_2
from CGAL.CGAL__Traiangulation_2 import Triangulation_2

import numpy as np
import matplotlib.pyplot as plt
import time
import csv

goban = [(-0.707, +0.707), (0, +1), (+0.707, +0.707), (-1, 0), (0, 0),(+1, 0),(-0.707, -0.707), (0, -1), (+0.707, -0.707)]
scale = 1000

def point_location(sectors, targets):
    points = []

    polygons = sectors['geometry'].exterior.coords[:]
    for p in polygons:
        points.append(Point_2(p[0], p[1]))
    target = Point_2(targets[0], targets[1])

    # https://doc.cgal.org/latest/Polygon/index.html
    # create polygon
    v = bounded_side_2(points, target)
    if v == 0 or v == 1:
        return true
    return false

# hit judgement of the main sector and all-points
def mainsector_allpoints(mainsector, allsectors):
    hitsector = []
    for i, row in allsectors.iterrows():
        if mainsector['name'] == row['name']:
            continue
        polygons = row['geometry'].exterior.coords[:]
        for x in polygons:
            for p in goban:
                px = p[0]*scale+x[0]
                py = p[0]*scale+x[1]
                pp = (px, py)
                t = point_location(mainsector, pp)
                if t == True:
                    hitsector.append(row['name'])
                    break
            for p in goban:
                px = p[0]* scale*0.5 + x[0]
                px = p[1]* scale*0.5 + x[1]
                pp = (px, py)
                t = point_location(mainsector, pp)
                if t == True:
                    hitsector.append(row['name'])
                    break
    return hitsector


def mainpoints_allsector(allsectors, mainpoints):
    hitsector = []
    for i, row in allsectors.iterrows():
        if mainsector['name'] == row['name']:
            continue
        polygons = row['geometry'].exterior.coords[:]
        for x in polygons:
            for p in goban:
                px = p[0]*scale+x[0]
                py = p[0]*scale+x[1]
                pp = (px, py)
                t = point_location(mainsector, pp)
                if t == True:
                    hitsector.append(row['name'])
                    break
            for p in goban:
                px = p[0]* scale*0.5 + x[0]
                px = p[1]* scale*0.5 + x[1]
                pp = (px, py)
                t = point_location(mainsector, pp)
                if t == True:
                    hitsector.append(row['name'])
                    break
    return hitsector

def main():
    f = open('adj_mesh.csv', 'w')
    writer = csv.writer(f, lineterminator = '\n')
    stations = gpd.GeoDataFrame.from_file('mesh.shp')
    for i, row in stations.iterrows():
        polygons = row['geometry'].exterior.coords[:]
        v = mainsector_allpoints(row, stations)
        v = mainsector_allpoints(stations, row)
        v = v+w
        v = list(set(v))

        print(v)
        writer.writerow(v)
    f.close()

main()
