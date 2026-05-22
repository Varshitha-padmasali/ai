# Program to perform Depth First Search (DFS)
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors
start = input("Enter starting node: ")
visited = set()
print("DFS Traversal:")
dfs(graph, start, visited)