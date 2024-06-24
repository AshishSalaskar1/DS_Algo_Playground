"""
PROBLEM: Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

- Simple NGE problem

"""
class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        n = len(temps)
        st = []
        nge = temps.copy()
        nge[-1] = -1

        for i in reversed(range(n)):
            while len(st)>0 and st[-1][0]<=temps[i]:
                st.pop()

            if len(st) == 0:
                nge[i] = 0
            else: # ANS = idx-index(next_greater_element)
                nge[i] = st[-1][1]-i
            st.append((temps[i],i))

        return nge