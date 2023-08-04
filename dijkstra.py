import numpy as np

# dijkstra

print(f"Initial status:")

# FIRST GRAPH ----------------------------------------
#
# graph = {}
#
# graph["start"] = {}
# graph["A"] = {}
# graph["B"] = {}
# graph["end"] = {}
#
# graph["start"]["A"] = 6
# graph["start"]["B"] = 2
# graph["A"]["end"] = 1
# graph["B"]["A"] = 3
# graph["B"]["end"] = 5
#
# print(f"graph = {graph}")
#
# costs = {}
#
# costs["start"] = 0
# costs["A"] = np.inf
# costs["B"] = np.inf
# costs["end"] = np.inf
#
# print(f"costs = {costs}")
#
# parents = {}
#
# parents["start"] = None
# parents["A"] = None
# parents["B"] = None
# parents["end"] = None
#
# print(f"parents = {parents}")
#
# not_processed = np.unique(np.array(["start", "A", "B"]))
#
#
# print(not_processed)
# FIRST GRAPH ----------------------------------------

# SECOND GRAPH ----------------------------------------
# creating graph
graph = {}

graph["start"] = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["d"] = {}
graph["end"] = {}

graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"]["d"] = 6
graph["c"]["end"] = 3
graph["d"]["end"] = 1

print(f"graph = {graph}")

# creating costs hash table
costs = {}

costs["start"] = 0
costs["a"] = np.inf
costs["b"] = np.inf
costs["c"] = np.inf
costs["d"] = np.inf
costs["end"] = np.inf

print(f"costs = {costs}")

# creating parents hash table
parents = {}

parents["start"] = None
parents["a"] = None
parents["b"] = None
parents["c"] = None
parents["d"] = None
parents["end"] = None

print(f"parents = {parents}")

# a set of unprocessed nodes (algorithm can be improved by removing this set)
not_processed = np.unique(np.array(["start", "a", "b", "c", "d"]))


# SECOND GRAPH ----------------------------------------

# function for finding next node with minimum cost
def find_min(not_processed, costs):
    int_min: int = np.inf
    res_node: str
    for i in not_processed:
        if costs[i] < int_min:
            int_min = costs[i]
            res_node = i
    return res_node


# print(find_min(not_processed, costs))

# function for dijkstra algorithm
def dijkstra(graph, costs, parents, not_processed):
    while not_processed.size:
        curr_node = find_min(not_processed, costs)
        # print(f"curr node = {curr_node}")
        not_processed = np.delete(not_processed, np.where(not_processed == curr_node))
        for i in graph[curr_node].keys():
            if costs[curr_node] + graph[curr_node][i] < costs[i]:
                costs[i] = costs[curr_node] + graph[curr_node][i]
                parents[i] = curr_node


dijkstra(graph, costs, parents, not_processed)

print(f"End status:")

print(f"costs = {costs}")
print(f"parents = {parents}")
print(f"answer = {costs['end']}")
