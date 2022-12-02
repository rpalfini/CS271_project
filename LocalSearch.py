import inputTransformer
import random


def random_permutation(N):
	list = []
	permutation = []
	for i in range(N):
		list.append(i)
	while len(list) > 0:
		node = list[random.randint(0, len(list) - 1)]
		list.remove(node)
		permutation.append(node)
	return permutation


def calc_cost(path, adj_matrix):
	cost = 0
	N = len(adj_matrix)
	for i in range(N - 1):
		cost += adj_matrix[path[i]][path[i + 1]]
	cost += adj_matrix[path[N - 1]][path[0]]
	return cost


def swap(path, idx_node1, idx_node2):
	temp = path[idx_node1]
	path[idx_node1] = path[idx_node2]
	path[idx_node2] = temp
	return path


def Prob(p):
	return random.randint(0, 100) < p


def SLS(path, adj_matrix):
	N = len(adj_matrix)
	best_solution = path
	best_cost = calc_cost(best_solution, adj_matrix)
	cost = N * 5000
	p = 1
	search = True
	while search:
		search = False
		for node1 in range(N):
			for node2 in range(N):
				if(node1 == node2):
					continue
				swap(path, node1, node2)
				new_cost = calc_cost(path, adj_matrix)
				if(new_cost < cost or Prob(p) == True):
					cost = new_cost
					best_solution = path.copy()
					# print(best_solution)
					# print(cost)
					search = True
				else:
					swap(path, node1, node2)
	return best_solution


file_input = open("11_5.0_1.0.out", "r")
adjacency_matrix = inputTransformer.getInput(file_input)
N = len(adjacency_matrix)
best_overall = []
best_overall_cost = N * 5000
list_searched = []
count = 500
while count > 0:
	path_random = random_permutation(N)
	not_converged = True
	if(path_random in list_searched):
		continue
	list_searched.append(path_random)
	while not_converged:
		best_solution = SLS(path_random, adjacency_matrix)
		if str(best_solution) == str(path_random):
			not_converged = False
		path_random = best_solution
		newcost = calc_cost(best_solution, adjacency_matrix)
		if(newcost < best_overall_cost):
			best_overall = best_solution
			print(best_solution)
			best_overall_cost = newcost
			print(best_overall_cost)
	count -= 1
