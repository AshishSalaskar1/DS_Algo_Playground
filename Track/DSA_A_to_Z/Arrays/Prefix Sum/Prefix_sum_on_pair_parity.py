"""
PROBLEM: https://leetcode.com/problems/special-array-ii/

LOGIC: PREFIX SUM on Parity Differences

-> prefix[i] = number of pairs till `i` (including `i`) which dont follow the parity needed (they are both odd or both even)
-> Query - start, end
    res = prefix[end]-prefix[start] == 0
    => assume prefix[end]=1 and prefix[start]=1 => then all pairs between start,end are valid
    Because, if any pair between (start,end) would voilate this then surely it would increment prefix[i] count and prefix[end] would not have been 1

"""

class Solution:
    def isArraySpecial(self, arr: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(arr)
        prefix = [0]*n

        for i in range(1,n):
            if (arr[i]&1==0 and arr[i-1]&1!=0) or (arr[i]&1!=0 and arr[i-1]&1==0):
                prefix[i] = prefix[i-1]
            else:
                prefix[i] = 1+prefix[i-1]
        
        res = []
        for start,end in queries:
            res.append(prefix[end]-prefix[start]==0)
        
        return res
