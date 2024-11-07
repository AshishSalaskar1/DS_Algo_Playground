class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def update(self, start, end, l, r, val, node=1):
        if self.lazy[node] != 0:
            self.tree[node] = max(self.tree[node], self.lazy[node])
            if l != r:
                self.lazy[node * 2] = max(self.lazy[node * 2], self.lazy[node])
                self.lazy[node * 2 + 1] = max(self.lazy[node * 2 + 1], self.lazy[node])
            self.lazy[node] = 0

        if start > r or end < l:
            return
        if start <= l <= r <= end:
            self.tree[node] = max(self.tree[node], val)
            if l != r:
                self.lazy[node * 2] = max(self.lazy[node * 2], val)
                self.lazy[node * 2 + 1] = max(self.lazy[node * 2 + 1], val)
            return

        mid = (l + r) // 2
        self.update(start, end, l, mid, val, node * 2)
        self.update(start, end, mid + 1, r, val, node * 2 + 1)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, idx, l, r, node=1):
        if self.lazy[node] != 0:
            self.tree[node] = max(self.tree[node], self.lazy[node])
            if l != r:
                self.lazy[node * 2] = max(self.lazy[node * 2], self.lazy[node])
                self.lazy[node * 2 + 1] = max(self.lazy[node * 2 + 1], self.lazy[node])
            self.lazy[node] = 0

        if l == r:
            return self.tree[node]

        mid = (l + r) // 2
        if idx <= mid:
            return self.query(idx, l, mid, node * 2)
        else:
            return self.query(idx, mid + 1, r, node * 2 + 1)

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        # Step 1: Coordinate Compression
        x_coords = set()
        for l, r, h in buildings:
            x_coords.add(l)
            x_coords.add(r)

        x_coords = sorted(x_coords)
        x_map = {x: i for i, x in enumerate(x_coords)}
        n = len(x_coords)

        # Step 2: Segment Tree initialization
        seg_tree = SegmentTree(n)

        # Step 3: Process the buildings to update the segment tree
        for l, r, h in buildings:
            seg_tree.update(x_map[l], x_map[r] - 1, 0, n - 1, h)

        # Step 4: Extract the skyline by querying the segment tree
        result = []
        prev_height = 0
        for i in range(n):
            curr_height = seg_tree.query(i, 0, n - 1)
            if curr_height != prev_height:
                result.append([x_coords[i], curr_height])
                prev_height = curr_height

        return result
