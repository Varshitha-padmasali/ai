from queue import PriorityQueue
def a_star(graph, heuristic, start, goal):
    pq = PriorityQueue()
    pq.put((0 + heuristic[start], 0, start, [start]))
    visited = set()
    while not pq.empty():
        f, g, node, path = pq.get()
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path, g
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                pq.put((new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 1,
    'G': 0
}
start = 'A'
goal = 'G'
path, cost = a_star(graph, heuristic, start, goal)
print("Optimal Path:", path)
print("Total Cost:", cost)