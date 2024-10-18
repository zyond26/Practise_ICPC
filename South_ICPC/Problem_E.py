from collections import defaultdict

def build_ancestor_graph(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    return graph

def is_ancestor(graph, x, y):
   
    visited = set()
    def dfs(node):
        visited.add(node)
        if node == y:
            return True
        for child in graph[node]:
            if child not in visited:
                if dfs(child):
                    return True
        return False

    return dfs(x)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
T = int(input())
queries = [tuple(map(int, input().split())) for _ in range(T)]

graph = build_ancestor_graph(n, edges)

for x, y in queries:
    if is_ancestor(graph, x, y):
        print("Yes")
    else:
        print("No")
