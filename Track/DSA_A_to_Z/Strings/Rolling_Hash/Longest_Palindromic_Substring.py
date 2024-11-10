"""
PROBLEM: https://leetcode.com/problems/longest-palindromic-substring/
Sol: https://leetcode.com/problems/longest-palindromic-substring/solutions/759291/straight-forward-short-and-clean-python-dp-with-detailed-simple-explanation/

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

SOLUTION:
- Same logic as Longest Common Substring, but you cant use binary search here
- WHY? Lets say there is no palindromic substring of size `k` doesnt mean that you cant have palindromic substrings of size > `k`

Ex: babad
size=2 -> there is no PalindromicSubstring => IN BS you will then seach in [0,1] (BUT THIS IS WRONG)
size=3 -> there is PalindromicSubstring = aba

"""
class Hasher:
    def __init__(self, s, base_system, modnum) -> None:
        self.n, self.k, self.p = len(s), base_system, modnum
        self.rev_hash = [0] * (self.n + 1)  # only for REVERSE
        self.hash = [0] * (self.n + 1)      # 1-BASED
        self.pow = [1] * (self.n + 1)       # 1-BASED initialized with 1

        # Compute forward hash and power values
        for i in range(1, self.n + 1):
            self.hash[i] = ((self.hash[i - 1] * self.k) + ord(s[i - 1]) + 1) % self.p
            self.pow[i] = (self.pow[i - 1] * self.k) % self.p

        # Compute reverse hash
        for i in range(self.n - 1, -1, -1):
            self.rev_hash[i] = ((self.rev_hash[i + 1] * self.k) + ord(s[i]) + 1) % self.p

    def get_hash(self, l, r):
        return (self.hash[r + 1] - self.hash[l] * self.pow[r - l + 1]) % self.p

    def get_rev_hash(self, l, r):  # hash of [l <- r]
        return (self.rev_hash[l] - self.rev_hash[r + 1] * self.pow[r - l + 1]) % self.p


class DoubleHasher:
    def __init__(self, s) -> None:
        self.s = s
        self.h1 = Hasher(s, 151, (10**8) + 7)
        self.h2 = Hasher(s, 181, (10**8) + 21)

    def get_hash(self, l, r):
        return (self.h1.get_hash(l, r), self.h2.get_hash(l, r))

    def get_rev_hash(self, l, r):
        return (self.h1.get_rev_hash(l, r), self.h2.get_rev_hash(l, r))


def is_k_substring_palindrome(hasher, size):
    n = len(hasher.s)
    for i in range(0, n - size + 1):
        if hasher.get_hash(i, i + size - 1) == hasher.get_rev_hash(i, i + size - 1):
            return True  # Found a palindromic substring of the given size
            # return hasher.s[i: i + size] # in case you want to print
    return False


def lps(s):
    hasher = DoubleHasher(s)

    for size in range(len(s),-1,-1):
        if is_k_substring_palindrome(hasher, size):
            return size


# Testing with examples
s = "babad"
print("Length of Longest Palindromic Substring:", lps(s))  # Expected output: 3 (for "bab" or "aba")
