"""
Link: https://leetcode.com/problems/asteroid-collision/description/
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

"""


class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        n = len(arr)
        st = []

        for x in arr:
            if x < 0: # only pop in case x is -ve (left moving stone)
                # keep on popping till
                # 1. Stack is not empty
                # 2. Stack.top() is not -ve (Left moving rock)
                # 3. Stack.top() < abs(x) (gets destroyed by left moving x)
                while len(st)!=0 and st[-1]>0 and st[-1]<abs(x):
                    st.pop()
                
                # stack is empty or stack.top() is -ve, you just add x (-ve and -ve will never meet)
                if len(st)==0 or st[-1]<0:
                    st.append(x)
                # stack is not empty, but st.top() == abs(x) (Both gets destroyed)
                elif st[-1] == abs(x):
                    st.pop()
            else:
                st.append(x)
        
        return st
