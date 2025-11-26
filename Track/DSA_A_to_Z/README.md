## Algorithm References
- https://liuzhenglaichn.gitbook.io/algorithm/
- Notion DSA Tracker: https://languid-knife-878.notion.site/DSA-038b19d91806431ea085bfdc7b11e945?pvs=74
- Mindmaps: https://whimsical.com/problem-types-5CTHziFHocX2JhFPB6CxeS@8ADn3nfZACad1E2znvKvQ98kKV43jQC6e77M
  
## Leetcode Lists
- Compilation of Topic lists: https://leetcode.com/discuss/study-guide/1612475/all-leetcode-discuss-lists-and-my-lists-so-far-topic-wisedifficulty-wise
  
- Two Pointer: https://leetcode.com/problem-list/two-pointers/
- Sweep Line: https://leetcode.com/problem-list/o1qf3c31/
- Rolling Hash: https://leetcode.com/problem-list/rolling-hash/ 

## Good Leetcode Articles
- 2 pointer/Sliding Window: https://leetcode.com/discuss/post/3722472/sliding-window-technique-a-comprehensive-ix2k/
- Binary Search: https://leetcode.com/discuss/post/3726061/binary-search-a-comprehensive-guide-by-i-3nxx/
- Bit Manipulation: https://leetcode.com/discuss/post/3695233/all-types-of-patterns-for-bits-manipulat-qezp/

## Python References

## `nonlocal` vs `global`
- `global` -> Variable is in global scope ( **not in class** )
- `nonlocal` -> Variable in any scope outside the current scope

```py

global_res = 0
class Solution:
    def solve(self,  arr):
        res = 0
        n = len(arr)
        def solve(i,csum):
            # you want to update res
            global res # GIVES ERROR
            nonlocal res # CORRECT
```

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

### Important
- If <num> is greater than everything, its placed at last -> `n` (**Note its `n` and not `n-1`**)
- If <num> is lesser than everything, its placed at first -> `0`


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

@lru_cache(maxsize=None) # Default maxsize param is 128 i.e it will only cache last 128 states and evict if more than that
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

## Heapq
- Faster than `PriorityQueue`, but not threadsafe
```py
from heapq import heapify, heappush, heappop

pq = [5,1,3]
heapify(pq)

print(pq) # [1,x,x,x,x,x]
print(pq[0]) # smallest element

print(heappop(pq)) # 1 #PEEK
print(heappush(pq, 0))
print(pq[0]) # 0 


pq = []
heapify(pq)
print(len(pq), bool(pq)) # 0 False

```

| Operation    | Time Complexity |
| :-------- | :------- |
| `put()`  | O(nlogn)    |
| `get()` | O(logn) - Peek + Delete head     |
| `peek()` or `queue[0]`    | O(1)    |
|`heapify()`| O(n) |

| Task | Sorting | Heap |
|------|--------|------|
| Get K largest | **O(n log n)** | **O(n log K)** 🚀 |
| Streaming top K | ❌ Bad | ✔️ Excellent |
| Always get min/max | ❌ | ✔️ O(1) peek |
| Insert new items | O(n) (must re-sort) | O(log n) |
| Remove top | O(n) | O(log n) |
| Build once | O(n log n) | **O(n)** (heapify) |

### Frozen Set vs Set
| When you want to put a set into another set => FROZENSET
1. **set**
    - **Mutable** → you can add, remove, update elements.
    - **Unhashable** → cannot be used as a key in a dictionary or added to another set.
    - Typical use: when you need to collect unique items but the collection may change.

1. **frozenset**
   - **Immutable** → once created, cannot be changed (no .add() or .remove()).
   - **Hashable** → can be used as a dictionary key or as an element of another set.
   - Typical use: when you want to store sets inside other sets (like your island shapes).


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

### Python Bit Operations
- Finding bit_length: `num.bit_length()`
  - This gives you the num of bits needed to represent `num` in binary, ignoring sign bits
  - Note: Its not number of set bits ( this can be position of right most set bit)


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

# 📘 DSA Maths & Formulae Ready Reckoner

Handy formulas for coding interviews (Google, etc.)

---

## 🔹 Strings

- **Number of substrings of length `n`**

$$
\frac{n \cdot (n+1)}{2}
$$

- **Number of subsequences of length `n`**

$$
2^n
$$

(Excluding empty subsequence → $2^n - 1$)

---

## 🔹 Arrays / Pairs / Triplets

- **Pairs from `n` elements**

$$
\binom{n}{2} = \frac{n \cdot (n-1)}{2}
$$

- **Triplets from `n` elements**

$$
\binom{n}{3} = \frac{n \cdot (n-1) \cdot (n-2)}{6}
$$

---

## 🔹 Sums & Series

- **Sum of first `n` natural numbers**

$$
\frac{n \cdot (n+1)}{2}
$$

- **Sum of squares**

$$
\frac{n \cdot (n+1) \cdot (2n+1)}{6}
$$

- **Sum of cubes**

$$
\left(\frac{n \cdot (n+1)}{2}\right)^2
$$

---

## 🔹 Combinatorics

- **Binomial coefficient**

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

- **Permutations**

$$
P(n,r) = \frac{n!}{(n-r)!}
$$

---

## 🔹 Graph Theory

- **Edges in a complete graph with `n` nodes**

$$
\binom{n}{2} = \frac{n \cdot (n-1)}{2}
$$

- **Possible undirected graphs with `n` nodes**

$$
2^{\binom{n}{2}}
$$

- **Possible directed graphs with `n` nodes (no self-loops)**

$$
2^{n \cdot (n-1)}
$$

- **Handshaking Lemma**

$$
\sum_{v \in V} \deg(v) = 2|E|
$$

- **Spanning trees in a complete graph (Cayley’s formula)**

$$
n^{n-2}
$$

- **Tree with `n` nodes** always has

$$
n - 1 \text{ edges}
$$

---

## 🔹 Trees

- **Max nodes at level `l`**

$$
2^l
$$

- **Max nodes in a binary tree of height `h`**

$$
2^{h+1} - 1
$$

- **Min nodes in a binary tree of height `h`**

$$
h + 1
$$

- **Height of complete binary tree with `n` nodes**

$$
\lfloor \log_2(n) \rfloor
$$

- **Leaf nodes in a full binary tree with `n` nodes**

$$
\frac{n+1}{2}
$$

- **Catalan number (number of BSTs with `n` distinct keys)**

$$
C_n = \frac{1}{n+1}\binom{2n}{n}
$$

- **Full Binary Tree Property**  
  If a binary tree has `I` internal nodes, leaves =

$$
L = I + 1
$$

- **Heap Height with `n` nodes**

$$
\lfloor \log_2(n) \rfloor
$$

---

## 🔹 Probability & Counting

- **Pigeonhole Principle**  
  If `n` items are put into `m` containers, at least one container has

$$
\lceil n/m \rceil
$$

items.

- **Birthday Paradox rule**  
  With

$$
\sqrt{365} \approx 23
$$

people, collision probability > 50%.

---

## 🔹 Logs (Handy for Time Complexity)

- **Change of base**

$$
\log_a b = \frac{\log_c b}{\log_c a}
$$

- **Stirling’s Approximation**

$$
\log(n!) \approx n \log n - n
$$

---
