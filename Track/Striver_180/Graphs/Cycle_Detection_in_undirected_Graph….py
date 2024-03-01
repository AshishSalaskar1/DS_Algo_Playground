"""
Link: https://www.codingninjas.com/studio/problems/detect-cycle-in-an-undirected-graph-_758967

Problem statement
Given an undirected graph of 'V' vertices and 'E' edges. Return true if the graph contains a cycle or not, else return false.

Note:
- There are no self-loops(an edge connecting the vertex to itself) in the given graph.
Example:
- 0 based indexing
- Given N=3, M =2, and edges are (1, 2) and (2, 3), with nodes 1, 2, and 3.
  We return false because the given graph does not have any cycle.


SOLUTION
- If there are any Cycles, ull visit same node twice  from 2 DIFFERENT PATHS
- Example: 1 <-> 2 <-> 3
    - In this case 1 -> 2, then 2 -> 1|3 [But u wont go visit 1 since u came from there]
    - This way we ignore same paths taken, [So dont consider 1 as loop since its already visited but u came from 1 itself]
   -  visit same node twice only when u reach there from 2 different paths
"""

def detect_cycle(adj):
    V = len(adj)

    # iterate all nodes and do BFS on each
    for i in range(V):
        # (node, where did u visit this from)
        q = [(i, -1)]
        vis = set([i])

        while len(q) != 0:
            curr, parent = q.pop(0)
            for nbr in adj[curr]:
                if nbr not in vis:
                    q.append((nbr, curr))
                    vis.add(nbr)
                # 1 <-> 2 <-> 3
                # nbr is visited already, but u came from this node only
                elif parent != nbr:
                    return True

    return False

v, e = map(int, input().split())
adj = [[] for _ in range(v)]
for _ in range(e):
  src, dest = map(int, input().split())
  adj[src].append(dest)
  adj[dest].append(src)

print(detect_cycle(adj))