from queue import PriorityQueue
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cmap = Counter(tasks)
        q = []  # FIFO queue to manage the cooldown period
        pq = PriorityQueue()
        
        for ch, count in cmap.items():
            pq.put((-count, ch))  # Use negative count to simulate max-heap behavior
        
        time = 0
        
        while not pq.empty() or q:
            time += 1
            
            if not pq.empty():
                max_count, max_ele = pq.get()
                max_count = -max_count - 1  # Decrement the task count
                
                # If there are more of the current task, put it in the cooldown queue
                if max_count > 0:
                    q.append((max_count, max_ele, time + n))
            
            # Move tasks from the cooldown queue back to the priority queue when they are ready
            if q and q[0][2] == time:
                pq.put((-q[0][0], q[0][1]))
                q.pop(0)
        
        return time
