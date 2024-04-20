from typing import List


"""
Problem: There are n cities numbered from 0 to n-1. You are given directional edges with wts
Goal: Find node which is reachable to lowest number of other nodes (if same answer pick bigger node)
Ex: 4 nodes
from 1 -> you can reach 2,3
from 2 -> you can node 1,3,5
from 3 -> you can reach 1,2
from 4 -> you can reach 2,4
RES: 1,3,4 but pick (4) as its greater

- SIMPLE FLOYD WARSHALL to find all_src-all_dest shortest dist
"""
class Solution:

    def findTheCity(self, V: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = [[float("inf") for _ in range(V)] for _ in range(V)]
        for u,v,wt in edges: # bidirectional edges
            mat[u][v] = wt
            mat[v][u] = wt

        for node in range(V): # set dist from itself as 0
            mat[node][node] = 0
        
        # FLOYD WARSHALL ALGO
        for k in range(V): # "via" node
            for i in range(V):
                for j in range(V):
                    if mat[i][k] != float("inf") and mat[k][j]!= float("inf"):
                        mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])

        res_count, res_city = float("inf"), -1
        for src in range(V):
            cities_within_dist = 0
            for dest in range(V):
                if mat[src][dest] != float("inf") and mat[src][dest] <= distanceThreshold:
                    cities_within_dist += 1

            # since you check nodes in sorted order, latest one is best in case of ties
            if cities_within_dist <= res_count:
                res_count = cities_within_dist
                res_city = src

        print(mat)
        print(res_city)
        return res_city
        
        
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
V = 5
distanceThreshold = 2

sol = Solution()
sol.findTheCity(V, edges, distanceThreshold)

