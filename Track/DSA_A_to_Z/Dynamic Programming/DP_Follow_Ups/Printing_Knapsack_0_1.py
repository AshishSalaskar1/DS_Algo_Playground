"""
Knapsack => Also print the ITEMS TO PICK to get max profit
Knapsack: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

EXAMPLES
1. W=5
weight = [ 1, 2, 3]
profit = [10,15,40]

Maximum Value: 55 (Pick items with weight 2 and 3)

2. W=10
weight = [ 2, 3, 4, 5, 9]
profit = [ 3, 4, 8, 8, 10]
Maximum Value: 16 (Pick items with weights 3 and 5, values 4 and 8)

3. W=9
weight = [ 1,  4,  5,  6,  3]
profit = [10, 40, 50, 70, 30]
Maximum Value: 100 (Pick items 6, 3)


RECURSIVE PRINTING
- MAIN LOGIC: Write another fn which calls the main functions 
-> USE THE ACTUAL CACHED FUNCTOIN n NOT THE DP ARRAY
    - Dp array in case wont store the base cases => those are directly returned

- assume fn(i, w) is ur Memoized function
- print_path(i, w):
    1. if base case => return
    2. Explore all possible cases [USE MEMOIZED DP FUNCTION FOR THIS - O(1)]
       dont_take = fn(i-1, w)
       take = fn(i-1, w-weights[i]) + profit (Only if weights[i] < w)
    3. Call print_path with actual recursion calls 

- Use recursive-fn to get take/not_take values and decide if it was picked up
  BUT, use the print function for ACTUAL RECURSION CALLS
  [YOU SHOULD NEVER RETURN THE RESULTS FROM MEMOIZED FUNCTOIN]


TABULATION PRINTING
- Your max profit is at dp[n][w] (Max profit u can make by including 0->n elements and bag size = W)

row, col = n, w
1. W=5, weight = [ 1, 2, 3], profit = [10,15,40]

N   0     1     2   3   4    5 <- CAPACITY/W
0  [ 0,   0,    0,  0,  0,   0]
1  [(0), 10,   10, 10, 10,  10]
2  [ 0,  10, (15), 25, 25,  25]
3  [ 0,  10,   15, 40, 50, (55)]

INIT: row=3, col=5
-> YOU DIDNT TAKE CUR ELEMENT = dp[row][col] == dp[row-1][col] 
    - "col" represent left weight, since your weight remained same -> you didnt pick current element

-> YOU TOOK CUR ELEMENT = dp[row][col] == dp[row-1][col]
    - Now we need to find which element in previous row you came from (FIND COL in ROW-1)
    dp[row][col] = 55, profit[3-1] = 40
    - YOU TOOK THIS ELEMENT -> so you added 40 profit after picking
    - So if you added 40 to profit now, your last profit state must be 55-40 = 15
    - Search in prev row, which col corresponds to 15
        => Its col=2, dp[2][2] = 15
    
    row -= 1
    col = 2 (IN CASE OF DONT TAKE, col remains the same)


LOGIC:
- if you are at dp[r][w] 
then you might have come from 2 places
1. dp[row-1][col] if dp[row-1][col] = dp[row][col] | capacity/col didnt change
2. If picked, then you can from col in row-1, having profit(dp[ro1-1][col]) = dp[row][col]-profit[row]
"""
from functools import lru_cache

class RecursiveSol:
    def __init__(self) -> None:
        pass
    
    @lru_cache
    def fn(self, i, rem_weight):
        if i == 0 or rem_weight == 0: return 0

        # CANT PICK
        if self.weight[i-1] > rem_weight: 
            return self.fn(i-1, rem_weight)
        else: # CAN PICK
            return max(
                self.fn(i-1, rem_weight), # DONT PICK
                self.profit[i-1] + self.fn(i-1, rem_weight-self.weight[i-1]) # PICK
            )

    def solve(self, w, weight, profit):
        self.weight = weight
        self.profit = profit
        self.n = len(weight)
        self.w = w
        
        return self.fn(self.n, w)
    
    def print_solution(self, i, rem_weight):
        if i == 0 or rem_weight == 0:
            return
        
        dont_take = self.fn(i-1, rem_weight)
        
        if self.weight[i-1] > rem_weight:  # MOVE AHEAD IN RECURSION - call print
            return self.print_solution(i-1, rem_weight)
        else:
            take = self.profit[i-1] + self.fn(i-1, rem_weight-self.weight[i-1])
            if dont_take >= take: # decide if it was picked up
                self.print_solution(i-1, rem_weight)
            else:
                print(f"Pick up element {i-1} => {self.weight[i-1]} {self.profit[i-1]}")
                self.print_solution(i-1, rem_weight-self.weight[i-1])
                
        



class TabulationSol:
    def __init__(self) -> None:
        pass
    

    def solve(self, w, weight, profit, print_sol = False):
        n = len(weight)
        
        dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(w+1):
                if i==0 or j==0: # 0 elements or 0 bag capacity
                    dp[i][j] = 0
                elif weight[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i-1][j-weight[i-1]] + profit[i-1]
                    )
        
        print(*dp, sep="\n")

        if not print_sol:
            return dp[n][w]

        
        # print solution
        row, col = n, w
        while row > 0:
            # if it was not then dp[row-1][col] == dp[row][col]
            if dp[row-1][col] == dp[row][col]:
                col = col
            else: # it did get picked 
                print(f"TAKE {row-1} => {weight[row-1]} : {profit[row-1]}")
                last_row_profit = dp[row][col]-profit[row-1]
                for last_col in range(0, w+1):
                    if dp[row-1][last_col] == last_row_profit:
                        col = last_col
                        break
                        
            row -= 1


        return dp[n][w]




W=5
weight = [ 1, 2, 3]
profit = [10,15,40]
sol = RecursiveSol()
print(sol.solve(W, weight, profit))
sol.print_solution(sol.n, W)

W=10
weight = [ 2, 3, 4, 5, 9]
profit = [ 3, 4, 8, 8, 10]
sol = RecursiveSol()
print(sol.solve(W, weight, profit))
sol.print_solution(sol.n, W)


W=9
weight = [ 1,  4,  5,  6,  3]
profit = [10, 40, 50, 70, 30]
sol = RecursiveSol()
print(sol.solve(W, weight, profit))
sol.print_solution(sol.n, W)

# TABULATION

print()
sol = TabulationSol()

W=5
weight = [ 1, 2, 3]
profit = [10,15,40]
sol = TabulationSol()
print(sol.solve(W, weight, profit, True))

W=10
weight = [ 2, 3, 4, 5, 9]
profit = [ 3, 4, 8, 8, 10]
sol = TabulationSol()
print(sol.solve(W, weight, profit, True))


W=9
weight = [ 1,  4,  5,  6,  3]
profit = [10, 40, 50, 70, 30]
sol = TabulationSol()
print(sol.solve(W, weight, profit, True))


