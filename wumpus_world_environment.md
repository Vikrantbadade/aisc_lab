# Wumpus World Environment

## Aim
Model the Wumpus World as a 4x4 grid and generate percepts for an agent.

## Theory
Wumpus World is a classic AI testbed for **knowledge-based agents** and **logical reasoning** in a partially observable environment.

### Components
- **Grid:** 4x4 cave, cells indexed (x, y), agent starts at (1,1)
- **Wumpus:** one monster, kills the agent if it enters its cell
- **Pits:** deadly cells that trap the agent
- **Gold:** the goal object
- **Agent:** moves, grabs gold, shoots one arrow, exits at (1,1)

### Percepts
| Percept | Meaning |
|---|---|
| Stench | Wumpus in an adjacent cell |
| Breeze | Pit in an adjacent cell |
| Glitter | Gold in current cell |
| Bump | Agent hit a wall |
| Scream | Wumpus has been killed |

Adjacent means up, down, left, right (no diagonals).

### PEAS Description
- **Performance:** +1000 for exiting with gold, -1000 for dying, -1 per action, -10 for using the arrow
- **Environment:** 4x4 grid with Wumpus, pits, gold
- **Actuators:** move forward, turn left/right, grab, shoot, climb
- **Sensors:** stench, breeze, glitter, bump, scream

### Environment Properties
- Partially observable (agent only senses nearby cells)
- Deterministic
- Sequential
- Static
- Discrete
- Single agent

### Reasoning
- No breeze/stench in a cell means all its neighbours are safe.
- Breeze means at least one neighbouring pit; stench means a neighbouring Wumpus.
- Propositional logic with inference (e.g. resolution) lets the agent deduce safe cells.

## Algorithm
1. Place Wumpus, pits, gold and agent.
2. Compute adjacent cells with wall checks.
3. On each move, update position and check for pit/Wumpus.
4. Generate percepts from the current cell's neighbours.

## Sample Output
```
Start (1, 1) {'Stench': False, 'Breeze': False, 'Glitter': False, 'Bump': False, 'Scream': False}
(2, 1) ['Breeze']
(2, 2) []
(2, 3) ['Stench', 'Breeze', 'Glitter']
```

## Conclusion
The environment correctly generates percepts, which an agent can use to reason about safe cells and find the gold.
