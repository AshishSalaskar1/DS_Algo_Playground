## Algorithm References
- https://liuzhenglaichn.gitbook.io/algorithm/
- Notion DSA Tracker: https://languid-knife-878.notion.site/DSA-038b19d91806431ea085bfdc7b11e945?pvs=74

## Leetcode Lists
- Compilation of Topic lists: https://leetcode.com/discuss/study-guide/1612475/all-leetcode-discuss-lists-and-my-lists-so-far-topic-wisedifficulty-wise
  
- Two Pointer: https://leetcode.com/problem-list/two-pointers/
- Sweep Line: https://leetcode.com/problem-list/o1qf3c31/
- Rolling Hash: https://leetcode.com/problem-list/rolling-hash/ 

## Python References

## Custom `cmp` function for sorting
- https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
```py
import functools

lst = [list(range(i, i+5)) for i in range(5, 1, -1)]

def fitness(item):
    return item[0]+item[1]+item[2]+item[3]+item[4]
def compare(item1, item2):
    return fitness(item1) - fitness(item2)

sorted(lst, key=functools.cmp_to_key(compare))
```

## Handling MOD
### Mod of negative numbers
- Ref: https://www.youtube.com/watch?v=AbGVbgQre7I
- `-x` mod `M` = `-x` - (highest number `smaller than -x` which is `multiple of M`)
- Ex: -6 % 5 = 4
    1. multiples of 5 smaller than -6 => -10, -15, -20 ( _**-5 cant be taken since -5>-6**_ )
    2. Highest = -10 
    3. -6-(-10) = 4  
   
### Mod Rules with operations
1. (`a+b`) % `m` = (`a%m` + `b%m`) % `m` 
2. (`a-b`) % `m` = (`a%m` - `b%m` + `m`) % `m` (_**Extra `+m` since (a-b) can become negative**_)
3. (`a/b`) % `m` = ((`a%m`)*(`b`<sup>-1</sup>`%m`))%`m` NOTE: (_`b`<sup>-1</sup> -> mod inverse of b_)
4. **IMP**: (`a`<sup>-1</sup>)`%m` = (`a`<sup>m-2</sup>)`%m`
    - You need to include MOD in power function also
    ```cpp
        ll power(ll x,ll y)
        {
            ll res = 1;
            while(y)
            {
                if(y&1) 
                    res = (res*x)%mod;
                y=y/2,x=(x*x)%mod;
            }
            return res%mod;
        }
        ans = ans*power(powerK[l],mod-2)%mod;
    ```

## Bisect
This works with the concept of Binary Search.

0. `bisect.bisect(arr,<num>)` -> Returns the right most index
1. `bisect.bisect_right(arr, x)` -> UPPER BOUND ( incase of multiple matches, insert at right most position )
2. `bisect.bisect_left(arr, x)` -> LOWER BOUND  ( incase of multiple matches, insert at left most position )
3. `bisect.insort(arr, x) ` -> INSERT AND SORT ( this is same as arr.append(x) -> arr.sort())

```py
import bisect
#      0 1 2 3 4 5 6 7  8
arr = [1,2,2,2,5,6,7,89,100]

# MATCH BEING FOUND
bisect.bisect(arr,2) # 4
bisect.bisect_left(arr,2) # 1
bisect.bisect_right(arr,2) # 4

# NO MATCH BEING FOUND -> ALL ARE SAME
bisect.bisect(arr,3) # 4
bisect.bisect_left(arr,3) # 4
bisect.bisect_right(arr,3) # 4

# USING KEYS
arr = [(0,1),(10,12)]
bisect.bisect(arr,3,key=lambda x:x[0])

```
<hr>

- `bisect.bisect(arr,<num>)` -> Returns the right most index(in case ele is already present) where the element can be inserted is returned
- `bisect.bisect_left(arr,<num>)` -> Returns the left most index in case ele is already present

- `bisect.insort(arr,<num>)` -> Inserts the <num> in the right most index in case the num is already present
- `bisect.insort_left(arr,<num>)` -> Inserts num in left most index.

### @cache
- `@cache` works in Python > 3.9
- `@lru_cache` for lower versions < 3.9 

**NOTE**: 
1. You can only pass tuples, int as arguments when using `@cache` or `@lru_cache`
```python
from functools import cache, lru_cache 

# all arguments to cached function must be immutable - tuple, string, dict
@cache
def fn():
    pass


# CLEARING CACHE -> ONLY FOR LRU_CACHE (@lru_cache(None))
fn.cache_clear()
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

## TODO Problems
- [ ] https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/ ( Dijkstras )
- [ ] https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/ (Prefix Sum + Smart Mods) 
