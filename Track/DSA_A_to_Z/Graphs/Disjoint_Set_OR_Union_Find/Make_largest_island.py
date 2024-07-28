"""
PROBLEM: You are given a arr with islands present (1 means land)
You can change any one cell from 0->1, give the largest island you can make by doing (you can choose not to change also)
Flatten arr -> linear list
0 1 2 -> 012 345 677
3 4 5
6 7 8
- Num : (row_index*nc) + col_index

BRUTE WAY:
    1. Update all islands present
    2. Iterate each cell with 0 -> try replace 0 by 1 and see if bigger island is created
        (TLE, You need to REVERT BACK the current union)

BETTER WAY:
    res = 0
    1. Update all the islands
    2. Iterate each with 0 
        cur_biggest_island = 0
        - Check if any 1 present in all 4 directions
            # this node connects all separate islands in 4 directions together
            - If present cur_biggest_island += uf.sizes[v]
        - cur_biggest_island += 1 (all nbr islands + you will also this node)
        - res = max(res, cur_biggest_island )
    3. If no 0 or you dont want to replace (this will never happen)
    -> Iterate through parent root of each node and check uf.sizes[uf.find_parent(node)] and update res if greater
    


"""
def get_node_num(row, col, nr, nc):
    return (row*nc) + col

class UF:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.sizes = [1 for x in range(n)]
    
    def find_parent(self, node):
        if self.parents[node] == node:
            return node
        
        self.parents[node] = self.find_parent(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        pu, pv = self.find_parent(u), self.find_parent(v)
        if pu == pv:
            return 
        elif self.sizes[pu] < self.sizes[pv]:
            self.parents[pu] = pv
            self.sizes[pv] += self.sizes[pu]
        else:
            self.parents[pv] = pu
            self.sizes[pu] += self.sizes[pv]

            
class Solution:
    def largestIsland(self, arr: List[List[int]]) -> int:
        nr, nc = len(arr), len(arr[0])
        uf = UF(nr*nc)
        vis = set()

        for x1 in range(nr):
            for y1 in range(nc):
                if arr[x1][y1] == 1:
                    dxs = [0,1,-1,0]
                    dys = [1,0,0,-1]

                    for dx,dy in zip(dxs, dys):
                        x2, y2 = x1+dx, y1+dy
                        if x2>=0 and y2>=0 and x2<nr and y2<nc and arr[x2][y2] == 1: # valid islands connected
                            u = get_node_num(x1,y1,nr,nc)
                            v = get_node_num(x2,y2,nr,nc)
                            uf.union(u,v)

        res = 0
        for x1 in range(nr):
            for y1 in range(nc):
                if arr[x1][y1] == 0:
                    print(x1,y1)
                    dxs = [0,1,-1,0]
                    dys = [1,0,0,-1]

                    island_roots = set()
                    # visit all 4 directions
                    for dx,dy in zip(dxs, dys):
                        x2, y2 = x1+dx, y1+dy
                        # store the parents of the components you are getting added to (can be > 1)
                        v = get_node_num(x2,y2,nr,nc)
                        if x2>=0 and y2>=0 and x2<nr and y2<nc and arr[x2][y2] == 1: # valid islands connected
                            island_roots.add(uf.find_parent(v))

                    cur_max_size = 0
                    # print(cur_max_size)
                    for island_root in island_roots:
                        cur_max_size += uf.sizes[island_root]

                    # size of all islands you can get added + You add curr node to those islands
                    res = max(res, cur_max_size+1)
                    # print(x1,y1,island_roots, uf.parents)
        

        # find largest island without changing any 0 -> 1 (0s not there, you dont want to change)
        for node in range(0, nr*nc):
            res = max(res, uf.sizes[uf.find_parent(node)])

        return res

                    




"""
1 1
1 0
"""
