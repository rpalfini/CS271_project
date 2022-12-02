
dict_heuristic = {}
minpath = []
len_Graph = -1


def getKey(visited, current):
    n = current
    for i in visited:
        n = (1 << (63 - i) | n)
    return n


def findMin(graphmap):
    global len_Graph
    global minpath
    len_Graph = len(graphmap)
    minpath.clear()
    for arr in graphmap:
        min = 5000000
        for i in arr:
            if i <= 0:
                continue
            if(i < min):
                min = i
        minpath.append(min)
    # minpath.sort()


# don't call this method
def fun_heuristic_recursive(max, cost, graphmap, current, visited, n):
    global len_Graph
    if (cost >= max):
        return cost
        
    if(n == 0 or (len(visited) == len_Graph)):
        return cost
    min = 0
    for i in range(len_Graph):
        if(i in visited):
            continue
        visited.append(i)
        a = fun_heuristic_recursive(max, graphmap[current][i] + cost - minpath[current], graphmap, i, visited, n - 1) 
        visited.remove(i)
        if(a == 0):
            continue
        if min == 0 or a < min:
           min = a
           continue
    return min


# this heuristic will only check next n steps and return smallest path value of next step for n steps
# input different n may help with the speed and memory usage
def fun_heuristic(max, graphmap, current, visited, n):
    # visited.sort()
    # key = str(current) + str(visited)
    key = getKey(visited, current)
    global dict_heuristic
    if key in dict_heuristic:
        return dict_heuristic[key]
    global len_Graph
    global minpath
    fix = 0
    for i in range(0, len_Graph):
        if i in visited:
            continue
        fix += minpath[i]
    heuristic = []
    for i in range(len_Graph):
        if(i in visited):
            heuristic.append(-1)
            continue
        visited.append(i)
        a = fun_heuristic_recursive(max, graphmap[current][i] + fix, graphmap, i, visited, n - 1)
        visited.remove(i)
        heuristic.append(a)
    dict_heuristic[key] = heuristic
    return heuristic
