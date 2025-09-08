"""
Number of Ways to Place People I: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description/?envType=daily-question&envId=2025-09-02

 04  14  24  34  44  54  64
[03] 13  23  33  43 [53] 63
 02  12 [22] 32  42  52  62
 01 [11] 21  31  41  51  61
 00  10  20 [30] 40  50  60

STEP 1: Sort by x(ASC) and in case of tie y(DESC)
Why? If 2 points have same x, we want to keep taller point first i.e greater y
- Because we need TOP_LEFT -> BOTTOM_RIGHT rectangles

STEP 2: 
1) i indicates your TOP_RIGHT point, j indicates your BOTTOM_LEFT point
2) Now whenever you visit, j and you find that j lies lower that i ( pair -> since its already sorted by x, dont need to check, ONLY CHECK Y)
- Now lets you say find one pair (i,j). Now further there maybe more pairs where (i, nextj) where j lied between i,j

EX:
PAIR 1: 03, 11
PAIR 2: 03, 22 
PAIR 3: 03, 53


if bottom_right_y == top_left_y
- Here you are saying there is one point with same height as `i`
- This means? Any other y after this will surely contain this point
"""


from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        pairs = 0

        points = sorted(points, key=lambda x:(x[0],-x[1]))

        for i in range(n):
            top_left_y = points[i][1]
            bottom_most_y = float("-inf")
            for j in range(i+1,n):
                bottom_right_y = points[j][1]

                # bottom_right_y>bottom_most_y => NEXT BOTTOM_RIGHT should be taller than last chosen point
                if bottom_right_y <= top_left_y and bottom_right_y>bottom_most_y:
                    pairs += 1
                    bottom_most_y = bottom_right_y
                    if bottom_right_y == top_left_y:
                        break
                

        return pairs


