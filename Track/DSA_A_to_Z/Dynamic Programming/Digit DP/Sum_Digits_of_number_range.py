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









