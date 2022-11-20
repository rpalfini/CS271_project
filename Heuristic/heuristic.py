dict_heuristic = {}
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
def fun_heuristic_recursive(graphmap, current, visited, n):
    if(n == 0 or (len(visited) == len(graphmap))):
    #    return graphmap[current][start]
        return 0
    min = 0
    for i in range(len(graphmap)):
        if(i in visited):
            continue
        tempvisited = visited.copy()
        tempvisited.append(i)
        a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, tempvisited, n - 1)
        if(a == 0):
            continue
        if min == 0 or a < min:
           min = a
           continue
    return min


# this heuristic will only check next n steps and return smallest path value of next step for n steps
# input different n may help with the speed and memory usage
def fun_heuristic(graphmap, current, visited, n):
    visited.sort()
    key = str(current) + str(visited)
    global dict_heuristic
    if key in dict_heuristic:
        return dict_heuristic[key]
    
    # global sorted
    # if sorted == False:
    #   findMin(graphmap)
    #   sorted = True
    global minpath
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
        a = graphmap[current][i] + fun_heuristic_recursive(graphmap, i, visited, n - 1) + fix
        visited.remove(i)
        heuristic.append(a)
    dict_heuristic[key] = heuristic
    return heuristic
