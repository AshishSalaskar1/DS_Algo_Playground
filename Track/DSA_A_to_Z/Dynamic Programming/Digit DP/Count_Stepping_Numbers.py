"""
https://leetcode.com/problems/count-stepping-numbers-in-range/description/?envType=problem-list-v2&envId=vj6gt2l1

SOLUTION:
- Classic Digit DP
- Handle edge cases -> dont include trailing 0s
"""
MOD = (10**9) + 7
class Solution:
    def getways(self, r: int) -> int:
        r = str(r)
        n = len(r)

        @cache
        def solve(index: int, bound: bool, prevnum: int) -> int:
            # reach end not all are trailing 0s
            if index == n:
                return 1 if prevnum != -1 else 0
            
            maxdig = int(r[index]) if bound else 9
            ans = 0

            for d in range(maxdig+1):
                newbound = bound and d==maxdig
                if prevnum == -1 and d==0:  # not starting yet - adding trailing zeroes
                    ans += solve(index+1, newbound, -1)
                elif prevnum == -1 and d!=0: # new number started nothing previous to check
                    ans += solve(index+1,newbound,d )
                else: # there is previous number
                    if abs(prevnum-d) == 1:
                        ans += solve(index+1,newbound,d )
                ans = ans%MOD

            return ans

        return solve(0,True,-1)

    def countSteppingNumbers(self, low: str, high: str) -> int:
        return (self.getways(int(high)) - self.getways(int(low)-1)) % MOD
        