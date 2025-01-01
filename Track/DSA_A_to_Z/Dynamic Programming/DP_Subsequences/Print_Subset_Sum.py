"""
PROBLEM:

INPUT
1. Arr is given
2. Queries

For each `Q` in query, check if subset_sum(arr,q) exist and if yes then put the subset which sums upto q
"""
import sys
from collections import deque, defaultdict
from queue import PriorityQueue
from functools import lru_cache 

def subset_sum_count(arr, target):
    n = len(arr)
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(target + 1):
            if j == 0:
                dp[i][j] = True  # Sum 0 is always achievable (with no elements)
            elif i > 0:  
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
    
    return dp

def print_path(i, j, path, dp, arr, res):
    # If we've found a valid subset (sum = 0), append the path to res and stop
    if j == 0:
        res.append(path[::-1])  # Add the path in original order
        return True  # Stop after finding one valid subset
    
    # If we run out of elements, return
    if i == 0:
        return False
    
    # Option 1: If the current element is not included
    if dp[i - 1][j]:
        if print_path(i - 1, j, path, dp, arr, res):
            return True
    
    # Option 2: If the current element is included (and valid)
    if j >= arr[i - 1] and dp[i - 1][j - arr[i - 1]]:
        path.append(arr[i - 1])  # Include the current element
        if print_path(i - 1, j - arr[i - 1], path, dp, arr, res):
            return True  # Stop after finding one valid subset
        path.pop()  # Backtrack, remove the element from the path

    return False  # No valid subset found

def main():
    n, q = [5,3]
    arr = [1,2,3,4,5]
    queries = [7,16,3]
    
    # List to store final results for each query
    final_res = []
    
    # Get the dp table for the maximum query
    dp = subset_sum_count(arr, max(queries))
    
    # Process each query
    for query in queries:
        res = []  # Initialize an empty list to store subsets for the current query
        
        if dp[n][query] is True:
            # Call print_path and stop after finding one valid subset
            print_path(n, query, [], dp, arr, res)
            if not res:  # If no valid subset found
                final_res.append([-1])
            else:
                final_res.append(res[0])  # Only add the first valid subset
        else:
            final_res.append([-1])  # If no subset can sum to the query
    
    print(final_res)
    return final_res

main()
