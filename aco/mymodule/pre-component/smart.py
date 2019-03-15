#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re  #to use regex

x=[]
y=[]
cities_set=[]

#open file and remove left characters
def read_tsp_data(tsp_name):
  tsp_name = tsp_name
  with open(tsp_name) as f:
    origin = f.read().splitlines()
    #  clear = [x.lstrip() for x in origin if x != ""]
  return origin
  
#regular expression
#return the number of cities
def get_cities_amounts(in_list):
  non_numeric = re.compile(r'[^\d]+')
  for piece in in_list:
    if piece.startswith("DIMENSION"):
      return non_numeric.sub("",piece)

#edit data → ['x1 y1','x2 y2' ...]
def get_coords(list,number):
  number = int(number)
  for item in list:
    for num in range(1, number + 1):
      if item.startswith(str(num)):
        index, space, rest = item.partition(' ')
        if rest not in cities_set:
          cities_set.append(rest)
          divide=re.split(" +",rest)
          x.append(float(divide[0]))
          y.append(float(divide[1]))
  return [x,y,number]

def produce(filename):
  file=filename
  data = read_tsp_data(file)
  number = int(get_cities_amounts(data))
  cities_set = get_coords(data,number)
  return cities_set

