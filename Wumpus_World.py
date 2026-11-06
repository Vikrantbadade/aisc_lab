from collections import deque

SIZE = 4
START = (1, 1)
WUMPUS = (1, 3)
GOLD = (2, 3)
PITS = {(3, 1), (3, 3), (4, 4)}

def adjacent(position):
    x, y = position
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

def inside(position):
    x, y = position
    return 1 <= x <= SIZE and 1 <= y <= SIZE

def get_percepts(position):
    nearby = adjacent(position)
    percepts = []

    if WUMPUS in nearby:
        percepts.append("Stench")
    if any(pit in nearby for pit in PITS):
        percepts.append("Breeze")
    if position == GOLD:
        percepts.append("Glitter")

    return percepts

def find_path(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        position = path[-1]

        if position == goal:
            return path

        for next_position in adjacent(position):
            if (
                inside(next_position)
                and next_position not in PITS
                and next_position != WUMPUS
                and next_position not in visited
            ):
                visited.add(next_position)
                queue.append(path + [next_position])

    return []

def display_grid(agent):
    for y in range(SIZE, 0, -1):
        row = []
        for x in range(1, SIZE + 1):
            position = (x, y)

            if position == agent:
                cell = "A"
            elif position == WUMPUS:
                cell = "W"
            elif position in PITS:
                cell = "P"
            elif position == GOLD:
                cell = "G"
            else:
                cell = "."

            row.append(cell)

        print(" ".join(row))

def run():
    print("Wumpus World")
    print("A = Agent, W = Wumpus, P = Pit, G = Gold")
    display_grid(START)

    path_to_gold = find_path(START, GOLD)

    if not path_to_gold:
        print("Gold cannot be reached.")
        return

    print("\nPath to gold:")
    for position in path_to_gold:
        print(position, get_percepts(position))

    print("\nGold collected!")
    path_to_exit = find_path(GOLD, START)

    print("\nPath to exit:")
    for position in path_to_exit:
        print(position, get_percepts(position))

    print("\nAgent exited the cave safely.")

run()
