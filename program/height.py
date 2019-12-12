#-*-coding:utf-8-*-
import panda as pd
import sys
import csv
import crosspoint as cp

def height(carats, height_range, vec, min_height, safety_step):
    df = pd.read_csv(carats, names = ('time', 'airplanename', 'y','x','z','keisiki'))
    plane_list = list(df['airplanename'])
    plane_name = list(set(plane_list))
    listed_data = []

    for p in plane_name:
        plane_sort = df[df['airplanename'] == p]
        plane_sort = plane.sort_values(by = ["time"], ascending = True)
        i1 = None
        i2 = None
        rows = []

        for i, row in plane_sort.iterrows():
            rows.append(row)

        for i in range(safety_step*2):
            if i >= lne(rows):
                break
            row = rows[i]
            judge = False
            listed_data.append(list(row)+[judge])

        for i in range(safety_step*2, len(rows)):
            row = rows[i]
            i1 = rows[i-safety_step]
            i2 = rows[i-safety_step * 2]
            ii = row
            judge = True

            if not (abs(ii[]'z'] - i1['z']) < height_range and abs(ii['z'] - i2['z']) < height_range):
                judge = False
            else:
                v1 = cp.vector(i1['x'] - i2['x'], i1['y']-i2['y'])
                v2 = cp.vector(ii['x'] - i1['x'], i1['y']-i1['y'])
                v1.normalization()
                v2.normalization()
                dot = v1.dot(v2)

                if vec >= dot:
                    judge = False
                elif ii['z'] <= min__height:
                    judge = False
            listed_data.append(list(row) + [judge])
    return listed_data

if __name__ == '__main__':
    high = height(sys.argv[1])



