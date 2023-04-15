
"""
== Question
Given an array of N integers and an integer D, left rotate the array by D place.
Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , d = 3
Output: 4 5 6 7 1 2 3
Explanation: The array is rotated to the left by 3 positions.

== Link
https://www.codingninjas.com/codestudio/problems/rotate-array_1230543?leftPanelTab=0


== Explain
- LEFT ROTATE
    1. reverse 0,k
    2. reverse k+1,n
    3. reverse 0,n
- RIGHT ROTATE
    1. reverse 0,n-k
    2. reverse n-k+1,n
    3. reverse 0,n
"""

def reverse(arr, i, j):
    """
    reverse given range in array 
    i, j are inclusive
    """
    lo, hi = i,j
    while lo<hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1

def rotate_by_k(arr,n,k):
    k = k%n
    reverse(arr, 0, k-1)
    reverse(arr, k,n-1)
    reverse(arr, 0,n-1)

    print(arr)



arr,k = [1,2,3,4,5,6,7],3
rotate_by_k(arr,len(arr),k)

arr,k = [3,7,8,9,10,11],2
rotate_by_k(arr,len(arr),k)