"""
Description
Given an array of N integers, Q queries, and an integer K. In each query two integers L, R is given, you have to find (A[L] + A[L+1] * K + A[L+2] * K^2 + …. A[R] * K^(R-L))% 10^9+7.

Input Format
The first line contains three space-separated integers N, Q, K where 1<=N<=10^6, 1<=Q<=10^6, 1<=K<=10^9.

Next line contains N space-separated integers (-1e9<=Ai<=1e9).

Next Q lines contain two space-separated integers L, R where 1<=L<=R<=N.

Output Format
For each query print the value of (A[L] + A[L+1] * K + A[L+2] * K^2 + …. A[R] * K^(R-L))% 10^9+7 in a new line.
"""
import sys

MOD = 1000000007

def create_prefix_arrays(arr, n, k):
    """
    Creates the prefix sum array and the modified array where
    each element is arr[i] * k^i % MOD.
    """
    power_k = [1] * (n + 1)
    modified_arr = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        power_k[i] = (power_k[i - 1] * k) % MOD
        modified_arr[i] = (arr[i - 1] * power_k[i]) % MOD
        prefix_sum[i] = (prefix_sum[i - 1] + modified_arr[i]) % MOD
    
    return power_k, prefix_sum

def main():
    
    n, q, k = list(map(int,sys.stdin.readline().split()))
    arr = list(map(int,sys.stdin.readline().split()))
    
    # Create the prefix arrays and power_k
    power_k, prefix_sum = create_prefix_arrays(arr, n, k)
    
    # Process queries
    results = []
    for i in range(q):
        l, r = list(map(int,sys.stdin.readline().split()))
        # Sum of the range
        ans = (prefix_sum[r] - prefix_sum[l - 1] + MOD) % MOD
        # Multiply by the modular inverse of power_k[l]
        ans = (ans * pow(power_k[l], MOD - 2, MOD)) % MOD
        results.append(ans)
    
    # Print results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
