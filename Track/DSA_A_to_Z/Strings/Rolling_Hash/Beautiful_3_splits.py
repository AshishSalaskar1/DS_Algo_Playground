"""
PROBLEM: https://leetcode.com/problems/count-beautiful-splits-in-an-array/

DISCUSSIONS: https://leetcode.com/problems/count-beautiful-splits-in-an-array/solutions/6147791/beats-100-prefix-hashing-rolling-hash-2-solutions

- Current code is neater but gets TLE, since function calls take some more space.
- You can stuff everything up in one functions such you dont make function calls to eliminate TLE

"""
from functools import lru_cache
class RollingHash:
    def __init__(self, arr, k, modprime):
        self.k = k
        self.modprime = modprime
        n = len(arr)

        self.hash = [0] * (n + 1)
        self.pow = [1] * (n + 1)

        for i in range(1, n + 1):
            self.pow[i] = (self.pow[i - 1] * k) % self.modprime
            self.hash[i] = (self.hash[i - 1] * k + arr[i - 1]) % self.modprime

    def get_hash(self, l, r):
        """
        Get the hash of the subarray arr[l:r+1].
        """
        return (self.hash[r + 1] - (self.hash[l] * self.pow[r - l + 1]) % self.modprime + self.modprime) % self.modprime
    
    @lru_cache
    def is_prefix(self, l1, r1, l2, r2):
        """
        Check if the subarray arr[l1:r1+1] is a prefix of arr[l2:r2+1].
        """
        len1 = r1 - l1 + 1
        len2 = r2 - l2 + 1

        if len1 > len2:
            return False

        hash1 = self.get_hash(l1, r1)
        hash2 = self.get_hash(l2, l2 + len1 - 1)

        return hash1 == hash2

class Solution:
    def beautifulSplits(self, nums):
        n = len(nums)
        if n < 3:
            return 0  # We need at least 3 elements to make a valid split

        mod = 1_000_000_007
        base = 31

        hasher = RollingHash(nums, base, mod)

        count = 0

        # Iterate over possible i and j such that 1 <= i < j < n
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                valid = False

                # Check if nums1 is a prefix of nums2
                if hasher.is_prefix(0, i - 1, i, j - 1):
                    valid = True

                # Check if nums2 is a prefix of nums3
                if not valid and hasher.is_prefix(i, j - 1, j, n - 1):
                    valid = True

                if valid:
                    count += 1

        return count

