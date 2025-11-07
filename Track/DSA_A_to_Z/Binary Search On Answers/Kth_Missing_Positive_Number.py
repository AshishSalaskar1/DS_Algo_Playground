"""
Problem:
- Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
- Return the kth positive integer that is missing from this array. [0 is not considered missing]
- This kth number can be > max(arr) also: [1,3,5], 5th missing number: 8


SOLUTION 1 - O(N):
- Take missing array of size max(arr)+1 and mark all elements present as visited
- Then mis_count=0, go on iterating the missing array and mis_count++ where it was visited and return if k==mis_count
- Answers lies outside this
    - res = [len(arr)-1] - [k-mis_count]
    - [len(arr)-1] -> you used for 1-based indexing
    - [k-mis_count] -> already u have found mis_count missing, u need (k-mis_count)th missing number
    - N this will be (k-mis_count) after max(arr) = len(arr)-1
"""
class Solution:
    # USE BINARY SEARCH ON ANSWERS
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)-1

        while lo<=hi:
            mid = lo + (hi-lo)//2
            n_miss = arr[mid]-(mid+1)
            if n_miss < k:
                lo = mid+1
            else:
                hi = mid-1

        # hi -> will point to index in arr for which n_missing <= k (NEAREST)
        # For this formula refer: https://takeuforward.org/arrays/kth-missing-positive-number/
        return  k + hi + 1 

    def findKthPositiveSlower(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        missing = [True for _ in range(max_num+1)]

        for x in arr:
            missing[x] = False
        
        mis_count = 0
        for idx, x in enumerate(missing[1:]): # start from 1
            if x is True:
                mis_count += 1
                if mis_count == k:
                    return idx+1 #because u ignore fist ele => missing[1:]
        

        return len(missing)-1 + (k-mis_count)



        