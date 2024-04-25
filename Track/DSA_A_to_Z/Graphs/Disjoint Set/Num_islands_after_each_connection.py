from typing import List

"""
PROBLEM: You are given empty grid, at each iteration you place a stone (replace 0 with 1). 
Print num_islands after each stone is placed after each iteration

Intuition: Dont calculate num islands each iteration -> store it in smart way

Flatten arr -> linear list
0 1 2 -> 012 345 677
3 4 5
6 7 8
- Num : (row_index*nc) + col_index

LOGIC
- islands = 0, res = [] (res contains num_islands after each iteration of stone being placed)
- for x,y in placed_stones:
    1. islands += 1 # assuming this a standalone island
    2. Visit all 4 directions
        - Make sure both nodes DONT BELONG TO SAME ISLAND (dont have same roots -> **IMP** EXPLAINED BELOW)
        - If possible: islands -= 1 (You are combining cur_standalone_island and some other island, 2 islands get combined into 1)
          This is because in (1) you assumed node is standalone island, but in case this gets connected you do -=1 to correct that
    res.append(islands)

Why decrement island IFF parents of nodes you are Unioning are not same?
1 0 0 1 0
1 0 x 1 0
1 0 1 1 0

- You are at (1,2)
    1. You visit left: (1,3) -> JOIN -> islands -= 1
    2. You visit down: (2,3) -> JOIN -> Islands -= 1
    (2) is wrong => since you already added it to same island in (1)
    - So Union and -=1 IFF parents are not same 


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


def numberOfIslandII(nr: int, nc: int, queries: List[List[int]], q: int)-> int:
    arr = [[0 for _ in range(nc)] for _ in range(nr)]
    uf = UF(nr*nc)

    res = []
    count = 0

    for query in queries:
        x1,y1 = query[0], query[1]

        if arr[x1][y1] == 1: # already visited
            res.append(count)
            continue
        
        arr[x1][y1] = 1
        count += 1 # consider this is a standalone island

        # check all 4 dirs
        dxs = [0,1,-1,0]
        dys = [1,0,0,-1]

        for dx,dy in zip(dxs, dys):
            x2, y2 = x1+dx, y1+dy
            if x2>=0 and y2>=0 and x2<nr and y2<nc and arr[x2][y2] == 1 : # valid islands connected
                u = get_node_num(x1,y1,nr,nc)
                v = get_node_num(x2,y2,nr,nc)

                # union only if new island is combined
                if uf.find_parent(u) != uf.find_parent(v):
                    uf.union(u,v)
                    count -=1 

        
        res.append(count)
    
    return res

"""
1 0 0 1 0
1 0 0 1 0
1 0 1 1 0

2 -> |3| -> 2 -> 1

1 2 3 4 5 6 7 8 8 7 6 6 6 4 4 4 4 4 3 2 2 1 1 1 1
1 2 3 4 5 6 7 8 8 7 6 6 6 4 4 4 4 4 3 2 1 1 1 1 1 


"""