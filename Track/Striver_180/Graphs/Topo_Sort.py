"""
Python submission issue: https://www.codingninjas.com/studio/problems/topological-sorting_973003

LOGIC: If theres an edge u->v then in the topological order `u` should appear before `v`

Solution:
- Do DFS from each node, after DFS happens put the elements onto a stack
- Intution on why u add after DFS and not at start of DFS:
    - Example graph: 5->0->1->2
    - U do `dfs(0)` -> `dfs(1)` -> `dfs(2)` -> STOP
    - U do `dfs(5)` -> STOP
    - Sort must be: 5 0 1 2,
        - in this case stack: [2, 1, 0, 5] <- TOP
        - if u had put in stack at start it will be [0, 1, 2, 5] <- TOP. 
          You have to separate out each dfs stack push and then reverse.
          [ rev(0, 1, 2) , rev(50]

"""
class Solution:
    def dfs(self, node):
        self.vis.add(node)

        for nbr in self.adj[node]:
            if nbr not in self.vis:
                self.dfs(nbr)

        # add to stack from depth first -> after DFS happens
        self.stack.append(node)

    def topologicalSort(self, adj, V):
        self.adj = adj
        self.vis = set()
        self.stack = []

        for node in range(V):
            if node not in self.vis:
                self.dfs(node)

        topo = []
        while len(self.stack) != 0:
            topo.append(self.stack.pop())

        print(topo)
        return topo

def topologicalSort(adj, V, E):
    sol = Solution()
    return sol.topologicalSort(adj, V)
    # return []