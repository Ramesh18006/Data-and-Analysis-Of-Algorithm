#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size of the matrix (n): ";
    cin >> n;
    int matrix[10][10];  // assuming max 10x10 for simplicity
    cout << "Enter the elements of the " << n << " x " << n << " matrix:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "Element [" << i+1 << "][" << j+1 << "]: ";
            cin >> matrix[i][j];
        }
    }

    // It Displays the matrix 
    cout << "\nThe matrix you entered is:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }

    // Get i and j from user
    int row, col;
    cout << "\nEnter the row number (i): ";
    cin >> row;
    cout << "Enter the column number (j): ";
    cin >> col;

    // It Checks for valid indixes and print the element
    if (row >= 1 && row <= n && col >= 1 && col <= n) {
        cout << "\nThe value at position (" << row << ", " << col << ") is: " 
             << matrix[row-1][col-1] << endl;
    } else {
        cout << "\nInvalid position! Please enter values between 1 and " << n << "." << endl;
    }

    return 0;
}
