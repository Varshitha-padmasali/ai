from queue import PriorityQueue
def best_first_search(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start, [start]))
    visited = set()
    while not pq.empty():
        h, node, path = pq.get()
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}
start = 'A'
goal = 'G'
path = best_first_search(graph, heuristic, start, goal)
print("Path found:", path)