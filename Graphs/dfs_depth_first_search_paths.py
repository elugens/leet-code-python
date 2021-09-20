# We are able to tweak both of the previous implementations to return all possible
#  paths between a start and goal vertex. The implementation below uses the stack
# data-structure again to iteratively solve the problem, yielding each possible
# path when we locate the goal. Using a generator allows the user to only compute
# the desired amount of alternative paths.

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))


print(list(dfs_paths(graph, 'A', 'F')))
