N = 8


def printSolution(board):
    print("\nOne Possible Solution:\n")
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solveNQUtil(board, col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQUtil(board, col + 1):
                return True

            board[i][col] = 0

    return False


def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


solveNQ()





























'''
Algorithm: 8 Queens Problem using Backtracking

1. Start the program.
2. Initialize an 8×8 chessboard with all positions set to 0.
3. Place 8 queens on the chessboard such that no two queens attack each other.
4. Start placing queens column by column using a recursive function.
5. For each column, check every row to find a safe position for placing a queen.
6. Check whether the selected position is safe by verifying:
   a) No queen exists in the same row on the left side.
   b) No queen exists in the upper-left diagonal.
   c) No queen exists in the lower-left diagonal.
7. If the position is safe:
   a) Place the queen by setting the position to 1.
   b) Recursively move to the next column.
8. If all 8 columns are successfully filled, return True, indicating that a solution is found.
9. If no valid position is available, remove the previously placed queen (backtracking) by resetting its position to 0.
10. Continue trying other positions until a valid arrangement is found.
11. If no solution exists, display "Solution does not exist".
12. Otherwise, display the chessboard with Q representing queens and . representing empty positions.
13. Stop the program.

'''
