""""
PROBLEM:

Given an array, find the number of subarrays having distinct elements <= `k` in them

"""

def distinct_eles_less_than_k(arr: list[int], k: int) -> int:
    n = len(arr)
    res = 0
    l,r = 0, -1

    hmap = {}

    while r<n:
        print("=>", l, r, hmap)
        # move right as far as possible
        while r+1<n and (arr[r+1] in hmap or len(hmap)<k):
            r += 1
            hmap[arr[r]] = hmap.get(arr[r],0)+1

        res += (r-l+1) # num of subarrays starting at l and ending at r

        if l>r: # 0 items in subarray
            l += 1
            r = l-1
        else:
            hmap[arr[l]] -= 1
            if hmap[arr[l]] == 0:
                hmap.pop(arr[l])
            l += 1
        
        print("<=", l, r, hmap)
    
    return res





arr = [1,2,1,3]
k = 2
print(distinct_eles_less_than_k(arr, k )) # RES = 8
