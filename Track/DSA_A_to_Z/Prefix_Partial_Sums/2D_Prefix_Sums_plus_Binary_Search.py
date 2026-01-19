"""
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/submissions/1889989039/?envType=daily-question&envId=2026-01-19
"""
from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        nr, nc = len(mat), len(mat[0])

        # prefix_sum[r][c] = sum of submatrix from (0,0) to (r,c), inclusive
        prefix_sum = [[0] * nc for _ in range(nr)]

        # Build 0-based prefix sum
        for r in range(nr):
            for c in range(nc):
                top = prefix_sum[r - 1][c] if r > 0 else 0
                left = prefix_sum[r][c - 1] if c > 0 else 0
                top_left = prefix_sum[r - 1][c - 1] if r > 0 and c > 0 else 0

                prefix_sum[r][c] = top + left - top_left + mat[r][c]

        # Get sum of submatrix with top-left (r1, c1) and bottom-right (r2, c2)
        def get_submatrix_sum(r1: int, c1: int, r2: int, c2: int) -> int:
            total = (
                prefix_sum[r2][c2]
                - (prefix_sum[r1 - 1][c2] if r1>0 else 0)
                - (prefix_sum[r2][c1 - 1] if c1>0 else 0)
                + (prefix_sum[r1 - 1][c1 - 1] if r1>0 and c1>0 else 0)
            )

            return total

        left, right = 1, min(nr, nc)
        best = 0

        # Binary search on side length
        while left <= right:
            mid = (left + right) // 2
            found_valid_square = False

            for r in range(nr - mid + 1):
                if found_valid_square:
                    break
                for c in range(nc - mid + 1):
                    square_sum = get_submatrix_sum(
                        r, c,
                        r + mid - 1, c + mid - 1
                    )
                    if square_sum <= threshold:
                        found_valid_square = True
                        break

            if found_valid_square:
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best
