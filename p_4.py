from collections import deque


def get_valid_moves(state, num_disks, num_pegs=3):
    legal_moves = []

    # Find the top disk on each peg
    top_disks = {peg: -1 for peg in range(num_pegs)}

    # Disk 0 = largest, Disk n-1 = smallest
    for disk in range(num_disks - 1, -1, -1):
        top_disks[state[disk]] = disk

    # Generate valid moves
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


# ---------------- MAIN ----------------

n = int(input("Enter number of disks: "))

print("\nEnter the starting peg for each disk")
print("(A = 0, B = 1, C = 2)")
print("Enter from LARGEST disk to SMALLEST disk.\n")

initial = []

for i in range(n, 0, -1):
    peg = int(input(f"Disk {i}: "))
    initial.append(peg)

initial_state = tuple(initial)
goal_state = tuple([2] * n)  # All disks on Peg C

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
