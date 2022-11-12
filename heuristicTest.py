import inputTransformer
from Heuristic import heuristic

file_input = open("input.txt", "r")
graph = inputTransformer.getInput(file_input)
for i in graph:
    print(i)
print(str(heuristic.fun_heuristic(graph, 1, [1], 2)))
