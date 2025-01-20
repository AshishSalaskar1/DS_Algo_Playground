"""
Description
Given an array of N integers and Q queries. In each query two integers L, R is given, you have to find (A[L] + A[L+1]*2 + A[L+2]*3 + A[L+3]*4...A[R]*(R-L+1)) % 10^9+7.

Input Format
The first line contains two space-separated integers N, Q where 1<=N<=10^6, 1<=Q<=10^6.

Next line contains N space-separated integers (-1e9<=Ai<=1e9).

Next Q lines contain two space-separated integers L, R where 1<=L<=R<=N.

Output Format
For each query print the value of (A[L] + A[L+1]*2 + A[L+2]*3 + A[L+3]*4...A[R]*(R-L+1)) % 10^9+7 in a new line.
"""
import sys

MOD = 1000000007

# Standard prefix sum array
def create_prefix_arr(arr, n):
    prefix_arr = [0] * (n + 1)  
    for i in range(1, n + 1):
        prefix_arr[i] = (prefix_arr[i - 1] + arr[i - 1]) % MOD
    return prefix_arr

# Prefix sum of arr[i] * i
def create_prefix_mul_arr(arr, n):
    prefix_mul_arr = [0] * (n + 1)  
    for i in range(1, n + 1):
        prefix_mul_arr[i] = (prefix_mul_arr[i - 1] + arr[i - 1] * i) % MOD
    return prefix_mul_arr

def main():
    
    # Read n (size of array) and q (number of queries)
    n, q = list(map(int,sys.stdin.readline().split()))
    arr = list(map(int,sys.stdin.readline().split()))
    
    # Create prefix arrays
    prefix_arr = create_prefix_arr(arr, n)
    prefix_mul_arr = create_prefix_mul_arr(arr, n)
    
    results = []
    
    # Process each query
    for i in range(q):
        l, r =list(map(int,sys.stdin.readline().split()))
        
        # Compute the result for the query
        sum_mul = (prefix_mul_arr[r] - prefix_mul_arr[l - 1] + MOD) % MOD
        sum_plain = (prefix_arr[r] - prefix_arr[l - 1] + MOD) % MOD
        res = (sum_mul - (l - 1) * sum_plain % MOD + MOD) % MOD
        
        results.append(res)
    
    # Print all results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
