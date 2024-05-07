"""
DP USED ->  1 BASED (to avoid extra conditions)

CASES
- you know that len(LCS) = dp[n1][n2]
- Start from (n1,n2) bottom last element => (i=n1,j=n2)
- Now you can move in 3 directions -> UP, LEFT, Diagonally TOPLEFT
    1. In case s1[i-1][j-1] => same chars in both arrays => ADD IN ANSWERS
        Since the chars are same, you came from (i-1, j-1) i.e diagonally
    2. UP > LEFT => you came from UP
    3. LEFT >= UP => you can from left (ASSUMING EQUAL MEANS LEFT)


"""

def findLCS(n1: int, n2: int, s1: str, s2: str) -> str:
    if n1 == 0 or n2==0:
        return ""
    
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    for i in range(n1+1):
        for j in range(n2+1):
            if i==0 or j==0:
                dp[i][j] == 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs_len = dp[-1][-1]
    res = []
    i,j = n1, n2

    while i>0 and j>0:
        if s1[i-1] == s2[j-1]: # you came from i-1, j-1 (since you move diagonally only when last chars are same) => THIS IS ALSO PART OF ANSWER
            res.insert(0, s1[i-1])
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]: # you can either move up or right (pick one which gives you max)
            i -= 1
        else:
            j -= 1
    
    return "".join(res)


