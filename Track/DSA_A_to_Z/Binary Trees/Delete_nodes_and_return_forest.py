"""
PROBLEM: https://leetcode.com/problems/delete-nodes-and-return-forest/

SOLUTION:
Ref: https://leetcode.com/problems/delete-nodes-and-return-forest/solutions/5488067/postorder-traversal-c-python-java

- is_new_root indicates if this is new tree (Which means previous node was deleted)
- Check if this node is to be deleted
    - pass this to both calls (right and left) -> Dont bother about deleting this node since we will send back None to whatever called this
- In case is_new_root and cur_node_val not in to_delete => ADD THIS TO RES
    - This a new root, BUT this node also might be in to_delete list
- If this is in to_delete, that means previous nodes connetion to this needs to be BROKEN -> RETURN None
    - else return root

- Main idea: No matter if you delete this current node or not, yet iterate left and right subtrees
    - In case next node was deleted you anyways get returned None
    - If this needs to be deleted,, you return None (Link to the parent who called this node will become None -> CHAIN BROKEN)
    - If this is valid node, update the right and left calls 
- Why continue with left and right calls if this needs to be deleted?
    - In this case, you are making calls passing is_new_root=True to left and right subtrees, so these will themselves get added as roots in RES
    - And you return None -> previous links to this will be broken
    - No need to write lot of conditions as written in SlowerSolution at bottom
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import deque
from typing import List, Optional
class Solution:
    def solve(self, root: TreeNode, is_new_root: bool) -> TreeNode:
        if root is None:
            return None
    
        should_delete = root.val in self.to_delete
        if not should_delete and is_new_root: # parent was deleted -> THIS IS NEW ROOT
            self.res.append(root)

        root.left = self.solve(root.left, should_delete)
        root.right = self.solve(root.right, should_delete)
        
        return None if should_delete else root # break connection to parent in case this is deleted, else keep the chain going on


    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        self.to_delete = to_delete
        self.solve(root, True)
        return self.res



class SlowerSolution:
    def dfs(self, node: TreeNode, new_root: bool = False) -> list[TreeNode]:
        if node is None:
            return 

        if new_root:
            print(f"At {node.val} => appending {node.left} and {node.right}")
            if node.val in self.to_delete:
                self.dfs(node.right, True)
                self.dfs(node.left, True)
                return
            else:
                self.res.append(node)

        if node.right:
            if node.right.val in self.to_delete:
                self.dfs(node.right.left, True)
                self.dfs(node.right.right, True)
                node.right = None
            else:
                self.dfs(node.right)
        
        if node.left:
            if node.left.val in self.to_delete:
                self.dfs(node.left.left, True)
                self.dfs(node.left.right, True)
                node.left = None
            else:
                self.dfs(node.left)
                
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = to_delete
        self.res = []

        if root is None:
            return []

        if root.val in self.to_delete:
            self.dfs(root.left, True)
            self.dfs(root.right, True)
        else:
            self.res.append(root)
            self.dfs(root, False)

        for node in self.res:
            if node:
                print(node.val)

        return self.res  