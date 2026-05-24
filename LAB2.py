import heapq
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def to_tuple(state):
    return tuple(tuple(row) for row in state)
# Generate next states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            # Swap blank tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors
# A* Search Algorithm
def solve_puzzle(start):
    pq = []
    visited = set()
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal_state:
            return path + [current]
        state_tuple = to_tuple(current)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [current])
                )
    return None
# Print puzzle state
def print_state(state):
    for row in state:
        print(row)
    print()
print("Enter initial state (use 0 for blank):")
start_state = []
for i in range(3):
    row = list(map(int, input().split()))
    start_state.append(row)
solution = solve_puzzle(start_state)
if solution:
    print("\nSolution Steps:\n")
    for step in solution:
        print_state(step)
else:
    print("No solution found.")