 # -*- coding: utf-8 -*-
import sys
import math
from tkinter import *

# 標準入力よりデータを読み込む
def read_data(filename):
    buff = []
    f = open(filename)
    lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    for line in lines2:
        b = line.split()
        buff.append((int(b[0]), int(b[1])))
    return buff

# 距離の計算
def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)

# 経路の距離を求める
def path_length(path):
    global distance_table
    n = 0
    i = 1
    for i in range(1, len(path)):
        n += distance(path[i - 1], path[i])
    n += distance(path[0], path[-1])
    return n

# 分割する方向を決定する
def divide_direction(buff):
    x1 = min(map(lambda x: x[0], buff))
    y1 = min(map(lambda x: x[1], buff))
    x2 = max(map(lambda x: x[0], buff))
    y2 = max(map(lambda x: x[1], buff))
    #xが大きければTrue, yが大きければFalse
    return x2 - x1 > y2 - y1

# 分割する
def divide(buff, axis):
    buff.sort(key=lambda x:x[axis])
    n = len(buff) // 2
    path1 =buff[0:n+1]
    path2 = buff[n:]
    return buff[n], path1, path2

# 差分を計算する
def differ(p, c, q):
    return distance(p, c) + distance(c, q) - distance(p, q)

# 共有点を探す
def search(x, buff):
    for i in range(len(buff)):
        if buff[i] == x:
            if i == 0: return len(buff) - 1, i, i + 1
            if i == len(buff) - 1: return i - 1, i, 0
            return i - 1, i, i + 1

# テスト
def divide_test(buff):
    if len(buff) <= 6:
        draw_path(buff)
    else:
        if divide_direction(buff):  #縦が長いときx座標を基準にソート
             p, b1, b2 = divide(buff, 0)
        else:                       #横が長いときy座標を基準にソート
             p, b1, b2 = divide(buff, 1)
        divide_test(b1)
        divide_test(b2)

# データ入力
point_table = read_data('input.txt')
print(type(point_table))

# 経路の表示
def draw_path(path):
    x0, y0 = path[0]
    for i in range(1, len(path)):
        x1, y1 = path[i]
        c0.create_line(x0, y0, x1, y1)
        x0, y0 = x1, y1
    c0.create_line(x0, y0, path[0][0], path[0][1])
    for x, y in path:
        c0.create_oval(x - 4, y - 4, x + 4, y + 4, fill = "green")

max_x = max(map(lambda x: x[0], point_table)) + 20
max_y = max(map(lambda x: x[1], point_table)) + 20
root = Tk()
c0 = Canvas(root, width = max_x, height = max_y, bg = "white")
c0.pack()

divide_test(point_table)

root.mainloop()
