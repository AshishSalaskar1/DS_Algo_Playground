
"""
PROBLEM: Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=leetcode-75

SOLUTION:
- Balloons: [[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]
1|----------|10
   3|-----|9
    4|-------|11
      6|-|7
      6|--|9
        8|----|12
         9|---|12

-> [1,10] - next baloon is [3,9]
    - to burst both together [3,10]
    - start = max(1,3) [You want to burst both, taking min might burst only prev and not cur]
    - end = min(10,9) [You want to burst both, taking max might burst only cur and not prev]
    => [3,10]

INTUTION: 
[[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]
=> [] [1, 10]
=> [[1, 10]] [3, 9]
<= [[3, 9]]
=> [[3, 9]] [4, 11]
<= [[4, 9]]
=> [[4, 9]] [6, 7]
<= [[6, 7]]
=> [[6, 7]] [6, 9]
<= [[6, 7]]
=> [[6, 7]] [8, 12]
<= [[6, 7], [8, 12]]
=> [[6, 7], [8, 12]] [9, 12]
<= [[6, 7], [9, 12]]
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = []
        points = sorted(points)
        print(points)

        for [start,end] in points:
            # print("=>", res, [start,end])
            if len(res) == 0:
                res.append([start,end])
                continue

            [prev_start, prev_end] = res[-1]
            if prev_start <= start <= prev_end:
                res[-1][0] = max(prev_start, start)
                res[-1][1] = min(prev_end, end)
            else:
                res.append([start,end])
            # print("<=", res)
        
        return len(res)



"""
[10,16],[2,8],[1,6],[7,12]

[1,6] [2,8] [7,12] [10,16]
"""

"""
Example 1:

points = [[10,16],[2,8],[1,6],[7,12]] => Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 <= POINTS
- - - - - - - - -  B  B  B  B  B  B  B  - [10,17]
- B B B B B B B -  -  -  -  -  -  -  -  - [2,8]
B B B B B B - - -  -  -  -  -  -  -  -  - [1,6]
- - - - - - B B B  B  B  B  -  -  -  -  - [7,12]





Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
"""
