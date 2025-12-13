# Advanced Graph Algorithms - Quick Reference

### TODOLIST
- [x] SCC - Kosaraju [YT Video](https://www.youtube.com/watch?v=R6uoSjZ2imo)
- [x] Bridges - Tarzan [YT Video](https://www.youtube.com/watch?v=qrAub5z8FeA)
- [ ] Articulation Point [YT Video](https://www.youtube.com/watch?v=j1QDfU21iZk)
- [x] Eulers Path/Circuit [YT Video](https://www.youtube.com/watch?v=iwUJeJ8BZM4&t=13s)
- [ ] Hamiltonian Path/Circuit 
- [ ] Dinics Algo - Flow 
- [ ] Hopcroft–Karp - Bipartite Graphs 


## 1. Strongly Connected Components (Kosaraju's Algorithm)

**Use:** Find groups of nodes where every pair has paths to each other (social network clusters, dependency analysis, deadlock detection)

**How It's Done:**
1. **Get Order:** DFS on original graph, store finish times in stack
2. **Reverse Graph:** Reverse all edge directions
3. **DFS on Reversed:** Pop nodes from stack, run DFS on reversed graph - each new DFS discovers one SCC

**Key Insight:** 
- SCCs act as islands connected by bridges
- Reversing edges reverses bridge direction, but SCC internal connectivity remains
- Finish-time ordering ensures we process SCCs in correct topological order

**Tips:**
- Works on disconnected graphs - iterate through all unvisited nodes in step 1
- Stack gives reverse topological order of SCCs
- Within each SCC, all nodes remain mutually reachable even after reversal
- Use `store_order` flag to differentiate between two DFS phases
- Time: O(V + E), Space: O(V)
- Useful for: Finding cycles, simplifying graphs, optimization problems

---
## 2. Bridges (Tarzan's Algorithm)

**Use:** Find critical edges whose removal increases connected components (network vulnerability analysis)

**How It's Done:**
- DFS with two time arrays: `vistime[node]` (visit time) and `low[node]` (earliest reachable ancestor)
- For edge `node → nbr`: if `low[nbr] > vistime[node]` → it's a bridge
- Logic: No alternative path exists to reach ancestors, so removing this edge disconnects the graph

**Tips:**
- Exclude parent when updating `low[node]` to avoid false negatives
- For visited neighbors: use `low[node] = min(low[node], low[nbr])`
- For already seen neighbors: use `low[node] = min(low[node], vistime[nbr])`
- Time: O(V + E), Space: O(V)

---

## 3. Euler's Path/Circuit (Hierholzer's Algorithm)

**Use:** Find path/circuit visiting every **edge** exactly once (route planning, puzzles, circuit design)

**How It's Done:**
- Check degree conditions first (see table below)
- Use modified DFS: remove edges as you traverse, no seen set needed
- Build path in reverse by appending nodes after exploring all their edges
- Key difference from normal DFS: allows revisiting nodes, focuses on edges

### Conditions & Start/End Selection

| TYPE | GRAPH | CONDITIONS | START | END |
|------|-------|------------|-------|-----|
| **CIRCUIT** | Undirected | All vertices have **even** degree | Any vertex with edges | Same as start |
| **CIRCUIT** | Directed | All vertices: **indegree = outdegree** | Any vertex with edges | Same as start |
| **PATH** | Undirected | **Exactly 2** vertices have **odd** degree; rest even | Either odd-degree vertex | The other odd-degree vertex |
| **PATH** | Directed | Exactly 1 vertex: **outdegree = indegree + 1** (start)<br>Exactly 1 vertex: **indegree = outdegree + 1** (end)<br>Rest: **indegree = outdegree** | Vertex with outdegree = indegree + 1 | Vertex with indegree = outdegree + 1 |

**No Euler Path/Circuit Exists:**
- Undirected: More than 2 odd-degree vertices
- Directed: Any vertex has `|indegree - outdegree| > 1`, or multiple start/end candidates

**Tips:**
- For **undirected**: Remove **both** directions when taking an edge: `adj[u].remove(v)` AND `adj[v].remove(u)`
- For **directed**: Only remove `adj[u].remove(v)`
- Always use deep copy of adjacency list before running Hierholzer's
- Result path is reversed, so return `path[::-1]`
- Graph must be connected (weakly for directed)
- Time: O(E), Space: O(E)

---


## At-a-Glance Comparison

| Algorithm | Primary Use | When to Use |
|-----------|-------------|-------------|
| **Bridges (Tarzan's)** | Find critical edges | Network reliability, identifying single points of failure, graph connectivity analysis |
| **Euler's Path/Circuit** | Visit all edges once | Route optimization (mail delivery, snow plowing), circuit drawing without lifting pen, DNA sequencing |
| **Kosaraju's SCC** | Find mutually reachable groups | Social network analysis, dependency resolution, compiler optimization, finding cycles in directed graphs |

**Key Differences:**
- **Bridges:** Focuses on edge criticality
- **Euler's:** Focuses on edge traversal (visits every edge once, can revisit nodes)
- **Kosaraju's:** Focuses on node grouping (mutual reachability in directed graphs)
- **Hamiltonian** (for reference): Visits every **node** once, no edge constraint
