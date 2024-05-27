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