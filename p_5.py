from collections import deque

def get_successors(state):
    successors = []
    stacks = [list(stack) for stack in state]

    for i in range(len(stacks)):
        if not stacks[i]:
            continue

        block = stacks[i][-1]

        for j in range(len(stacks)):
            if i == j:
                continue

            new_stacks = [s[:] for s in stacks]
            new_stacks[i].pop()
            new_stacks[j].append(block)

            new_stacks = [tuple(s) for s in new_stacks if s]
            successors.append(tuple(new_stacks))

        new_stacks = [s[:] for s in stacks]
        new_stacks[i].pop()
        new_stacks.append([block])

        new_stacks = [tuple(s) for s in new_stacks if s]
        successors.append(tuple(new_stacks))

    return successors


def bfs(start, goal):
    queue = deque()
    queue.append((start, []))

    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path + [current]

        for nxt in get_successors(current):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [current]))

    return None


def print_state(state):
    print("-" * 25)
    for i, stack in enumerate(state):
        print(f"Stack {i+1}: {list(stack)}")
    print("-" * 25)


start = (('C', 'B', 'A'),)

goal = (('A', 'B', 'C'),)

solution = bfs(start, goal)

if solution:
    print("\nSolution Found!\n")

    for step, state in enumerate(solution):
        print(f"Step {step}")
        print_state(state)

else:
    print("No solution found.")























'''
Algorithm: Block World Problem using Breadth-First Search (BFS)

1. Start the program.
2. Import the deque module to implement a queue.
3. Define the initial state with blocks A, B, and C arranged in a single stack.
4. Define the goal state with the blocks arranged in the required order.
5. Generate all possible successor states by performing the following operations:
   a) Select the top block from each non-empty stack.
   b) Move the selected block onto another existing stack.
   c) Move the selected block to a new separate stack.
   d) Generate a new state after each move.
6. Initialize a queue with the initial state and an empty path.
7. Create a visited set and add the initial state to avoid repeating states.
8. Repeat while the queue is not empty:
   a) Remove the first state from the queue.
   b) Check whether the current state matches the goal state.
   c) If yes, return the solution path.
   d) Otherwise, generate all possible successor states.
   e) If a successor state is not visited, add it to the visited set and queue along with the updated path.
9. If the queue becomes empty without reaching the goal, return None.
10. Display the solution path step by step, showing the arrangement of blocks in each stack.
11. If no solution exists, display "No solution found".
12. Stop the program.
'''
