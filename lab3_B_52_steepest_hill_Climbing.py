import random

# Goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heuristic function (number of misplaced tiles)
def heuristic(state):
    misplaced = sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j])
    return misplaced

# Generate a random initial state
def generate_initial_state():
    numbers = list(range(9))
    random.shuffle(numbers)
    return [numbers[i:i+3] for i in range(0, 9, 3)]

# Get neighbors by swapping the blank space (0) with adjacent tiles
def get_neighbors(state):
    neighbors = []
    i, j = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)
    
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < 3 and 0 <= y < 3:
            neighbor = [row[:] for row in state]
            neighbor[i][j], neighbor[x][y] = neighbor[x][y], neighbor[i][j]
            neighbors.append(neighbor)
    
    return neighbors

def steepest_hill_climbing(initial_state, max_iterations):
    current_state = initial_state
    current_cost = heuristic(current_state)
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current_state)
        neighbors_costs = [heuristic(neighbor) for neighbor in neighbors]
        best_neighbor_cost = min(neighbors_costs)
        
        if best_neighbor_cost < current_cost:
            current_cost = best_neighbor_cost
            current_state = neighbors[neighbors_costs.index(best_neighbor_cost)]
        else:
            break  # No better neighbor found
    
    return current_state, current_cost

# Example usage
initial_state = generate_initial_state()
max_iterations = 100

best_state, best_cost = steepest_hill_climbing(initial_state, max_iterations)

print("Initial State:")
for row in initial_state:
    print(row)

print("\nBest State:")
for row in best_state:
    print(row)

print("\nMinimum Heuristic Cost:", best_cost)
