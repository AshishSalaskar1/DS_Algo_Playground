"""
PROBLEM: Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.


# 3, 1, 2, 4
3 -> [3]
1 -> [1], [3,1], [1,2],[3,1,2],[1,2,4], [3,1,2,4]
2 -> [2], [2,4]
4 -> [4]

- Treat this a Largest rectangle area
- For each number find the boundary on left and right
    1. Left boundary: first num on left which is lesser than arr[i]
    2. Right boundary: fist num on right which is lesser than arr[j]
    - You use [left+1, right-1] as your expandable window
    - This gives you number of subarrays which include arr[i] and arr[i] is lowest number in that

3 1 2 4 => [3, {}] [1, 2 4]
Num subarrays including 1 ->
    1. len(left+1)*len(right+1)
    - len(left+1) => elements in left + {empty}
    - len(right+1) => elements in right + [1] itself
  [3, {}] MULT [1,2,4]
-> 3 + [1],  [12], [124] => 31,312,3124
-> {} + [1], [12], [124] => 1, 12, 124


HUGE EDGE CASE 
[2,2] -> ANSWER=6 -> [2], [2], [2,2] => 2+2+2 = 6
# res_count = (i-lsb+1)*(rsb-i+1)
left_small = [-1,-1]
right_small = [-1,-1]
=> at index 0: (0-0+1)*(1-0+1) = 2 (2*2)
=> at index 1: (1-0+1)*(1-1+1) = 2 (2*2)
-> Gives you 8 (which is wrong..Needed is 6)

SOLUTION: You need to use NextSmallerOrEqual element for one direction
- here START <- ELE (use NextSmallerElement)
- ELE -> END (use NextSmallerElement)

"LINK": https://www.youtube.com/watch?v=5Hag64mLXac&list=PLEL7R4Pm6EmDSG2vFQN8S04AQfLHC0jR7&index=10&ab_channel=AryanMittal
"""


class Solution:
    def sumSubarrayMins(self, arr) -> int:
        n = len(arr)
        # first smaller or equal element in left side, save index
        lsmall = [-1 for _ in range(n)]
        st = []
        for i in range(n):
            # here NextGreaterThanOrEqual element
            while len(st) != 0 and arr[st[-1]] > arr[i]:
                st.pop()
            if len(st)!=0:
                lsmall[i] = st[-1]
            st.append(i)

        # first smaller element in right side, save index
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

            lsb = lsmall[i]+1 if lsmall[i]!=-1 else 0 # left side boundary
            rsb = rsmall[i]-1 if rsmall[i]!=-1 else n-1 # right side boundary

            subarrays_where_cur_is_min = ((i-lsb+1)*(rsb-i+1))%(10**9+7)
            res += (subarrays_where_cur_is_min*arr[i])%(10**9+7)
            res = res % (10**9+7)

        # print(lsmall, rsmall)
        return res

# sol = Solution()
# sol.sumSubarrayMins([2,2])
