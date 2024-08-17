"""
PROBLEM: https://leetcode.com/problems/best-sightseeing-pair/
- Given an array find the max pair sum = arr[i]+arr[j]+i-j where i<j

REF: https://www.youtube.com/watch?v=lk7WUhAwYGA

NEXT PROBLEM ON SAME CONCEPT: https://leetcode.com/problems/maximum-number-of-points-with-cost/

SOLUTION:
- Partition the equation such that one part depends on i and another on j
- Then you can optimize both parts separately

=> a[i]+a[j]+i-j = (a[i]+i) + (a[j]-j) => MAXIMISE THESE TWO THINGS SEPARATELY
max_equation_1 = a[i]+i -> DEPENDS ONLY ON i
max_equation_2 = a[j]-j -> DEPENDS ONLY ON j

At any point you want to maximise both equations, 
1. We keep track of max(max_equation_1) before cur_element
2. Check res = max(res, max_equation_1+arr[j]-j)
3. Update max_equation_1 [Done after updating res, since you need i<j and max_equation_1 depends on i]



"""
class Solution:
    def maxScoreSightseeingPair(self, arr: List[int]) -> int:
        # a[i]+a[j]+i-j = (a[i]+i) + (a[j]-j) => MAXIMISE THESE TWO THINGS SEPARATELY
        n = len(arr)
        max_eq1 = arr[0]+0
        res = 0

        for j in range(1, n):
            res = max(res, max_eq1 + arr[j] - j )
            # udpate after res, because u need max eqn1 before j
            max_eq1 = max(max_eq1, arr[j]+j)

        return res        