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
