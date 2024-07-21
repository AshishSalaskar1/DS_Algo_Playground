"""
PROBLEM: https://leetcode.com/problems/build-a-matrix-with-conditions

Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]

Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []


Input: k = 4, rowConditions = [[1,3],[4,3],[3,2]], colConditions = [[1,2],[4,2],[4,3]]
Output: [[1,0,0,0], [0,4,0,0], [0,0,0,3], [0,0,2,0]]

COL ORDER: 1 4 2 3
ROW ORDER: 1 4 3 2
# 1 4 2 3

# 1 x x x     1
# x 4 x x     4
# x x x 3     3
# x x 2 x     2
"""



from queue import deque

def create_adj_matrix(n, conditions):
    adj = {key:[] for key in range(1,n+1)}
    for src, dest in conditions:
        adj[src].append(dest)

    return adj

def topological_sort(adj: list[list[int]]) -> list[int]:
    """
    Returns None->Cycle, else toposort
    """
    indegrees = {}
    q = deque()
    topo_sort = []

    for src, dests in adj.items():
        if src not in indegrees:
            indegrees[src] = 0
        for dest in dests:
            indegrees[dest] = indegrees.get(dest,0) + 1
    
    for node, degs in indegrees.items():
        if degs == 0:
            q.append(node)
    
    while len(q)!=0:
        node = q.popleft()
        topo_sort.append(node)

        for nbr in adj[node]:
            indegrees[nbr] -= 1
            if indegrees[nbr] == 0:
                q.append(nbr)
    
    return topo_sort if len(topo_sort) == len(adj) else None

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_adj = create_adj_matrix(k, rowConditions)
        col_adj = create_adj_matrix(k, colConditions)

        row_orders = topological_sort(row_adj)
        col_orders = topological_sort(col_adj)

        # You cant have this order - SOME CYCLE EXISTS
        if row_orders is None or col_orders is None:
            return []

        print(row_orders, col_orders)
        arr = [[0 for _ in range(k)] for _ in range(k)]

        for i in range(k):
            for j in range(k):
                if row_orders[i] == col_orders[j]:
                    arr[i][j] = row_orders[i]


        return arr
        

