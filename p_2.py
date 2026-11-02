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
Algorithm: Grid Navigation

1. Initialize a 3×3 grid with a starting position (S), goal position (G), and obstacle (X).
2. Set the starting position to (0,0) and the goal position to (2,2).
3. Create an empty list to store visited cells.
4. Start a loop and add the current position to the visited list if it is not already visited.
5. Check whether the current position is equal to the goal position. If yes, stop the loop.
6. Check for valid movement in the following order:
   a) Move Right
   b) Move Down
   c) Move Left
   d) Move Up
7. Before moving, check that the next cell is within the grid, is not an obstacle, and has not been visited.
8. If a valid move is found, update the current position.
9. If no valid move is available, terminate the loop.
10. Finally, display all the visited cells.
'''
