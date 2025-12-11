"""
https://leetcode.com/problems/shifting-letters-ii/?envType=problem-list-v2&envId=o1qf3c31

HERE `number_of_shifts` == number of concurrent meetings happening at each time

Extra: This same problem can be solved using partial sum approach as well.
- You just assume arr=[0,..0] and then consider each shift as +1 or -1 operation on the subarray (start,end)

"""

from collections import defaultdict
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        
        def shift(ch: str, val: int, direction: str,) -> str:
            idx = ord(ch)-ord('a')
            val = val%26
            next_idx = (idx + (-1 if direction=="left" else 1)*val)%26
            # if direction == "right": next_idx = (idx+val) % 26
            # else: next_idx = (idx+) % 26 
            
            return chr(ord('a')+next_idx)
        
        
        def partial_sum_solution() -> str:
            prefix = [0] * (n + 1)

            for start, end, direction in shifts:
                prefix[start] += (1 if direction == 1 else -1)
                if end + 1 < n:
                    prefix[end + 1] -= (1 if direction == 1 else -1)

            
            res = ""
            csum = 0
            for i in range(n):
                csum += prefix[i]
                if ops[i] == 0: res += s[i]
                elif ops[i] > 0: res += shift(s[i], ops[i],"right")
                else: res += shift(s[i], abs(ops[i]),"left")

            return res


        # SWEEP LINE SOLUTION
        events = defaultdict(list)
        for start, end, direction in shifts:
            events[start].append((direction, "start"))
            events[end+1].append((direction, "end"))
        

        ops = [0]*n
        curops = 0
        for ts in range(n):
            for direction, op in events[ts]:
                if op == "start":  curops += 1 if direction == 1 else -1
                else: curops += -1 if direction == 1 else 1
            ops[ts] = curops

        res = ""
        for i in range(n):
            if ops[i] == 0: res += s[i]
            elif ops[i] > 0: res += shift(s[i], ops[i],"right")
            else: res += shift(s[i], abs(ops[i]),"left")

        # PARTIAL SUM SOLUTION
        return partial_sum_solution()
        
        return res




        
        