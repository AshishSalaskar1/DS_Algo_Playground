## Python References

### @cache
```python
from functools import cache

# all arguments to cached function must be immutable - tuple, string, dict
@cache
def fn():
    pass
```

##E PriorityQueue
```python
from queue import PriorityQueue # MIN HEAP BY DEFAULT

pq = PriorityQueue() # cant do heapify, like build from a list

pq.put((1,2)) # EACH ITEM MUST BE COMPARABLE (if class implement __gt__(self.other) method)
pq.put((1,2))
pq.put((1,2))

pq.get() # POPS THE MIN ELEMENT

pq.empty()
pq.qsize()

pq.queue # list in which first ele = min

# MAX  HEAP -> Multiply by -1 both while inserting and poppping
pq.put(-x)
-pq.get()
```

| Operation    | Time Complexity |
| :-------- | :------- |
| `put()`  | O(nlogn)    |
| `get()` | O(logn) - Peek + Delete head     |
| `peek()` or `queue[0]`    | O(1)    |
|`heapify()`| O(n) |


### Deque
```python
from collections import deque

q = deque()

q.append(1) # insert at end
q.appendleft() # insert at start
    
q.pop() # pop from end
q.popleft() # pop from last

q[0] #  first element
q[-1] # last element

len(q) # length of the queue
```

### Python Magic Methods
1. **__gt__(self, other)**:
- Compare current object(self) with another object
- return True if self > other

2. **__repr__(self)**:
- return string representation of your object
