"""
PROBLEM: Smallest Number in Infinite Set
- https://leetcode.com/problems/smallest-number-in-infinite-set/?envType=study-plan-v2&envId=leetcode-75

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

- SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
- int popSmallest() Removes and returns the smallest integer contained in the infinite set.
- void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

INTUTION: 
- Initial lowest=1
- `lowest` is the lower bound of the infinite set: [lowest, lowest+1, ...... INF]
- addBack(val) -> you need to add only if n is not in the infinte set
    - LOGIC: if val > lowest (no need ot add)
             if val < lowest: 
                You will need to save this val in a set/PQ

- popSmallest():
    if PQ is not empty -> return from that
    else return lowest (and then lowest+=1)

NOTE: If you are using PQ, we dont need duplicates (so use SET to maintain unique vals and not add duplicates) 

Ex: 
lowest = 1 [1,2,3,4,5.....]
1. addback(2) => nothing happens 
2. popSmallest() called 3 times -> lowest=4 [4,5,6,7......INF]
3. addBack(2,3) -> 2 < lowest=4
    PQ = (2,3)
    lowest = 4
4. popSmallest(): since pq is not empty -> send 2 back
"""



from queue import PriorityQueue
class SmallestInfiniteSet:

    def __init__(self):
        self.lowest = 1
        self.pq = PriorityQueue()
        self.ns = set() # needed to make sure duplicates are not put into PQ
        
    def popSmallest(self) -> int:
        # if PQ is not empty -> return min from PQ
        if len(self.pq.queue) > 0:
            min_ele = self.pq.get()
            self.ns.remove(min_ele)
        else: # PQ is empty, return min
            min_ele = self.lowest
            self.lowest += 1
    
        return min_ele
        

    def addBack(self, num: int) -> None:
        if num < self.lowest:
            if num not in self.ns:
                self.pq.put(num)
                self.ns.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)