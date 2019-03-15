# -*- coding: utf-8 -*-
import numpy as np
import math as math

mx_range=15

def box_muller(num):
    seed = []
    flag = 0
    while( len(seed) < num ):
        if flag == 1:
          flag = 0
          Y = y2

        if flag == 0:
          flag = 1
          u1 = np.random.uniform(0,1)
          u2 = np.random.uniform(0,1)
          if u1 == 0: u1 = np.random.uniform(0,1)

          y1 = np.power((-2 * math.log(u1)),0.5) * math.cos((np.pi * u2)/2)
          y2 = np.power((-2 * math.log(u1)),0.5) * math.sin((np.pi * u2)/2)
          Y = y1

        X = 1 / np.power(Y,2)
        if X < mx_range:
          seed.append(X)

    return seed

def make_levy_randseed(num):
    hn_seed = box_muller(num)

    rand_num = []
    for j in range(len(hn_seed)):
      for k in range(mx_range):
        if hn_seed[j] >k and hn_seed[j] < k+1:
          rand_num.append(k)
    return rand_num

    """
    for j in range(0,15,1):
      print(j,'~',j+1,':',(len([i for i in hn_seed if i>j and i<j+1]))/num)
    print(len(hn_seed))
    """
levy_num = make_levy_randseed(100)
print(levy_num)

"""
print(levy_num)
for i in range(15):
  print(sum(j==i for j in levy_num))
"""



