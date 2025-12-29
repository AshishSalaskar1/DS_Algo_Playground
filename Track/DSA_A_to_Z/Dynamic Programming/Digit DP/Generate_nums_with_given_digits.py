"""
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/?envType=problem-list-v2&envId=vj6gt2l1


Solution: Classic digit DP + IMP LOGIC IN SKIPPING

# How skipping works in other problems?
-> if number hasnt started yet + you pick "0" => this is same as traling 0s and number is still not started


But here -> you have fixed digits ( it may not consider 0s)
- Hence you need to explictly call in case number is not valid and you want to skip starting it ( same as adding tralings 0 to already non-valid/ non-started number)

EX: N = 500
indxex: 0, bound = True, isvalid = False
- normal problem: 0__ ( same as not picking ), 1__, 2__, 3__, 4__, 5__ ( maxbound)

But here the digits are fixed and maynot contain 0: digits = ["1","3","5","7"]
-> then 0__ is not possible here
- Hence we explicitly call the skip case when isvalid = False
"""
from functools import cache
from typing import List

class Solution:
    def getways(self, r: int) -> int:
        r = str(r)
        n = len(r)

        @cache
        def solve(index: int, bound: bool, isvalid: bool) -> int:
            if index == n:
                return 1 if isvalid else 0

            maxd = int(r[index]) if bound else 9
            ans = 0

            # SKIP STARTING HERE -> same as just picking 0 ( BUT HERE 0 maynot be in digits )
            if not isvalid:
                ans += solve(index + 1, False, False)

            for d in self.digits:
                if d > maxd:
                    break

                newisvalid = isvalid or (d!=0) 
                newbound = bound and (d == maxd)

                ans += solve(index + 1, newbound, newisvalid)

            return ans

        # Start with isvalid = False because we haven't placed any digits yet
        return solve(0, True, False)

    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        self.digits = sorted(int(x) for x in digits)
        return self.getways(n)