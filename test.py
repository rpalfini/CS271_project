import copy
from Heuristic import heuristic
import inputTransformer

# pending

import time
time_dfs = 0
time_hx = 0



def DFS(startnode, adj_matrix, node, path, visited):

    # time
    t_nanosec = time.time_ns()
    global total_t
    global time_dfs
    global time_hx
    total_t += 1
    #

    # path
    global optimal_path
    global current_path
    global upper_bound
    #
    current_path.append(node)

    # update this time complexicty. make deep copy of list,increase space complexcity, may need to add node back in future/not linear space?
    visited.append(node)

    N = len(adj_matrix)

    # visit all the node,return the path
    if len(visited) == N:
        new_distance = path + adj_matrix[node][Start_node]
        if new_distance <= upper_bound:
            upper_bound = new_distance
            optimal_path = copy.deepcopy(current_path)

        current_path.remove(node)
        visited.remove(node)
        return

    #time
    te_nanosec = time.time_ns()
    time_dfs += te_nanosec - t_nanosec
    t_nanosec = time.time_ns()
    #possible bug for visited
    hx = heuristic.fun_heuristic(adj_matrix, node, visited, 4)
    te_nanosec = time.time_ns()
    time_hx += te_nanosec - t_nanosec
    t_nanosec = time.time_ns()
    hxc = list(filter(lambda a: a != 0 and a != -1, hx))
    hxc.sort()

    #break condition
    if(path + hxc[0] > upper_bound):
        current_path.remove(node)
        visited.remove(node)
        return

    #heuristic
    count = 0
    sorted_node = []
    l = len(hxc)
    N = len(graph)
    while(count < l):
        # if(hxc[count] <= 0):
        #    break
        for i in range(0, N):
            if hx[i] == hxc[count]:
               sorted_node.append(i)
               count += 1
               break
    te_nanosec = time.time_ns()
    time_dfs += te_nanosec - t_nanosec

    for i in sorted_node:
        DFS(startnode, adj_matrix, i, path + adj_matrix[node][i], visited)

    current_path.remove(node)
    visited.remove(node)
    return


file_input = open("11_5.0_1.0.out", "r")
graph = inputTransformer.getInput(file_input)
N = len(graph)
Start_node = 0
need_visit = [i for i in range(0, N)]

# 3/2 MST
upper_bound = max([max(d) for d in graph])*N
v_visited = []

total_t = 0

optimal_path = []
current_path = []
heuristic.findMin(graph)
time_nanosec = time.time_ns()
DFS(Start_node, graph, Start_node, 0, v_visited)
time_nanosec_end = time.time_ns()

optimal_path.append(Start_node)

distance_verify = 0
# verfiy
for i in range(0, len(optimal_path) - 1):
    distance_verify += graph[optimal_path[i]][optimal_path[i + 1]]
print('path: ', optimal_path)
print('path_verify:', distance_verify)
#

print("shortest path cost: " + str(upper_bound))
print("cost to loop: " + str(total_t))
t = 1
for i in range(1, N):
    t *= i
print("cost to loop all: " + str(t))
print("dfs ns time: " + str(time_dfs))
print("hx ns time: " + str(time_hx))