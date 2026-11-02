from collections import deque


def get_valid_moves(state, num_disks, num_pegs=3):
    legal_moves = []

    top_disks = {peg: -1 for peg in range(num_pegs)}

    for disk in range(num_disks - 1, -1, -1):
        top_disks[state[disk]] = disk

    for source in range(num_pegs):
        if top_disks[source] != -1:
            source_disk = top_disks[source]

            for destination in range(num_pegs):
                if source != destination:
                    dest_disk = top_disks[destination]

                    if dest_disk == -1 or dest_disk > source_disk:
                        legal_moves.append((source, destination, source_disk))

    return legal_moves


def apply_move(state, move):
    new_state = list(state)
    source, destination, disk = move
    new_state[disk] = destination
    return tuple(new_state)


def solve_hanoi_bfs(initial_state, goal_state, num_disks):
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for move in get_valid_moves(current_state, num_disks):
            next_state = apply_move(current_state, move)

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))

    return None



n = int(input("Enter number of disks: "))

print("\nEnter the starting peg for each disk")
print("(A = 0, B = 1, C = 2)")
print("Enter from LARGEST disk to SMALLEST disk.\n")

initial = []

for i in range(n, 0, -1):
    peg = int(input(f"Disk {i}: "))
    initial.append(peg)

initial_state = tuple(initial)
goal_state = tuple([2] * n)  

solution = solve_hanoi_bfs(initial_state, goal_state, n)

peg_names = ["A", "B", "C"]

print("\nInitial State:", initial_state)
print("Goal State   :", goal_state)

if solution:
    print(f"\nMinimum Moves = {len(solution)}\n")

    for step, (src, dest, disk) in enumerate(solution, start=1):
        disk_number = n - disk
        print(
            f"Step {step}: Move Disk {disk_number} from Peg {peg_names[src]} to Peg {peg_names[dest]}"
        )
else:
    print("No solution exists.")























'''
Algorithm: Tower of Hanoi using BFS

1. Start the program.
2. Import the deque module to implement a queue.
3. Accept the number of disks from the user.
4. Accept the starting peg of each disk (A, B, or C), from largest to smallest.
5. Store the initial state as a tuple and set the goal state with all disks on Peg C.
6. Find the top disk of each peg to identify which disks can be moved.
7. Generate all possible valid moves by checking the following conditions:
   a) The destination peg must be empty or contain a larger disk.
   b) A larger disk cannot be placed on a smaller disk.
8. Apply each valid move by transferring the disk from the source peg to the destination peg, creating a new state.
9. Initialize a queue with the initial state and an empty path.
10. Create a visited set to avoid exploring previously visited states.
11. Repeat while the queue is not empty:
    a) Remove the first state from the queue.
    b) Check whether the current state matches the goal state.
    c) If yes, return the solution path.
    d) Otherwise, generate all valid moves.
    e) Apply each move to create a new state.
    f) If the new state is not visited, add it to the visited set and queue along with the updated path.
12. If the queue becomes empty without finding the goal, return None.
13. Display the initial state and goal state.
14. If a solution exists, display the minimum number of moves and step-by-step disk movements.
15. Otherwise, display "No solution exists".
16. Stop the program.
'''
