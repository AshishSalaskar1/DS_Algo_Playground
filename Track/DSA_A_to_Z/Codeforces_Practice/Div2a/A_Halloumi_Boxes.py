"""
https://codeforces.com/problemset/problem/1903/A
"""

import sys

def get_input():
    n = int(sys.stdin.readline())
    cases = []
    
    for _ in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        k = data[1]
        nums = list(map(int, sys.stdin.readline().split()))
        cases.append((k,nums))
    
    return n, cases

def main():
    n,cases = get_input()
    for k,nums in cases:
        n = len(nums)
        is_sorted = True
        
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                is_sorted = False
                break

                
        if is_sorted or k>1:
            print("YES")
        else:
            print("NO")


main()
