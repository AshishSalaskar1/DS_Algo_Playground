"""
You  are given a array of 0s and 1s. You need to find the largest subarray which has all 1s
Plus, you are given `k` -> you can flip any `k` number of values from 0->1 or 1->0

"""


def largest_subarray_1_with_k_flips(arr, k):
    n = len(arr)

    res = 0
    l,r = 0, -1  # WINDOW LENGTH = 0
    zero_count = 0

    while r < n:
        # increase right as far as possible
        while r+1<n and (arr[r+1]==1 or zero_count<k):
            r += 1
            if arr[r] == 0: zero_count += 1
        
        res = max(res, r-l+1)

        if l>r: # WINDOW LENGTH = 0 -> RESET WINDOW
            l += 1
            r = l-1
        else:
            # increment left now
            if arr[l] == 0: zero_count -= 1
            l += 1

    return res
         






arr = [0,1,0,0,1,1,0,0,1]
k = 2
print(largest_subarray_1_with_k_flips(arr, k))


arr = [1,0,0,1,1]
k = 0
print(largest_subarray_1_with_k_flips(arr, k))

arr = [0,0,0,1,1]
k = 0
print(largest_subarray_1_with_k_flips(arr, k))