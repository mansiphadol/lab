import heapq

class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0 if parent is None else parent.depth + 1

    def __lt__(self, other):
        return self.depth + self.heuristic() < other.depth + other.heuristic()

    def heuristic(self):
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row, col = divmod(self.state[i][j] - 1, 3)
                    total_distance += abs(row - i) + abs(col - j)
        return total_distance

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_possible_moves(blank_row, blank_col):
    moves = []
    if blank_row > 0:
        moves.append((-1, 0))
    if blank_row < 2:
        moves.append((1, 0))
    if blank_col > 0:
        moves.append((0, -1))
    if blank_col < 2:
        moves.append((0, 1))
    return moves

def astar_search(initial_state, goal_state):
    open_list = []
    closed_list = set()

    start_node = Node(initial_state)
    goal_node = Node(goal_state)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(tuple(map(tuple, current_node.state)))

        if current_node.state == goal_node.state:
            path = []
            while current_node.parent is not None:
                path.append(current_node.move)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        blank_row, blank_col = get_blank_position(current_node.state)
        possible_moves = get_possible_moves(blank_row, blank_col)

        print("Open List:", [node.state for node in open_list])
        print("Closed List:", [node for node in closed_list])
        print("------------------------")

        for move_row, move_col in possible_moves:
            new_row, new_col = blank_row + move_row, blank_col + move_col
            new_state = [list(row) for row in current_node.state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            new_node = Node(new_state, current_node, (move_row, move_col))

            if tuple(map(tuple, new_node.state)) in closed_list:
                continue

            heapq.heappush(open_list, new_node)

    return None  # No path found

# Example usage
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
path = astar_search(initial_state, goal_state)
print("Path:", path)
