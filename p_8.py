import math

board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(3):
        print(" " + board[i * 3] + " | " + board[i * 3 + 1] + " | " + board[i * 3 + 2])
        if i < 2:
            print("---|---|---")
    print()


def check_winner(player):
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False


def is_draw():
    return " " not in board


def minimax(is_max):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best


def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1

            if 0 <= pos < 9 and board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Enter a valid number.")


print("Positions are:")
print("1 | 2 | 3")
print("--|---|--")
print("4 | 5 | 6")
print("--|---|--")
print("7 | 8 | 9")

while True:
    print_board()
    human_move()

    if check_winner("X"):
        print_board()
        print("You Win!!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break































'''
Algorithm: Tic-Tac-Toe using Minimax Algorithm

1. Start the program.
2. Import the math module and initialize a 3×3 game board with empty spaces.
3. Define a function to display the Tic-Tac-Toe board.
4. Define a function to check whether a player has won by checking all rows, columns, and diagonals.
5. Define a function to check whether the game is a draw when all positions are filled.
6. Implement the Minimax algorithm to find the best possible move for the AI:
   a) If AI (O) wins, return +1.
   b) If the human player (X) wins, return -1.
   c) If the board is full, return 0.
   d) If it is the AI's turn, select the move with the maximum score.
   e) If it is the human's turn, select the move with the minimum score.
   f) Try each empty position, calculate its score recursively, and undo the move after checking.
7. Define the AI move function:
   a) Check all available positions.
   b) Temporarily place O in each empty position.
   c) Use Minimax to calculate the score.
   d) Select the position with the highest score and place O there.
8. Define the human move function to accept a position between 1 and 9.
9. Validate the user's input and allow only valid empty positions.
10. Display the board and start the game loop.
11. Accept the human player's move and check for a win or draw.
12. If the game is not over, let the AI make its best move.
13. After the AI move, check again for a win or draw.
14. Repeat until a player wins or the game ends in a draw.
15. Display the final result and stop the program.

'''
