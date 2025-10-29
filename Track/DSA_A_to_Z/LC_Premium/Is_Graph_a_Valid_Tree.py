"""
You have a graph of n nodes labeled from 0 to n - 1 and edges.


Return true if the edges of the given graph make up a valid tree, and false otherwise.


Example 1:
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true
    Explanation:
        The graph consists of 5 nodes labeled from 0 to 4 and has 4 edges. A valid tree must have exactly n-1 edges, which in this case is 4, so the count is correct.
        Additionally, there are no cycles because every new edge connects a previously disconnected node.
        The graph is also fully connected, meaning all nodes can be reached from any other node.
        Since all conditions of a tree are satisfied, the given graph forms a valid tree.

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    Output: false
        Explanation:
        The graph consists of 5 nodes and 5 edges. A valid tree must have exactly n-1 edges, but here there are 5 edges instead of 4, which is already a problem.
        Additionally, the edge [1,3] forms a cycle because there is already a path from 1 to 3 through 1-2-3.
        Even though the graph is connected, the presence of a cycle means it does not satisfy the conditions of a tree.
        Therefore, the given graph is not a valid tree.



SOLUTION:
A graph can be a tree if these 2 conditions are satisfied
 1. Every node is reachable from every other node
 2. There are no loops

1. You run a DFS from any node -> Ideally you should have visited `n` number of nodes
2. When running DFS, if you visit same node again -> Then there is a loop

TRICKY PART in 2: You need parent
- Edges: 0->1, 1->2
- adj = 0 :[1], 1: [0,1]
- WRONG LOGIC
    1. DFS(0) 
    2. DFS(1)
    3. DFS(0) ==> LOOP ACCORDING TO THIS ( WRONG) 
- CORRECT LOGIC
    1. DFS(0, -1) 
    2. DFS(1, 0)
    3. => DFS(0) ==> THIS CALL IS NEVER MADE
"""

from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        vis = set()
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def dfs(node, parent):
            if node in vis: return False
            
            vis.add(node)

            status = True
            for nbr in adj[node]: 
                # YOU DONT VISIT PARENT AGAIN
                if nbr!=parent: status = status and dfs(nbr, node)

            return status
        
        res = dfs(0, -1)

        if res is False or len(vis)!=n:
            return False
        
        return True