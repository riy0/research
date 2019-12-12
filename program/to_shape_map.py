#-*-coding:utf-8-*-

import numpy as np
import pandas as pd
import geopandas as pgd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import fiona

p1 = gpd.GeoSeries(
    Polygon([(30, 128), (30, 129), (31,129), (31, 128)]),
    Polygon([(30, 128), (30, 129), (31,129), (31, 128)]),
    Polygon([(30, 128), (30, 129), (31,129), (31, 128)]),
    Polygon([(30, 128), (30, 129), (31,129), (31, 128)]),
    Polygon([(30, 128), (30, 129), (31,129), (31, 128)])
])
