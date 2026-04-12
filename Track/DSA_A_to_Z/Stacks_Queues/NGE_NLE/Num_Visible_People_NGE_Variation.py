"""
Link: https://leetcode.com/problems/number-of-visible-people-in-a-queue/
10, 6, 8, 5, 11, 9
3,  1, 2, 1, 1,  0

Is this pure NGE? NOO
1 NGE(10) is (11) - 4-0=4
- But you have 10 [6 8 5] 11
- Here you cant see 5, its hidden behind 6


SOLUTION:
- Whenever you pop from st -> it means it was <=x -> you can surely see it
- Then you can see the NGE ALSO

-> here in this case 10 [6 8 5] 11 how did 5 get skipped
 - When calculating NGE for 8, you already remove [5] and left NGE = 8
 - IMP: At any pos i, the st will contains elements that you can see from here 


"""
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0]*n

        st = []
        for i in range(n-1,-1,-1):
            while st and st[-1] <= heights[i]:
                st.pop()
                res[i] += 1 # there is one element that you can surely see
            
            if st:
                res[i] += 1 # you can see the next greater element also
            
            st.append(heights[i])
        
        return res



        