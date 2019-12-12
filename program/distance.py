#-*-coding: utf-8-*-

import point_location as pl
import crosspoint as cp

class error_cal:
    def __init__(self, sector, sectorinfo):
        self.sector = sector
        self.sectorinfo = sectorinfo
        def loop_line(self, base, step, nowsector_names, stablepoints):
            global_time_b = None
            base_new = len(stablepoints)
            sector_name = none
            sign = step / abs(step)
            x, y = 0,0

            for i in range(len(nowsector_names)):
                l2 = cp.line(stablepoints[base].x.stablepoints[base].y.stablepoints[base+step].x.stablepoints[base+step].y)
                time_a = (stablepoints[base + step].timevalue) - (stablepoints[base].timevalue)
                polygon = self.sectorinfo[nowsector_names[i]]['geometry'].exterior.coords[:]

                x,y, time_b = cp.crosspoint(polygon, l2, time_a)
                global_time_t = stablepoints[base].timevalue + time_b

                for j in range(len(stablepoints)):
                    read_point = stablepoints[j]
                    base_temp = j
                    if real_point.timevalue > global_time_t:
                        break
                predict_line = cp.line(stablepoints[base].x, stablepoints[base].y, x, y)
                distance_now = predict_line.length()

                distance_min = 1e+10
                if distance_min > distance_now:
                    px = x
                    py = y
                    distance_min = distance_now
                    base_new = base_temp
                    global_time_b = global_time_t
                    sector_name =nowsector_names[i]

            return base_new, px, py, global_time_b, sector_name

    def dist_time(self.x, y, global_time_b, stablepoints, nowsector, base_temp, altlimit):
        real_point = stablepoints[base_temp]
        target = (realpoint.x, real_point.y)
        alt1, sym, alt2 = altlimit[nowsector['name']]

            hoge = pl.pointlocation(nowsector['geometry'].exterior.coords[:], target)
            if hoge != -1:
                counter = 0
                for i in range(base_temp, len(stablepoints), +1):
                    target = (stablepoints[i].x, stablepoints[i].y)
                    flag = pl.point_location(nowsector['geometry'].exterior.coords[:], target)

                    target_alt = stablepoints[i].alt
                    if (sym == '+' and target_alt >= alt1 * 100) or\
                       (sym == '-' and target_alt <= alt1 * 100) or\
                       (sym == 'B' and target*100 <= target_alt and target_alt <= alt2 * 100):
                       alt flag = 1
                    else:
                        altflag = -1

                    if flag == -1 or alt_flat == 1:
                        dist = cp.line(x, y, target[0], target[1])
                        dist =dist.length()
                        time_c = global_time_b - stablepoints[i].timevalue
                        return i, dist, time_c, counter, stablepoints[i].timevalue
                    couter += 1
                return len(stablepoints), 0,1,0,0

            else:
                counter = 0
                bin_f = base
                bin_b = base_temp
                while bin_f <= bin_b:
                    bin_m = bin_f + (bin_b - bin_f) // 2

                    target = (stablepoints[bin_m].x, stablepoints[bin_m].y)
                    flag = pl.point_location(nowsector(['geometry'].exterior.coords[:], target))

                    target_alt = stablepoints[bin_m].alt

                    if (sym == '+' and target_alt >= alt1 * 100) or\
                       (sym == '-' and target_alt <= alt1 * 100) or\
                       (sym == 'B' and target*100 <= target_alt and target_alt <= alt2 * 100):
                       alt_flag = 1
                    else:
                        alt_flag = -1


                    if flag =-1 or alt_flag == -1:
                        target = (stablepoints[bin_ m -1].x, stablepoints[bin_m - 1].y)
                        flag = pl.point_location(nowsector(['geometry'].exterior.coords[:], target))

                        target_alt = stablepoints[bin_m-1].alt

                        if (sym == '+' and target_alt >= alt1 * 100) or\
                            (sym == '-' and target_alt <= alt1 * 100) or\
                            (sym == 'B' and target*100 <= target_alt and target_alt <= alt2 * 100):
                            alt_flag_pre = 1
                        else:
                            alt_flag_pre = -1

                        if flag == -1 or alt_flat == 1:
                            dist = cp.line(x, y, target[0], target[1])
                            dist =dist.length()
                            time_c = global_time_b - stablepoints[bin_m].timevalue
                            return i, dist, time_c, counter, stablepoints[bin_m].timevalue

                        bin_b = bin_m-1

                    else:
                        target = (stablepoints[bin_ m+1].x, stablepoints[bin_m+1].y)
                        flag_post = pl.point_location(nowsector(['geometry'].exterior.coords[:], target))

                        target_alt = stablepoints[bin_m+1].alt

                        if (sym == '+' and target_alt >= alt1 * 100) or\
                            (sym == '-' and target_alt <= alt1 * 100) or\
                            (sym == 'B' and alt1 *100 <= target_alt and target_alt <= alt2 * 100):
                            alt_flag_pre = 1
                        else:
                            alt_flag_pre = -1

                        if flag_post == -1 or alt_flag_post == -1:
                            dist = cp.line(x,y, target[0], target[1])
                            dist = dist.length()
                            time_c = gloval_time_b -stablepoints[bin_m+1].timevalue
                            return bin_m+1, dist, time_c, counter, stablepoints[bin_m+1].timevalue

                        bin_fg = bin_m+1
                    counter+1
                print "ERROR"
