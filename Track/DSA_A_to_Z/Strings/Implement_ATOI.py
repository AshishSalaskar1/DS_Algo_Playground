"""
https://leetcode.com/problems/string-to-integer-atoi/submissions/1289047894/
"""

class Solution:
    def myAtoi(self, arr: str) -> int:
        arr = arr.strip() # it may have leading whitespaces
        n = len(arr)

        if n==0:
            return 0

        sign = 1
        res = 0
        i = 0

        if arr[0] == "-":
            sign = -1

        if arr[0] in ["+","-"]:
            i = 1

        while i<n and arr[i]=="0": # remove all leading zeros
            i += 1
        
        while i<n and arr[i].isdigit(): # scan only till its a digit
            res = (res*10) + int(arr[i])
            i += 1

        res *= sign
        if res > (2**31)-1:
            return (2**31)-1
        elif res < -(2**31):
            return -(2**31)
        
        return res

        