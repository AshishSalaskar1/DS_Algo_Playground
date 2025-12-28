# DIGIT DP

### Resources
- https://www.youtube.com/watch?v=yNKhlzYjDDs
- https://www.youtube.com/watch?v=cthI6e5KGgg&list=PLps5s7uQvz8kSh36EwW4_o1Qqjfm2vA1r&index=1
- https://leetcode.com/problem-list/2chw7ar7/
- Great Editorial: https://leetcode.com/discuss/post/7378015/digit-dp-templates-by-csenshi-uwlc/

### When to use
- You are given a range **L** to **R**
- Find count/print **numbers** from **L**  to **R** that satisfy some condition


### IDEA
- Think of this as  TRIE, you start filling digits from L->R. 
- Now when you fill, you may have certain conditions on what digits can you use here
- The TRIE + BOUND makes sure you traverse from `L`->`R`
- The answer calculate and pruning depends on your questions now
![Screenshot-from-2025-12-28-23-22-07.png](https://i.postimg.cc/ZRh4B6QM/Screenshot-from-2025-12-28-23-22-07.png)

#### Main Idea
`ANS(L,R)` = `ANS(R)` - `ANS(L-1)` ( *in case L and R are both inclusive* )
 
#### `bound` variable
- This indicates whether the current state ( index ) has some bound or not
1. If no bound -> pick any digit from 0->9
2. If bound -> pick digit from `0->int(r[index])
- 💡 **If a state is NOT BOUND -> then ALL IT SUBSETS are never bound**
    - Ex: In the above example, `0__` is unbound -> you can chose anything going ahead
    - Why? Since first digit `0` < `2` -> no matter what you chose after it will never be greater than `2xx` which is our `R` range

##### 💡  IMPORTANT CONSIDERATIONS
- **If a state is NOT BOUND -> then ALL IT SUBSETS are never bound**
    - Ex: In the above example, `0__` is unbound -> you can chose anything going ahead
    - Why? Since first digit `0` < `2` -> no matter what you chose after it will never be greater than `2xx` which is our `R` range
- **STATES**
  1. `index` or we also call this as level
  2. `bound` whether the current state is bound or not
  3. `ans` based states as and when needed
- 💡  Bugs with `cache`
  - `cache` decorator in python lives for entire scope -> and here you make 2 calls to `solve()`
  - This will cause the cache to be there for both
  - SOLUTION 1: You `fn.cache_clear()`
  - SOLUTION 2: Make sure `cache`d function is different and can be called multiple times independently
- **Trailing 0 Issues**
  - Remeber you can select `0` also -> but when you select `0` the counting needed for problems can get messed up
  - Ex: count number of digit/even-odd digits. In this case `0001` has only 1 digit -> You need to ignore trailing 0s
  - 💡 Use variable `validNum` that is set to True when the first non-zero digit is seen OR `nCount` which is count of digits taken
  - Check `Num_Beautiful_integers_divisible_by_k.py`, `Count_balanced_integers_in_range.py`

#### **How does DP help here**
- TRUST ME BRO ~!!!!


### Example 1: Given a range L,R -> Find the sum of digits for eahc number that fall in this range
```py
"""
l,r = 9, 15
9  - 9 
10 - 1
11 - 2
12 - 3
13 - 4
14 - 5
15 - 6

SUM = 30

"""

from functools import lru_cache

def digit_sum_upto(x: int) -> int:
    s = str(x)
    n = len(s)

    @lru_cache(None)
    def solve(index: int, bound: bool, csum: int) -> int:
        if index == n:
            return csum

        ans = 0
        maxdig = int(s[index]) if bound else 9

        for d in range(maxdig + 1):
            ans += solve(
                index + 1, # index
                bound and (d == maxdig), # new bound
                csum + d # new sum
            )
        return ans

    return solve(0, True, 0)


# Example
l, r = 9, 15

result = digit_sum_upto(r) - digit_sum_upto(l - 1)
print(result)  # 30

```