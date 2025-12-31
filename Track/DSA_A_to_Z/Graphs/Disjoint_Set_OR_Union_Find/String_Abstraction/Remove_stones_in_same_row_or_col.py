"""
Problem: 
- On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
- A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones kept (List<x,y>) return the largest possible number of stones that can be removed.


INTUITIONS:
1. Consider rows and columns as separate entities (since its said as any one)
    - if stone placed at (x,y) consider you are unioning row_x and col_y 
2. Represent rows and cols separately
    - Given that 0 < xi,yi < 10^4
    - So consider rows from 0-10^4, cols from (10^4+1)+col_index
    - (x,y) => (x, (10^4+1)+y) 
3. Consider you have an island of 10 stones (You can remove 9 stones)
    - You can keep on removing 9 stones since they will have atleast row or col in common
    - Order in which you remove is not asked (will be same as ordered in which you added those to the UF)


  - TOTAL STONES REMOVED: len(stones) - N_ISLANDS
  
SOLUTION:
- For each x,y pair of stone cordinates -> UNION((x, (10^4+1)+y)
- At last this will create present number of islands 
- Find how many stones can be safely removed:
    - If island has `x` stones you can remove `x-1` nodes
    - BRUTE FORCE
      1. Visit each island and keep on adding len(island)-1 nodes (TLE)
    - OPTIMAL
      - How many stones will be left on board = no of islands (for each island you keep only 1)
      - Let remaining stones = no of islands = N_ISLANDS
      - Total stones added = len(stones)
    - [NOTE]: while finding num of islands use find_parent and not just parent[node] (might have missed path compression)
"""


class DSU:
    def __init__(self):
        self.parents = {}
        self.sizes = {}
    
    def get_parent(self, node):
        if node == self.parents[node]:
            return node
        
        self.parents[node] = self.get_parent(self.parents[node])
        return self.parents[node]
    

    
    def add_stone(self, i,j):
        row, col = i, (10**4+1)+j

        self.parents[row] = self.parents.get(row,row)
        self.sizes[row] = self.sizes.get(row,1)

        self.parents[col] = self.parents.get(col,col)
        self.sizes[col] = self.sizes.get(col,1)

        row_root = self.get_parent(row)
        col_root = self.get_parent(col)

        if row_root == col_root:
            return 
        elif self.sizes[row_root] < self.sizes[col_root]:
            self.parents[row_root] = col_root
            self.sizes[col_root] += self.sizes[row_root]
        else:
            self.parents[col_root] = row_root
            self.sizes[row_root] += self.sizes[col_root]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()
        for stone in stones:
            x,y = stone[0], stone[1]
            dsu.add_stone(x,y)

        # check all conn-comps having size > 1 (size(cc)-1  is the stones you can remove)
        res = 0
        print(dsu.parents)
        print(dsu.sizes)
        
        return len(stones) - len({dsu.get_parent(n) for n in dsu.parents})