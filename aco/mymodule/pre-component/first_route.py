 # -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#Calculate total distance traveled for given visit order
def calculate_total_distance(order, distance_matrix):
  idx_s = np.array(order)
  idx_e = np.array(order[1:])
  idx_e = np.append(idx_e, order[0])
  distance_arr = distance_matrix[idx_s, idx_e]

  return np.sum(distance_arr)

def calculate_2opt_exchange_cost(visit_order, i, j, distance_matrix):
    """Calculate the difference of cost by applying given 2-opt exchange"""
    n_cities = len(visit_order)
    a, b = visit_order[i], visit_order[(i + 1) % n_cities]
    c, d = visit_order[j], visit_order[(j + 1) % n_cities]

    cost_before = distance_matrix[a, b] + distance_matrix[c, d]
    cost_after = distance_matrix[a, c] + distance_matrix[b, d]
    return cost_after - cost_before

def apply_2opt_exchange(visit_order, i, j):
    """Apply 2-opt exhanging on visit order"""
    tmp = visit_order[i + 1: j + 1]
    tmp.reverse()
    visit_order[i + 1: j + 1] = tmp
  #  visit_order[i + 1: j + 1] = tmp[::1]

    return visit_order

def improve_with_2opt(visit_order, distance_matrix):
    """Check all 2-opt neighbors and improve the visit order"""
    n_cities = len(visit_order)
    cost_diff_best = 0.0
    i_best, j_best = None, None

    for i in range(0, n_cities - 2):
        for j in range(i + 2, n_cities):
            if i == 0 and j == n_cities - 1:
                continue

            cost_diff = calculate_2opt_exchange_cost(
                visit_order, i, j, distance_matrix)

            if cost_diff < cost_diff_best:
                cost_diff_best = cost_diff
                i_best, j_best = i, j

    if cost_diff_best < 0.0:
        visit_order_new = apply_2opt_exchange(visit_order, i_best, j_best)
        return visit_order_new
    else:
        return None

def local_search(visit_order, distance_matrix, improve_func):
    """Main procedure of local search"""
  #  cost_total = calculate_total_distance(visit_order, distance_matrix)

    while True:
        improved = improve_func(visit_order, distance_matrix)
        if not improved:
            break

        visit_order = improved

    return visit_order

def calc_2opt(city_xy,order):
  order=order.tolist()
  x = city_xy[:, 0]
  y = city_xy[:, 1]
  N=len(x)
  distance_matrix = np.sqrt((x[:, np.newaxis] - x[np.newaxis, :]) ** 2 +
                          (y[:, np.newaxis] - y[np.newaxis, :]) ** 2)
  #weight=np.random.random_sample((N,N))
  improved = local_search(order, distance_matrix, improve_with_2opt) 
  #total_distance = calculate_total_distance(improved, distance_matrix)
  #print('近傍探索適用後の総移動距離 = {}'.format(total_distance))
  return improved

