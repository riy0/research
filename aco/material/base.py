 # -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import mymodule

#Calculate total distance traveled for given visit order
def calculate_total_distance(order, distance_matrix):
  idx_s = np.array(order)
  idx_e = np.array(order[1:] + [order[0]])
  distance_arr = distance_matrix[idx_s, idx_e]

  return np.sum(distance_arr)

#make a line
def visualize_visit_order(order, city_xy):
  """Visualize traveling path for given visit order"""
  print(order)
  route = np.array(order + [order[0]])  # add point of departure
  print (route)
#  print(city_xy)
  x_arr = city_xy[:, 0][route]
  y_arr = city_xy[:, 1][route]

  plt.figure(figsize=(4, 4))
  plt.plot(x_arr, y_arr, 'o-')
  plt.show()

def __init__(self,alpha=1.0,beta=1.0,rho=0.95,Q=1.0):
  self.alpha=alpha
  self.beta=beta
  self.rho=rho
  self.Q=Q

if __name__ == '__main__':
  #default
  tsp=mymodule.smart.produce("tsp/eil51.tsp")
  distance_x=tsp[0]
  distance_y=tsp[1]
  N=len(distance_x)

  city_xy = np.zeros((len(distance_x),2))
  for i in range(N):
    city_xy[i][0]=int(distance_x[i])
    city_xy[i][1]=int(distance_y[i])

  x = city_xy[:, 0]
  y = city_xy[:, 1]
  #距離の表を作成
  distance_matrix = np.sqrt((x[:, np.newaxis] - x[np.newaxis, :]) ** 2 + (y[:, np.newaxis] - y[np.newaxis, :]) ** 2)
  weight=np.random.random_sample((N,N))

  order = list(np.random.permutation(N))
  visualize_visit_order(order, city_xy)
  total_distance = calculate_total_distance(order, distance_matrix)
  #print('初期解の総移動距離 = {}'.format(total_distance))

