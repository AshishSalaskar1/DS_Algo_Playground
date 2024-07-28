"""
PROBLEM: https://leetcode.com/problems/candy/description/
- Each child has a assigned rating
- You are giving candies to these children subjected to the following requirements:
    1) Each child must have at least one candy.
    2) Children with a higher rating get more candies than their neighbors. (EQUALS DONT MATTER)
- Return the minimum number of candies you need to have to distribute the candies to the children.

SOLUTION:
- Initially give 1 candy to all students
- Now go from left -> right, n increase in case rating is greater than previous
- No go from left <- right, n increase in case rating is greater than next one

WHY YOU NEED L->R and R<-L both?
Example: [1, 2, 87, 87, 87, 2, 1]
-> init  [1, 1, 1 ,  1,  1, 1, 1]
- You iterate L->R and make check ratings of i with (i-1) and (i+1) both

=> 0, 1
[1, 2, 87, 87, 87, 2, 1]
[1, 1, 1 ,  1,  1, 1, 1]

=> 1, 2 (increase to 2, since rating 2>1)
[1, 2, 87, 87, 87, 2, 1]
[1, 2, 1 ,  1,  1, 1, 1]

=> 2, 87 (increase to 3, since rating 87>2)
[1, 2, 87, 87, 87, 2, 1]
[1, 2, 3 ,  1,  1, 1, 1]

=> 3,87 (it remains same since 87==87==87)
[1, 2, 87, 87, 87, 2, 1]
[1, 2, 3 ,  1,  1, 1, 1]

=> 4,87 (becomes 2 since rating 87>2 and ur value needs be greater than taken[5]=1) 
[1, 2, 87, 87, 87, 2, 1]
[1, 2, 3 ,  1,  2, 1, 1]

=> 5,2 (left is fine since 87<2, but right side 1<2, so you increment it by 1) 
[1, 2, 87, 87, 87, 2, 1]
[1, 2, 3 ,  1,  2, 2, 1]

FAILURE CASE: You incremented 1->2, now its bigger than right but its also equal to left(2). THIS VOILATES THE CONDITION
- SOLUTION: After iteratin from 0->n, go back from 0<-n and make sure such cases are adjusted

"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left, right = [1]*n, [1]*n
        
        # L -> R
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = 1+left[i-1]
        
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                right[i] = 1+right[i+1]
        
        res = 0
        for i in range(n):
            res += max(left[i], right[i])
        
        return res

# SAME LOGIC -> BUT ELIMINATE THIRD LOOP (Does same thing as MAX(left, right))
class SolutionVerbose:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1]*n

        if n == 1:
            return 1

        for i in range(n):
            if i==0:
                if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                    res[i] = res[i+1]+1
            elif i==n-1:
                if ratings[i] > ratings[i-1] and res[i] <= res[i-1]:
                    res[i] = res[i-1]+1
            else:
                if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                    res[i] = res[i+1]+1
                if ratings[i] > ratings[i-1] and res[i] <= res[i-1]:
                    res[i] = res[i-1]+1
        print(res)
        for i in reversed(range(n)):
            if i==0:
                if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                    res[i] = res[i+1]+1
            elif i==n-1:
                if ratings[i] > ratings[i-1] and res[i] <= res[i-1]:
                    res[i] = res[i-1]+1
            else:
                if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                    res[i] = res[i+1]+1
                if ratings[i] > ratings[i-1] and res[i] <= res[i-1]:
                    res[i] = res[i-1]+1
        # print(res)
        return sum(res)
