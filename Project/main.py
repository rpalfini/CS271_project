from Project import inputTransformer
from Project import heuristic

file_input = open("input.txt", "r")
graph = inputTransformer.getInput(file_input)
print(graph)
print(str(heuristic.fun_heuristic(graph)))
