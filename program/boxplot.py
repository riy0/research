#coding: utf-8

import matplotlib.pyplot as plt
import csv
import math
import sys

step = [1,2,3]
height_range = [200,400, 600]
vec = [0,0.9962, 0.9994]
min_height = [5000, 7500, 10000]
safety_step = [1,2,3]

flightlist = sys.argv[1:]
for flight in flightlist:
    for i in step:
        for j in height_range:
            for h in vec:
                for g in min_height:
                    for d in safety_step:
                        filename = "result/%s_acc1_st%d_hr%d_cis%1.4f_mg%d_ss%d.csv"%(flight, i, j, h, g, d)

                        try:
                            with open(filename, 'r') as hakohige:
                                counter = []
                                counterper = []
                                readerf = csv.reader(hakohige)
                                header = next(reader)

                                print filename

                                for row in reader:
                                    if row[5] is not " " and row[5] is not "":
                                        counter.append(float(row[5]))
                                        couterper.append(float(row[2]))

                                plt.figure(figsize=(10, 8))

                                plt.subplots_adjust(wspace = 0.4, hspace = 0.6)

                                plt.subplot(1,2,1)
                                plt.title('Error steps')
                                plt.boxplot(counter)
                                plt.ylabel('[%]')

                                plt.savefig("result/%s_acc1_st%d_hr%d_cos%1.4f_mh%d_ss%d.png"%
                                        \(flight, i, j, h, g, d) dpi = 100, bbox_inches = 'tight')

                                plt.cla()
                                plt.clf()
                                plt.close()
                        except IOError:
                            pass



