# Program to perform Breadth First Search (BFS)
from collections import deque
# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
# Main Program
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors
start = input("Enter starting node: ")
print("BFS Traversal:")
bfs(graph, start)