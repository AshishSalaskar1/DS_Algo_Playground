""" Logic

- Consider max rectange you can make using current bar (height=arr[i], width=1)
 1. From START <- I find first bar smaller than arr[i]
 2. From I -> END find first bar smaller than arr[i]
 - Smaller means you cant both these, these act like boundaries 
 - You can pick (left_smaller+1 : right_smaller-1) bars including arr[i]

"""

class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)

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
            # Why +1 in RBH and -1 in RBH
            # Your bounds are one bar/rectangle after the smallest_on_left and one bar/rect before smallest_on_right
            lbh = lsmall[i]+1 if lsmall[i]!=-1 else 0
            rbh = rsmall[i]-1 if rsmall[i]!=-1 else n-1
            res = max(res, (rbh-lbh+1)*arr[i])
        
        return res
