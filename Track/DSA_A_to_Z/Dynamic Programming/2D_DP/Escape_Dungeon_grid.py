"""
PROBLEM:
You have a grid, you need to travel from (0,0) to (n,m). At each point you can lose/gain energgy (Including first and last cell)
-> Need minimum energy that you need to start such that you reach (n,m) from (0,0)


SOLUTION:

dp[i][j] = minimum energy needed to reach (n,m) from (0,0)

1. If you are in last row -> you can only move right
2. If you are in Right most col -> you can only move down
3. Other cells, you can go RIGHT or DOWN

RECURSIVE CALCULATION
- How to calculate dp[i][j]? We need to check 2 options dp[i+1][j] and dp[i][j+1]
    1. dp[i+1][j] - dungeon[i][j]
    2. dp[i][j+1] - dungeon[i][j]
- Why? 
    - To move from next to end you need dp[i+1][j] or dp[i][j+1] energy
    - Plus you need dungeon[i][j] to exit from current note
    - So dp[i+1][j]/dp[i][j+1] - dungeon[i][j] (if dungeon[i][j] is -ve, you add it to next steps else if its +ve you subtract it)
- Answers from both options?
    1. Both are negative? You dont need excess energy to move -> Means you only need unit energy to move (i.e 1)
    2. Both are positive? You need excess energy -> But TAKE MINIMUM OF BOTH OPTIONS

"""

def minInitialHealth(dungeon, n, m):
    # Create a DP table to store the minimum health needed at each cell
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the bottom-right corner (exit room)
    dp[n-1][m-1] = max(1, 1 - dungeon[n-1][m-1])
    
    # Fill the last row (only move rightward)
    for j in range(m-2, -1, -1):
        dp[n-1][j] = max(1, dp[n-1][j+1] - dungeon[n-1][j])
    
    # Fill the last column (only move downward)
    for i in range(n-2, -1, -1):
        dp[i][m-1] = max(1, dp[i+1][m-1] - dungeon[i][m-1])
    
    # Fill the rest of the DP table
    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
    
    # The minimum health needed at the start is in dp[0][0]
    return dp[0][0]

def main():
    T = int(input())  # Number of test cases
    
    for _ in range(T):
        n, m = map(int, input().split())
        dungeon = []
        
        for _ in range(n):
            row = list(map(int, input().split()))
            dungeon.append(row)
        
        result = minInitialHealth(dungeon, n, m)
        print(result)

# Run the main function to handle input and output
if __name__ == "__main__":
    main()

