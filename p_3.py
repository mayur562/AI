import heapq


def h(s, goal):
    return sum(
        s[i][j] != goal[i][j] and s[i][j] != "_" for i in range(3) for j in range(3)
    )


def astar(start, goal):
    pq = []
    heapq.heappush(pq, (h(start, goal), 0, start, []))
    open_set = {tuple(map(tuple, start))}
    closed = set()

    while pq:
        f, g, s, path = heapq.heappop(pq)
        key = tuple(map(tuple, s))
        open_set.discard(key)

        if key in closed:
            continue

        closed.add(key)

        if s == goal:
            print("\nSolution found!")
            for step, state in enumerate(path + [s]):
                print("\nStep", step)
                for row in state:
                    print(*row)
            return

        x, y = next((i, j) for i in range(3) for j in range(3) if s[i][j] == "_")

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            a, b = x + dx, y + dy

            if 0 <= a < 3 and 0 <= b < 3:
                t = [r[:] for r in s]
                t[x][y], t[a][b] = t[a][b], t[x][y]

                k = tuple(map(tuple, t))

                if k not in closed and k not in open_set:
                    open_set.add(k)
                    heapq.heappush(pq, (g + 1 + h(t, goal), g + 1, t, path + [s]))

    print("No solution!")


print("Enter start matrix:")
start = [input().split() for _ in range(3)]

print("Enter goal matrix:")
goal = [input().split() for _ in range(3)]

astar(start, goal)
