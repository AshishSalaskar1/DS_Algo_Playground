"""
Problem: https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

- MAIN LOGIC

1. Why you need number_count, waviness
- number_count: total number of unique numbers (NOT DIGITS)
- Waviness: count of wavy digits in all unique numbers

Lets say current number is "123" further is getting generated
- Now the current waviness (1) will get added to every unique that can be generated starting from "123"
- Hene you need the total count of numbers which can be generated eventually in this path


"123" - add=1
cnt,sm = solve() -> will return the waviness n count from here after "123"

- So surely that cnt gets added to ans_cnt
ans_cnt += cnt

- total waviness added: sum + (add*cnt) => the current waviness gets added to every unique number after "123xxx"
hence = add*cnt 
ans_sum += sm + add * cnt
"""
from functools import cache

class Solution:
    def digit_dp(self, num: int) -> int:
        if num <= 0:
            return 0

        s = str(num)
        n = len(s)

        @cache
        def solve(idx: int, bound: bool, started: bool,
                  prev2: int, prev1: int):

            if idx == n:
                return (1, 0)  # (count, waviness)

            ans_cnt = ans_sum = 0
            maxdigit = int(s[idx]) if bound else 9

            for d in range(maxdigit + 1):
                newbound = bound and (d == maxdigit)

                if not started:
                    if d == 0:
                        cnt, sm = solve(idx + 1, newbound, False, -1, -1)
                    else:
                        cnt, sm = solve(idx + 1, newbound, True, -1, d)

                    ans_cnt += cnt
                    ans_sum += sm
                    continue

                # DIGIT IS PEAK OR VALLEY
                # <prev2, prev1, d> => You check if `prev1` is the peak
                add = 0
                if prev2 != -1 and ( # to have waviness its length >= 3
                    (prev2 < prev1 > d ) or
                    (prev2 > prev1 < d )
                ):
                    add = 1 # add one waviness

                cnt, sm = solve(idx + 1, newbound, True, prev1, d)

                ans_cnt += cnt
                ans_sum += sm + add * cnt

            return (ans_cnt, ans_sum)

        return solve(0, True, False, -1, -1)[1]

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.digit_dp(num2) - self.digit_dp(num1 - 1)