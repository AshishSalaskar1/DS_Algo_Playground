"""
PROBLEM: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream

SOLUTION: Maintain a minHeap of size k always
- NOTE: You only add elements, no pop operation is being performed
- arr = [1,2,3,4,5] k=3
- The third largest element is 3 here
- OR: If you remove 2 lower element = [3,4,5], then lowest of this is your kth largest
    - Because at end you are left with k-last big number in which min is the k largest
"""

from queue import PriorityQueue
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = PriorityQueue() # MAX HEAP
        for x in nums:
            self.pq.put(x)
     

    def add(self, val: int) -> int:
        self.pq.put(val)
        
        while self.pq.qsize() > self.k:
            self.pq.get() 

        return self.pq.queue[0]   
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)