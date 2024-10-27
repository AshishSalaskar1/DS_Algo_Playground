
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
      - node.val = (r-l+1)*val [UPDATE = REPLACE VALUES]
      - node.val += (r-l+1)*val [UpDATE = ADD VAl to all ranges]
    2. Mark Current Node as lazy
    3. Store Lazy val -> so that it can propagated later
      - self.lazy = val [UPDATE = REPLACE VALUES]
      - self.lazy += val [UpDATE = ADD VAl to all ranges]
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

This called


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
