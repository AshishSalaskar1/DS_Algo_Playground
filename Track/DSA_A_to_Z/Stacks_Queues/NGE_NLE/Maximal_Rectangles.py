"""
PROBLEM: https://leetcode.com/problems/maximal-rectangle/


SOLUTION: Run largestRectangleArea() on each 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

1. [1 0 1 0 0] => 1
2. [2 0 2 1 1] => 3
3. [3 1 3 2 2] => 6
4. [4 0 2 3 1] => 4

"""

class Solution:
    def largestRectangleArea(self, arr: list[int]) -> int:
        n = len(arr)
        print(arr)

        # first smaller element in left side, save index -> MODIFIED NGE/NSE
        lsmall = [-1 for _ in range(n)]
        st = []
        for i in range(n):
            while len(st) != 0 and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st)!=0:
                lsmall[i] = st[-1]
            st.append(i)

        # first smaller element in right side, save index -> MODIFIED NGE/NSE
        rsmall = [-1 for _ in range(n)] 
        st = []
        for i in reversed(range(n)):
            while len(st) != 0 and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st)!=0:
                rsmall[i] = st[-1]
            st.append(i)

        res = 0
        for i in range(n):
            lbh = lsmall[i]+1 if lsmall[i]!=-1 else 0
            rbh = rsmall[i]-1 if rsmall[i]!=-1 else n-1
            res = max(res, (rbh-lbh+1)*arr[i])
        
        print(res)
        return res

    def maximalRectangle(self, arr: List[List[str]]) -> int:
        nr, nc = len(arr), len(arr[0])
        bricks = [int(x) for x in arr[0]]

        res = self.largestRectangleArea(bricks)
        
        for row in range(1,nr):
            for col in range(0,nc):
                if arr[row][col] == '1':
                    bricks[col] += 1
                else:
                    bricks[col] = 0
            res = max(res,self.largestRectangleArea(bricks))
        
        return res
