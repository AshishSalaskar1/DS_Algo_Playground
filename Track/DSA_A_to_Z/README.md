## Algorithm References
- https://liuzhenglaichn.gitbook.io/algorithm/
- Notion DSA Tracker: https://languid-knife-878.notion.site/DSA-038b19d91806431ea085bfdc7b11e945?pvs=74

## Python References

### @cache
- `@cache` works in Python > 3.9
- `@lru_cache` for lower versions < 3.9 
```python
from functools import cache, lru_cache 

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


## Docs
- CSES Problem set: https://cses.fi/problemset/list/
- Euler Tour: 
    - Explainations with variations: https://www.youtube.com/playlist?list=PL-Jc9J83PIiHymm1DHZBkac0_hhFBXryO
    - Questions:
        1. Subtree sum with node value updates: https://cses.fi/problemset/task/1137/
        2. Depth of tree given subtree deletions: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/?envType=problem-list-v2&envId=my4z5092
- Fenwick Trees: 
    - Explaination: https://www.youtube.com/watch?v=pTg7NezkV28
     - Questions:
        1. Subtree sum with node value updates: https://cses.fi/problemset/task/1137/
    
## CP tips in Python
- Codeforces Blog: https://codeforces.com/blog/entry/21851
- `input()` is slower, so use `sys.stdin.readline()`. (`sys.stdin.read()` is fastest, but it reads all input at once)
- Puttting your code in a function and calling it is 1.5-3x better than putting in outside ( Something to do with Python interpreter reserving Memory)
- For strings, `s1 += s2` is faster than doing `s1 = s1+s2`