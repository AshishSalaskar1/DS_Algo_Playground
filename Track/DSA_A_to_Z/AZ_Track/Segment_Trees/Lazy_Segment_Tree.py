"""
Ref: https://github.com/aryan-0077/Competitive-Programming/blob/main/segTree_lazyPropogation_v1.sublime-snippet
"""
from collections import defaultdict
class Node:
    def __init__(self, val=0) -> None:
        self.val = val

def merge(left: Node, right: Node) -> Node:
        return Node(
            left.val + right.val
        )

class SegmentTreeRangeUpdateReplace:
    def __init__(self, arr, n) -> None:
        self.st = [Node() for _ in range((4*n+1))]
        self.arr = arr
        self.n = n
        self.build(1, 0, n-1)
        self.lazy = defaultdict(int)

    def push_down_lazy(self, i, l, r):
        # the value of node(i) is already correct - it was filled while marking it as Lazy
        # Now just make the subsets as lazy
        mid = (l+r)//2
        self.apply_lazy(2*i, l, mid, self.lazy[i])
        self.apply_lazy((2*i)+1, mid+1, r, self.lazy[i])

        self.lazy.pop(i)

    def apply_lazy(self, i, l, r, lazy_val):
        # mark the current node as lazy => Update its actual value (BECAUSE U NEED THAT)
        if l!=r: # if this is a LEAF => no lazy needed
            # IT MAY ALREADY BE LAZY ALSO => doesnt matter you just replace with new valu
            self.lazy[i] = lazy_val

        self.st[i] = Node((r-l+1)*lazy_val)

    def build(self, i, l, r):
        if l==r:
            self.st[i] = Node(self.arr[l])
            return

        mid = (l+r)//2
        self.build(2*i, l, mid)
        self.build(2*i+1, mid+1, r)
        self.st[i] = merge(self.st[2*i], self.st[2*i+1])

    def range_update(self, i, l, r, ul, ur, val):
        if l>ur or r<ul: return

        if ul<=l<=r<=ur: # cur range falls within update_range
            self.apply_lazy(i, l, r, val)
            return

        # partial overlap
        # in case its lazy -> push down to its child
        if i in self.lazy: self.push_down_lazy(i, l, r)

        mid = (l+r)//2
        self.range_update(2*i, l, mid, ul, ur, val)
        self.range_update(2*i+1, mid+1, r, ul, ur, val)
        self.st[i] = merge(self.st[2*i], self.st[2*i+1])


    def query_point(self, i, l, r, q):
        if q<l or q>r: return Node()

        # if your cur range falls within the query range
        if l==r:    return self.st[i]

        if i in self.lazy: self.push_down_lazy(i, l, r)
        mid = (l+r)//2
        return merge(
            self.query_point(2*i, l, mid,  q),
            self.query_point((2*i)+1, mid+1, r, q)
        )

    def query_range(self, i, l, r, ql, qr):
        if l>qr or r<ql: return Node()

        # if your cur range falls within the query range
        if ql<=l<=r<=qr:
            return self.st[i]

        if i in self.lazy: self.push_down_lazy(i, l, r)
        mid = (l+r)//2
        return merge(
            self.query_range(2*i, l, mid,  ql, qr),
            self.query_range((2*i)+1, mid+1, r, ql, qr)
        )

class SegmentTreeRangeUpdateAdd:
    def __init__(self, arr, n) -> None:
        self.st = [Node() for _ in range((4*n+1))]
        self.arr = arr
        self.n = n
        self.build(1, 0, n-1)
        self.lazy = defaultdict(int)

    def push_down_lazy(self, i, l, r):
        mid = (l+r)//2
        self.apply_lazy(2*i, l, mid, self.lazy[i])
        self.apply_lazy((2*i)+1, mid+1, r, self.lazy[i])

        self.lazy.pop(i)

    def apply_lazy(self, i, l, r, lazy_val):
        if l!=r:
            self.lazy[i] += lazy_val

        # HERE YOUR UPDATING EXISTING VALUE = so val+=
        # Logic: lets say st[i] = 10 for (5,7) = SUM(5,7)=10
        # now, val=5 gets added, st[i] = st[i] + (r-l+1)*5
        # new_val = old_val + (num_nodes*val)
        self.st[i].val += (r-l+1)*lazy_val

    def build(self, i, l, r):
        if l==r:
            self.st[i] = Node(self.arr[l])
            return

        mid = (l+r)//2
        self.build(2*i, l, mid)
        self.build(2*i+1, mid+1, r)
        self.st[i] = merge(self.st[2*i], self.st[2*i+1])

    def range_update(self, i, l, r, ul, ur, val):
        if l>ur or r<ul: return

        if ul<=l<=r<=ur: # cur range falls within update_range
            self.apply_lazy(i, l, r, val)
            return

        # partial overlap: in case its lazy -> push down to its child
        if i in self.lazy: self.push_down_lazy(i, l, r)

        mid = (l+r)//2
        self.range_update(2*i, l, mid, ul, ur, val)
        self.range_update(2*i+1, mid+1, r, ul, ur, val)
        self.st[i] = merge(self.st[2*i], self.st[2*i+1])


    def query(self, i, l, r, ql, qr):
        if l>qr or r<ql: return Node()

        # if your cur range falls within the query range
        if ql<=l<=r<=qr:
            return self.st[i]

        if i in self.lazy: self.push_down_lazy(i, l, r)
        mid = (l+r)//2
        return merge(
            self.query(2*i, l, mid,  ql, qr),
            self.query((2*i)+1, mid+1, r, ql, qr)
        )



#  0 1 2 3 4 5 6  7
# [3,5,6,1,2,7,8,10]

arr = [3,5,6,1,2,7,8,10]
n = len(arr)
st = SegmentTreeRangeUpdateReplace(arr, n)

# querying: [3:6] = [1,2,7,8] = 18
print(st.query_range(1, 0, n-1, 3, 6).val)

# update(3,5,5) => [3,5,6,5,5,5,8,10]
#  0 1 2 3 4 5 6  7
# [3,5,6,5,5,5,8,10]
st.range_update(1, 0, n-1, 3, 5, 5)

# querying: [3:6] = [5,5,5,8] = 23
print(st.query_range(1, 0, n-1, 3, 6).val)


st = SegmentTreeRangeUpdateAdd(arr, n)

# querying: [3:6] = [1,2,7,8] = 18
print(st.query(1, 0, n-1, 3, 6).val)

# update(3,5,5) => [3,5,6,6,7,12,8,10]
#  0 1 2 3 4  5 6  7
# [3,5,6,6,7,12,8,10]
st.range_update(1, 0, n-1, 3, 5, 5)

# querying: [3:6] = [6,7,12,8] = 33
print(st.query(1, 0, n-1, 3, 6).val)
