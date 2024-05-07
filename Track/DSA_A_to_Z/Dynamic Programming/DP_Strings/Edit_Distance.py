"""
PROBLEM:
- Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. You have the following three operations permitted on a word:
    Insert a character | Delete a character | Replace a character

SOLUTION:
- Consider two strings str1 and str2, you have 3 cases
1. Either strings is empty -> res=len(non_empty_string) [Because you will either delete all char from non-empty str or add all into empty one]
2. Last chars of both strings are same -> you dont need to change them
3. Do some change -> 1 work done
    That change can be 
        1) INSERT a char in str1 which is same as last char in str2
        2) DELETE last char from str1
        3) REPLACE the last char in str1 with same as last char in str2

"""

class Solution:
    def solve(self,i,j):
        if i<0 or j<0:
            return 0

        if i==0: # 0 means First String is EMPTY (check <0 in case you are using 0 based indexing)
            return j
        if j==0:
            return i

        if self.word1[i-1] == self.word2[j-1]:
            return self.solve(i-1, j-1)
        else:
            return 1 + min(
                self.solve(i-1, j),
                self.solve(i,j-1),
                self.solve(i-1,j-1)
            )
        
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        self.n1, self.n2 = n1, n2
        self.word1, self.word2 = word1, word2

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0: # i==0, means str1 is empty
                    dp[i][j] = j
                elif j==0:  # i==0, means str2 is empty
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]: # last chars are same -> no need to do anything
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j-1], # insert a char in str1 same as last char of str2 (ash,bed => ashd,bed -> ash,be )
                        dp[i-1][j], # delete the last char in str1 
                        dp[i-1][j-1] # replace last char of str1 same as last char of str2 ( now str1 and str2 have last chars same)
                    )
        
        return dp[n1][n2]

