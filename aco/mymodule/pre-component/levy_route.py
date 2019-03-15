 # -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
import random

def decide_scale_param():
  param = [ 1/2, 1, 2, 4, 8]

  scale = random.randint(0,4)
  return param[scale]

# decide percentage using by levy flight
def levy_percentage(x):
  c = decide_scale_param()
  return math.sqrt(c/(2*math.pi)) * math.exp((-c)/(2*x)) / x**(3/2)


