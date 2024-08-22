"""
PROBLEM: https://leetcode.com/problems/find-median-from-data-stream/description/

SOLUTION:

=> INTUITION
- Consider array of numbers. There are 2 options
1. EVEN Numbers
    - Pick 2 mids and mean of those 2
2. ODD Numbers: 
    - Pick mid element

- Assume the array is sorted and divided into 2 parts (each array is size of n//2-EVEN or n//2+1-ODD)
1. EVEN: L=[1,2,3,4] R=[5,6,7,8] 
    - Here median = 4+5/2 = max(LEFT) + max(RIGHT) // 2 

2a. ODD: L=[1,2,3] R=[4,5,6,7]
    - min(RIGHT)
2b. ODD: L=[1,2,3,4] R=[5,6,7]
    - max(LEFT)

EVEN = max(LEFT) + max(RIGHT) // 2 
ODD = in case len(LEFT) > len(RIGHT) => max(LEFT)
ODD = in case len(LEFT) < len(RIGHT) => MIN(RIGHT)

IMPLEMENTATION NEEDED
- 2 Sorted arrays LEFT and RIGHT which may differ only by 1 in terms of size
- LEFT array is a maxHeap -> you need max of left
- RIGHT array is a minHeap -> you need min of right
"""

from queue import PriorityQueue
class MedianFinder:

    def __init__(self):
        self.left = PriorityQueue()
        self.right = PriorityQueue()
        

    def addNum(self, num: int) -> None:
        if not self.right.empty() and num < self.right.queue[0]: # insert into left half
            self.left.put(-num)
        else:
            self.right.put(num)

        lsize = self.left.qsize()
        rsize = self.right.qsize()

        if abs(lsize-rsize) > 1:
            if lsize > rsize:
                self.right.put(-self.left.get())
            else:
                self.left.put(-self.right.get())

    def findMedian(self) -> float:
        lsize = self.left.qsize()
        rsize = self.right.qsize()

        # print(self.left.queue, self.right.queue)

        if lsize == rsize:
            return (-self.left.queue[0] + self.right.queue[0] )/ 2
        elif lsize > rsize:
            return -self.left.queue[0]
        else:
            return self.right.queue[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()