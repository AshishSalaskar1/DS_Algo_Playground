## You can buy and sell any number of time
## Sell at each profit peak that you can get

def maximumProfit(arr):
    # Write your code here.
    res = 0
    n = len(arr)
    
    for i in range(n-1):
        if arr[i+1]>arr[i]:
            res += (arr[i+1]-arr[i])
    
    return res

## You can only buy and sell once
- The max profit you can earn by selling at index `x` : `arr[x]` - `min_cost_before_i`

def maximumProfit(arr):
    # Write your code here.
    res = 0
    min_till_now = float('inf')

    for x in arr:
        # max profit by selling at this day
        res = max(res, x-min_till_now)

        # check if min changes
        min_till_now = min(min_till_now, x)
    
    return res