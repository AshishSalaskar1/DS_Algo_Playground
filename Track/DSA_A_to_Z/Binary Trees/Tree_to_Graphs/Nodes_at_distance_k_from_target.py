"""
Same as burning tree
1. Tree -> Undirected graph
2. BFS levels = level `k`

IMPROVEMENT: Store TreeNode directly instead of TreeNode.val
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # tree -> graph    
        adj = {}
        q=[root]
        while len(q) != 0:
            cur = q.pop(0)
            if cur.left:
                adj[cur.val] = [*adj.get(cur.val,[]), cur.left.val]
                adj[cur.left.val] = [*adj.get(cur.left.val,[]), cur.val]
                q.append(cur.left)
            if cur.right:
                adj[cur.val] = [*adj.get(cur.val,[]), cur.right.val]
                adj[cur.right.val] = [*adj.get(cur.right.val,[]), cur.val]
                q.append(cur.right)
        
        vis = set()
        lvl = 1
        q = [target.val]

        # k=0, return target itself
        if k==0:
            return [target.val]
        while len(q) != 0:
            cur_lvl_n = len(q)
            cur_lvl = []

            for _ in range(cur_lvl_n):
                cur = q.pop(0)
                vis.add(cur)

                for x in adj.get(cur, []):
                    if x not in vis:
                        cur_lvl.append(x)
                        q.append(x)
            
            print(lvl, cur_lvl)
            if lvl == k:
                return cur_lvl
            lvl += 1
        
        return []


# storing TreeNode objects
def printNodesAtDistanceK(root, target, k):
    # tree -> graph    
    adj = {}
    q=[root]
    while len(q) != 0:
        cur = q.pop(0)
        if cur.left:
            adj[cur] = [*adj.get(cur,[]), cur.left]
            adj[cur.left] = [*adj.get(cur.left,[]), cur]
            q.append(cur.left)
        if cur.right:
            adj[cur] = [*adj.get(cur,[]), cur.right]
            adj[cur.right] = [*adj.get(cur.right,[]), cur]
            q.append(cur.right)
    
    vis = set()
    lvl = 1
    q = [target]

    # k=0, return target itself
    if k==0:
        return [target]
    while len(q) != 0:
        cur_lvl_n = len(q)
        cur_lvl = []

        for _ in range(cur_lvl_n):
            cur = q.pop(0)
            vis.add(cur)

            for x in adj.get(cur, []):
                if x not in vis:
                    cur_lvl.append(x)
                    q.append(x)
        
        # print(lvl, cur_lvl)
        if lvl == k:
            return list(set(cur_lvl))
        lvl += 1
    
    return []



