"""
PROBLEM: https://leetcode.com/problems/remove-k-digits/
https://www.youtube.com/watch?v=cFabMOnJaq0

SOLUTION: Monotonic increasing stack/queue (NOT STRICTLY)
=> INTUITION
- Given a number, smallest number will be a number in increasing order
  12345 (sorted so smallest) -> 51234 => 12345 will be smallest
- When you iterate you try to keep it in sorted order (MONOTONIC INCREASING)
    - in this process whenever you need to pop, consider that as one removal (k-=1)
    - try to keep it monotonic until you have removals left (k>0)
- After this lets assume you didnt need all `k` removals to make it Monotonic increasing
    - In this case you remove remaining `k` elements from last (since its sorted and hence remove)

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for digit in num:
            while st and k > 0 and st[-1] > digit:
                st.pop()
                k -= 1
            st.append(digit)
        
        # If we still have k > 0, remove from the end
        while k > 0 and st:
            st.pop()
            k -= 1
        
        # Build result string and remove leading zeros
        res = "".join(st).lstrip("0")
        
        # If string is empty, return "0"
        return res if res else "0"

class Solution:
    def removeKdigits(self, arr: str, k: int) -> str:
        stack = []
        for ch in arr:
            while k>0 and stack and int(stack[-1]) > int(ch):
                k -= 1
                stack.pop()
            
            # in case stack is empty - then dont pick 0s (trailing 0s wont make sense)
            if len(stack) == 0 and ch == "0":
                continue
            
            stack.append(ch)
        
        # you can only pivk N-K (but stack can have more or less elements)
        res = ''.join(stack)
        if k>0: # You processed entire string but still "k" elements are left to be removed (remove last k elements)
            res = res[:len(res)-k]
        return res if res else '0' # if res="" -> return "0"
         