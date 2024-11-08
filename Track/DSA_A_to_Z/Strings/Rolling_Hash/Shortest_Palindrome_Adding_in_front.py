"""
Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"

VARIATION:
- Find min chars to add to end such that its palindrome
- SAME SOLUTION: but you find LPS ending at n

SOLUTION:
- You need to find min number of chars added to start of string such that entire string is palindrome
- Best case is that entire string is palindrome - no need to add anything

1. 💡Find longest palindrome substring starting for 0
2. If you have this palindrome [0,k] then since [0,k] is already a palindrome, 
    you will add reverse of remanining items to front
3. res = reverse(s[k+1:n]) + s

Note: Since you kept max of string as is (LPS(0, max_ending)), hence additions are always minimum

Example: aacecaaaxy
LPS starting at 0: aacecaa
- Now left part is "a" => |aacecaa|axy
- Reverse the remaining part and add to start
- Res: yxa |aacecaa|axy


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
        self.h1 = Hasher(s, 31, (10**8) + 7)
        self.h2 = Hasher(s, 47, (10**8) + 21)

    def get_hash(self, l, r):
        return (self.h1.get_hash(l, r), self.h2.get_hash(l, r))

    def get_rev_hash(self, l, r):
        return (self.h1.get_rev_hash(l, r), self.h2.get_rev_hash(l, r))


def min_additions_from_start_to_make_palindrome(s):
    hasher = DoubleHasher(s)

    # 1. Find LONGEST PALINDROMIC SUBSTRING STARTING FROM 0/start
    longest_pal_index = (0,0)
    for j in range(len(s)-1, -1, -1):
        if hasher.get_hash(0,j) == hasher.get_rev_hash(0,j):
            longest_pal_index = (0, j)
            break

    longest_pal_from_start = s[longest_pal_index[1]+1:]
    return longest_pal_from_start[::-1]+s




s = "aacecaaa" # "aaacecaaa"
print(min_additions_from_start_to_make_palindrome(s))

s = "abcd" # "dcbabcd"
print(min_additions_from_start_to_make_palindrome(s))

 