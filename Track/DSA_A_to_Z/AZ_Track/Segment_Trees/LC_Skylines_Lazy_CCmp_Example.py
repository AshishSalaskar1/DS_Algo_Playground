"""
Problem: https://leetcode.com/problems/the-skyline-problem/

Range Update + Point Query
"""

from collections import defaultdict
class Node:
    def __init__(self, val=float("-inf")):
        self.val = val  # Store the max height value

def merge(left, right):
    return Node(max(left.val, right.val))

class SegmentTree:
    def __init__(self, n):
        self.st = [Node() for _ in range(4 * n + 1)]
        self.lazy = defaultdict(int)
        self.n = n

    def apply(self, i, l, r, val):
        self.st[i].val = max(self.st[i].val, val)
        if l != r:
            self.lazy[i] = max(self.lazy[i], val)

    def pushDown(self, i, l, r):
        if i in self.lazy:
            mid = (l + r) // 2
            self.apply(2 * i, l, mid, self.lazy[i])
            self.apply(2 * i + 1, mid + 1, r, self.lazy[i])
            self.lazy.pop(i)  # Clear the lazy value for the current node

    def update(self, i, l, r, ul, ur, val):
        if ur < l or ul > r:    return
        if ul <= l and r <= ur:  # Current range fully within update range
            self.apply(i, l, r, val)
            return

        self.pushDown(i, l, r)  # Push down any pending lazy updates before updating

        mid = (l + r) // 2
        self.update(2 * i, l, mid, ul, ur, val)  # Update left child
        self.update(2 * i + 1, mid + 1, r, ul, ur, val)  # Update right child
        self.st[i] = merge(self.st[2 * i], self.st[2 * i + 1])  # Recalculate the current node

    def query(self, i, l, r, q):
        if q > r or q < l:  return Node()  # Return negative infinity for invalid range

        if l==r:    return self.st[i]
        self.pushDown(i, l, r)  # Push down any pending lazy updates before querying
        mid = (l + r) // 2
        return merge(
            self.query(2 * i, l, mid, q),
            self.query(2 * i + 1, mid + 1, r, q)
        )

class Solution:
    def getSkyline(self, buildings):
        # Step 1: Coordinate compression
        cords = []
        for l, r, _ in buildings:
            cords.append(l)
            cords.append(r)

        cords = sorted(set(cords))  # Remove duplicates and sort
        cord_map = {x: i for i, x in enumerate(cords)}  # Map each coordinate to a compressed index

        # Step 2: Create the segment tree
        st = SegmentTree(len(cord_map))

        for l, r, height in buildings:
            compressed_l = cord_map[l]
            compressed_r = cord_map[r] - 1  # Update range is inclusive, so subtract 1
            st.update(1, 0, st.n - 1, compressed_l, compressed_r, height)

        last_h = 0
        res = []
        for x in cords:
            cur_h = st.query(1, 0, st.n - 1, cord_map[x]).val
            cur_h = 0 if cur_h == float("-inf") else cur_h  # Replace -inf with 0
            if cur_h != last_h:  # Only add a point if the height changes
                res.append([x, cur_h])
                last_h = cur_h

        return res
