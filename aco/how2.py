import math
import numpy as np
import matplotlib.pyplot as plt
import mymodule
import random

#print(mymodule.levy_route.levy_percentage(random.uniform(0,1.5)))

# 描画範囲の指定
#x = np.arange(x軸の最小値, x軸の最大値, 刻み)
x = np.arange(0, 3, 0.01)
y = np.arange(0, 1, 0.01)

#levy_flightの確率密度関数の描画

param = [1/2,1,2,4,8]
for c in param:
  a = np.exp((-c)/(2*(x)))
  b = (x)**(3/2)
  y = math.sqrt(c/(2*math.pi)) * a/b
  # 横軸の変数。縦軸の変数
  plt.plot(x, y)

# 描画実行
plt.show()

"""
x=np.array([1,2,3,4,5])
print(x)
x=np.append(x,10)
print(x)
x=np.arange(5)
a=np.true_divide(x,4)
print(a)
def ngongo():

  a= np.array([1,2,3,4,5])
  d= np.sum(a)-a[3]
  print(d)

a= np.array([1,2,3,4,5])

now=np.random.randiint(10)
print(now)

now=np.random.randiint(a)

def ngongo():
  a=3
  if a>1:
    return 4
  return 5
"""
