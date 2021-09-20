# The implementation below uses the stack data-structure to build-up and return
# a set of vertices that are accessible within the subjects connected component.
# Using Python’s overloading of the subtraction operator to remove items from a
# set, we are able to add only the unvisited adjacent vertices.

# This is the graph

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


result = dfs(graph, 'A')

print(result)
