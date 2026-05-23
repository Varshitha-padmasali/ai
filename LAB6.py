






































from queue import PriorityQueue
def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start])) #cost,current node,path
    visited = set()
    while not pq.empty():
        cost, node, path = pq.get()
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path, cost
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                pq.put((cost + weight, neighbor, path + [neighbor]))
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
start = 'A'
goal = 'G'
path, cost = uniform_cost_search(graph, start, goal)
print("Shortest Path:", path)
print("Total Cost:", cost)
