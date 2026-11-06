from collections import deque

def next_states(state):
    x, y = state
    pour_to_3 = min(x, 3 - y)
    pour_to_4 = min(y, 4 - x)

    states = [
        (4, y),
        (x, 3),
        (0, y),
        (x, 0),
        (x - pour_to_3, y + pour_to_3),
        (x + pour_to_4, y - pour_to_4)
    ]

    return [s for s in states if s != state]

def bfs():
    start = (0, 0)
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        state = path[-1]

        if 2 in state:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state in next_states(state):
            if next_state not in visited:
                queue.append(path + [next_state])

    return []

def dfs():
    start = (0, 0)
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        state = path[-1]

        if 2 in state:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state in next_states(state):
            if next_state not in visited:
                stack.append(path + [next_state])

    return []

print("BFS:")
for state in bfs():
    print(state)

print("DFS:")
for state in dfs():
    print(state)
