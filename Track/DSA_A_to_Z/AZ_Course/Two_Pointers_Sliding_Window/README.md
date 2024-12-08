## Main Patterns
1. Two Pointers Strict -> one moves only right and another moves only left
2. Two Pointers Independent -> There are two pointers and they can move left/right independently



## Main Template
**Important things to remember here** <br>
1. INIT ->  `l,r = 0, -1  # WINDOW LENGTH = 0`
2. RESETTING WINDOW -> `if l>r: l++, r=l-1` ( this is needed in case you cant take anything in the current window )
   
```py

def largest_subarray_1_with_k_flips(arr, k):
    n = len(arr)

    res = 0
    l,r = 0, -1  # WINDOW LENGTH = 0
    zero_count = 0

    while r < n:
        # INCREASE RIGHT AS FAR AS POSSIBLE
        while r+1<n and (arr[r+1]==1 or zero_count<k):
            r += 1
            if arr[r] == 0: zero_count += 1
        
        res = max(res, r-l+1)

        if l>r: # 0-ELEMENTS IN WINDOW-> RESET WINDOW
            l += 1
            r = l-1
        else:
            # INCREMENT LEFT 
            if arr[l] == 0: zero_count -= 1
            l += 1

    return res
         
```

## Variations
1. <= k, >=k, ==k
2. Sum of length/length^2 of possible subarrays