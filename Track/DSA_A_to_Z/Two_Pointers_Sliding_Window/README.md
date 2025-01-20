## Main Patterns
1. Two Pointers Strict -> one moves only right and another moves only left
2. Two Pointers Independent -> There are two pointers and they can move left/right independently



## Main Template - For (2) pattern - Mostly Asked
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
|  **PROBLEM**: Given an array, find the number of subarrays having distinct elements <= `k` in them
 ( Solved in 2_Num_subarrays_with_distinct_elements_less_k.py)

**Variations that can be formed**<br>
1. <= k, >k, ==k
2. Sum of length/length^2 of possible subarrays


**Solutions** 
1. **Follow up: `>=k`**
    - Num of subarrays `>=k` => Num of subarrays `<=N` - Num of subarrays `<=k-1` (will be <k in case its `>k`)
    - => `n*(n+1)//2` - Num of subarrays `<=N`
2. **Follow up: `>k`**
    - Num of subarrays `>k` => Num of subarrays `<=N` - Num of subarrays `<=k` 
    - => `n*(n+1)//2` - Num of subarrays `<=k`
3. **Follow up: `== k`**
    - Num of subarrays `==k` => Num of subarrays `<=k` - Num of subarrays `<=k-1` 
    - => Num of subarrays `<=k` - Num of subarrays `<=k-1`
4. 💡 **Sum of length of all possible subarrays each having distinct numbers <=k**
    - In the existing code, after we move the `right` pointer as much as possible, we then get the `len` = `right`-`left`=1
    - This means that we have `len` number of subarrays answers
    - SIMILARLY, `length of all these possible subarrays` = `len*(len+1)/2` ( so you do ans+=len*(len+1)//2 in each answer addition)
    - **Why?** You have `len` number of possible subarrays, first one will have size 1, second as size 2 so on and last one will have size = `len` => 1+2+3+.....+`len`  = **len*(len+1)//2**


## Practice Problems
- https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/3771308/java-c-python-sliding-window/?envType=daily-question&envId=2024-12-11
- https://leetcode.com/discuss/study-guide/3630462/Top-20-Sliding-Window-Problems-for-beginners
- https://leetcode.com/problem-list/two-pointers/