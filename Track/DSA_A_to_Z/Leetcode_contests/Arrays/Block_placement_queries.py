"""
PROBLEM
- LINK:https://leetcode.com/problems/block-placement-queries/description/

SOLUTION: This gives TLE -> use SEGEMENT TREES
"""

from sortedcontainers import SortedList, SortedSet, SortedDict 

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        blocks = SortedSet()
        bres = {}
        
        res = []
        for q in queries:
            if q[0] == 1:
                pos = q[1]
                blocks.add(q[1])
                bres[pos] = float("-inf")
                
                last_block = 0
                for block in blocks:
                        if block > pos:
                            break
                        # valid block
                        span_size = block-last_block
                        bres[pos] = max( bres[pos], span_size)
                        last_block = block
                        
            elif q[0] == 2:
                end, target_size = q[1], q[2]
                cursize = 0
                canplace = False
                
                if len(blocks) == 0 and (end-0)>= target_size:
                    canplace = True
                else:
                    poss = []
                    for block in blocks:
                        if block <= end:
                            poss.append(block)
                    
                    for block in reversed(poss):
                        if bres[block] >= target_size:
                            canplace = True
                            break
                res.append(canplace)
                    
        
        return res
                            
                

