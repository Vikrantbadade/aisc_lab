# Missionaries and Cannibals Problem

## Aim
To implement state-space search for the Missionaries and Cannibals problem using Python.

## Theory
Three missionaries and three cannibals are on one side of a river. They must cross the river using a boat that can carry at most two people.

Cannibals must never outnumber missionaries on either riverbank when missionaries are present. The boat must carry at least one person during every crossing.

A state is represented as `(M, C, B)`:
- `M` represents the number of missionaries on the left bank.
- `C` represents the number of cannibals on the left bank.
- `B` represents the boat position: `0` for the left bank and `1` for the right bank.

The initial state is `(3, 3, 0)` and the goal state is `(0, 0, 1)`.

Breadth-First Search (BFS) explores the possible states level by level. It uses a queue and avoids visiting the same state more than once. Since every crossing has equal cost, BFS finds a solution with the minimum number of crossings.

## Result
The Missionaries and Cannibals problem is solved using state-space search. All six people reach the opposite bank without violating the safety condition.
