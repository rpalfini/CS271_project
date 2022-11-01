import copy
import random
import networkx as nx
import matplotlib.pyplot as plt

#pending

#1.graph with edge weight
#2.store the path


N = 3

random.seed(10)
adj_matrix = [[(random.randint(1,500) if i != i2 else 0) for i in range(N)] for i2 in range(N)]
print(adj_matrix)


G = nx.DiGraph()
for i in range(0,N):
    G.add_node(i)
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] > 0:
            G.add_edge(i,j,weight = adj_matrix[i][j])
nx.draw(G)
plt.show()


Start_node = 0
need_visit = [i for i in range(0,N)] #+ [Start_node]

#3/2 MST
upper_bound = 500*N


def DFS(adj_matrix,node,need_visit,path):
    #
    #print(node)
    global upper_bound
    #break condition
    if path > upper_bound:
        return upper_bound

    temp_need_visit = copy.deepcopy(need_visit)
    temp_need_visit.remove(node)

    #visit all the node,return the path
    if not temp_need_visit:
        return path+adj_matrix[node][Start_node]
    # make deep copy of list,increase space complexcity, may need to add node back in future/not linear space?

    for i in range(0,N):
        #no selfvisit, no repeated
        if i == node or (i not in need_visit):
            continue
        else:
            temp = DFS(adj_matrix,i,temp_need_visit,path + adj_matrix[node][i])
            upper_bound = min(temp ,upper_bound)
    return temp
DFS(adj_matrix,Start_node,need_visit,0)
print(upper_bound)



