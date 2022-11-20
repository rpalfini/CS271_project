dict_heuristic = {}
max_V = 0
sorted = False
minpath = -1


def findMin(graphmap):
    minpath = -1
    for arr in graphmap:
        for i in arr:
            if i <= 0:
                continue
            if minpath == -1 or i < minpath:
                minpath = i


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
    
    #global sorted
    #if sorted == False:
    #   findMin(graphmap)
    #   sorted = True
    global minpath
    global max_V
    max_V = 0
    fix = max(0, (len(graphmap) - len(visited) - n)) * minpath
    heuristic = []
    for i in range(len(graphmap)):
        if(i in visited):
            heuristic.append(-1)
            continue
        if(n == 0):
            heuristic.append(0)
            continue
#        tempvisited = visited.copy()
        visited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(start, graphmap, i, visited, n - 1, max_V) + fix
        visited.remove(i)
        heuristic.append(a)
    dict_heuristic[key] = heuristic
    return heuristic
