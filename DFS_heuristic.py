import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
from Heuristic import heuristic
import inputTransformer

# pending

# 1.graph with edge weight
# 2.store the path

# N = 18

# random.seed(10)
# adj_matrix = [[(random.randint(1, 500) if i != i2 else 0) for i in range(N)] for i2 in range(N)]
# print(adj_matrix)

# G = nx.DiGraph()
# for i in range(0,N):
#    G.add_node(i)
# for i in range(N):
#    for j in range(N):
#        if adj_matrix[i][j] > 0:
#            G.add_edge(i,j,weight = adj_matrix[i][j])
# nx.draw(G)
# plt.show()

import time 
time_dfs = 0
time_hx = 0


def DFS(startnode, adj_matrix, node, need_visit, path, visited):
    t_nanosec = time.time_ns()
    global total_t
    global time_dfs
    global time_hx
    total_t += 1
    #
    # print(node)
    global upper_bound
    # break condition
    if path > upper_bound:
        # print("break: " + str(path) + ">" + str(upper_bound))
        return upper_bound
    temp_need_visit = copy.deepcopy(need_visit)
    temp_need_visit.remove(node)
    temp_visited = copy.deepcopy(visited)
    temp_visited.append(node)
    # if(len(temp_visited)==N):
    #    print("DFS")
    #    print("visited:" + str(temp_visited))
    #    print("need:" + str(temp_need_visit))
    
    # visit all the node,return the path
    if not temp_need_visit:
        return path + adj_matrix[node][Start_node]
    # make deep copy of list,increase space complexcity, may need to add node back in future/not linear space?
    te_nanosec = time.time_ns()
    time_dfs += te_nanosec - t_nanosec
    t_nanosec = time.time_ns()
    hx = heuristic.fun_heuristic(Start_node, adj_matrix, node, temp_visited, 4)
    te_nanosec = time.time_ns()
    time_hx += te_nanosec - t_nanosec
    t_nanosec = time.time_ns()
    hxc = list(filter(lambda a: a != 0 and a != -1, hx))
    hxc.sort()
    if(path + hxc[0] > upper_bound):
        return upper_bound
    count = 0
    sorted_need = []
    l = len(hxc)
    N = len(graph)
    while(count < l):
        if(hxc[count] <= 0):
            break
        for i in range(0, N):
            if hx[i] == hxc[count]:
               sorted_need.append(i)
               count += 1
               break
    te_nanosec = time.time_ns()
    time_dfs += te_nanosec - t_nanosec
    for i in sorted_need:
        temp = DFS(startnode, adj_matrix, i, sorted_need, path + adj_matrix[node][i], temp_visited)
        upper_bound = min(temp , upper_bound)
    return upper_bound


file_input = open("11_5.0_1.0.out", "r")
graph = inputTransformer.getInput(file_input)
print(graph)
N = len(graph)
Start_node = 0
need_visit = [i for i in range(0, N)]  # + [Start_node]

# 3/2 MST
upper_bound = 100000 * N
v_visited = []

total_t = 0

time_nanosec = time.time_ns()
DFS(Start_node, graph, Start_node, need_visit, 0, v_visited)
time_nanosec_end = time.time_ns()

print("shortest path cost: " + str(upper_bound))
print("cost to loop: " + str(total_t))
t = 1
for i in range(1, N):
    t *= i 
print("cost to loop all: " + str(t))
print("dfs ns time: " + str(time_dfs))
print("hx ns time: " + str(time_hx))
