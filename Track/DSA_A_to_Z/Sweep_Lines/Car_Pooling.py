"""
PROBLEM: https://leetcode.com/problems/car-pooling/submissions/1436410743/
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num_ppl, frm, to in trips:
            events.append((frm,num_ppl))
            events.append((to,-num_ppl))

        events.sort() 
        cur_ppl = 0

        for i in range(len(events)):
            cur_ppl += events[i][1]

            if cur_ppl > capacity:
                return False

        return True      