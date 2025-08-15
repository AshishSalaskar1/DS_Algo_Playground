### Some Thoughts


#### 1. When to use BFS vs Djikstras
- Whenever you need to find SHORTEST PATH and no weights -> BFS
- If weights -> Dijkstras

#### 2. Cycles in Djikstras, Bellman Ford
| Algorithm         | Handles Cycles? | Condition to Stop Revisiting a Node | Needs `visited` Set? | Notes |
|-------------------|----------------|--------------------------------------|----------------------|-------|
| Dijkstra's        | Yes (no negative edges) | Only revisit if a shorter distance is found; popping from PQ ensures shortest path is final | No | Cycles with positive weights are fine |
| Bellman–Ford      | Yes (can handle negative edges, no negative cycles) | Only relax edges if shorter distance is found | No | Runs for `V-1` iterations; detects negative cycles |
| Floyd–Warshall    | Yes (negative edges OK, no negative cycles) | Iterative DP; no concept of "revisit" | No | Computes all-pairs shortest paths |
| BFS (unweighted)  | Yes (if unweighted graph) | Visit once and mark `visited` | Yes | Avoids infinite loops by marking visited nodes |

  - Why Dijstras work for positive cycles and not for negative ones?
    - In Dijstras, you dont have a VIS set but YOU DONT visit a node `IF ITS DIST IS NOT LESSER`.
    - So with +ve cycles, the dist to nodes in cycle will always be more and hence Dikjstras wont visit it
    - BUT, with -ve weights the nodes in cycle may have lesser distance n hence it wont work for -ve weighted cycles
