# Dynamic Programming Cheatsheet

Repo snippets (no logic modified)

Subset sum equal to target (from DP_Subsequences/Subset_sum_equal_to_target_(DP-_14).py)
```python
def subsetSumToK(n, k, arr):
    dp = [[False for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        for j in range(k+1):
            if j==0: # to make 0 target -> dont pick anything \
                dp[i][j] = True
            elif i==0: # you have only first element (1 coin)
                dp[i][j] = True if j==arr[i] else False
            elif arr[i] > j: # you cant pick current one (curr > needed_target)
                dp[i][j] = dp[i-1][j]
            else: # you can either pick this one or ignore
                dp[i][j] = dp[i-1][j-arr[i]] or dp[i-1][j]
    
    return dp[-1][-1]
```

See also in folder for more DP patterns
- Knapsack, Unbounded Knapsack, Coin Change, Target Sum, Partition Equal Subset Sum
- LIS and strings DP folders for sequence-based patterns
- DP_on_Trees for tree-based DP

---

## At a glance
- Define state: dp[i][t] meaning using first i items achieve target t (as in subset-sum). Initialize base cases explicitly.
- Transitions: pick vs not-pick for 0/1 choices; order matters in permutations vs combinations.
- Space: Often compress 2D to 1D (reverse iterate when transitioning on previous row/simple knapsack).
- Complexity: O(n*target) time/memory for subset-sum; be mindful of constraints.

## Pitfalls
- Off-by-one in indices when mapping 1-based descriptions to 0-based arrays.
- Using sentinel values consistently (inf / -inf / None) and guarding arithmetic with them.
- Mutation hazards when compressing to 1D (iterate direction correctly).

---

## 🗺️ Quick map
- 🧩 Subsequence/knapsack family (pick/not-pick)
- 🧮 Table vs space-compressed 1D
- 🧷 Base cases and sentinels

## ✅ Study checklist
- [ ] Clear state definition (indices/ranges/target)?
- [ ] Base cases and transitions written before coding?
- [ ] Space compression direction correct?
- [ ] Time/space within constraints for n, target?
