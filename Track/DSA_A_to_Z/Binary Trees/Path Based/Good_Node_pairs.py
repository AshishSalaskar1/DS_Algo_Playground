"""
PROBLEM: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

Note: Node values can repeat (not unique)
SLOWER SOLUTION - O(n*leaf_node_count):
1. Tree -> Graph (Store nodes and not the node.val since values can repeat)
2. Find all leaves
3. Run BFS from each leaf
    - if you encounter another leaf (not the current leaf) and dist < max_dist = add it to pairs
    - If dist > max_dist = stop iterating (since BFS visits nearest first and further ones will have dist > max_dist)
    - A->B same as B->A so take care while counting

    
OPTIMIZED SOLUTION:

- BASE CASE: if node is leaf return [1]
- Each node returns a list of distances from leaf node
- So list returned indicates there is leaf node in left/right subtree at distance as given

Case 1: Leaf present in both subtree (Leaves in left subtree can be connected to right subtree via some path)
left_subtree = [1], right = [1]
=> (1,1) =2<max_dist -> pair++
=> now return [2,2] (Indicates from this node there are 2 leaf nodes each at dist 2 2 from above/parent node)

Case 2: Leafs present only in right or left subtree
-> No pairs since you need atleast 1 leaf in each subtree
=> return concat(lsubtre, rsubtree) and increment each by 1

Example:  max_dist = 3
lstree = [1,2], rstree = [2,3]
Pairs = (1,2), (1,3), (2,2), (2,3)
Out of these only 1 is valid since rest sum up to > max_dist/3
"""


from queue import deque, PriorityQueue
from collections import defaultdict
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def solve(self, node: TreeNode) -> list[int]:
        if node is None:
            return None

        # node is leaf node
        if node.left is None and node.right is None:
            return [1]

        lstree = self.solve(node.left)
        rstree = self.solve(node.right)

        # print(f"Node: {node.val} => {lstree}{rstree}")

        cur_dists = []
        if lstree and rstree: # both left and right subtrees have leaf node => check all possible pairs
            for ldist in lstree:
                for rdist in rstree:
                    if ldist+rdist <= self.maxdist:
                        # print(f"({ldist})({rdist}) => Node: {node.val}")
                        self.pairs += 1
        
        if lstree:
            cur_dists.extend([x+1 for x in lstree])
        if rstree:
            cur_dists.extend([x+1 for x in rstree])
        
        return cur_dists

    def countPairs(self, root: TreeNode, max_distance: int) -> int:
        self.pairs = 0
        self.maxdist = max_distance
        self.solve(root)

        return self.pairs
                    



class SlowerSolution:
    def countPairs(self, root: TreeNode, max_distance: int) -> int:
        if root is None:
            return 0
        
        adj = defaultdict(list)
        leaves = set()
        pairs = set()

        def dfs(node, parent=None):
            if node:
                if parent:
                    if node.left is None and node.right is None:
                        leaves.add(node)
                    adj[node].append(parent)
                    adj[parent].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)

        # Run BFS from each LEAF to OTHER LEAVES - So that min path is already handled in BFS
        for leaf in leaves:
            q = deque()
            q.append((leaf, 0))

            while len(q) != 0:
                node, dist = q.popleft()
                if dist > max_distance:
                    break
                for nbr in adj[node]:
                    # cur_leaf -> another_lead having dist < max_dist
                    if nbr!=leaf and nbr in leaves and dist+1 <= max_distance:
                        # avoid duplicate pairs being added
                        if (leaf, nbr) not in pairs and (nbr, leaf) not in pairs:
                            pairs.add((leaf, nbr))
                    q.append((nbr, dist+1))
        
        # print(pairs)
        return len(pairs)
            