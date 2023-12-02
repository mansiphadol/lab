#include <iostream>
#include <vector>
#include <cmath>

// Function to calculate the possible moves based on the current board position
void calculatePossibleMoves(const std::vector<std::vector<int>>& board) {
    int blankRow = -1;
    int blankCol = -1;
    int numRows = board.size();

    // Find the indices of the blank space
    for (int i = 0; i < numRows; ++i) {
        for (int j = 0; j < numRows; ++j) {
            if (board[i][j] == 0) {
                blankRow = i;
                blankCol = j;
                break;
            }
        }
    }

    int difference = std::abs(blankRow - blankCol);

    // Calculate the possible moves based on the difference between row and column indices
    if (difference == 1) {
        std::cout << "Three moves are possible." << std::endl;
    } else if (difference == 2) {
        std::cout << "Two moves are possible." << std::endl;
    } else if (difference == 0) {
        if (blankRow == 0 && blankCol == 0) {
            std::cout << "Two moves are possible." << std::endl;
        } else if (blankRow == 0 && blankCol == 2) {
            std::cout << "Two moves are possible." << std::endl;
        } else if (blankRow == 1 && blankCol == 1) {
            std::cout << "Four moves are possible." << std::endl;
        } else if (blankRow == 2 && blankCol == 0) {
            std::cout << "Four moves are possible." << std::endl;
        } else if (blankRow == 2 && blankCol == 2) {
            std::cout << "Two moves are possible." << std::endl;
        }
    }
}

int main() {
    std::vector<std::vector<int>> board = {
        {1, 2, 3},
        {4, 0, 5},
        {6, 7, 8}
    };

    calculatePossibleMoves(board);

    return 0;
}
