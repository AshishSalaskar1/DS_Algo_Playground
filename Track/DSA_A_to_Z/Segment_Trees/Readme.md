
# Segment Tree
## General Functions
1. Node: Can hold any values
2. Merge: Merges node1 and node2 (Consider this as + in simplist form)
3. Update(loc, val) => updates value at `loc` in the array (here loc is arr index)
4. Query: Find `merge operation result` from `L` -> `R` (if merge is simple add, query(l,r) => sum of elements from l->r)

**Notes**:
1. Make sure while updating the **indices/loc is always 0-indexed**
2. **Merge should be picked such that it works on separate parts**. You should be able to split the problem into sub parts
  Ex: merge(0,10) should be same as merge(merge(0,5), merge(6,10))
---
### Time Complexity
- build - O(n)
- Point Update - O(logn)
- Query - O(logn)
- Range Update
  - Sequence of point updates = O(range*logn)
  - Lazy Propagation
---
## Range Query, Point Update
Use normal segment tree.
- Updates happen on a point - update(loc,val)
- Query happens on range - query(l,r)
---
## Range Updates, Point Query
- **Use Prefix sum with difference array concept**
- Updates happen on a range - update(l,r,update_val) (here update_val is added/subbed from each point in `l` to `r`)
- Query happens on point - query(loc) (return value at arr[loc] after previous queries)


**Solution:**
1. Make diff array, for i=1->n, diff[i] = arr[i]-arr[i-1]
2. udpate(l,r,val): diff[l] += val, diff[r+1] -= val
3. query(loc): Calculate **prefix sum upto loc** (You will need to generate the prefix sum each time)

---
## Range Updates +  Range/Point Query => Lazy Propagation
- Lazy Propagation and everything else: https://www.youtube.com/watch?v=NofRIGE7oWU
- Lazy Prop Code: https://github.com/aryan-0077/Competitive-Programming/blob/main/segTree_lazyPropogation_v1.sublime-snippet

**How it works?** 
- In `query` if your current query (l->r) lies inside (ql->qr) you directly return st[i] and dont bother to go deeper
- Same way, `update(l,r,ql,qr)` if (l->r) lies within (ql->qr) you just update this node and **mark it as lazy**
  (this indicates that value of this range is correct, but child nodes dont have the updated value)
<br><br>
- **MARKING NODE AS LAZY** -> `apply_lazy(i,l,r,val)`
	- **If node is Lazy -> its st[i].val is updated -> but childrens are not**
    1. Calculate correct val of current node: For example in simple range sum,
    ```py
      - node.val = (r-l+1)*val [UPDATE = REPLACE VALUES]
      - node.val += (r-l+1)*val [UPDATE = ADD VAl to all ranges]
    ```
    2. Mark Current Node as lazy
    3. Store Lazy val -> so that it can propagated later
    ```py
      - self.lazy = val [UPDATE = REPLACE VALUES]
      - self.lazy += val [UpDATE = ADD VAl to all ranges]
    ```
    - Here, you also add existing lazy value (THIS NODE MIGHT HAVE BEEN MARKED AS LAZY BEFORE ALSO => Take into account previous lazy/unpropagated values also)
<br><br>
-   **PUSHING DOWN LAZY NODE** -> `push(i,l,r)
	- Lets say a node is marked as Lazy (means its val is proper but has unpropagated values)
	1. If its leaf node (l==r), no need to do anything
	2. If not leaf, the make its child nodes as lazy (you need mid also)
	```py
	mid = (l+r)//2
    self.apply_lazy(2*i, l, mid, self.lazy[i])
    self.apply_lazy((2*i)+1, mid+1, r, self.lazy[i])
	```
	3. Mark this as not lazy again
<br><br>
- **WHEN TO PUSH LAZY NODES TO CHILDREN**
	- Lets say in `update` or `query` function, if the current node is lazy i.e `i in self.lazy` then for sure you might need to go to its children (and those are not updates)
	- If node is lazy ->   `push(i,l,r)` . 
		1. This will propagate all the unpropagated lazy val stores in lazy[i] to its children
		2. `apply_lazy()` on 2i and 2i+1 nodes, mark them as lazy
		3. Mark cur node as not lazy now

<br><br>
**Important Things to remember**
1. Remember how lazy is default initiated. This gets used in `apply()` function, since you update your lazy val keeping in mind it can also have previous lazy_val. In case it doesnt, you need to have a solution (for range sum its default can be 0, -inf for min problems, 0 for skylines etc)
2. You can do both `range_query` and `point_query`. 
	- `range_query`: Same as usual ST
	- `point_query` -> check if outside range -> (l==r) -> other 2 halves

---
## K-th Segment Tree
**Use Case**: <br>
You want a data structure, where you can `add`, `delete` elements. And you can query to get the `kth smallest element` (kth position element in case the array is sorted)

**Overall Time Complexity**
- Initialization (__init__): O(n)
- Operation (add or remove): O(log⁡n)
- Query (k-th smallest): O(log⁡n)

**Solution**
- st[i] = (l,r) => saves number of elements added in DS which fall in range (l,r) inclusive
- Query Logic:
  1. **if k >= left_sub_tree.val: search in left_space, k=k**
  2. **if k < left_sub_tree.val: search in left_space, k= k-left_sub_tree.val:**
- Add logic: Go on reducing (l,r) until l==r, then self.st[i].val = 1
- Remove logic: Go on reducing (l,r) until l==r, then self.st[i].val = 0
- `n` = 1 + max of elements that can be added
- You dont mantain an `arr` array here. Instead vals are stored at indexes

<br><br>
**Case 1**<br>
lets say k=3, You are at (l,r), (l,mid)=4, (mid+1,r)=3
1. Left subtree has val = 4 (means 4 values fall between l->mid)
2. Right subtree has val = 3 (means 3 values fall between mid+1 -> r)
- Now, you want to find 3rd number. And you know that (l,mid) has 4, so surely your 3rd will also lie there
- Because, (mid+1,r) is greater than mid. That means (l,mid) will have till 4th element

<br><br>
**Case 2**<br>
lets say k=4, You are at (l,r), (l,mid)=2, (mid+1,r)=5
1. Left subtree has val = 2 (means 2 values fall between l->mid)
2. Right subtree has val = 5 (means 5 values fall between mid+1 -> r)
- Now, you want to find 3rd number. And you know that (l,mid) has 2, so surely your 3rd will lie in right side
- left range (l,mid) has 2 items and 5 are left in right (mid+1,r)
- K = k-2 = 4-2 = 2. Why? You wanted 4th, out of which smallest 2 are already there in left range. Now in the right range you need to find 2nd, hence k=4-2=2

---
## Problem Examples
1. **Dynamic Range Sum Queries : Simple Segment Tries**
<br><br>
2. **Dynamic XOR Queries: Simple Segment Tree - use XOR instead of ADD**
<br><br>
3. **Dynamic Queries Find Min or Max in range with Updates**
    - Updates remain same: use merge instead of +
    - Instead of doing `add` do min/max
    - Node() default val: +inf(for min), -inf(for max)
    - node.val = min.max of elements from (l,r)
    - merge = min(left_res ,right_res)
<br><br>
4. **Dynamic Queries Find Min + Min_Count in range with Updates**
    - node.mv = min of elements from (l,r)
    - node.mvcount = count of node.minval in range (l,r)
    - merge(left, right)
        node = Node()
        if left.mv < right.mv: node.mv=left.mv, node.mvcount = left.mvcount
        if right.mv < left.mv: node.mv=right.mv, node.mvcount = right.mvcount
        else: node.mv=left.mv, node.mvcount = right.mvcount+left.mvcount
