# coding utf-8
import matplotlib.pyplot as plt
import sys
import os.path
import re
from datetime import datetime
import numpy as np
import math
import copy

ALPHA = 1
BETA = 5
Q = 100
RO = 0.4
AGENT = 50
GENERATION = 100

route=[]


class DAS:
    def __init__(self):
        # check commandline argument
        argv = sys.argv
        if len(argv) != 2:
            print("Usage: python3 %s problem.tsp" % argv[0])
            quit()

        # load data
        readflag = 0
        n = 0
        with open(argv[1]) as f:
            for row in f:
                array = row.split()
                if re.match("DIMENSION", array[0]):
                    self.townNum = int(array[-1])
                    self.pos = np.zeros((self.townNum, 2))
                if re.match("EDGE_WEIGHT_TYPE", array[0]):
                    distType = array[-1]
                if readflag == 1:
                    if len(array) == 3:
                        self.pos[n] = [float(array[1]), float(array[2])]
                    n += 1
                if re.match("NODE_COORD_SECTION", array[0]):
                    readflag = 1

        # initialize
        self.problem = (os.path.basename(argv[1])).split(".")[0]
        self.towns = np.array(range(self.townNum))
        self.roads = self.makeDist(distType)
        self.phero = np.where(1/self.roads < 0, 0, 1/self.roads)
        self.way = []
        self.changeFlag = 0

    # solve problem
    def solve(self):
        #print("Problem : " + self.problem)
        #print("Solving", end="")
        sys.stdout.flush()

        i, endFlag, notChangeCount = 0, 0, 0
        while endFlag == 0:
            # loop mmas -> dcaco -> dcaco
            if i % 3 == 0:
                self.runMMAS()
            else:
                self.runDCACO()
                if self.changeFlag == 1:
                    notChangeCount = 0
                else:
                    notChangeCount = notChangeCount + 1

            # judge end or continue
            if notChangeCount == 20:
                endFlag = 1

            # output
            if (i + 1) % 3 == 0:
                #print(".", end="")
                sys.stdout.flush()

            i = i + 1

        # result
        #print("\nBest Way :")
        #print(np.array(self.way) + 1)
        self.makeImage()
        route.append(self.getLength(self.way))
        print(self.getLength(self.way))

        #print("Complete!")

    # run Max-Min Ant System method
    def runMMAS(self):
        mmas = MMAS(self.towns, self.roads, self.phero)
        self.way = mmas.solve()
        self.phero = mmas.getPhero()

    # run Divide and Conquer Ant Colony Optimization
    def runDCACO(self):
        self.changeFlag = 0
        # divide a circuit into two pathes
        point = np.random.randint(self.townNum)
        tempWay = self.way[:-1]
        tempWay = tempWay[point:] + tempWay[:point]
        path = tempWay[:int(self.townNum/2)]

        # apply MMAS to a path
        dcaco = MMAS(path, self.roads, self.phero, path[0], path[-1])
        returnPath = dcaco.solve()

        # update way and pheromone if better result returns
        if self.getLength(returnPath) < self.getLength(path):
            self.changeFlag = 1
            #print("!", end="")
            # update way
            tempWay = returnPath + tempWay[int(self.townNum/2):]
            tempWay.append(tempWay[0])
            self.way = copy.deepcopy(tempWay)
            # update pheromone
            _filter = np.zeros((self.townNum, self.townNum))
            for i in range(len(path)):
                for j in range(len(path)):
                    if i < j:
                        if not (i == 0 and j == len(path) - 1):
                            _filter[path[i]][path[j]] = 1
                            _filter[path[j]][path[i]] = 1
            phero = dcaco.getPhero()
            self.phero = np.where(_filter == 1, phero, self.phero)


    # make distance matrix
    def makeDist(self, distType):
        dist = np.zeros((self.townNum, self.townNum)) - 1
        for i in range(self.townNum):
            for j in range(self.townNum):
                if i < j:
                    if distType == 'ATT':
                        d = int(math.ceil(np.sqrt(((self.pos[i][0]-self.pos[j][0])**2+(self.pos[i][1]-self.pos[j][1])**2)/10.0)))
                    elif distType == 'EUC_2D':
                        d = int(round(np.sqrt(((self.pos[i][0]-self.pos[j][0])**2+(self.pos[i][1]-self.pos[j][1])**2))))
                    else:
                        d = int(round(np.sqrt(((self.pos[i][0]-self.pos[j][0])**2+(self.pos[i][1]-self.pos[j][1])**2))))
                    dist[i][j] = d
                    dist[j][i] = d
        return dist

    # get length
    def getLength(self, way):
        length = 0
        for i in range(len(way) - 1):
            length += self.roads[(way[i], way[i + 1])]
        return length

    # make TSP image file
    def makeImage(self):
        p = np.copy(self.phero)
        phrange = p.max() - p.min() + 1
        p = p/phrange

        fig, ax = plt.subplots(figsize=(12, 8))
        plt.title("problem:" + self.problem + "," + " length:" + str(self.getLength(self.way)))
        for i in range(self.townNum):
            plt.scatter(self.pos[i][0], self.pos[i][1])
            plt.annotate(i + 1, (self.pos[self.way[i]][0]+1,
                                 self.pos[self.way[i]][1]-3), color='r')
            # plt.annotate(way[i], (self.pos[self.way[i]][0]+1,
            #                       self.pos[self.way[i]][1]+1), color='g')
            plt.plot([self.pos[self.way[i]][0], self.pos[self.way[(i + 1) % self.townNum]][0]],
                     [self.pos[self.way[i]][1], self.pos[self.way[(i + 1) % self.townNum]][1]], 'b')
        for j in range(self.townNum):
            if(i < j):
                plt.plot([self.pos[self.way[i]][0], self.pos[self.way[(i + 1) % self.townNum]][0]],
                         [self.pos[self.way[i]][1], self.pos[self.way[(i + 1) % self.townNum]][1]], 'r', alpha=p[i][j])
        plt.grid()
        # plt.savefig("./../hist/" + title + ".png")
        plt.show()
        plt.close('all')


class MMAS:
    def __init__(self, towns, roads, phero, start=None, end=None):
        self.towns = towns
        self.roads = roads
        self.phero = np.copy(phero)
        self.start = start
        self.end = end
        self.townNum = len(self.towns)

    # solve problem
    def solve(self):
        minWay = None
        for i in range(AGENT):
            way = self.antWalk()
            length = self.getLength(way)
            if minWay is None or self.getLength(minWay) > length:
                minWay = way
        self.updatePhero(minWay)
        return minWay

    # make way
    def antWalk(self):
        # initialize
        if self.start is None or self.end is None:
            start = np.random.choice(self.towns, 1)[0]
            end = start
        else:
            start = self.start
            end = self.end

        # Ant System
        current = start
        notVisited = np.copy(self.towns)
        notVisited = np.delete(notVisited, np.where(notVisited == start))
        notVisited = np.delete(notVisited, np.where(notVisited == end))
        visited = [current]
        for i in range(len(notVisited)):
            # calculate probability to select a path
            elem = np.power(self.phero[current, notVisited], ALPHA) * np.power(self.roads[current, notVisited], -BETA)
            prob = elem / np.sum(elem)
            choice = np.random.random()
            for j in range(len(notVisited)):
                choice = choice - prob[j]
                if choice < 0:
                    nextTown = notVisited[j]
                    break
            # select a path
            current = nextTown
            visited.append(current)
            notVisited = np.delete(notVisited, np.where(notVisited == current))
        visited.append(end)

        # optimize locally
        visited = self.localOptimization(visited)

        return visited

    def localOptimization(self, way):
        # 2-opt circuit
        if way[0] == way[-1]:
            tempWay = way[:-1]
            num = len(tempWay)
            for i in range(num):
                ch = [i, (i + 1) % num, (i+2)%num, (i+3) % num]
                r1 = self.roads[tempWay[ch[0]]][tempWay[ch[1]]] + self.roads[tempWay[ch[2]]][tempWay[ch[3]]]
                r2 = self.roads[tempWay[ch[0]]][tempWay[ch[2]]] + self.roads[tempWay[ch[1]]][tempWay[ch[3]]]
                if r1 > r2:
                    tmp = tempWay[ch[1]]
                    tempWay[ch[1]] = tempWay[ch[2]]
                    tempWay[ch[2]] = tmp
            tempWay.append(tempWay[0])

        # 2-opt path
        else:
            tempWay = copy.deepcopy(way)
            for i in range(len(way) - 3):
                ch = [i, i + 1, i + 2, i + 3]
                r1 = self.roads[tempWay[ch[0]]][tempWay[ch[1]]] + self.roads[tempWay[ch[2]]][tempWay[ch[3]]]
                r2 = self.roads[tempWay[ch[0]]][tempWay[ch[2]]] + self.roads[tempWay[ch[1]]][tempWay[ch[3]]]
                if r1 > r2:
                    tmp = tempWay[ch[1]]
                    tempWay[ch[1]] = tempWay[ch[2]]
                    tempWay[ch[2]] = tmp

        return tempWay

    # update pheromone
    def updatePhero(self, way):
        length = self.getLength(way)

        # calculate limit of pheromone
        elem = np.power(0.05, 1 / self.townNum)
        pheroMax = 1 / ((1 - RO) * length)
        pheroMin = pheroMax * (1 - elem) / (self.townNum / 2 - 1) / elem

        # calculate variation of pheromone
        deltaPhero = np.full_like(self.phero, 0)
        for i in range(len(way) - 1):
            deltaPhero[way[i], way[i + 1]] = Q/length
            deltaPhero[way[i + 1], way[i]] = Q/length

        # update pheromone
        tempPhero = np.copy(self.phero)
        tempPhero = RO * tempPhero + (1 - RO) * deltaPhero
        tempPhero = np.where(tempPhero < pheroMin, pheroMin, tempPhero)
        tempPhero = np.where(tempPhero > pheroMax, pheroMax, tempPhero)
        self.phero = tempPhero

    # get length
    def getLength(self, way):
        length = 0
        for i in range(len(way) - 1):
            length += self.roads[(way[i], way[i + 1])]
        return length

    # get pheromone
    def getPhero(self):
        return self.phero

    # get way
    def getWay(self):
        return self.way


if __name__ == "__main__":
    for i in range(1):
      das = DAS()
      das.solve()
    print(sum(route) /1 )
