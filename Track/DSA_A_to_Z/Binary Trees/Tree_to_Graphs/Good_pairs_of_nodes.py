"""
PROBLEM: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

Note: Node values can repeat (not unique)
SOLUTION:
1. Tree -> Graph (Store nodes and not the node.val since values can repeat)
2. Find all leaves
3. Run BFS from each leaf
    - if you encounter another leaf (not the current leaf) and dist < max_dist = add it to pairs
    - If dist > max_dist = stop iterating (since BFS visits nearest first and further ones will have dist > max_dist)
    - A->B same as B->A so take care while counting

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
            
                    


               