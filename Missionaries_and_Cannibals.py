from collections import deque

def valid(state):
    m, c, boat = state
    mr, cr = 3 - m, 3 - c
    return (
        0 <= m <= 3 and 0 <= c <= 3
        and (m == 0 or m >= c)
        and (mr == 0 or mr >= cr)
    )

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

    queue = deque([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()

        if state == goal:
            break

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                next_state = (m - dm, c - dc, 1)
            else:
                next_state = (m + dm, c + dc, 0)

            if valid(next_state) and next_state not in parent:
                parent[next_state] = state
                queue.append(next_state)

    path = []
    state = goal

    while state is not None:
        path.append(state)
        state = parent[state]

    print("Missionaries and Cannibals:")
    for state in reversed(path):
        print(state)

solve()
