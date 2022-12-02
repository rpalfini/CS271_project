import copy
import random
from graphviz import Digraph
import matplotlib.pyplot as plt
from Heuristic import heuristic
import inputTransformer

# pending

# 1.graph with edge weight
# 2.store the path

import time 
time_dfs = 0
time_hx = 0

# genrate graph
# g = Digraph('G')
# g.attr(compound='true')
# DFS_number = 0


def DFS(startnode, adj_matrix, node, need_visit, path, visited):

    # time
    t_nanosec = time.time_ns()
    global total_t
    global time_dfs
    global time_hx
    total_t += 1
    #

    # path
    global p
    global temp_p
    global upper_bound
    #

    # graph
    # global DFS_number
    # global g
    #

    # curr_node = str(node) + '|' + str(DFS_number)
    # break condition
    #if path > upper_bound:
        # g.edge(curr_node, 'terminated' + str(path))
    #    return

    temp_p.append(node)

    # update this time complexicty. make deep copy of list,increase space complexcity, may need to add node back in future/not linear space?

    # temp_visited = copy.deepcopy(visited)
    visited.append(node)
    N = len(adj_matrix)
    # visit all the node,return the path
    if len(visited) == N:
        new_distance = path + adj_matrix[node][Start_node]
        if new_distance <= upper_bound:
            upper_bound = new_distance
            p = copy.deepcopy(temp_p)
        #    g.edge(curr_node, 'solution|' + str(new_distance))
        # else:
        #    g.edge(curr_node, 'terminated|' + str(new_distance))

        temp_p.remove(node)
        visited.remove(node)
        return

    #
    te_nanosec = time.time_ns()
    time_dfs += te_nanosec - t_nanosec
    t_nanosec = time.time_ns()
    hx = heuristic.fun_heuristic(upper_bound - path, adj_matrix, node, visited, 3)
    te_nanosec = time.time_ns()
    time_hx += te_nanosec - t_nanosec
    t_nanosec = time.time_ns()
    hxc = list(filter(lambda a: a != 0 and a != -1, hx))
    hxc.sort()
    if(path + hxc[0] > upper_bound):
        temp_p.remove(node)
        # g.edge(curr_node, 'terminated|' + str(path + hxc[0]))
        visited.remove(node)
        return
    count = 0
    sorted_need = []
    l = len(hxc)
    while(count < l):
        for i in range(0, N):
            if path + hxc[count] > upper_bound:
                count += 1;
                break;
            if hx[i] == hxc[count]:
               sorted_need.append(i)
               count += 1
               break
    te_nanosec = time.time_ns()
    time_dfs += te_nanosec - t_nanosec

    for i in sorted_need:
        DFS(startnode, adj_matrix, i, sorted_need, path + adj_matrix[node][i], visited)
    temp_p.remove(node)
    visited.remove(node)
    return


file_input = open("11_5.0_1.0.out", "r")
graph = inputTransformer.getInput(file_input)
N = len(graph)
Start_node = 0
need_visit = {i for i in range(0, N)}  # + [Start_node]

# 3/2 MST
upper_bound = 100000 * N
v_visited = []

total_t = 0

p = []
temp_p = []
heuristic.findMin(graph)
time_nanosec = time.time_ns()
DFS(Start_node, graph, Start_node, need_visit, 0, v_visited)
time_nanosec_end = time.time_ns()

p.append(Start_node)

distance_verify = 0
# verfiy
for i in range(0, len(p) - 1):
 distance_verify += graph[p[i]][p[i + 1]]
print('path: ', p)
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

# g.render('1.png', format='png')
