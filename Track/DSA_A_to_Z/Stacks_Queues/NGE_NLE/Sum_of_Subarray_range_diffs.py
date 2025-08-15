"""

PROBLEM: https://leetcode.com/problems/sum-of-subarray-ranges/

SOLUTION
- Same as "Sum of subarray minimums"
- "Sum of subarrays maximums" - "Sum of subarrays minimums"
"""
class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        # first smaller or equal element in left side, save index
        lsmall = [-1 for _ in range(n)]
        st = []
        for i in range(n):
            # here NextGreaterThanOrEqual element
            while len(st) != 0 and arr[st[-1]] > arr[i]:
                st.pop()
            if len(st) != 0:
                lsmall[i] = st[-1]
            st.append(i)

        # first smaller element in right side, save index
        rsmall = [-1 for _ in range(n)]
        st = []
        for i in reversed(range(n)):
            while len(st) != 0 and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st) != 0:
                rsmall[i] = st[-1]
            st.append(i)

        res = 0
        for i in range(n):
            lsb = lsmall[i] + 1 if lsmall[i] != -1 else 0  # left side boundary
            rsb = rsmall[i] - 1 if rsmall[i] != -1 else n - 1  # right side boundary

            subarrays_where_cur_is_min = (i - lsb + 1) * (rsb - i + 1)
            res += subarrays_where_cur_is_min * arr[i]

        return res

    def sumSubarrayMaxs(self, arr):
        n = len(arr)
        lgreat = [-1 for _ in range(n)]
        st = []
        for i in range(n):
            while len(st) != 0 and arr[st[-1]] < arr[i]:
                st.pop()
            if len(st) != 0:
                lgreat[i] = st[-1]
            st.append(i)

        rgreat = [-1 for _ in range(n)]
        st = []
        for i in reversed(range(n)):
            while len(st) != 0 and arr[st[-1]] <= arr[i]:
                st.pop()
            if len(st) != 0:
                rgreat[i] = st[-1]
            st.append(i)

        res = 0
        for i in range(n):
            lsb = lgreat[i] + 1 if lgreat[i] != -1 else 0  # left side boundary
            rsb = rgreat[i] - 1 if rgreat[i] != -1 else n - 1  # right side boundary

            subarrays_where_cur_is_max = (i - lsb + 1) * (rsb - i + 1)
            res += subarrays_where_cur_is_max * arr[i]

        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        minsum = self.sumSubarrayMins(nums)
        maxsum = self.sumSubarrayMaxs(nums)
        return maxsum - minsum
        