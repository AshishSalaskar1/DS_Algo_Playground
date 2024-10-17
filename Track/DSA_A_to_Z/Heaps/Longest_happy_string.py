"""
Problem: https://leetcode.com/problems/longest-happy-string/description/?envType=daily-question&envId=2024-10-16
- You are given number of a,b and c's
- You need to create largest possible string such that no 3 same chars are together

SOLUTION: HEAP + Greedy
- You will always try to use the most_count_remaining
- If you cant insert it, try second most one
"""

from queue import PriorityQueue
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = PriorityQueue()
        counts = {"a":a, "b": b,"c":c}
        for char, freq in counts.items():
            if freq > 0:
                pq.put( (-freq, char) )
        
        res = ""
        while not pq.empty():
            topele = pq.get()
            topf, topch = -topele[0], topele[1]

            # YOU CANT USE THE TOP CHAR > TRYING SECOND TOP CHAR
            if len(res) >= 2 and res[-1] == res[-2] == topch:
                # pq exhausted while searching for second most top char
                if pq.empty():
                    break

                # TRYING SECOND TOP CHAR
                secondtopele = pq.get()
                stopf, stopch = -secondtopele[0], secondtopele[1]
                res += stopch
                stopf -= 1

                # put back the SECOND TOP CHAR
                if stopf > 0:
                    pq.put( (-stopf, stopch) )
                pq.put( (-topf, topch) ) # put back the FIRST TOP CHAR
            else: # You can use the topmost char
                res += topch
                topf -= 1
                if topf > 0:
                    pq.put( (-topf, topch) )
                 
        return res