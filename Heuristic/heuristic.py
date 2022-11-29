
#dict_heuristic = {}
minpath = []
len_Graph = -1


def findMin(graphmap):
    global len_Graph
    global minpath
    len_Graph = len(graphmap)
    minpath.clear()
    for arr in graphmap:
        for i in arr:
            if i <= 0:
                continue
            minpath.append(i)
    minpath.sort()

# don't call this method
def fun_heuristic_recursive(graphmap, current, visited, n):
    global len_Graph
    if(n == 0 or (len(visited) == len_Graph)):
    #    return graphmap[current][start]
        return 0
    min = 0
    for i in range(len_Graph):
        if(i in visited):
            continue
        visited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, visited, n - 1)
        visited.remove(i)
        if(a == 0):
            continue
        if min == 0 or a < min:
           min = a
           continue
    return min


# this heuristic will only check next n steps and return smallest path value of next step for n steps
# input different n may help with the speed and memory usage
def fun_heuristic(graphmap, current, visited, n):
    #visited.sort()
    #key = str(current) + str(visited)
    #global dict_heuristic
    #if key in dict_heuristic:
    #    return dict_heuristic[key]
    global len_Graph
    global minpath
    fix = n
    for i in range(0,max(0, (len_Graph - len(visited) - n))):
        fix+=minpath[i]
    heuristic = []
    for i in range(len_Graph):
        if(i in visited):
            heuristic.append(-1)
            continue
        if(n == 0):
            heuristic.append(0)
            continue
        visited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, visited, n - 1) + fix
        visited.remove(i)
        heuristic.append(a)
    #dict_heuristic[key] = heuristic
    return heuristic
