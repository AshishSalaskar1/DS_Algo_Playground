"""
Problem: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

- Given array you want to make it have only 1 mountain/peak point. For this you can remove other elements
- Return the minimum number of elements youn need to remove to achieve this 


SOLUTION: Longest Increasing Subsequence + Longest Decreasing Subsequence
- Assume, you try to consider each item as the peak in the resultant array
- If you assume arr[i] as peak, then 
    1. All elements on left will form a LIS
    2. All elements on right will form a LCS
    - Here LIS and LCS will omit the elements which dont follow the order (its LI-Subsequence and not LI-Subset)
    - Now, lis[i]+lcs[i] = length of the final array with arr[i] as peak, this length is what you want to maximise
    - More the final length of the array = lesser number of deletions
- Deletions needed to make arr having one peak at i = (N-lis[i]+lds[i]+1)

Note: 
- Compare deletions only when lis[i] and lds[0] both are > 1.
Why? Because if either lis or lds = 0, means there are no elements to right or left of the cur peak assumed element
- MOUNTAIN/PEAK: needs to have some elements to its right and left (ONE SIDED PEAKS ARE NOT CONSIDERED)
- It should follow pattern: INCREASE -> PEAK -> DECREASE (INCREASE -> PEAK or PEAK -> DECREASE wont be considered as peak)
""" 

class Solution:
    def minimumMountainRemovals(self, arr: List[int]) -> int:
        n = len(arr)
        lis = [1]*n
        lds = [1]*n

        for i in range(1,n):
            for j in range(i):
                if arr[j]<arr[i]:
                    lis[i] = max(lis[i],1+lis[j])
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if arr[j]<arr[i]:
                    lds[i] = max(lds[i],1+lds[j])

        min_removals = n
        for i in range(n):
            if lis[i] > 1 and lds[i]>1:
                min_removals = min(min_removals,n-lis[i]-lds[i]+1)

        return min_removals
        