"""
PROBLEM: https://leetcode.com/problems/longest-palindromic-substring/
Sol: https://leetcode.com/problems/longest-palindromic-substring/solutions/759291/straight-forward-short-and-clean-python-dp-with-detailed-simple-explanation/

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


SOLUTION
- if len(str) == 1, then its a palindrome
- if len(str) == 2, & str[start] == str[end] => then its palindrome
- len(str) > 2, (str[start]==str[end]) && is_palindrome(str[start+1:end-1])
    ababa -> a==a and is_palindrome(bab)

Here, in our DP table -> i=startIndex, j=endIndex
1. We first fill dp[i][j] where i==j with 1 [Len == 1]
2. Then fill dp[i][j] where (j-i)=1 [Len == 2]
3. Fill remaining Lengths

"""




def lps(s: str) -> str:
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    res, maxlen = -1, -1

    # palindomes of len=1
    for i in range(n):
        dp[i][i] = True
        res = s[i]
        maxlen = 1
    
    # palindromes of len=2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            res = s[i:i+1+1]
            maxlen = 2
    
    # palindromes if len>2 = 3,4....
    for length in range(3, n+1):
        for i in range(n-length+1):
            l,r = i, i+length-1
            if s[l] == s[r] and dp[l+1][r-1]:
                dp[l][r] = True
                if length > maxlen:
                    maxlen = length
                    res = s[l:l+length] 
    
    return res  

s = "babad"
print(lps(s))

s = "cbbd"
print(lps(s))