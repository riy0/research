#-*-coding:utf-8-*-
import sys
import csv

class Snap_Point:
    def __init__(self, timevalue, planename, sectorname):
        self.timevalue = float(timevalue)
        self.planename = planename
        self.sectorname = sectorname


class Snap_Plane:
    def __init__(self, filename):
        plane_csv = "result/"filename+".csv"
        with open(plane_csv, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            allplane = {}
            for row in reader:
                if not in allplane.has_key(row[0]):
                    allplane[row[0]] = []
                plane = Snap_Point(row[1], row[0], row[12:])
                allplane[row[0]].append(plane)
        self.allplane = allplane
        self.filename = filename

    def get_s(self, planename, snap_time):
        flight = self.allplane[planename]
        for i in range(1, len(flight)):
            if flight[i-1].timevalue <= float(snap_time) and float(snap_time) <= flight[i].timevalue:
                return flight[i-1].sectorname
        return None

    def get_p(self, snap_time):
        snap_dict = {}
        for p in self.allplane.keys():
            sector = self.get_s(p, snap_time)
            if sector is none:
                continue
            sectors = str(sector)
            if not snap_dict.has_key(sector_s):
                snap_sict[sector_s] = s
            snap_dict[sector_s].append(p)

        snapshot_csv = "result/snapshot_"+self.filename+"_"str(snap_time)+".csv"
        with open(snapshot.csv, "") as f:
            writer = csv.writerow([i]+row)

if __name__ == '__main__':
    filename = sys.argv[1]
    stime = sys.argv[2]
    hoge = Snap_Plane(filename)
    hoge.get_p(stime)

