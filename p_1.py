environment = {'A' : 'Clean' , 
               'B' : 'Dirty'}

location = 'A'

while True:
    print("Current Location : ",location)
    print("Environment : ",environment)

    if environment['A'] == 'Clean' and environment['B'] == 'Clean':
        print("Goal Achieved Successfully !!! Both Rooms are cleaned...")
        break

    if environment[location] == 'Dirty':
        print("Action : [SUCK]")
        environment[location] = 'Clean'

    else:

        if location == 'A' :
            location = 'B'
        else:
            location = 'A'

    





























### Algorithm: Vacuum Cleaner Agent
'''
1. Start the program.
2. Initialize two rooms, A and B, with their initial states as Clean or Dirty.
3. Set the vacuum cleaner's initial location to room A.
4. Start a `while True` loop.
5. Display the current location and the condition of both rooms.
6. Check whether both rooms are clean:
   - If yes, display the goal-achieved message and stop the loop using `break`.
7. If the current room is Dirty:
   - Perform the SUCK action.
   - Change the room's status to Clean.
8. Otherwise, move the vacuum cleaner to the other room:
   - If it is in A, move to B.
   - If it is in B, move to A.
9. Repeat the process until both rooms become clean.
10. Stop the program.
'''
