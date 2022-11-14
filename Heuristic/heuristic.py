# similar to this part from this video but in opposite way, I think it is modification of dijkstra
# video is in Chinese, there is animation to show how the algo works
# https://youtu.be/_B8XV1iIvq8?t=97
from tensorflow.python.ops.gen_array_ops import upper_bound


def fun_moddijkstra(graphmap, goal):
    row = len(graphmap)
    heuristic = []
    cost = []
    lock = []
    untravel = row - 1
    current = goal
    for x in range(row):
        cost.append(0)
        heuristic.append(-1)
        lock.append(False)
    heuristic[goal] = 0
    lock[goal] = True
    # finish init
    # keep loop until all path are traveled
    while(untravel > 0):
        nodelist = graphmap[current]
        list_cost = graphmap[current].copy()
        # find cost of paths
        for i in range(len(nodelist)):
            if(lock[i] == True):
                continue
            path = nodelist[i]
            if(path <= 0):
                continue
            tempcost = path + heuristic[current]
            if(heuristic[i] > tempcost or heuristic[i] == -1):
                heuristic[i] = tempcost
        # Find path to go
        minval = list_cost[0]
        next_to_Travel = 0
        for i in range(1, len(list_cost)):
            if(lock[next_to_Travel] == True) and (lock[i] == False):
                next_to_Travel = i
                continue
            if(lock[i]):
                continue
            v_num = list_cost[i] + heuristic[current]
            if(v_num < minval and v_num > 0):
                minval = v_num
                next_to_Travel = i
        # Finished finding path
        if(lock[next_to_Travel] == False):
            lock[next_to_Travel] = True
            untravel -= 1
        current = next_to_Travel
    return heuristic


import numpy as np


# not used/fit for this project
def fun_full_map_heuristic(graphmap):
    heuristic = []
    for i in range(len(graphmap)):
        a = fun_moddijkstra(graphmap, i)
        heuristic.append(a)
    return np.transpose(heuristic)


dict_heuristic = {}
max_V = 0
sorted = False
minpath = -1


def findMin(graphmap):
    global minpath
    for arr in graphmap:
        for i in arr:
            if i <= 0:
                continue
            if minpath == -1 or i < minpath:
                minpath = i

    return minpath


# don't call this method
def fun_heuristic_recursive(start, graphmap, current, visited, n, max):
    if(n == 0 or (len(visited) == len(graphmap))):
    #    return graphmap[current][start]
        return 0
    heuristic = []
    for i in range(len(graphmap)):
        if(i in visited):
            continue
        tempvisited = visited.copy()
        tempvisited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(start, graphmap, i, tempvisited, n - 1, max)
        if(a == 0):
            continue
        if max == 0:
           max = a
           heuristic.append(a)
           continue
        if a < max:
          heuristic.append(a)
    if(len(heuristic) == 0):
        return 0
    heuristic.sort()
    return heuristic[0]


# this heuristic will only check next n steps and return smallest path value of next step for n steps
# input different n may help with the speed and memory usage
def fun_heuristic(start, graphmap, current, visited, n):
    visited.sort()
    key = str(current) + str(visited)
    global dict_heuristic
    if key in dict_heuristic:
        return dict_heuristic[key]
    
    global sorted
    if sorted == False:
        findMin(graphmap)
        sorted = True
        
    global minpath
    global max_V
    max_V = 0
   # minp = findMin(graphmap)
    fix = max(0, (len(graphmap) - len(visited) - n)) * minpath
    heuristic = []
    for i in range(len(graphmap)):
        if(i in visited):
            heuristic.append(-1)
            continue
        if(n == 0):
            heuristic.append(0)
            continue
        tempvisited = visited.copy()
        tempvisited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(start, graphmap, i, tempvisited, n - 1, max_V) + fix
        heuristic.append(a)
    dict_heuristic[key] = heuristic
    return heuristic
