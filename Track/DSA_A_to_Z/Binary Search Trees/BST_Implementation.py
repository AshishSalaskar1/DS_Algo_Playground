class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, arr: list[int] | None = None):
        self.root = None
        if arr:
            self.root = self._create_bst_from_array(arr)

    # Create balanced BST from array
    def _create_bst_from_array(self, arr: list[int]) -> Node:
        arr.sort()

        def bstgen(lo: int, hi: int):
            if lo > hi:
                return None
            if lo == hi:
                return Node(arr[lo])

            mid = (lo + hi) // 2
            root = Node(arr[mid])
            root.left = bstgen(lo, mid - 1)
            root.right = bstgen(mid + 1, hi)
            return root

        return bstgen(0, len(arr) - 1)

    # Insert into BST
    def insert(self, val: int) -> None:
        if not self.root:
            self.root = Node(val)
            return

        cur = self.root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = Node(val)
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = Node(val)
                    return
                cur = cur.right

    # Search in BST
    def search(self, val: int) -> bool:
        cur = self.root
        while cur:
            if cur.val == val:
                return True
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return False



# Create BST from array (balanced)
bst = BST([10, 5, 15, 3, 7, 12])

# Insert new values
bst.insert(6)
bst.insert(20)

# Search values
print(bst.search(7))    # True
print(bst.search(6))    # True
print(bst.search(8))    # False

# Create empty BST and add later
bst2 = BST()
bst2.insert(10)
bst2.insert(5)
bst2.insert(15)

print(bst2.search(15))  # True
print(bst2.search(1))   # False
