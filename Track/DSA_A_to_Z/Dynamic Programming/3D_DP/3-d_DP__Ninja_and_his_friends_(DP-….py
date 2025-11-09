"""
Problem:
- Given a grid, Alice and Bob are placed at start and end of first row respectively
- They both can travel to next row in 3 ways (Down, Diagonally Left + Right)
- If one person captures a cell, other one cant use it
- Find max collections both can make by travelling from FIRST -> LAST ROW (any cell in last row)


SOLUTION:
- DP Params: 
    - (r1, c1) (r2,c2) for tracking position of both Alice and Bob
    - But, we know that they can move only down each row. So r1=r2 always
    - Variables params now: (r, c1, c2)
- Recursion
    DP Mean: Given that both are at loc (r,c1,c2), what is max sum you can make by reaching the last row from here
    1. if outside boundary -> cant visit -> return 0
    2. Base case: both reached last row (will always reach together since traverse 1 row at a time)
        - Both reached same cell (You can pick only one) => points(r, c1) c1==c2
        - Reached diff cells => Return points(r, c1) + points(r, c2)
    3. Non Base case:
        - Position (r,c1) and (r,c2).There are 9 ways you can traverse to next row (both move simultaneously)
        - # Next Possible Column Position : (c1-1, c1, c1+1) * (c2-1, c2, c2+1)
        - # Next Possibe Row Position: r+1
        - Traverse all 9 paths n see which gives you the most sum
    

"""


class Solution:
    
    def solve(self, r, c1, c2):
        if (r, c1, c2) in self.mem:
            return self.mem[(r, c1, c2)]

        if r<0 or r>=self.nr or c1<0 or c2<0 or c1>=self.nc or c2>=self.nc:
            return 0
        elif r==self.nr-1:
            if c1 == c2:
                self.mem[(r, c1, c2)] = self.arr[r][c1]
                return self.arr[r][c1]
            else:
                self.mem[(r, c1, c2)] = self.arr[r][c1] + self.arr[r][c2]
                return self.arr[r][c1] + self.arr[r][c2]
        else:
            # 9 ways you can traverse to next row (both move simultaneously)
            # c1 : (c1-1, c1, c1+1) * (c2-1, c2, c2+1)
            max_score = 0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    c1_next = c1+i
                    c2_next = c2+j
                    cur_decision_score = 0
                    if c1_next == c2_next:
                        cur_decision_score = self.arr[r][c1] + self.solve(r+1, c1_next, c2_next)
                    else:
                        cur_decision_score = self.arr[r][c1] + self.arr[r][c2] + self.solve(r+1, c1_next, c2_next)

                    max_score = max(cur_decision_score, max_score)
            
        self.mem[(r, c1, c2)] = max_score
        return max_score


    
    def maximumChocolates(self, r , c, grid):
        self.arr = grid
        self.nr = r
        self.nc = c
        self.mem = {}

        res = self.solve(r=0,c1=0,c2=c-1)
        print(res)




arr = [
    [2, 3, 1, 2],
    [3, 4, 2, 2],
    [5, 6, 3, 5]
]

sol = Solution()
res = sol.maximumChocolates(len(arr), len(arr[0]), arr)