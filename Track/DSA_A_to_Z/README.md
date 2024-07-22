## Python References

### @cache
```python
from functools import cache

# all arguments to cached function must be immutable - tuple, string, dict
@cache
def fn():
    pass
```

## PriorityQueue
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

### Python STR <-> ASCII VALUE
```python
ord('a') # 97 => CHAR -> ASCII
chr('97') # a => ASCII -> CHAR
```

### Tree to Graph Conversion
- Here we are storing `Node` object and not the `Node` value (since in some cases Node value can repeat)
```python
def countPairs(root: TreeNode, max_distance: int) -> int:
    if root is None:
        return 0
    
    adj = defaultdict(list)
    leaves = set()
    pairs = set()

    def dfs(node, parent=None):
        if node:
            if parent:
                if node.left is None and node.right is None:
                    leaves.add(node)
                adj[node].append(parent)
                adj[parent].append(node)
            dfs(node.left, node)
            dfs(node.right, node)
    
    dfs(root)

```



### Python Magic Methods
1. **__gt__(self, other)**:
- Compare current object(self) with another object
- return True if self > other

2. **__repr__(self)**:
- return string representation of your object
