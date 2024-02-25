COULDNT DO THIS WITH STACK MANUALLY

Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]
Thus dfs will be 0 2 4 3 1

Input: V = 4, adj = [[1,3], [2,0], [1], [0]]

Output: 0 1 2 3

"""
class Solution:
    def dfs(self, cur_node):
        self.res.append(cur_node)
        
        for nbr in self.adj[cur_node]:
            if nbr not in self.vis:
                self.vis.add(nbr)
                self.dfs(nbr)
    
    def dfsOfGraph(self, V, adj):
        self.n_nodes = V
        self.adj = adj
        self.vis = set([0])
        self.res = []
        
        self.dfs(0)
        
        return self.res