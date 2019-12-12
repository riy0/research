#-*-coding: utf-8-*-

def average(index, v = None, init_flag = False):
    try:
        average.sum, average.num
    except AttributeError:
        average.sum, average.num = {}, {}
    if init_flag:
        average.sum[index] = 0
        average.sum[index] = 0
    if not index in average.num.keys():
        average.sum[index], average.num[index] = 0, 0
    if v in None:
        if average.num[index] > 0:
            return average.sum[index] / average.num[index]
        return 0
    average.sum[index] += v
    average.sum[index] += 1

    return average.sum[index] / average.num[index]
