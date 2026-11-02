grid = [['s',0,0],
        ['x',0,0],
        [0,0,'g']]

visited = []
row = 0
col = 0
goal = (2,2)

print("Grid Navigation Begins...")

while True:
    if (row,col) not in visited:
        visited.append((row,col))
    print("Current position : ",(row,col))
    print("Visited : ",visited)

    if (row,col) == goal:
        print("Goal Completed...")
        break

    moved = False

    if col+1 < 3 and grid[row][col+1] != 'x' and (row,col+1) not in visited:
        print("Action : MOVE RIGHT")
        col+=1
        moved = True 

    elif row+1 < 3 and grid[row+1][col] != 'x' and (row+1 , col) not in visited :
        print("Action : MOVE DOWN")
        row+=1
        moved = True

    elif col-1 >=0 and grid[row][col-1] != 'x' and (row,col-1) not in visited :
        print("Action : MOVE LEFT")
        col-=1 
        moved = True

    elif row-1 >= 0 and grid[row-1][col] != 'x' and (row-1,col) not in visited:
        print("Action : MOVE UP")
        row-=1
        moved = True

    if not moved:
        print("No valid move available...")
        break

print("Final Visited Cells : ",visited)




























'''
Algorithm: Grid Navigation using Search
Start the program.
Initialize a 3×3 grid with a starting point (S), goal point (G), obstacles (X), and empty cells (0).
Initialize an empty list called visited to store the visited positions.
Set the starting position to row 0 and column 0, and the goal position to (2,2).
Start a while True loop.
Add the current position to the visited list if it is not already visited.
Display the current position and visited cells.
Check whether the current position is equal to the goal position.
If yes, display "Goal Completed" and terminate the loop.
Set moved = False.
Check possible movements in the following order:
Move RIGHT if the next cell is valid, not an obstacle, and not visited.
Otherwise, move DOWN under the same conditions.
Otherwise, move LEFT.
Otherwise, move UP.
Update the row or column according to the movement and set moved = True.
If no valid movement is available, display a message and stop the loop.
Display all the final visited cells.
Stop the program.
'''
