class Node:
    # DEFAULT VAL: +INF
    def __init__(self, val=float("inf")) -> None:
        self.val = val

def merge(left: Node, right: Node) -> Node:
    node = Node()
    node.val = min(left.val, right.val)
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
        # INF: [l,r] doesnt not fall in or overlaap with [ql,qr]
        if l>qr or r<ql:    return Node(float("inf"))

        # this returns (l,r) => remaining will get added subsequently (ql,l) and (r,qr)
        if ql<=l<=r<=qr:    return self.st[i]

        mid = l + ((r-l)//2)
        return merge(
            self.query(2*i, l, mid, ql, qr),
            self.query((2*i)+1, mid+1, r, ql, qr)
        )

#  0 1 2 3 4 5 6  7
# [3,5,6,1,2,7,8,10]

arr = [3,5,6,1,2,7,8,10]
n = len(arr)
st = SegmentTree(arr, n)

# querying: [4:6] = [2,7,8] = 2
print(st.query(1, 0, n-1, 4, 6).val)

# update: 5->15 arr[5] = 7 -> 15
# querying: [3:6] = [1,2,15,8] = 1
st.update(1, 0, n-1, 5, 15)
print(st.query(1, 0, n-1, 3, 6).val)
