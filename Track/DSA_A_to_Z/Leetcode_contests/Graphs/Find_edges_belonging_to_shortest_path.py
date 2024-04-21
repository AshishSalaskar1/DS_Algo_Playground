"""
SOLUTION 1: Sort of Brute Force
- Find shortest path from SRC -> DEST using Dijkstras
- Use DFS to print all possible paths from SRC->DEST but having total_len <= MIN_DIST_RES_FROM_DIJSKTRAS

SOLUTION 2: Two way Djikstras
- DIJKSTRAS(0 -> N-1) = res1
- DIJKSTRAS(N-1 -> 0) = res2
- RES = res1[v-1]

- Give edge u-> v (wt), its part of shortest path from SRC->DEST if
 1. shortest_dist[0 -> u] + wt + shortest_dist[(V-1) -> v] == RES (SRC -> U -> V -> DEST)
 2. shortest_dist[0 -> v] + wt + shortest_dist[(V-1) -> u] == RES (SRC <- U <- V <- DEST)
 If either (1) or (2) is True, add edge to shortest path
 - You need second condition here since its a directional graph


"""

from queue import PriorityQueue

class Solution:
    def build_adj(self, edges, V):
        adj = [[] for _ in range(V)]
        for src, dest, wt in edges:
            adj[src].append((dest, wt))
            adj[dest].append((src, wt))

        return adj 

    def dijkstra(self, edges: List[List[int]], V: int, src: int):
        adj = self.build_adj(edges, V)
        pq = PriorityQueue()

        # add src node to PQ
        pq.put((0,src))

        dist = [float("inf") for _ in range(V)]
        dist[src] = 0

        while pq.qsize() != 0:
            udist, u = pq.get() # pick node at least distance in PQ from src

            # visit all nbrs of node and update
            for v, wt in adj[u]:
                if udist + wt < dist[v]: # shorter path found  from src->nbr
                    dist[v] = udist+wt
                    pq.put((udist+wt, v))

        # self.solve(adj, 0, V-1, dist[V-1])
        return dist
    
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        d_from_src = self.dijkstra(edges, n, 0)
        d_from_dest = self.dijkstra(edges, n, n-1)
        print(d_from_src,d_from_dest)
        min_dist = d_from_src[-1]
        res = []
        for u,v,wt in edges:
            # this is part of shortest path
            if (d_from_src[u] + wt + d_from_dest[v] == min_dist) or \
            (d_from_src[v] + wt + d_from_dest[u] == min_dist):
                res.append(True)
            else: # not part of shortest path
                res.append(False)
        
        return res

    
    
    # def dfs(self, adj, node, dest, curlen, max_path, paths):
    #     paths = paths.copy()
    #     paths.append(node)
        
    #     if node == dest:
    #         self.mega_res.append(paths)
    #         print("MEGA RES:",paths)
        
    #     for nbr, wt in adj[node]:
    #         if nbr not in self.vis and curlen+wt <= max_path:
    #             # print(f"visiting {nbr} from {node}")
    #             self.vis.add(nbr)
    #             self.dfs(adj, nbr, dest, curlen+wt, max_path, paths)
    #             self.vis.remove(nbr)
                 
    
    # def solve(self, adj, src, dest, max_path):
    #     print(src, dest, max_path)
    #     self.vis = set()
    #     self.path = []
    #     self.mega_res = []
    #     self.dfs(adj,src,dest, 0, max_path, [])


    # def findAnswerBruteForce(self, n: int, edges: List[List[int]]) -> List[bool]:
    #     res_dist = self.dijkstra(edges, n, len(edges),0)
    #     res = set()
    #     bool_res = []
        
    #     paths = set()
    #     for val_path in self.mega_res:
    #         for i in range(0,len(val_path)-1):
    #             paths.add((val_path[i], val_path[i+1]))
    #             paths.add((val_path[i+1], val_path[i]))
    #     print(paths)
            
            
    #     for u,v,wt in edges:
    #         if (u,v) in paths:
    #             # print((u,v))
    #             bool_res.append(True)
    #         else:
    #             bool_res.append(False)
        
    #     return bool_res
            
        
        
        