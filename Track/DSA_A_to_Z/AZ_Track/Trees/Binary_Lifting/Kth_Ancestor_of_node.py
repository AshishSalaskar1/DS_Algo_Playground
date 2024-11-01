"""
Problem: https://leetcode.com/problems/kth-ancestor-of-a-tree-node/description/

SOLUTION: Simple Binary-Lifting
CATCH: Generally you consider 1 as root node (and 0 acts as out of bound node)
- Here, 0 is the root node and -1 acts as the out-of-bound node (need to explicitly handle it)

- Keep array size as [n+1] such that you can use -1 (last node) as the out-of-bounds node

TC: O(Q*logN)
- For each query, you lift/traverse at max log(n) times
SC: O(Q*logN)


Detailed Explaination: https://github.com/AshishSalaskar1/DS_Algo_Playground/tree/master/Track/DSA_A_to_Z/AZ_Track/Trees/Binary_Lifting

"""

class TreeAncestor:
    def dfs(self, node, parent):
        self.lift[node][0] = parent

        for i in range(1, 20):
            if self.lift[node][i-1] != -1: # did not go out of bounds
                self.lift[node][i] = self.lift[self.lift[node][i-1]][i-1]
            else:
                self.lift[node][i] = -1  # Mark as invalid if out of bounds.

        for child in self.adj[node]:
            if child != parent:
                self.dfs(child, node)

    def __init__(self, n: int, parents: List[int]):
        self.lift = [[-1 for _ in range(20)] for _ in range(n+1)]
        self.adj = [[] for _ in range(n+1)]

        for node_idx, parent in enumerate(parents):
            if parent != -1:  # Skip invalid edges for the root.
                self.adj[parent].append(node_idx)
                self.adj[node_idx].append(parent)

        # Assuming node 0 is the root.
        self.dfs(0, -1)

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(19, -1, -1):
            if node == -1: # you are already over the root node (OUT OF BOUNDS)
                break
            if k & (1 << i): # BINARY LIFTING
                node = self.lift[node][i]
        return node
