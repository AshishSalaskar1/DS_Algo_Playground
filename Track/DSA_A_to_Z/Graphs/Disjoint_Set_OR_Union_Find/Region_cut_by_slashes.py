
"""
PROBLEM: https://leetcode.com/problems/regions-cut-by-slashes
- You can have " ", "/" and "\" 
SOLUTION 1: DFS
- https://leetcode.com/problems/regions-cut-by-slashes/solutions/5614788/simple-approach-using-expanded-grid-with-flood-fill-for-counting-regions
- Represent each grid with a 3x3 grid

EXAMPLE 1
| |/|
|/| |

|0|0|0|0|0|1|
|0|0|0|0|1|0|
|0|0|0|1|0|0|
|0|0|1|0|0|0|
|0|1|0|0|0|0|
|1|0|0|0|0|0|

-> Now find all the 0-islands = 2 in this case

EXAMPLE 2
|/|\|
|\|/| 

|0|0|1|1|0|0|
|0|1|0|0|1|0|
|1|0|0|0|0|1|
|1|0|0|0|0|1|
|0|1|0|0|1|0|
|0|0|1|1|0|0|

-> Now find all the 0-islands = 5 in this case


SOLUTION 2: Union Find
- Video: https://www.youtube.com/watch?v=LKHE5AVTmTk
- Illustration: https://imgur.com/a/asK7SLa

- Each cell has 4 parts - top, left, right, bottom

=> Case 1: "/"
  top /
left / right
    / bottom

- Merge top+left, bottom+right


=> Case 2: "\"
     \ top 
left  \ right
bottom \

- Merge left+bottom, right+top

=> Case 3: " "
- Merge all 4

=> Case 4: Merge with prev row cell - IMPORTANT
- BOTTOM of previous cell UNION TOP of current cell

=> Case 5: Merge with prev col cell - IMPORTANT
- RIGHT of previous cell UNION LEFT of current cell

"""


from typing import List, Tuple

class UF:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}
    
    def find_parent(self, node: Tuple) -> Tuple:
            if self.parent[node] == node:
                return node
            return self.find_parent(self.parent[node])

    def union(self, u: Tuple, v: Tuple) -> None:
        if u not in self.parent:
            self.parent[u] = u
        if v not in self.parent:
            self.parent[v] = v
            
        self.parent[self.find_parent(u)] = self.find_parent(v)

class UF_WITH_PATH_COMPRESSESION_ON_SIZE:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}
    
    def find_parent(self, node: Tuple) -> Tuple:
            if self.parent[node] == node:
                return node
            
            self.parent[node] = self.find_parent(self.parent[node])
            return self.parent[node]

    def union(self, u: Tuple, v: Tuple) -> None:
        # print(f"Union of {u} and {v}")
        if u not in self.parent:
            self.parent[u] = u
            self.size[u] = 1
        if v not in self.parent:
            self.parent[v] = v
            self.size[v] = 1
            

        upar, vpar = self.find_parent(u), self.find_parent(v)
        if upar == vpar:
            return 

        if self.size[vpar] > self.size[upar]: # vpar is bigger, attach upar to vpar
            self.parent[upar] = vpar
            self.size[vpar] += self.size[upar]
        else: # vpar is smaller, attach vpar to upar
            self.parent[vpar] = upar
            self.size[upar] += self.size[vpar]

class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        uf = UF_WITH_PATH_COMPRESSESION_ON_SIZE()

        for row in range(n):
            for col in range(n):
                if grid[row][col] == "/":
                    uf.union( (row,col,"top"), (row,col,"left"))
                    uf.union( (row,col,"bottom"), (row,col,"right"))
                elif grid[row][col] == "\\":
                    uf.union( (row,col,"left"), (row,col,"bottom"))
                    uf.union( (row,col,"top"), (row,col,"right"))
                elif grid[row][col] == " ":
                    uf.union( (row,col,"top"), (row,col,"right"))
                    uf.union( (row,col,"left"), (row,col,"bottom"))
                    uf.union( (row,col,"bottom"), (row,col,"top"))
                
                
                
                if row > 0:
                    uf.union( (row-1,col,"bottom"), (row,col,"top"))
                if col > 0:
                    uf.union( (row,col-1,"right"), (row,col,"left"))
            

        return len(set([uf.find_parent(node) for node in uf.parent.keys()]))




sol = Solution()

# each item indicates ROW CONTENT
grid = [" /","/ "] # 2 
print(sol.regionsBySlashes(grid))


grid = [" /","  "] # 1
print(sol.regionsBySlashes(grid))


grid = ["/\\","\\/"] # 5
print(sol.regionsBySlashes(grid))


grid = ["/ /", " / ", "/ /"] # 4
print(sol.regionsBySlashes(grid))
