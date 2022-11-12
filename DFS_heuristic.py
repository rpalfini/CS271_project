import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
from Heuristic import heuristic

# pending

# 1.graph with edge weight
# 2.store the path

N = 16

random.seed(10)
adj_matrix = [[(random.randint(1, 500) if i != i2 else 0) for i in range(N)] for i2 in range(N)]
print(adj_matrix)

# G = nx.DiGraph()
# for i in range(0,N):
#    G.add_node(i)
# for i in range(N):
#    for j in range(N):
#        if adj_matrix[i][j] > 0:
#            G.add_edge(i,j,weight = adj_matrix[i][j])
# nx.draw(G)
# plt.show()

Start_node = 0
need_visit = [i for i in range(0, N)]  # + [Start_node]

# 3/2 MST
upper_bound = 100000 * N
v_visited = []

total_t = 0


def DFS(startnode, adj_matrix, node, need_visit, path, visited):
    global total_t
    total_t += 1
    #
    # print(node)
    global upper_bound
    # break condition
    if path > upper_bound:
        #print("break: " + str(path) + ">" + str(upper_bound))
        return upper_bound
    temp_need_visit = copy.deepcopy(need_visit)
    temp_need_visit.remove(node)
    temp_visited = visited.copy()
    temp_visited.append(node)
    #if(len(temp_visited)==N):
    #    print("DFS")
    #    print("visited:" + str(temp_visited))
    #    print("need:" + str(temp_need_visit))
    
    # visit all the node,return the path
    if not temp_need_visit:
        return path + adj_matrix[node][Start_node]
    # make deep copy of list,increase space complexcity, may need to add node back in future/not linear space?

    hx = heuristic.fun_heuristic(Start_node, adj_matrix, node, temp_visited, 2)
    hxc = list(filter(lambda a: a != 0 and a != -1, hx))
    hxc.sort()
    count = 0
    sorted_need = []
    l = len(hxc)
    
    while(count < l):
        if(hxc[count] <= 0):
            break
        for i in range(0, N):
            if hx[i] == hxc[count]:
               sorted_need.append(i)
               count += 1
               break
    
    for i in sorted_need:
        temp = DFS(startnode, adj_matrix, i, sorted_need, path + adj_matrix[node][i], temp_visited)
        upper_bound = min(temp , upper_bound)
    return upper_bound


DFS(Start_node, adj_matrix, Start_node, need_visit, 0, v_visited)
print("shortest path cost: " + str(upper_bound))
print("cost to loop: " + str(total_t))
t = 1
for i in range(1, N + 1):
    t *= i 
print("cost to loop all: " + str(t))

