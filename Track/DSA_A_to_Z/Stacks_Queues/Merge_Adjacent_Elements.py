"""
PROBLEM: https://leetcode.com/problems/merge-adjacent-equal-elements/

"""
class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            if st and st[-1] == x:
                st[-1] = x*2
            else:
                st.append(x)
            
            while len(st) >= 2 and st[-1] == st[-2]:
                st[-1] = st.pop()*2 
        
        return st


        