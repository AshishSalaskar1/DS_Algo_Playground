"""
STOCK SPAN PROBLEM:
- Given an array arr of size n, where each element arr[i] represents the stock price on day i. Calculate the span of stock prices for each day.
- The span Si for a specific day i is defined as the maximum number of consecutive previous days (including the current day) for which the stock price was less than or equal to the price on day i.

Input: n = 7, arr = [120, 100, 60, 80, 90, 110, 115]
Output: [1, 1, 1, 2, 3, 5, 6]

Input: n = 6, arr = [15, 13, 12, 14, 16, 20]
Output: [1, 1, 1, 3, 5, 6]

"""
class Solution:
    def stockSpan(self, arr, n):
        st = []
        pge = [-1]*n # previous greater element

        for i,x in enumerate(arr):
            while st and arr[st[-1]] <= x: st.pop()
            if st: pge[i] = st[-1]
            st.append(i)
        
        res = [1]*n

        for i in range(n):
            if pge[i] == -1: res[i] = i+1
            else: res[i] = i-pge[i]
    
        return res