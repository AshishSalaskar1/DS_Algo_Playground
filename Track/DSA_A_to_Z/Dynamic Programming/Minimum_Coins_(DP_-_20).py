"""

MAIN:
- When its asked min/max NUMBER OF COINS -> use this 1D DP type
- When its min/max/total WAYS OF SELECTING -> 2D DP like knapsack
PROBLEM
- Given list of coins and target, find min coins to make that target

> Why greedy doesnt work
- GREEDY: Sort coins and then iterate from largest coin and go on picking max coins u can
Why not Greedy ?
While greedy is the first intuitive solution that might come to a person's mind for problems like these, we have to try eliminate greedy by forming test cases.

Assume, coins = [1, 6, 7, 9, 11] , amount = 13.
Going via the greedy way, we will pick the coin with the highest denomination first = 11. And then pick two 1s. Which makes it 13 = 11 + 1 + 1. And return answer as 3.
But clearly, our answer is 13 = 6 + 7 which makes minimum number of coins as 2.

The reason for this is non-uniformity of the coin elements, which lead us to wrong results for greedy. Thus, greedy fails for this case.


SOLUTION
- dp[0 -> target+1] = INF
- dp[i] = min num of coins needed to make target `i`
- Iterate from 0 -> target:
    - Again iterate through all coins (SORT THEM BEFORE)
    - Update min if u can pick the coin based on value


"""


# coins = [1, 6, 7, 9, 11] , amount = 13

def minimumElements(coins: List[int], target: int) -> int:
    n = len(coins)

    # why sorted -> you wont have to iterate all coins for each iteration
    coins = sorted(coins)

    dp = [float('inf') for _ in range(target+1)]
    dp[0] = 0

    for cur_target in range(1, target+1):
        for coin in coins:
            # all coins after this coin > curr_target
            if coin > cur_target:
                break
            else: # pick coin so add 1, remaining target updated
                dp[cur_target] = min(dp[cur_target], 1+dp[cur_target-coin])
    
    return dp[-1] if dp[-1] != float("inf") else -1