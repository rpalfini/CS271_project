# similar to this part from this video but in opposite way, I think it is modification of dijkstra
# video is in Chinese, there is animation to show how the algo works
# https://youtu.be/_B8XV1iIvq8?t=97
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


# don't call this method
def fun_heuristic_recursive(graphmap, current, visited, n):
    if(n == 0):
        return 0
    heuristic = []
    for i in range(len(graphmap)):
        tempvisited = visited.copy()
        tempvisited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, tempvisited, n - 1)
        heuristic.append(a)
    heuristic.sort()
    return heuristic[0]


# this heuristic will only check next n steps and return smallest path value of next step for n steps
# input different n may help with the speed and memory usage
def fun_heuristic(graphmap, current, visited, n):
    heuristic = []
    for i in range(len(graphmap)):
        if(i in visited):
            heuristic.append(-1)
        if(n == 0):
            heuristic.append(0)
            continue
        tempvisited = visited.copy()
        tempvisited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, tempvisited, n - 1)
        heuristic.append(a)
    return heuristic
