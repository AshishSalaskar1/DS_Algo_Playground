"""
Problem: https://leetcode.com/problems/is-graph-bipartite/

Is Graph Bipartite? ==> Graph coloring using 2 colors?

=> LOGIC
- Can you fill each node in graph with 2 colors (0 or 1)
- If you give one color to a node, its neighbors cant have same color
"""


from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        colors = [-1] * V

        for i in range(V):
            if colors[i] != -1:
                continue
            
            q = deque([i])
            colors[i] = 0  # Assign color 0

            while len(q) != 0:
                node = q.popleft()
                for nbr in graph[node]:
                    if colors[nbr] == colors[node]:
                        return False
                    elif colors[nbr] == -1:  # Fixed typo here
                        colors[nbr] = 1 if colors[node] == 0 else 0
                        q.append(nbr)
        
        return True


        

        