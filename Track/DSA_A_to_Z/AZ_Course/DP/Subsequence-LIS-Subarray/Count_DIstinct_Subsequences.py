"""
Problem: https://leetcode.com/problems/distinct-subsequences-ii/

Find count of all distinct subsequences that can be formed (ignoring "")


Implementation:
1. dp[i] = NUMBER OF NEW sbsqs ending at i (i.e by adding s[i] to all previous possible sbsqs)
    - dp[i] doesnt store all subsequences from s[0:i]
    - Only stores the new subsequences formed by adding s[i] with all its previously possible sbsqs

2. prefix[i] = SUM of COUNT of all possible sbsqs till i (including s[i])

- Both dp and prefix count are unique/distinct ones only

EXAMPLE:
abaab = 17
1. a  -> a - 1
2. ab  -> ab, b - 2
3. aba -> aa, aba, ba, a - 4 -->  aa, aba, ba, [a]x => aa, aba, ba - 3
4. abaa -> aa, aba, ba, aaa, abaa, baa, aa
    - aa -> came from sbsqs of (1 - a, you added "a" to all these existing subsequences)
    - aba, ba -> came from sbsqs of (1 - ab)
    - aaa, abaa, baa, aa -> came from sbsqs of (1 - aba)

num_distinct_sbsqs[i] = num_distinct_sbsqs[i-1] - new_subsequences_formed_at[j] (j -> last char same as s[i]) 
"""
MOD = (10**9)+7

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        prefix = [0 for _ in range(n + 1)]

        last_seen = {}
        prefix[0] = 1  # Base case: empty string contributes one subsequence
        dp[0] = 1 # Base case: empty string contributes one subsequence

        for i in range(1, n + 1):
            ch = s[i - 1]

            # Add new subsequences by appending the current character = you add s[i-1] to all possible subsequences before this 
            dp[i] = prefix[i - 1] % MOD

            # Remove duplicates caused by previously seen characters
            if ch in last_seen:
                # last_seen[ch]-1 -> You need the TOTAL_COUNT_SBSQS before last_seen[ch]
                # prefix[last_seen[ch]] -> will contain COUNT_SBSQS before + last_seen[ch]
                count_last_seen = prefix[last_seen[ch]-1] # number of subsequences before "last_seen_char"

                # count last seen are removed 
                dp[i] = (dp[i] - count_last_seen) % MOD 

            # Update prefix sum for this position
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD

            # Update last seen position for the current character
            last_seen[ch] = i 

        # Result is the total number of distinct subsequences
        return (prefix[n] - 1) % MOD  # Subtract 1 to exclude the empty subsequence


# Example usage
sol = Solution()
print(sol.distinctSubseqII("ababc"))  # Example test case
