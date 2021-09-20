# The second implementation provides the same functionality as the first,
# however, this time we are using the more succinct recursive form. Due to a
# common Python gotcha with default parameter values being created only once,
# we are required to create a new visited set on each user invocation.
# Another Python language detail is that function variables are passed by
# reference, resulting in the visited mutable set not having to reassigned upon
# each recursive call.

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt, visited)
    return visited


print(dfs(graph, 'A'))
