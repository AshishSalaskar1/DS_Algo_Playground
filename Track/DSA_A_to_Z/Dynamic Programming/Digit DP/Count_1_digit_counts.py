class Solution:
    def get_ways(self, r: str):
        n = len(r)

        @cache
        def solve(index: int, bound: bool, onecount: int):
            if index == n:
                return onecount

            ans = 0
            maxd = int(r[index]) if bound else 9

            for d in range(maxd + 1):
                newbound = bound and (d == maxd)
                ans += solve(
                    index + 1,
                    newbound,
                    onecount + (1 if d==1 else 0)
                )

            return ans

        return solve(0, True, 0)

    def countDigitOne(self, n: int) -> int:
        return self.get_ways(str(n))
        