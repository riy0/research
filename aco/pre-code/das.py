#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import mymodule
from scipy.spatial import distance as dis

class TSP:
  def __init__(self,path=None,alpha = 1.0,beta = 5.0,Q = 100,rho = 0.80):
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
    return locations
  
  def set_loc(self,filename):
    """ 位置座標を設定する関数 """
    self.loc = self.read_tsp(filename)							# x,y座標
    self.N = len(self.loc)						# データ数
    self.dist = dis.squareform(dis.pdist(self.loc))	# 距離の表を作成
    self.weight = np.random.random_sample((self.N,self.N))	# フェロモンの量
    self.result = np.arange(self.N)
 
  def cost(self,order):
    """ コストを計算する関数 """
    s=np.array(order)
    e=np.array(order[1:])
    e= np.append(e,order[0])
    distance_arr=self.dist[s,e]
    return np.sum(distance_arr)
 
  def plot(self,order=None):
    """ 指定された順序でプロットする関数 """
    plt.figure(figsize=(5,5))
    route=np.array(order)
    route=np.append(route,route[0])
    x=self.loc[:,0][route]
    y=self.loc[:,1][route]

    plt.plot(x,y,'o-')
    plt.show()

  def divide(self,order,i):
    # [1,2,3,4,5]だったら[1,2,3],[4,5]に分割
    point = np.random.randint(self.N)	# 分割する都市
    mass = np.array(order)
    #print(self.cost(mass))
    n = len(mass) // 2
    mass=np.append(mass,order)
    path1= mass[point:point+n]
    path2= mass[point+n:point+n*2+1]
    path1= self.divide_ant_search(path1,50,i)
    combined =np.array(path1)
    combined =np.append(path1,path2)

    if self.cost(self.result) > self.cost(combined):
      self.result = combined
    return self.result

  #フェロモンの更新とMMAS
  def evaluate_func(self,current,city):
    a = np.power(self.weight[current,city],self.alpha)
    b = np.power((1/(self.dist[current,city])),self.beta)
    upper= a * b
    evaluation= upper / (np.sum(upper))
    percentage = evaluation / np.sum(evaluation)	# 移動確率
    return self.random_index(percentage)			# 移動先の要素番号取得

  def solve(self,n_agent):
    """ 巡回セールスマン問題を蟻コロニー最適化で解く """
    order = np.zeros(self.N,np.int)	#フェロモン変化量
    self.delta = np.zeros((self.N,self.N))	#フェロモン変化量
    #for i in range():
    for i in range(33):
      print("%d回目" %i )
      self.ant_search(order,n_agent,i)
      self.divide(self.result,i)
      self.divide(self.result,i)
      #普通の→ 分割した片方 → 再度分割して片方

  def divide_ant_search(self,order,n_agent,i):
    #n匹目のあり
    result=order.copy()
#    base=order.copy()
    for k in range(self.N):
      #分割点を固定
      city = np.array(result)             # 配列をコピー
      city = city[city != city[0]] 
      city = city[city != city[-1]]

      #スタート地点の決定
      current=np.random.choice(city)
      city = city[ city != current]
      #order[0]=base[0]
      order[1]=current
      #n匹目のありが探索を開始
      for j in range(1,len(order)-2):
        next_city=self.evaluate_func(current,city) #次の都市を選択

        # 状態の更新
        current = city[next_city]
        city = city[ city != current]
        order[j+1] = current
      order[-1]=order[-1]
      L = self.cost(order) # 経路のコストを計算

      # 今までで最も良ければ結果を更新
      if self.cost(result) > L:
        result = order.copy()
        if(i > 30):
          result=mymodule.first_route.calc_2opt(self.loc,result)
          L=self.cost(result)
          order=result.copy()
        print("Agent ... %d , Cost ... %lf" % (k,self.cost(result)))

      # フェロモンの変化量を計算
      self.calc_divide_pheromone(order,L,result)
    return result

  def calc_divide_pheromone(self,order,L,result):
    n=len(order)
    p= math.pow(0.05,(1.0/n))
    tmax= (1.0/1-self.rho) * (1.0/self.cost(result))
    tmin= (tmax*(1.0-p)) / ((n/2.0-1) *p)
    self.delta[:,:] = 0.0
    c = self.Q / L
    for j in range(len(order)-1):
      self.delta[order[j],order[j+1]] = c
      self.delta[order[j+1],order[j]] = c
    # フェロモン更新
    # MMASによりmax valueとmin valueを調整
    self.weight *= self.rho
    self.weight += self.delta
    self.weight[np.where(self.weight > tmax)]=tmax
    self.weight[np.where(self.weight < tmin)]=tmin

  def ant_search(self,order,n_agent,i):
    #n匹目のあり
    for k in range(n_agent):
      city = np.arange(self.N)             # 都市数の配列
      current = np.random.randint(self.N)	# 現在居る都市番号

      city = city[ city != current ]
      order[0] = current

      #n匹目のありが探索を開始
      for j in range(1,self.N):
        #評価関数より次の都市を選択
        next_city=self.evaluate_func(current,city)

        # 状態の更新
        current = city[next_city]
        city = city[ city != current ]
        order[j] = current
      L = self.cost(order) # 経路のコストを計算

      # 今までで最も良ければ結果を更新
      if self.cost(self.result) > L:
        self.result = order.copy()
        if(i > 30):
          self.result=mymodule.first_route.calc_2opt(self.loc,self.result)
          L=self.cost(self.result)
          order=self.result.copy()
        print("Agent ... %d , Cost ... %lf" % (k,self.cost(self.result)))
      #print(L)

      # フェロモンの変化量を計算
      self.calculate_pheromone(order,L)
    return self.result

  def calculate_pheromone(self,order,L ):
    p= math.pow(0.05,(1.0/self.N))
    tmax= (1.0/1-self.rho) * (1.0/self.cost(self.result))
    tmin= (tmax*(1.0-p)) / (((self.N/2.0)-1) *p)
    self.delta[:,:] = 0.0
    c = self.Q / L
    for j in range(self.N-1):
      self.delta[order[j],order[j+1]] = c
      self.delta[order[j+1],order[j]] = c
    # フェロモン更新
    # MMASによりmax valueとmin valueを調整
    self.weight *= self.rho
    self.weight += self.delta
    self.weight[np.where(self.weight > tmax)]=tmax
    self.weight[np.where(self.weight < tmin)]=tmin

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
  tsp.set_loc("tsp/att48.tsp")
  
  tsp.solve(n_agent=50)		# 1000匹の蟻を歩かせる
  #tsp.divide(tsp.result)
  print(tsp.cost(tsp.result))
  tsp.plot(tsp.result)		# 計算後



