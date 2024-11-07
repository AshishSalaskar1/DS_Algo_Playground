

class Node:
    def __init__(self, val=0) -> None:
        self.val = val

def merge(left: Node, right: Node) -> Node:
    node = Node()
    node.val = left.val + right.val
    return node

class KSegmentTree:
    def __init__(self, n) -> None:
        self.st = [Node() for _ in range((4*n+1))]
        self.n = n

    def operation(self, i, l, r, val, op="add") -> None:
        if val<l or val>r: return
        if l==r:
            if op == "add": self.st[i].val = 1
            if op == "remove": self.st[i].val = 0
            return

        mid = (l+r)//2
        self.operation(2*i,l,mid,val,op=op)
        self.operation(2*i+1,mid+1,r,val,op=op)
        self.st[i] = merge(self.st[2*i], self.st[2*i+1])


    def query(self, i, l, r, k):
        if l==r:
            return l
        mid = (l+r)//2

        # left range has more than k nodes
        if self.st[2*i].val >= k:
            return self.query(2*i, l, mid, k)
        else: # left range has < k nodes - (so out of k, self.st[2*i] are removed => k= k-self.st[2*i] )
            return self.query(2*i+1, mid+1,r,k-self.st[2*i].val)

# ranks = [1,3,2,4,5, 6]
# arr =   [2,5,3,6,8,10]
#
arr =   [2,5,3,6,8,10]

n=10**4
st = KSegmentTree(n)
for x in arr:
    st.operation(1,0,n-1,x,op="add")

print(st.query(1,0,n-1,3)) # 5
print(st.query(1,0,n-1,4)) # 6

st.operation(1,0,n-1,6,op="remove")
# ranks = [1,3,2,4, 5]
# arr =   [2,5,3,8,10]
print(st.query(1,0,n-1,3)) # 5
print(st.query(1,0,n-1,4)) # 8
