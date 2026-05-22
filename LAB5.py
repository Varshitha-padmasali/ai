# Program to perform Iterative Deepening Search (IDS)
# Depth Limited Search
def dls(graph, node, goal, limit, visited):
    if node == goal:
        return True
    if limit <= 0:
        return False
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, goal, limit - 1, visited):
                return True
    return False
# Iterative Deepening Search
def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        print("Depth Limit:", depth)
        if dls(graph, start, goal, depth, visited):
            print("Goal found at depth", depth)
            return True
    return False
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors
start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))
if not ids(graph, start, goal, max_depth):
    print("Goal not found")