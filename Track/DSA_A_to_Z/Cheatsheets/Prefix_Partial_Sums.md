# Prefix and Partial Sums Cheatsheet

---

## 🗺️ Quick map
- ➕ 1D prefix sums (range sum in O(1))
- 🔁 Difference arrays (range add updates)
- 🧭 2D prefix sums (rect sums)

## ✅ Study checklist
- [ ] Build once, query many: O(n) build, O(1) query (O(1) per rect with 2D).
- [ ] Indexing off-by-one (inclusive/exclusive) handled?
- [ ] For differences: apply final prefix to realize values.

2D Prefix Sum (from Prefix_Partial_Sums/2D_Prefix_Sum_Rect_Sum.py)
```python
MOD = (10**9)+7

# IMP: THE QUERIES ARE ALL 1-BASED
def prefix_sum(arr, nr, nc):
    """
    Returns the calculated 2D sum array
    """
    prefix =[[0 for _ in range(nc+1)] for _ in range(nr+1)]
    # calculate prefix sum
    for i in range(1,nr+1):
        for j in range(1,nc+1):
            prefix[i][j] = (arr[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1])%MOD
    
    return prefix

def rect_sum(prefix_arr, l, r, u, d):
    return (prefix_arr[d][r] - prefix_arr[u-1][r] - prefix_arr[d][l-1] + prefix_arr[u-1][l-1])%MOD
```

See also in folder
- 2_Good_Nums_Partial_N_Prefix.py (partial sums idea)
- 3_Max_Value_in_Rectangle_after_updates.py (2D diff updates -> realize via prefix)
- 4_AP_on_prefix_sum.py and 5_GP_on_prefix_sum.py (series)
- Max_subarray_Sum_with_length_divisible_by_k.py (prefix sum + mods)
