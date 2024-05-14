"""
PROBLEM:
Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
EASIER STATEMENT:
- Given an array you need to pick "k" elements such that their sum is maximum
- You can only pick contigous elements from first:first+i and last-j:last (either also is fine but len of both == "k")

=> Example: [1,2,3,4,5,6,1], k = 3
- Way 1: [1,2,3],4,5,6,1 --> sum:6
- Way 2: [1,2],3,4,5,6,[1] --> sum:4
- Way 3: [1],2,3,4,5,[6,1] --> sum:8
- Way 4: 1,2,3,4,[5,6,1] --> sum:12
- ANS: 12


SOLUTION 1: Sliding Window
- First pick "k" elements from start->start+k and calcualte their sum
- SLIDING WINDOW
    - Now reduce one from start, and pick from end (reduce = csum-arr[x])

-> res = SUM(arr[:k])
- [left_start, left_end] ...... [right_start, right_end]
- left_start = 0, and right_end = n (FIXED, Remaining 2 are left and right pointers for us) 


SOLUTION 2: Prefix Sum
- Calculate prefix and suffix sums
- res = max(prefix[k-1], suffix[n-k]) # pick first k or last k
- for i: 0->k (exclude k)
    - left_sum = [0:i+1]
    - right_sum = [n-(k-i+1):n]
    - if you have 3 elements in left_sum, then you will pick "k"-(i+1) elements from last/end/back

"""

class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = 0
        prefix = [0] * n
        suffix = [0] * n

        csum = 0
        for i in range(n):
            csum += arr[i]
            prefix[i] = csum
        csum = 0
        for i in reversed(range(n)):
            csum += arr[i]
            suffix[i] = csum

        print(prefix)
        print(suffix)

        # pick k from start and k from end (k from end case cant be checked in for loop)
        # because you start off with 1 element in left (0 -> k)
        res = max(prefix[k-1], suffix[n-k]) # pix

        for i,x in enumerate(arr[:k]): # you can pick atmost k elements from start
            # sum of elements picked from start
            left_subarray_sum = prefix[i]
            right_subarray_sum = 0

            # elements picked from end 
            n_end = k-(i+1) # number of elements to pick from last/end
            right_start = n - n_end 

            if right_start < n: # you have picked atleast 1 element from end
                right_subarray_sum = suffix[right_start]
            
            res = max(res, left_subarray_sum + right_subarray_sum)
        
        return res
                
                


    def maxScoreSlidingWindow(self, arr: List[int], k: int) -> int:
        n = len(arr)

        if n==k: # you can pick all array elements
            return sum(arr)
        
        csum = sum(arr[:k]) # pick all k from starting
        res = csum

        left_end = k-1 # u have picked all k from start
        right_start = n # u havent picked any from right, so its N and not N-1

        while left_end >= 0 and right_start >= 0: # till you can decrement both
            csum -= arr[left_end] # remove left_end

            left_end -= 1 # decrease one from left end subarray
            right_start -= 1 # add one to right end subarray

            csum += arr[right_start] # you added on to right end subarray
            res = max(res, csum)
        
        return res

        