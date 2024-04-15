"""
Intuition: Sort of like Dijstras + DP
- Do normal djiktras, but maintain a ways array
- ways[i] = no of ways to reach node i from src, in least distance

IMP NOTE ON PATHS:
- (udist, u) -> (u->v) -> dist from src->v is best
- How many ways you can reach from src->v IS NOT 1 (You might visit from more than 1 paths and still reach V)
- Then, ways_to_reach(v) = ways_to_reach(u) (if you can reach u in 10 ways from src, then since u->v you can reach v also 10 ways)
- here ways_to_reach(i) -> no of ways to reach "i" from "src" node

- Update ways logic
# ways_to_reach[V] -> ways_to_reach[U] (if u reach u, then surely you can reach v) 
# if there is only 1 path to reach v, then ways_to_reach(u) will also be 1 [BUT MULTIPLE CAN BE THERE]

1.Found path which is least but already found -> INCREMENT WAYS
- ways[v] = (ways[v]+ways[u]) -> wkt ways_to_reach(v) = ways_to_reach(u)

2. Newly found shortest path -> SET WAYS[v]
- ways[v] = ways[u] # reset/set count (newly found path is better than "n" previous best paths)

"""

from queue import PriorityQueue

class Solution:
    def create_adj(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        return adj

    def countPaths(self, V: int, roads: List[List[int]]) -> int:
        src, dest = 0, V-1
        adj = self.create_adj(V, roads)

        dist = [float("inf") for _ in range(V)]
        ways = [0 for _ in range(V)]
        dist[src] = 0
        ways[0] = 1 # you can visit 0 from itself 1 ways

        pq = PriorityQueue()
        pq.put((0, src))

        while pq.qsize() != 0:
            udist, u = pq.get()

            for v, wt in adj[u]: # all nbrs of U
                # existing ways + ways to reach v (ways to reach u)
                if udist+wt == dist[v]: # you found another best way to reach "v" (same least distance)
                    ways[v] = (ways[v]+ways[u])%(10**9+7)

                # ways_to_reach[V] -> ways_to_reach[U] (if u reach u, then surely you can reach v) 
                # if there is only 1 path to reach v, then ways_to_reach(u) will also be 1 [BUT MULTIPLE CAN BE THERE]
                if udist+wt < dist[v]: # found shorter way to reach "v"
                    ways[v] = ways[u] # reset/set count to(newly found path is better than "n" previous best paths)
                    dist[v] = udist + wt
                    pq.put((udist+wt, v))


        return ways[dest]