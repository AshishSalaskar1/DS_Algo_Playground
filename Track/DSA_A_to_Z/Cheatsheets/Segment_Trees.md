# Segment Trees Cheatsheet (verbatim)

From Segment_Trees/Segment_Tree_Template.py
```python
class Node:
    def __init__(self, val=0) -> None:
        self.val = val

def merge(left: Node, right: Node) -> Node:
    node = Node()
    node.val = left.val + right.val
    return node

class SegmentTree:
    def __init__(self, arr, n) -> None:
        self.st = [Node() for _ in range((4*n+1))]
        self.arr = arr
        self.n = n
        self.build(1, 0, n-1)

    def build(self, i, l, r) -> None:
        if l==r:
            self.st[i].val = self.arr[l]
            return

        mid = l + ((r-l)//2)
        self.build(2*i, l, mid)
        self.build((2*i)+1, mid+1, r)
        self.st[i] = merge(self.st[2*i],self.st[(2*i)+1])

    def update(self, i, l, r, pos, val) -> None:
        if pos<l or pos>r:  return
        if l==r:
            self.st[i].val = val
            self.arr[pos] = val
            return

        mid = l + ((r-l)//2)
        self.update(2*i, l, mid, pos, val)
        self.update((2*i)+1, mid+1, r, pos, val)
        self.st[i] = merge(self.st[2*i],self.st[(2*i)+1])

    def query(self, i, l, r, ql, qr) -> Node:
        # [l,r] doesnt not fall in or overlaap with [ql,qr]
        if l>qr or r<ql:    return Node(0)

        # this returns (l,r) => remaining will get added subsequently (ql,l) and (r,qr)
        if ql<=l<=r<=qr:    return self.st[i]

        mid = l + ((r-l)//2)
        return merge(
            self.query(2*i, l, mid, ql, qr),
            self.query((2*i)+1, mid+1, r, ql, qr)
        )
```

---

## 🗺️ Quick map
- 🔎 Overview and use-cases (range aggregates, lazy updates)
- ⚡ At a glance (patterns and pitfalls)
- 🧩 Core snippets (above, verbatim from repo)
- 🧠 Misconceptions and fixes
- 🧭 When to use which subtype (point/range/lazy)
- ⏱️ Complexity cheat

## ✅ Study checklist
- [ ] Can I define the node merge and identity correctly?
- [ ] Do I know when I need lazy vs not?
- [ ] Can I search for k-th/first-true by descending the tree?
- [ ] Are ranges inclusive and indices consistent?

## At a glance
- Build: O(n), Query/Update: O(log n). Node stores merge of children (sum/min/max/custom struct).
- Point update vs range update (lazy propagation for range updates/queries).
- Iterative segment trees (flat arrays) can be simpler/faster; recursive is clearer for custom nodes.

## Pitfalls
- Correct neutral elements for merge (e.g., 0 for sum, +inf/-inf for min/max).
- Lazy pushes: propagate before descending; clear tags after push.
- Be mindful of 0/1-based segments and inclusive ranges.

## Common patterns
- Range aggregate with point updates: sum/min/max/gcd/xor; Node stores a simple value; merge is associative.
- Range updates + range queries (lazy):
  - Range add and sum/min/max queries via additive lazy tags.
  - Range assign (set to x) needs assign-tag that overrides add; tags must be composed carefully.
- Order statistics / K-th: build on frequency array; descend tree comparing left.size vs k to find k-th 1.
- First/last index satisfying predicate: binary search on tree using stored aggregates (e.g., first index with prefix sum ≥ K, or any positive in range).
- Max subarray sum: Node with (sum, pref, suff, best) and custom merge (as in the repo’s Node pattern).
- Range GCD: Node stores gcd; merge via gcd; identity = 0.

## Identify the technique and decide subtype
- Static queries only (no updates): prefer Sparse Table for idempotent ops (min/max/gcd). If not idempotent (sum), still OK but memory heavy; segtree also fine.
- Point updates + prefix/range sum only: BIT/Fenwick is simpler and lighter; segtree if you need more ops than sum/max-prefix.
- Range updates or mixed ops (sum + min, custom structs): Segment Tree with Lazy.
- Need to find k-th/first-true index or support custom searches over aggregates: Segment Tree (descend by children using aggregates).
- Large coordinate values or dynamic indices: Coordinate compress; for truly dynamic sparse domains, use a map-backed dynamic segtree.
- Performance hint: If n,q ~ 2e5 and both range updates and queries appear, you almost certainly want lazy segtree.

## Confusions and fixes
- Neutral/identity element mistakes:
  - sum: 0; min: +inf; max: -inf; gcd: 0. Custom Node must define a true identity element used for no-overlap returns.
- Lazy propagation order:
  - Always push before descending to children on partial overlaps.
  - When both assign and add exist, assign overrides add: compose as (child.assign = x, child.add = 0); for add-only, child.add += add.
- Overlap handling (three cases):
  - No overlap -> return identity; Full overlap -> apply and return; Partial -> push then recurse and merge.
- Indexing and ranges:
  - Keep leaf-to-array mapping consistent (commonly 0-based array with [l,r] inclusive segments). Split as mid = (l+r)//2, recurse [l,mid], [mid+1,r].
- When you do NOT need lazy:
  - Range queries with point updates don’t need lazy; only range updates (or heavy query-side propagation) require it.
- Searching on tree:
  - While descending for k-th/first-true, guard child availability (e.g., if left aggregate already meets condition, go left, else subtract and go right).
- Python recursion and speed:
  - Deep recursion may hit limits; consider iterative segtree or increase recursionlimit for n ~ 2e5 if using recursion.
- Memory/layout choices:
  - Tree arrays sized at 4*n are typical for recursive segtrees; iterative segtrees often use 2*n flat arrays.
- Not a segtree problem:
  - If queries are offline and only need prefix-like aggregates, prefix sums or difference arrays may be enough; don’t overuse segtrees.
