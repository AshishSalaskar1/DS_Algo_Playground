"""
NGE from L->R (Will work in case all days are given n you need to find)
- Here you get day-by-day, you will run NGE each time

SOLUTION: - O(N) Solution: MONOTONICALL DECREASING DEQUE
-> New element comes in (assign it a index starting from 0)
  - Keep on popping elements until the top of stack/queue is > cur
  - Now you know that the span is from (remaining_top - cur_idx)
  - Since you need both idx and val, put both in Queue
"""

class Ele:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
    
    def __repr__(self):
       return f"({self.idx}, {self.val})"

class StockSpanner:
    def __init__(self):
        self.idx = -1
        self.q = []
        
    def next(self, price: int) -> int:
        self.idx += 1
        while len(self.q) != 0 and self.q[-1].val <= price:
            self.q.pop()
        
        res = self.idx+1 if len(self.q) == 0 else self.idx-self.q[-1].idx
        self.q.append(Ele(self.idx, price))
        print(self.q)
        return res

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)