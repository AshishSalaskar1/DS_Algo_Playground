from typing import List


"""
Problem: https://leetcode.com/problems/diagonal-traverse/
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]


BRUTE: Check in up and down directions like you do DFS

TRICK: 
- For a given diagonal elements, sum of their indexes is same
- If that sum is even - UP Direction, else - DOWN direction

# 00 01 02 -> 0 1 2
# 10 11 12 -> 1 2 3
# 20 21 22 -> 2 3 4

- Diag1: 00 -> sum=0 -> UP
- Diag2: 01, 10 -> sum=1 -> DOWN
- Diag3: 20, 11, 02 -> sum=2 -> UP
- Diag4: 12, 21 -> sum=3 -> DOWN
- Diag5: 22 -> sum=4 -> UP

Maintain a dict with {
    "diagonal_index_sum": [elements in TOP->DOWN order] (since you visit from top row to bottom)
}

if idx_sum = EVEN -> REVERSE (Since they are now in top-down)
elif idx_sum = ODD -> NOTHING (Since you want top-down order)
"""
class Solution:
    def findDiagonalOrder(self, arr: List[List[int]]) -> List[int]:
        nr, nc = len(arr), len(arr[0])
        hmap = {}
        for i in range(nr):
            for j in range(nc):
                idx_sum = i+j
                if idx_sum in hmap:
                    hmap[idx_sum].append(arr[i][j])
                else:
                    hmap[idx_sum] = [arr[i][j]]

        res = []
        # sort based on idx_sums -> 0,1,2,3.. [Dict key order cant be gauranteed]
        for idx_sum, eles in sorted(hmap.items(), key=lambda x:x[0]):
            print(idx_sum, eles)
            if idx_sum % 2 == 0: # even
                res.extend(eles[::-1])
            else:
                res.extend(eles)
                
        return res


    def visit(self, i, j, dir):
        print("trying: ",i,j,self.res)
        if (i,j) in self.vis or i<0 or j<0 or i>=self.nr or j>=self.nc:
            return

        self.res.append(self.arr[i][j])
        self.vis.add((i,j))

        if dir == "up":
            self.visit(i+1, j+1, "up")
        else:
            self.visit(i-1, j-1, "down")


    def findDiagonalOrderBrute(self, arr: List[List[int]]) -> List[int]:
        self.arr = arr
        self.nr = len(arr)
        self.nc = len(arr[0])

        self.vis = set()
        self.res = []

        for j in range(self.nc):
            # even -> up, odd: down
            if j%2 == 0:
                self.visit(0, j, "up")
            else:
                self.visit(0, j, "down")
        
        return self.res


sol = Solution()
res = sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)