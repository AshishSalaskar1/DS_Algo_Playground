"""
Problem: https://leetcode.com/problems/design-a-number-container-system

Solution: Hmap + PQ
-> index_number -> stores index->number mappping
-> number_idx -> PQ that stores all indexes of a seen number

# Change(idx, number)
self.number_index[number].put(index)
self.index_number[index] = number

# find(number)
- if number not in number_idx -> return -1 (not found)
- while pq is not empty
    - get min_index 
        -> if index_number[min_idx] != number ( MEANS THAT IT WAS REPLACED after getting added, its value must be different)
            -> pop this and continue
        -> else return min_index

"""
from queue import PriorityQueue
from collections import defaultdict
class NumberContainers:

    def __init__(self):
        self.index_number = {}
        self.number_index = defaultdict(PriorityQueue)
        

    def change(self, index: int, number: int) -> None:
        self.number_index[number].put(index)
        self.index_number[index] = number
        

    def find(self, number: int) -> int:
        if number not in self.number_index:
            return -1

        cur_pq = self.number_index[number]

        while cur_pq.qsize()>0:
            min_idx = cur_pq.queue[0]
            if self.index_number[min_idx] != number: # this is an older left over index
                cur_pq.get()
            else:
                return min_idx
        
        return -1
            
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)