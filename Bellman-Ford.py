import numpy as np

# Bellman-Ford
print(f"Initial status")

graph = {}

graph["s"] = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["d"] = {}
graph["e"] = {}

graph["s"]["e"] = 8
graph["s"]["a"] = 10
graph["a"]["c"] = 2
graph["b"]["a"] = 1
graph["c"]["b"] = -2
graph["d"]["c"] = -1
graph["d"]["a"] = -4
graph["e"]["d"] = 1

print(f"graph = {graph}")

costs = {}

costs["s"] = 0
costs["a"] = np.inf
costs["b"] = np.inf
costs["c"] = np.inf
costs["d"] = np.inf
costs["e"] = np.inf

print(f"costs = {costs}")

parents = {}

parents["s"] = None
parents["a"] = None
parents["b"] = None
parents["c"] = None
parents["d"] = None
parents["e"] = None

print(f"parents = {parents}")


def bellman_ford(graph, costs, parents):
    for _ in range(len(graph) - 1):
        flag: bool = True
        for i in graph:
            if costs[i] != np.inf:
                for j in graph[i].keys():
                    if costs[i] + graph[i][j] < costs[j]:
                        costs[j] = costs[i] + graph[i][j]
                        parents[j] = i
                        flag = False
        if flag:
            return


bellman_ford(graph, costs, parents)

print(f"End status:")

print(f"costs = {costs}")
print(f"parents = {parents}")
