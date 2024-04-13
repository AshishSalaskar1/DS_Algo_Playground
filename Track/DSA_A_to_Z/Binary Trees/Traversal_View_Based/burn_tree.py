"""
Graph Based Solution:
1. Convert tree -> bidirectional graph
2. Run bfs from "Start" as root, each lvl gets burned in 1 sec
3. Max lvl reached  = time taken to burn entire tree
"""


# Binary tree node class for reference.
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None


def add_nodes_to_adj(src, dest, adj):
    adj[src] = [*adj.get(src, []), dest]

def timeToBurnTree(root, start):
    adj = {}

    # level order and add nodes
    q = [root]
    while len(q) != 0:
        cur = q.pop(0)
        cur_val = cur.data

        if cur.left:
            adj[cur_val] = [*adj.get(cur_val, []), cur.left.data]
            adj[cur.left.data] = [*adj.get(cur.left.data, []), cur_val]
            q.append(cur.left)

        if cur.right:
            adj[cur_val] = [*adj.get(cur_val, []), cur.right.data]
            adj[cur.right.data] = [*adj.get(cur.right.data, []), cur_val]
            q.append(cur.right)
    
    # BFS
    q = [(start,1)]
    max_lvl = 0
    vis = set()

    # print(adj)
    while len(q) != 0:
        cur, lvl = q.pop(0)
        vis.add(cur)
        max_lvl = max(max_lvl, lvl)

        for x in adj.get(cur,[]):
            if x not in vis:
                q.append((x, lvl+1))
    
    return max_lvl-1
