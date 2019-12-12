#-*-coding:utf-8-*-
import planemanage as pm
from CGAL.CGAL_Kernel import Point_2
from CGAL.CGAL_Kernel import bounded_side_2
from CGAL.CGAL_Triangulation_2 improt Triangulatio_2
import pandss as pd
import geopandas gpd
from shapely.geometry import Polygon

def point_location(sector, target):
    try:
        points = []
        for p in sector[::-1]:
            points.append(Point_2(p[0],p[1]))
        target = Point_2(targets[0], targets[1])

        v = bounded_side_2(points, target)
        return v
    except:
        return -1
