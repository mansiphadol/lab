#include <iostream>
#include <string>
#include <vector>
#include <cmath>

// Function to check if there is a clear winner in the board position
bool hasWinner(const std::string& boardPosition) {
    // Check rows
    int score;
    for (int i = 0; i < 9; i += 3) {
        if (boardPosition[i] != '0' && boardPosition[i] == boardPosition[i + 1] && boardPosition[i] == boardPosition[i + 2]) {
            score=100;
            cout<<score;
            return true;  // Row has a clear winner
        }
    }

    // Check columns
    for (int i = 0; i < 3; ++i) {
       
        if (boardPosition[i] != '0' && boardPosition[i] == boardPosition[i + 3] && boardPosition[i] == boardPosition[i + 6]) {
            score=100;
            cout<<score;
            return true;  // Column has a clear winner
        }
    }

    // Check diagonals
    if ((boardPosition[0] != '0' && boardPosition[0] == boardPosition[4] && boardPosition[0] == boardPosition[8]) ||
        (boardPosition[2] != '0' && boardPosition[2] == boardPosition[4] && boardPosition[2] == boardPosition[6])) {
            score=100;
            cout<<score;
            
        return true;  // Diagonal has a clear winner
    }

    return false;  // No clear winner found
}

// Function to check if the board position is valid
bool isValidPosition(const std::string& boardPosition) {
    int countX = 0, countO = 0;

    // Check if the position length is valid
    if (boardPosition.size() != 9) {
        return false;
    }

    for (char ch : boardPosition) {
        if (ch == '1') {
            countX++;
        } else if (ch == '2') {
            countO++;
        } else if (ch != '0') {
            return false;  // Invalid character found
        }
    }

    // Check if the difference in counts of 'X' and 'O' is at most 1
    if (std::abs(countX - countO) > 1) {
        return false;
    }

    // Check if there is no clear winner yet
    if (hasWinner(boardPosition)) {
        return false;
    }

    return true;
}



// Function to convert ternary vector to decimal
int convertToDecimal(const std::string& boardPosition) {
    int decimal = 0;
    int base = 1;

    // Convert the vector to decimal representation
    for (int i = boardPosition.length() - 1; i >= 0; i--) {
        if (boardPosition[i] == '1') {
            decimal += base;
        } else if (boardPosition[i] == '2') {
            decimal += 2 * base;
        }

        base *= 3;
    }

    return decimal;
}

int main() {
    std::string boardPosition;

    std::cout << "Enter the current board position: ";
    std::cin >> boardPosition;

    if (isValidPosition(boardPosition)) {
        std::cout << "The board position is valid." << std::endl;

        // Calculate the decimal equivalent
        int decimal = convertToDecimal(boardPosition);
        std::cout << "Decimal equivalent: " << decimal << std::endl;
    } else {
        std::cout << "Invalid board position!" << std::endl;
    }

    return 0;
}

