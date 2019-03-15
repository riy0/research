#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mymodule
from scipy.spatial import distance as dis

class TSP:
  def __init__(self,path=None,alpha = 1.0,beta = 5.0,Q = 100,rho = 0.90):
    """ 初期化を行う関数 """
    self.alpha = alpha					# フェロモンの優先度
    self.beta = beta					# ヒューリスティック情報(距離)の優先度
    self.Q = Q							# フェロモン変化量の係数
    self.rho = rho	# 蒸発率
  
  def read_tsp(self,filename):
    tsp=mymodule.smart.produce(filename)
    x,y=tsp[0],tsp[1]
    N=len(x)
    locations=np.empty((N,2))
    for i in range(N):
      locations[i][0]=(x[i])
      locations[i][1]=(y[i])
    print(locations[39])
    return locations

  def set_loc(self,filename):
    """ 位置座標を設定する関数 """
    self.loc = self.read_tsp(filename)							# x,y座標
    self.n_data = len(self.loc)						# データ数
    self.dist = dis.squareform(dis.pdist(self.loc))	# 距離の表を作成
    self.weight = np.random.random_sample((self.n_data,self.n_data))	# フェロモンの量
    self.result = np.arange(self.n_data)			# もっともよかった順序を保存する

  def cost(self,order):
    """ 指定された順序のコスト計算関数 """
    n_order = len(order)
    return np.sum( [self.dist[order[i],order[(i+1)%n_order]] for i in np.arange(n_order) ] )

  def plot(self,order=None):
    """ 指定された順序でプロットする関数 """
    plt.figure(figsize=(3,3))
    if order is None:
      plt.plot(self.loc[:,0],self.loc[:,1],'o-')
    else:
      route=np.array(order)
      route=np.append(route,route[0])
      x=self.loc[:,0][route]
      y=self.loc[:,1][route]

      plt.plot(x,y,'o-')
    plt.show()

  def solve(self,n_agent):
    """ 巡回セールスマン問題を蟻コロニー最適化で解く """

    order = np.zeros(self.n_data,np.int) 		# 巡回経路
    delta = np.zeros((self.n_data,self.n_data))	#フェロモン変化量
    for i in range(1):
      self.ant_search(n_agent,order,delta)

  def ant_search(self,n_agent,order,delta):
    #n匹目のあり
    for k in range(n_agent):
      city = np.arange(self.n_data)
      now_city = np.random.randint(self.n_data)	# 現在居る都市番号

      city = city[ city != now_city ]
      order[0] = now_city
      #n匹目のありが探索を開始
      for j in range(1,self.n_data):
        upper=np.power(self.weight[now_city,city],self.alpha)*np.power((1/(self.dist[now_city,city])),self.beta)
        a=np.sum(upper)
#        upper = np.power(self.weight[now_city,city],self.alpha)*np.power(self.dist[now_city,city],-self.beta)
        old_err_state = np.seterr(divide='raise')
        ignored_states = np.seterr(**old_err_state)
        evaluation = np.true_divide(upper,a)	# 評価関数
        percentage = evaluation / np.sum(evaluation)	# 移動確率
        index = self.random_index(percentage)			# 移動先の要素番号取得

        # 状態の更新
        now_city = city[index]
        city = city[ city != now_city ]
        order[j] = now_city
      #L = self.cost(order) # 経路のコストを計算

      check= np.array(order)
      check = np.append(order,order[0])
      L = self.cost(check) # 経路のコストを計算

#     print(L)
#     print(A)

      # フェロモンの変化量を計算
      delta[:,:] = 0.0
      c = self.Q / L
    #  for j in range(self.n_data-1):
     #   delta[order[j],order[j+1]] = c
      #  delta[order[j+1],order[j]] = c
      for j in range(self.n_data):
        delta[check[j],check[j+1]] = c
        delta[check[j+1],check[j]] = c
      # フェロモン更新
      self.weight *= self.rho
      self.weight += delta

      # 今までで最も良ければ結果を更新
      if self.cost(self.result) > L:
        self.result = order.copy()

        # デバッグ用
      print("Agent ... %d , Cost ... %lf" % (k,self.cost(self.result)))
    return self.result

  def random_index(self,percentage):
    """ 任意の確率分布に従って乱数を生成する関数 """
    n_percentage = len(percentage)

    while True:
      index = np.random.randint(n_percentage)
      y = np.random.random()
      if y < percentage[index]:
        return index

if __name__=="__main__":
  #tsp = TSP(path="input.csv")
  tsp = TSP()
  a= tsp.set_loc("tsp/eil51.tsp")
  print(a)
  tsp.plot()					# 計算前
  tsp.solve(n_agent=1000)		# 1000匹の蟻を歩かせる
  tsp.plot(tsp.result)		# 計算後
