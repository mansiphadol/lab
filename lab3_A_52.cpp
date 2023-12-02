#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cstdlib>

using namespace std;

const int N = 3;

const vector<vector<int>> goalState = {
    {1, 2, 3},
    {8, 0, 4},
    {7, 6, 5}
};

struct PuzzleState {
    vector<vector<int>> state;
    int cost;
};

int calculateCost(const vector<vector<int>>& state) {
    int cost = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (state[i][j] != goalState[i][j] && state[i][j] != 0) {
                ++cost;
            }
        }
    }
    return cost;
}

void printState(const vector<vector<int>>& state) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << state[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

vector<vector<int>> generateNeighbor(const vector<vector<int>>& state, int row, int col, int newRow, int newCol) {
    vector<vector<int>> neighbor = state;
    swap(neighbor[row][col], neighbor[newRow][newCol]);
    return neighbor;
}

PuzzleState hillClimbing(const vector<vector<int>>& initial, int maxIterations) {
    PuzzleState current = {initial, calculateCost(initial)};
    int iterations = 0;
    
    cout << "Initial State:" << endl;
    printState(current.state);
    cout << "----------------------------------------" << endl;
    
    while (iterations < maxIterations) {
        vector<vector<int>> bestNeighbor;
        int bestNeighborCost = current.cost;
        
        for (int row = 0; row < N; ++row) {
            for (int col = 0; col < N; ++col) {
                if (current.state[row][col] == 0) {
                    int moves[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Up, Down, Left, Right
                    
                    for (const auto& move : moves) {
                        int newRow = row + move[0];
                        int newCol = col + move[1];
                        
                        if (newRow >= 0 && newRow < N && newCol >= 0 && newCol < N) {
                            vector<vector<int>> neighborState = generateNeighbor(current.state, row, col, newRow, newCol);
                            int neighborCost = calculateCost(neighborState);
                            
                            if (neighborCost < bestNeighborCost) {
                                bestNeighbor = neighborState;
                                bestNeighborCost = neighborCost;
                            }
                        }
                    }
                }
            }
        }
        
        if (bestNeighborCost >= current.cost) {
            break; // No better neighbor found, exit
        }
        
        current.state = bestNeighbor;
        current.cost = bestNeighborCost;
        
        iterations++;
        
        cout << "Iteration " << iterations << " - Cost: " << bestNeighborCost << endl;
        printState(current.state);
        cout << "----------------------------------------" << endl;
    }
    
    return current;
}

int main() {
    srand(time(nullptr));
    
    vector<vector<int>> initialState = {
        {1, 2, 4},
        {8,0, 5},
        {7, 6, 3}
    };
    cout << "Initial State Cost: " << calculateCost(initialState) << endl; // Calculate and print the cost
    cout << "----------------------------------------" << endl;
    
    PuzzleState finalPuzzleState = hillClimbing(initialState, 100);
    
    cout << "Final State:" << endl;
    printState(finalPuzzleState.state);
    cout << "Cost: " << finalPuzzleState.cost << endl;
    
    return 0;
}
