"""
https://takeuforward.org/data-structure/detect-cycle-in-a-directed-graph-using-dfs-g-19/

Logic: 
- In directed graph, you can say that cycle is there is while traversing a path, u encounter the same node twice
- Since its directed graph, 2 different paths can reach same node [DOESNT MEAN ITS CYCLE - works in undirected]
- For each DFS call update global vis, path_vis -> in case cycle found in this node or its sub-path return True
- Else before leaving this DFS call re-set the path_vis 
"""



class Solution:

    def dfs(self, node: int):
        self.vis.add(node)
        self.cur_path_traversal.add(node)

        # traverse nbrs 
        for nbr in self.adj[node]:
            if nbr not in self.vis: # newly visited node
                if self.dfs(nbr): # cycle found in this SUB-PATH
                    return True
            else:
                # node is visited globally and also part of cur traversed path
                if nbr in self.cur_path_traversal:
                    return True
        
        # remove curr node from cur_traversed_path : sort of backtrack
        self.cur_path_traversal.remove(node)
        return False
            

    def check_cycles(self, adj, v):
        self.adj = adj
        self.vis = set()
        self.cur_path_traversal = set()
        
        # dfs from all nodes, since all nodes might not be reachable from single source
        for node in range(v):
            if v not in self.vis:
                is_cycle = self.dfs(node)
                if is_cycle:
                    return True
        
        return False


def isCyclic(edges, v, e):
    adj = [[] for _ in range(v)]
    for x,y in edges:
        adj[x].append(y)
    
    sol = Solution()
    return sol.check_cycles(adj, v)


