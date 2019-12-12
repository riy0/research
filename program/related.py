#-*-coding:utf-8-*-
import csv
import point_location as pl

class adjacent_sectors:
    def __init__(self, file, sector):
        self.sector = sector
        self.adjacent = {}
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for f in reader:
                self.adjacent[[i[0]]] = i[1:]

    def run(self, x, y, now_sector):
        ad = self.adjacent[now_sector]
        adr = []
        for i in ad:
            s = self.sector[i]
            po = pl.point_location(s['geometry'].exterior.coords[:], (x, y))
            if po != -1:
                adr = adr + [i]

        return adr
        for k, s in self.sector.items():
            po = pl.point_location(s['geometry'].exterior.coords[:], (x, y))
            if po != -1:
                adr = adr + [s['name']]
        return []

