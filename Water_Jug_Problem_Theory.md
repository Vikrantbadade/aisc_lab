# Water Jug Problem Using BFS and DFS

## Aim
To implement the Water Jug problem using Breadth-First Search (BFS) and Depth-First Search (DFS).

## Theory
Two unmarked jugs are available:
- A 4-litre jug.
- A 3-litre jug.

Both jugs are initially empty. The objective is to measure exactly 2 litres in either jug.

The allowed operations are:
1. Fill a jug completely.
2. Empty a jug completely.
3. Pour water from one jug into the other until the source jug is empty or the destination jug is full.

A state is represented as `(x, y)`, where `x` is the amount of water in the 4-litre jug and `y` is the amount of water in the 3-litre jug. The initial state is `(0, 0)`. A goal state is any state where `x = 2` or `y = 2`.

### Breadth-First Search (BFS)
BFS explores states level by level. It uses a queue and finds the shortest solution when every operation has equal cost.

### Depth-First Search (DFS)
DFS explores one path as deeply as possible before backtracking. It uses a stack and does not guarantee the shortest solution.

## Difference Between BFS and DFS

| BFS | DFS |
|---|---|
| Explores states level by level. | Explores one path deeply before backtracking. |
| Uses a queue. | Uses a stack. |
| Finds the shortest path when all steps have equal cost. | Does not guarantee the shortest path. |
| Usually requires more memory. | Often requires less memory. |

## Result
The Water Jug problem is solved using BFS and DFS. Both algorithms find a state in which one of the jugs contains exactly 2 litres.
