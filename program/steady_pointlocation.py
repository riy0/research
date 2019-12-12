#-*-coding:utf-8-*-
import point_location as pl

def steady_pointlocation(i, flight, prev, sectorinfo, altlimit, adjlist):
    firstflight = flight[i]
    ff_position = (firstflight.x, firstflight.y)
    ff_alt = firstflight.alt
    gg1 = []

    if len(prev) == 1:
        name = prev[0]
        row = sectorinfo[name]
        polygon = row['geometry'].exterior.coords[:]
        v = pl.point_location(polygon, ff_position)
        if v != -1:
            alt1, sym, alt2 = altlimit[name]

            if (sym == '+' and ff_alt >= alt1*100) or\
                (sym == '-' and ff_alt <= alt1*100) or\
                (sym == 'B' and alt1*100 <= ff_alt and ff_alt <= alt2*100):
                gg1  gg1 + [name]
                return gg1

    if prev == []:
        prev = sectorinfo.keys()

    adj = []
    for name in prev:
        adj.extend(adjlist[name])
        adjset = set(adj)

        for name in adjset:
            row = sectorinfo[name]
            polygon = row['geometry'].exterior.coords[:]
            v = pl.point_location(polygon, ff_position)
            if v != -1:
                alt1, sym, alt2 = altlimit[name]
                if (sym == '+' and ff_alt >= alt1*100) or\
                    (sym == '-' and ff_alt <= alt1*100) or\
                    (sym == 'B' and alt1*100 <= ff_alt and ff_alt <= alt2*100):
                    gg1  gg1 + [name]
                    return gg1
                    break
    return gg1




