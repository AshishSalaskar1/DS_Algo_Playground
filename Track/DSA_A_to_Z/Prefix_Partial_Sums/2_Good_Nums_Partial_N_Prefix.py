"""
PROBLEM: 
There are N students and ith student likes all numbers in the range [li ,ri ], both inclusive. A number is good if it is liked by at least K students.

You are even Q queries. Each query consists of two numbers L, R. You have to find how many numbers in the range [L,R] is good.

LOGIC
IDEA: Use partial sum and then get the final array where arr[i]= the number of students who like the ith number.

1. Treat this as partial sum, like(l,r) is like adding +1 to add elements in range(l,r) -> INITIAL ARRAY IS ZERO
2. Now do prefix sum -> now arr[i] = number of students who liked `i`

But,`i` is good number if liked by more than `k` students
3. Replace values in arr by 1 if its good else 0
4. Now we need the SUM(l,r) in this new array == NUMBER OF GOOD NUMBERS BETWEEN L,R

"""

import sys
from collections import deque, defaultdict
from queue import PriorityQueue
from functools import lru_cache 


def solve():
    pass

def main():
    n_updates, k, q = list(map(int,sys.stdin.readline().split()))
    n = 1000005
    arr = [0]*n

    for _ in range(n_updates):
        l,r = list(map(int,sys.stdin.readline().split()))
        arr[l] += 1
        arr[r+1] -= 1

    # prefix sum after partial updates
    # now arr[i] = number of students who liked `i`
    for i in range(1,n):
        arr[i] += arr[i-1]

    # Good number =1 , else 0
    arr = [1 if x>=k else 0 for x in arr]

    # prefix sum again for count of good numbers
    for i in range(1,n):
        arr[i] += arr[i-1]
    
    for _ in range(q):
        l,r = list(map(int,sys.stdin.readline().split()))
        print(arr[r]-arr[l-1])
    

        
main()