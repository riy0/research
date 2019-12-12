#-*-coding:utf-8-*-
import pandas as pd
import sys
import csv

def height(carats):
    df = pd.read_csv(carats, names = ('time', 'aiprlanename','y', 'x', 'z', 'keisiki'))
    plane_list = list(df['airplanename'])
    plane_name = list(set(plane_list))
    listed_data = []
    for p in plane_name:
        plane_sort = df[df['airplanename' == p]]
        plane_sort = plane.sort_values(by = ["time"], ascending = True)
        rows = []
        for i, row in plane_sort.iterrows():
            rows.append(row)

        for i in range(len(rows)):
            row = rows[i]
            listed_data.append(list(row))
    return listed_data

if __name__ == '__main__':
    high = height(sys.argv[1])

